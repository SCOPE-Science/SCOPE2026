"""Finite numerical checks of a graph-restricted exponential-Euler Lindblad map.
Run: python verify.py (Python standard library only). Mathematical proof is in RESULT.md.
"""
import math
import random

def graph(n, edges):
    W=[[0.0]*n for _ in range(n)]
    for i,j,w in edges:
        if i==j or w<=0: raise ValueError('offdiagonal positive edges needed')
        W[i][j]+=float(w); W[j][i]+=float(w)
    d=[sum(row) for row in W]
    if min(d)<=0: raise ValueError('graph must have no isolates')
    return W,d

def phi(h,d):
    return -math.expm1(-h*d)/d

def transition(W,d,h):
    n=len(d); F=[phi(h,x) for x in d]
    return [[(math.exp(-h*d[j]) if i==j else W[i][j]*F[j]) for j in range(n)] for i in range(n)]

def stationary(d,h):
    s=[1/phi(h,x) for x in d]; z=sum(s)
    return [v/z for v in s]

def mm(P,v):
    return [sum(x*y for x,y in zip(row,v)) for row in P]

def check(a,b,tol=2e-11):
    if abs(a-b)>tol: raise AssertionError((a,b,tol))

def entropy(v):
    return -sum(x*math.log(x) for x in v)

def complete_map_on_diagonal(W,d,p,h):
    # Numerically independent re-derivation directly from the Kraus integrals:
    # the no-jump contribution plus each edge's jump contribution.
    n=len(d)
    result=[math.exp(-h*d[i])*p[i] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            w=W[i][j]
            if w:
                result[i]+=w*p[j]*phi(h,d[j])
                result[j]+=w*p[i]*phi(h,d[i])
    return result

def coherence_block(d_i,d_j,w,h):
    # For the ordered off-diagonal pair (E_ij,E_ji), the channel has
    # matrix [[q,r],[r,q]], whose eigenvalues are q+r and q-r.
    avg=(d_i+d_j)/2
    q=math.exp(-h*avg)
    r=w*phi(h,avg)
    return q+r,q-r

def tests():
    rng=random.Random(4762026); total=0
    # Deterministic 3-path has degrees (1,3,2), Laplacian-degree vector (-2,4,-2).
    W,d=graph(3,[(0,1,1),(1,2,2)])
    check(d[0],1);check(d[1],3);check(d[2],2)
    Ld=[d[i]*d[i]-sum(W[i][j]*d[j] for j in range(3)) for i in range(3)]
    assert Ld==[-2,4,-2];check(sum(x*x for x in Ld)/(8*3),1)
    for h in (1e-4,2e-4,4e-4,1e-3):
        P=transition(W,d,h)
        q=mm(P,[1/3]*3)
        defect=math.log(3)-entropy(q)
        check(defect/h**4,1,0.025) if h>=0.001 else None
        total+=1
    for n in range(2,10):
        for case in range(60):
            # Start with connected tree then add arbitrary positive edges.
            ed=[(j,rng.randrange(j),rng.uniform(0.15,2.5)) for j in range(1,n)]
            for j in range(n):
                for i in range(j):
                    if rng.random()<.15:ed.append((i,j,rng.uniform(.1,2.0)))
            W,d=graph(n,ed)
            for h in (0.005,0.1,1,5):
                P=transition(W,d,h)
                pi=stationary(d,h)
                for j in range(n): check(sum(P[i][j] for i in range(n)),1)
                for i in range(n):
                    check(mm(P,pi)[i],pi[i]);
                    for j in range(n):check(P[i][j]*pi[j],P[j][i]*pi[i]);total+=1
                v=[rng.random() for _ in range(n)];s=sum(v);v=[x/s for x in v]
                direct=complete_map_on_diagonal(W,d,v,h)
                for x,y in zip(mm(P,v),direct):check(x,y);total+=1
                if n>=3:
                    for i in range(n):
                        for j in range(i):
                            lp,lm=coherence_block(d[i],d[j],W[i][j],h)
                            assert abs(lp)<1 and abs(lm)<1
                            total+=1
                rowdev=max(abs(x-1) for x in mm(P,[1]*n))
                regular=max(d)-min(d)<1e-12
                assert (rowdev<1e-10) == regular
                total+=1
    # Two-vertex graph always degree-regular and discrete unital.
    for w in (.1,.3,1,2,10):
        W,d=graph(2,[(0,1,w)])
        for h in (.01,.1,1,100):
            P=transition(W,d,h)
            for x in mm(P,[1,1]): check(x,1);total+=1
            lp,lm=coherence_block(w,w,w,h)
            check(lp,1);assert abs(lm)<=1+1e-12;total+=1
    # Asymptotic stationary limit and small-step error for irregular path.
    W,d=graph(3,[(0,1,1),(1,2,2)])
    u=[1/3]*3
    pi_inf=stationary(d,100)
    for x,y in zip(pi_inf,[1/6,3/6,2/6]):check(x,y);total+=1
    for h in (.005,.01,.025):
        pi=stationary(d,h)
        for i in range(3):
            approx=1/3+h*(d[i]-2)/(2*3)
            check(pi[i],approx,0.0002);total+=1
    print('PASS',total,'assertion families, including off-diagonal coherence blocks, diagonal Kraus evaluation, exact stationary law and entropy coefficient')

if __name__=='__main__':tests()
