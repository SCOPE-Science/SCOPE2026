#!/usr/bin/env python3
"""Independent checks for rank-enumerating nilpotents in uniform-chain centralizers.
Only the Python standard library is required."""
import itertools
from collections import Counter
from fractions import Fraction
from math import comb, factorial

def partial_injections(n):
    for k in range(n+1):
        for dom in itertools.combinations(range(n),k):
            for img in itertools.permutations(range(n),k):
                out=[-1]*n
                for x,y in zip(dom,img):out[x]=y
                yield tuple(out)

def compose(f,g):
    return tuple(-1 if g[x]<0 else f[g[x]] for x in range(len(g)))

def is_nilpotent(p):
    for x in range(len(p)):
        seen=set();y=x
        while y>=0:
            if y in seen:return False
            seen.add(y);y=p[y]
    return True

def alpha_uniform(c,L):
    a=[]
    for i in range(c):
        a.extend(list(range(i*L+1,(i+1)*L))+[-1])
    return tuple(a)

def brute(c,L):
    a=alpha_uniform(c,L)
    total=Counter();nils=Counter()
    for p in partial_injections(c*L):
        if compose(a,p)==compose(p,a):
            r=sum(x>=0 for x in p)
            total[r]+=1
            if is_nilpotent(p):nils[r]+=1
    return dict(total),dict(nils)

def matching(c,L):
    total=Counter();nils=Counter()
    def visit(i,used,targets,lengths,rank):
        if i==c:
            total[rank]+=1
            for x in range(c):
                seen=set();v=x
                while v in targets:
                    if v in seen:
                        # A cyclic component induces an actual permutation precisely
                        # if all selected chain-prefix lengths equal L.
                        cyc=[];u=v
                        while True:
                            cyc.append(u);u=targets[u]
                            if u==v:break
                        if all(lengths[u]==L for u in cyc):return
                        break
                    seen.add(v);v=targets[v]
            nils[rank]+=1
            return
        visit(i+1,used,targets,lengths,rank)
        for j in range(c):
            if used&(1<<j):continue
            targets[i]=j
            for t in range(1,L+1):
                lengths[i]=t
                visit(i+1,used|1<<j,targets,lengths,rank+t)
            del targets[i];del lengths[i]
    visit(0,0,{}, {},0)
    return dict(total),dict(nils)

def add(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return c

def sub(a,b):return add(a,[-x for x in b])
def mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def analytic(c,L):
    # E(z)=exp(z/(1-wz)); w(v)=v+...+v^L.
    # nilpotent EGF = E(z)*(1-v^L z)/(1-w z).
    # all-centralizer EGF = E(z)/(1-w z).
    w=[Fraction(0)]+[Fraction(1)]*L
    wp=[[Fraction(1)]]
    for i in range(1,c+1):wp.append(mul(wp[-1],w))
    E=[[Fraction(1)]]
    for n in range(1,c+1):
        s=[Fraction(0)]
        for k in range(n):
            t=mul(wp[k],E[n-1-k]);s=add(s,[(k+1)*x for x in t])
        E.append([x/n for x in s])
    total=E[c][:];nil=E[c][:]
    vL=[Fraction(0)]*L+[Fraction(1)]
    for j in range(1,c+1):
        total=add(total,mul(wp[j],E[c-j]))
        nil=add(nil,mul(sub(wp[j],mul(vL,wp[j-1])),E[c-j]))
    total=[x*factorial(c) for x in total]
    nil=[x*factorial(c) for x in nil]
    assert all(x.denominator==1 for x in total+nil)
    return ({i:int(v) for i,v in enumerate(total) if v},
            {i:int(v) for i,v in enumerate(nil) if v})

for c,L in [(1,1),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
    B=brute(c,L);F=analytic(c,L);M=matching(c,L)
    assert B==F==M,(c,L,B,F,M)
    print(f'c={c} L={L} n={c*L} commuting={sum(B[0].values())} nilpotent={sum(B[1].values())} rank_profiles=PASS')
for c in range(1,6):
    for L in range(1,5):
        A=analytic(c,L)
        if c<=4:assert A==matching(c,L),(c,L,A)
        assert sum(A[0].values())==sum(comb(c,k)**2*factorial(k)*L**k for k in range(c+1))
print('VERIFY_OK_UNIFORM_CHAIN_CENTRALIZER_RANK_PROFILES')
