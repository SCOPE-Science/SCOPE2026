from itertools import permutations
from fractions import Fraction
from math import comb, factorial
from collections import Counter


def total_depth_and_depthmax(seq):
    nodes={}
    root=None
    total=0
    maxdepth=0
    for x in seq:
        if root is None:
            root=x; nodes[x]=[None,None,0]; continue
        q=root
        while True:
            left=x<q; idx=0 if left else 1
            if nodes[q][idx] is None:
                d=nodes[q][2]+1
                nodes[q][idx]=x; nodes[x]=[None,None,d]
                total+=d
                if x==len(seq):maxdepth=d
                break
            q=nodes[q][idx]
    return total,maxdepth

def factorial_cdf_depth(t):
    # Records in first t-1 positions
    d={0:Fraction(1)}
    for j in range(1,t):
        e={}
        for k,p in d.items():
            e[k]=e.get(k,0)+p*Fraction(j-1,j)
            e[k+1]=e.get(k+1,0)+p*Fraction(1,j)
        d=e
    return d

for n in range(2,9):
    N=factorial(n-1)
    hist=[Counter() for _ in range(n+1)]
    joint=[Counter() for _ in range(n+1)]
    strict=[0]*(n+1)
    cond_expect=[]
    for tau in permutations(range(1,n)):
        base,_=total_depth_and_depthmax(tau)
        deltas=[]
        for t in range(1,n+1):
            seq=tau[:t-1]+(n,)+tau[t-1:]
            total,depth=total_depth_and_depthmax(seq)
            delta=total-base
            records=0
            cur=0
            for v in tau[:t-1]:
                if v>cur:cur=v; records+=1
            expected=records+(n-1-cur)
            assert delta==expected,(n,t,tau,delta,expected)
            hist[t][delta]+=1
            joint[t][(records,n-1-cur)]+=1
            deltas.append(delta)
        for t in range(1,n):
            assert deltas[t-1]>=deltas[t],(n,t,tau,deltas)
            if deltas[t-1]>deltas[t]:strict[t]+=1
    for t in range(1,n+1):
        empirical=Fraction(sum(v*c for v,c in hist[t].items()),N)
        H=sum(Fraction(1,j) for j in range(1,t))
        theoretical=H+Fraction(n-t,t)
        assert empirical==theoretical,(n,t,empirical,theoretical)
        dm=factorial_cdf_depth(t)
        ss={n-1:Fraction(1)} if t==1 else {s-1:Fraction(comb(n-s-1,t-2),comb(n-1,t-1)) for s in range(1,n-t+2)}
        for (r,m),c in joint[t].items():
            assert Fraction(c,N)==dm.get(r,0)*ss.get(m,0),(n,t,r,m,c,dm,ss)
        for r in dm:
            for m in ss:
                assert Fraction(joint[t].get((r,m),0),N)==dm[r]*ss[m],(n,t,r,m)
    for t in range(1,n):
        assert Fraction(strict[t],N)==Fraction(n-t-1,(n-1)*t)
        for k in range(1,n+1):
            cnt=0
            for tau in permutations(range(1,n)):
                r=max(tau[:t-1],default=0)
                cnt+=(max(0,tau[t-1]-r-1)>=k)
            prob=Fraction(cnt,N)
            rhs=Fraction(comb(n-k-1,t), (n-1)*comb(n-2,t-1)) if n-k-1>=t else Fraction(0)
            assert prob==rhs,(n,t,k,prob,rhs)
    assert strict[n-1]==0
    assert all(strict[t]>0 for t in range(1,n-1))
    print('PASS n',n,'base permutations',N,'strict coupling counts',strict[1:n])
print('ALL PASS')
