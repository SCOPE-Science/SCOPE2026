"""Independent exact-rational enumeration of discounted hitting sets on windmills.

Python 3, standard library only. Checks all nonempty vertex subsets for each
listed finite graph against the closed cardinality and optimizer census.
"""
from fractions import Fraction as F
from math import comb

def adjacencies(m,q):
    n=1+m*q
    a=[set() for _ in range(n)]
    for k in range(m):
        clique=[0]+list(range(1+k*q,1+(k+1)*q))
        for i,u in enumerate(clique):
            for v in clique[i+1:]:
                a[u].add(v);a[v].add(u)
    return [sorted(z) for z in a]

def solve(A,b):
    n=len(b)
    if n==0:return []
    T=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        h=next(i for i in range(j,n) if T[i][j]!=0)
        T[j],T[h]=T[h],T[j]
        v=T[j][j]
        T[j]=[u/v for u in T[j]]
        for i in range(n):
            if i!=j and T[i][j]!=0:
                c=T[i][j]
                T[i]=[a-c*d for a,d in zip(T[i],T[j])]
    return [T[i][-1] for i in range(n)]

def worst_support(adj, mask, l):
    n=len(adj)
    U=[v for v in range(n) if not (mask>>v)&1]
    if not U:return F(1)
    ix={u:i for i,u in enumerate(U)}
    A=[[F(int(i==j)) for j in range(len(U))] for i in range(len(U))]
    b=[F(0)]*len(U)
    for i,v in enumerate(U):
        for w in adj[v]:
            if w in ix:A[i][ix[w]]-=l/len(adj[v])
            else:b[i]+=l/len(adj[v])
    return min(solve(A,b))

def theorem(m,q,l,t):
    levels=[l*(s+1)/(q-l*(q-s-1)) for s in range(q)]+[F(1)]
    r=next(s for s,h in enumerate(levels) if t<=h)
    center=comb(q,r)**m
    if r==q:return 1+m*q,center,0,F(0),r
    def params(s):
        if s==q:return F(0),F(q)
        den=q-l*(q-s-1)
        return (q-s)*l/den,F(s)+(q-s)*l*s/den
    Ar,Br=params(r);As,Bs=params(r+1)
    x=l*((m-1)*Br+Bs)/(m*q-l*((m-1)*Ar+As))
    threshold=l*(x+r)/(q-l*(q-r-1))
    co=m*comb(q,r+1)*comb(q,r)**(m-1) if t<=threshold else 0
    return 1+m*r,center+co,co,threshold,r

def verify():
    checked=0
    for m,q in [(2,2),(3,2),(2,3),(3,3),(2,4)]:
        adj=adjacencies(m,q)
        for l in [F(1,2),F(4,5)]:
            arr=[]
            for mask in range(1,1<<len(adj)):
                arr.append((mask.bit_count(),bool(mask&1),worst_support(adj,mask,l)))
            levels=[F(0)]+[l*(s+1)/(q-l*(q-s-1)) for s in range(q)]+[F(1)]
            thresholds=set(levels[1:])
            for r in range(q):
                base=(levels[r]+levels[r+1])/2
                _,_,_,theta,_=theorem(m,q,l,base)
                assert levels[r]<theta<levels[r+1]
                thresholds.add(theta)
            a=sorted({F(0)}|thresholds)
            tests=sorted(set(a+[ (u+v)/2 for u,v in zip(a,a[1:]) ])-{F(0)})
            for t in tests:
                p=theorem(m,q,l,t)
                ok=[z for z in arr if z[2]>=t]
                k=min(z[0] for z in ok)
                best=[z for z in ok if z[0]==k]
                obs=(k,len(best),sum(not z[1] for z in best))
                assert obs==p[:3],(m,q,l,t,obs,p)
                checked+=1
        print('EXACT_OK',m,q,flush=True)
    print('TOTAL_EXACT_OK',checked)

if __name__=='__main__': verify()
