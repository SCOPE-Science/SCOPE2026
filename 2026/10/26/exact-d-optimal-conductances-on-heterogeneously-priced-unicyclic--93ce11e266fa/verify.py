"""Reproduce exact and numerical checks for unicyclic Laplacian determinant design.

Run: python3 verify.py
Only Python standard library is required.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random


def cycle_allocation(costs, B):
    """Numerically find the unique D-optimal cycle edge conductances."""
    k = len(costs)
    if k < 3 or min(costs) <= 0 or B <= 0:
        raise ValueError('Requires >=3 positive costs and B>0')
    j = max(range(k), key=lambda i: costs[i]); cmax = costs[j]
    if cmax >= sum(costs) - cmax:
        return [0.0 if i == j else B / ((k-1)*costs[i]) for i in range(k)]
    hi = 1/(4*cmax)
    def m(t, c):
        return 2*t*c/(1+sqrt(max(0, 1-4*t*c)))
    minusend = sum(m(hi,c) for c in costs)
    if minusend >= 1:
        lo=0.
        for _ in range(150):
            mid=(lo+hi)/2
            if sum(m(mid,c) for c in costs)>1: hi=mid
            else:lo=mid
        z=(lo+hi)/2
        x=[m(z,c) for c in costs]
    else:
        lo=0.
        for _ in range(150):
            mid=(lo+hi)/2
            t=sum(m(mid,c) for i,c in enumerate(costs) if i!=j)/m(mid,cmax)
            if t > 1: lo=mid
            else:hi=mid
        z=(lo+hi)/2
        x=[m(z,c) for c in costs]
        x[j]=1-x[j]
    return [B/(k-1)*(1-x[i])/costs[i] for i in range(k)]


def tau_unicyclic(cyc, bridges):
    out=Q(1)
    for z in bridges: out*=z
    ans=Q(0)
    for j in range(len(cyc)):
        p=Q(1)
        for i,z in enumerate(cyc):
            if i!=j: p*=z
        ans+=p
    return out*ans


def det(A):
    """Exact Gaussian determinant, no floating point operations."""
    A=[[Q(v) for v in row] for row in A]
    ans=Q(1); n=len(A)
    for i in range(n):
        j=next((j for j in range(i,n) if A[j][i]),None)
        if j is None:return Q(0)
        if j!=i:
            A[i],A[j]=A[j],A[i]
            ans=-ans
        pivot=A[i][i];ans*=pivot
        for j in range(i+1,n):
            alpha=A[j][i]/pivot
            for l in range(i+1,n):A[j][l]-=alpha*A[i][l]
            A[j][i]=Q(0)
    return ans


def cofactor(n, edges):
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for a,b,w in edges:
        L[a][a]+=w; L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
    return det([row[:-1] for row in L[:-1]])


def verify_exact():
    # Cyclic triangle 0-1-2-0 with bridges 0-3-4.
    examples=[
        (('uniform',), [Q(1),Q(1),Q(1)], [Q(10),Q(10),Q(10)], Q(4500)),
        (('interior-dominant',), [Q(3,2),Q(1),Q(1)], [Q(4),Q(12),Q(12)], Q(3600)),
        (('exact-transition',), [Q(2),Q(1),Q(1)], [Q(0),Q(15),Q(15)], Q(3375)),
        (('strict-deletion',), [Q(3),Q(1),Q(1)], [Q(0),Q(15),Q(15)], Q(3375)),
    ]
    for lab,cs,ws,expected in examples:
        bridges=[Q(5),Q(3)]
        edges=[(0,1,ws[0]),(1,2,ws[1]),(2,0,ws[2]),(0,3,bridges[0]),(3,4,bridges[1])]
        actual=cofactor(5,edges)
        assert actual==tau_unicyclic(ws,bridges)==expected,(lab,actual)
        assert sum(c*w for c,w in zip(cs,ws))+Q(3)*bridges[0]+Q(5)*bridges[1]==Q(60)
        approx=cycle_allocation([float(z) for z in cs],30)
        assert max(abs(v-float(w)) for v,w in zip(approx,ws))<1e-9,(lab,approx,ws)
    return len(examples)


def verify_random():
    rng=Random(20261024)
    trials=0; candidates=0; max_rel=0
    for k in range(3,9):
        for rep in range(28):
            bridgecount=rep%4
            B=30+rng.random()*100
            cs=[0.2+6*rng.random() for _ in range(k)]
            bc=[0.2+6*rng.random() for _ in range(bridgecount)]
            if rep%7==0:
                cs[0]=sum(cs[1:])*(0.75+0.5*rng.random())
            N=k+bridgecount
            Bc=B*(k-1)/(N-1)
            ww=cycle_allocation(cs,Bc)
            bw=[B/((N-1)*c) for c in bc]
            spent=sum(a*b for a,b in zip(cs,ww))+sum(a*b for a,b in zip(bc,bw))
            assert abs(spent-B)<3e-10*B,(N,rep,spent,B)
            good=float(tau_unicyclic(ww,bw))
            assert good>0
            totalprices=cs+bc
            for _ in range(40):
                numbers=[rng.random()+0.02 for _ in range(N)]
                factor=B/sum(a*x for a,x in zip(totalprices,numbers))
                test=[factor*x for x in numbers]
                other=float(tau_unicyclic(test[:k],test[k:]))
                if other>good: max_rel=max(max_rel,other/good-1)
                assert other<=good*(1+1e-9),('violated',cs,bc,ww,bw,test,other,good)
                candidates+=1
            # Verify exact formula for positive-cycle-edge inclusion probabilities and KKT.
            if min(ww)>1e-9:
                res=[1/w for w in ww];S=sum(res)
                lam=(N-1)/B
                for i in range(k):
                    diff=res[i]*(1-res[i]/S)
                    assert abs(diff-lam*cs[i])<1e-8*(1+lam*cs[i])
            else:
                j=min(range(k),key=lambda i:ww[i]); assert cs[j]>=sum(cs)-cs[j]
            trials+=1
    return trials,candidates,max_rel


def main():
    exact=verify_exact()
    trials,candidates,max_rel=verify_random()
    print('EXACT_GRAPH_DETERMINANTS_OK:',exact)
    print('RANDOM_UNICYCLIC_INSTANCES_OK:',trials)
    print('FEASIBLE_COMPETITORS_CHECKED:',candidates)
    print('MAX_COMPETITOR_OPTIMUM_RELATIVE_EXCESS:',format(max_rel,'.6g'))
    print('VERIFICATION_OK')

if __name__=='__main__':main()
