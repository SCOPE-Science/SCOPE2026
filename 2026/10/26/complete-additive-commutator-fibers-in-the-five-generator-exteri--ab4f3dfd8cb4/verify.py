#!/usr/bin/env python3
"""Independent exterior-coordinate and linear-fiber checks for odd prime fields.
No external packages. Run python3 verify.py.
"""
import itertools,random,math
from collections import Counter
from functools import lru_cache

N=5
DEG={k:[m for m in range(1<<N) if m.bit_count()==k] for k in range(N+1)}
I2={m:i for i,m in enumerate(DEG[2])}
I4={m:i for i,m in enumerate(DEG[4])}

def wedge(m,n):
    if m&n:return (0,0)
    inv=sum(((n&((1<<i)-1)).bit_count()) for i in range(N) if (m>>i)&1)
    return ((-1 if inv%2 else 1),m|n)

def two(a,b,p):
    v=[0]*10
    for i,m in enumerate(DEG[1]):
        if not a[i]:continue
        for j,n in enumerate(DEG[1]):
            if not b[j]:continue
            z,mask=wedge(m,n)
            if z:v[I2[mask]]=(v[I2[mask]]+z*a[i]*b[j])%p
    return tuple(v)

def four_image_columns(a,b,p):
    res=[]
    for v in (a,b):
        for t in DEG[3]:
            col=[0]*5
            for i,m in enumerate(DEG[1]):
                z,mask=wedge(m,t)
                if z:col[I4[mask]]=(col[I4[mask]]+z*v[i])%p
            res.append(col)
    return res

def basis(cols,p):
    piv={}
    for col in cols:
        x=[int(z)%p for z in col]
        for i in sorted(piv):
            if x[i]:
                z=x[i]
                x=[(a-z*b)%p for a,b in zip(x,piv[i])]
        j=next((i for i,z in enumerate(x) if z),None)
        if j is None:continue
        d=pow(x[j],-1,p)
        piv[j]=[(z*d)%p for z in x]
    return piv

def member(piv,target,p):
    x=list(target)
    for i in sorted(piv):
        if x[i]:
            z=x[i];x=[(a-z*b)%p for a,b in zip(x,piv[i])]
    return not any(x)

def direct_beta(a,A,b,B,p):
    z=[0]*5
    for v,three in ((a,B),(A,b)):
        if len(v)==5:
            for i,m in enumerate(DEG[1]):
                for j,n in enumerate(DEG[3]):
                    s,t=wedge(m,n)
                    if s:z[I4[t]]=(z[I4[t]]+s*v[i]*three[j])%p
        else:
            for j,m in enumerate(DEG[3]):
                for i,n in enumerate(DEG[1]):
                    s,t=wedge(m,n)
                    if s:z[I4[t]]=(z[I4[t]]+s*v[j]*three[i])%p
    return tuple(z)

def check(p):
    rng=random.Random(310159+p)
    zero2=(0,)*10
    target2=two((1,0,0,0,0),(0,1,0,0,0),p)
    zero4=(0,)*5
    target4=(1,0,0,0,0)
    check_targets=[(zero2,zero4),(zero2,target4),(target2,zero4),(target2,target4)]
    sums={(u,v):0 for u,v in check_targets}
    values=range(p)
    count=0
    # Enumerate all degree-one pairs for q=3. q=5 uses targeted exhaustive
    # representative lines and prescribed exterior-product fibers, not full q^10.
    if p==3:
        vectors=list(itertools.product(values,repeat=5))
        pairs=itertools.product(vectors,repeat=2)
    else:
        vectors=list(itertools.product(values,repeat=5))
        # Every vector a, paired with b=lambda*a, and a selected independent b.
        pairs=((a,b) for a in vectors for b in itertools.chain(
            (tuple((t*x)%p for x in a) for t in values),
            (tuple((x+(i==0))%p for i,x in enumerate(a)),)))
    for a,b in pairs:
        count+=1
        t=two(a,b,p)
        applicable=[v for u,v in check_targets if t==u]
        if not applicable:continue
        span=basis(four_image_columns(a,b,p),p)
        ways=p**(20-len(span))
        for v in applicable:
            if member(span,v,p):sums[(t,v)]+=ways
        if count%10000==1:
            for _ in range(2):
                A=tuple(rng.randrange(p) for _ in DEG[3])
                B=tuple(rng.randrange(p) for _ in DEG[3])
                assert member(span,direct_beta(a,A,b,B,p),p)
    if p==3:
        H=(p**5-1)//(p-1);K=(p**4-1)//(p-1)
        expected={
            (zero2,zero4):p**20+H*(p*p-1)*p**16,
            (zero2,target4):K*(p*p-1)*p**16,
            (target2,zero4):p*(p*p-1)*p**15,
            (target2,target4):p*(p*p-1)*p**15,
        }
        assert sums==expected,(sums,expected)
    # independent direct exterior products validate signs and the odd-product computation
    for _ in range(1000):
        a=tuple(rng.randrange(p) for _ in range(5));b=tuple(rng.randrange(p) for _ in range(5))
        A=tuple(rng.randrange(p) for _ in range(10));B=tuple(rng.randrange(p) for _ in range(10))
        cols=four_image_columns(a,b,p)
        calc=[0]*5
        for j,x in enumerate(B):
            for i,v in enumerate(cols[j]):calc[i]=(calc[i]+x*v)%p
        for j,x in enumerate(A):
            for i,v in enumerate(cols[10+j]):calc[i]=(calc[i]-x*v)%p
        assert tuple(calc)==direct_beta(a,A,b,B,p)
    return count,sums

def full_commutator(x,y,p):
    out=[0]*32
    for m in range(32):
        if not x[m]:continue
        for n in range(32):
            if not y[n]:continue
            s,z=wedge(m,n)
            t,w=wedge(n,m)
            out[z]=(out[z]+s*x[m]*y[n])%p if s else out[z]
            if t:out[w]=(out[w]-t*x[m]*y[n])%p
    return tuple(out)

def full_test(p):
    rng=random.Random(p*2002)
    for _ in range(250):
        x=[rng.randrange(p) for _ in range(32)]
        y=[rng.randrange(p) for _ in range(32)]
        a=tuple(x[m] for m in DEG[1]);b=tuple(y[m] for m in DEG[1])
        A=tuple(x[m] for m in DEG[3]);B=tuple(y[m] for m in DEG[3])
        alpha=two(a,b,p)
        beta=direct_beta(a,A,b,B,p)
        want=[0]*32
        for i,m in enumerate(DEG[2]):want[m]=(2*alpha[i])%p
        for i,m in enumerate(DEG[4]):want[m]=(2*beta[i])%p
        assert full_commutator(x,y,p)==tuple(want)
if __name__=='__main__':
    for p in (3,5):
        full_test(p)
        checked,totals=check(p)
        print('field',p,'leading_pairs',checked,'target_cases',len(totals))
    for q in (3,5,7,9):
        D=(q**5-1)*(q*q+1)
        H=(q**5-1)//(q-1)
        K=(q**4-1)//(q-1)
        full=(D*q**5+K*(q**5-1)+H)*(q*q-1)*q**50+q**54
        assert full==q**64
        assert q**5*(1+D)==q**12+q**10-q**7
    print('VERIFY_OK_EXTERIOR5_COMMUTATOR_FIBERS')
