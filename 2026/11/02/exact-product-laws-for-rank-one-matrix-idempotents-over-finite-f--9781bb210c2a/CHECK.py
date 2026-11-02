#!/usr/bin/env python3
"""Independent exact word enumeration of products of rank-one idempotents."""
from collections import Counter
from fractions import Fraction
from itertools import product

def vecs(n,q):
    return [v for v in product(range(q),repeat=n) if any(v)]

def reps(n,q):
    out=[]
    for v in vecs(n,q):
        i=next(i for i,x in enumerate(v) if x)
        inv=pow(v[i],-1,q)
        w=tuple((x*inv)%q for x in v)
        if w not in out: out.append(w)
    return out

def dot(a,b,q): return sum(x*y for x,y in zip(a,b))%q

def mat_mul(a,b,n,q):
    return tuple(sum(a[i*n+t]*b[t*n+j] for t in range(n))%q for i in range(n) for j in range(n))

def mat_trace(a,n,q):return sum(a[i*n+i] for i in range(n))%q

def nilpotent(a,n,q):
    z=tuple(0 for _ in range(n*n))
    p=a
    for _ in range(n-1): p=mat_mul(p,a,n,q)
    return p==z

def verify(n,q,kmax):
    lines=reps(n,q); N=(q**n-1)//(q-1)
    assert len(lines)==N
    E=set()
    for u in lines:
        for v in product(range(q),repeat=n):
            if dot(v,u,q)==1:
                e=tuple((u[i]*v[j])%q for i in range(n) for j in range(n))
                E.add(e)
    E=sorted(E)
    assert len(E)==N*q**(n-1)
    assert all(mat_mul(x,x,n,q)==x for x in E)
    R={tuple((u[i]*v[j])%q for i in range(n) for j in range(n))
       for u in lines for v in vecs(n,q)}
    assert len(R)==N*(q**n-1)
    T=len(E)
    z=tuple(0 for _ in range(n*n))
    distribution=Counter({x:1 for x in E})
    s=Fraction(q**(n-1),N)
    t=Fraction(1,q*N)
    for k in range(1,kmax+1):
        if k>1:
            d=Counter()
            for a,frequency in distribution.items():
                for e in E:
                    d[mat_mul(a,e,n,q)]+=frequency
            distribution=d
        assert sum(distribution.values())==T**k
        prob_zero=Fraction(distribution[z],T**k)
        prob_nil=Fraction(sum(v for x,v in distribution.items() if nilpotent(x,n,q)),T**k)
        prob_non_nil=1-prob_nil
        formula_non_nil=s**k+(N-1)*t**k
        formula_zero=1-s**(k-1)
        assert prob_non_nil==formula_non_nil,(n,q,k,prob_non_nil,formula_non_nil)
        assert prob_zero==formula_zero,(n,q,k,prob_zero,formula_zero)
        d=Fraction(1,N**(k-1))
        c=formula_non_nil
        for scalar in range(1,q):
            observed=Fraction(sum(freq for a,freq in distribution.items() if mat_trace(a,n,q)==scalar),T**k)
            predicted=(c-d)/(q-1) + (d if scalar==1 else 0)
            assert observed==predicted,(n,q,k,scalar,observed,predicted)
        nonzero_nil=Fraction(sum(freq for a,freq in distribution.items() if a!=z and nilpotent(a,n,q)),T**k)
        assert nonzero_nil==s**(k-1)-c
        # Complete pointwise distribution, including zeros of absent probability.
        for a in R:
            scalar=mat_trace(a,n,q)
            if scalar==0:
                pmass=(s**(k-1)-c)/(N*(q**(n-1)-1))
            else:
                pmass=((c-d)/(q-1)+(d if scalar==1 else 0))/(N*q**(n-1))
            assert Fraction(distribution[a],T**k)==pmass,(n,q,k,scalar,a)
        assert all(a in R or a==z for a in distribution)
        tv=sum((abs(Fraction(distribution[x],T**k)/s**(k-1)-Fraction(1,len(R))) for x in R),Fraction())/2
        pred_tv=((N-1)*t**k+(q-2)*d)/((q-1)*s**(k-1))
        assert tv==pred_tv,(n,q,k,tv,pred_tv)
        # Conjugation orbits are uniform: all rank-one outputs of a fixed trace have same count.
        for scalar in range(q):
            counters={freq for a,freq in distribution.items() if a!=z and mat_trace(a,n,q)==scalar}
            assert len(counters)<=1, (n,q,k,scalar,counters)
        print(f'n={n} q={q} k={k} idempotents={T} zero={prob_zero} nonzero_nil={prob_nil-prob_zero} nonnil={prob_non_nil}')
    # Independently count every cyclic sequence of projective image lines, with local weights.
    if N<=7:
        b=Fraction(q-1,q)
        for k in range(1,min(kmax,5)+1):
            total=sum((b**sum(lines[seq[i]]!=lines[seq[(i+1)%k]] for i in range(k))
                       for seq in product(range(N),repeat=k)),Fraction())
            assert total/N**k==s**k+(N-1)*t**k
    print(f'PASS n={n} q={q} lengths=1..{kmax}')

if __name__=='__main__':
    verify(2,2,7)
    verify(2,3,6)
    verify(3,2,5)
    print('VERIFY_OK')
