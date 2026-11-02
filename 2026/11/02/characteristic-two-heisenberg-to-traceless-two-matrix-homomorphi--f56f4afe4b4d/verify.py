#!/usr/bin/env python3
"""Direct exhaustive Lie-homomorphism tests; no external packages."""
from itertools import product
from collections import Counter

def make_field(q):
    if q in (2,3):
        add = lambda a,b:(a+b)%q
        sub = lambda a,b:(a-b)%q
        mul = lambda a,b:(a*b)%q
        return add,sub,mul
    if q==4:
        add=lambda a,b:a^b
        sub=add
        def mul(a,b):
            c=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):c ^= 1<<(i+j)
            if c&8:c^=0b1001
            if c&4:c^=0b111
            return c
        return add,sub,mul
    raise ValueError(q)

def bracket(X,Y,q,add,sub,mul):
    a,b,c=X; d,e,f=Y
    h=sub(mul(b,f),mul(c,e))
    ee=mul(2%(2 if q==4 else q),sub(mul(a,e),mul(d,b)))
    ff=mul(2%(2 if q==4 else q),sub(mul(c,d),mul(f,a)))
    return (h,ee,ff)

def candidate(img,n,q,add,sub,mul):
    if q%2==1:
        if img[2*n]!=(0,0,0):return False
        for i in range(2*n):
            for j in range(i+1,2*n):
                if bracket(img[i],img[j],q,add,sub,mul)!=(0,0,0):return False
        return True
    if n==1:return img[2]==bracket(img[0],img[1],q,add,sub,mul)
    if img[2*n]!=(0,0,0):return False
    for i in range(2*n):
        for j in range(i+1,2*n):
            if bracket(img[i],img[j],q,add,sub,mul)!=(0,0,0):return False
    return True

def actual(img,n,q,add,sub,mul):
    Z=img[-1]
    for i in range(2*n):
        if bracket(img[i],Z,q,add,sub,mul)!=(0,0,0):return False
    for i in range(2*n):
        for j in range(i+1,2*n):
            expected=Z if j==n+i and i<n else (0,0,0)
            if bracket(img[i],img[j],q,add,sub,mul)!=expected:return False
    return True

def image_rank(images,q,add,sub,mul):
    rows=[list(row) for row in zip(*images)]
    piv=0
    nc=len(images)
    for col in range(nc):
        ip=next((i for i in range(piv,3) if rows[i][col]!=0),None)
        if ip is None: continue
        rows[ip],rows[piv]=rows[piv],rows[ip]
        x=rows[piv][col]
        inverse=next(v for v in range(1,q) if mul(v,x)==1)
        rows[piv]=[mul(z,inverse) for z in rows[piv]]
        for j in range(3):
            if j==piv:continue
            factor=rows[j][col]
            if factor:
                rows[j]=[sub(z,mul(factor,w)) for z,w in zip(rows[j],rows[piv])]
        piv+=1
        if piv==3:break
    return piv

def expected_rank_counts(n,q):
    if q%2:
        return {0:1,1:expected_count(n,q)-1}
    if n>=2:
        t=q**(2*n)
        return {0:1,1:(t-1)*(q*q+q+1),2:(t-q)*(q+1)*(t-1)}
    t=(q-1)*(q+1)**2
    return {0:1,1:q*q-1+q*t,2:(q*q-q)*t,3:q*q*(q*q-1)*(q*q-q)}

def expected_count(n,q):
    return (1+(q**3-1)*(q**(2*n)-1)//(q-1)) if q%2 else (q**6 if n==1 else q**(2*n)*(1+(q+1)*(q**(2*n)-1)))

def exhaustive(n,q):
    add,sub,mul=make_field(q)
    good=0; comps=0; ranks=Counter()
    for flat in product(range(q),repeat=3*(2*n+1)):
        img=list(zip(*[iter(flat)]*3))
        correct=actual(img,n,q,add,sub,mul)
        predicted=candidate(img,n,q,add,sub,mul)
        if correct!=predicted:
            raise AssertionError(('classification',q,n,img,correct,predicted))
        good+=correct; comps+=1
        if correct:ranks[image_rank(img,q,add,sub,mul)]+=1
    expect=expected_count(n,q)
    assert good==expect,(q,n,good,expect)
    assert dict(ranks)==expected_rank_counts(n,q), (q,n,ranks,expected_rank_counts(n,q))
    print(f'EXHAUSTIVE q={q} n={n} maps={comps} homomorphisms={good} rank_counts={dict(sorted(ranks.items()))} exact_formula={expect}')

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(2,2),(1,4)]:exhaustive(n,q)
    print('HEISENBERG_TO_SL2_HOM_OK 4 exhaustive field/rank cases')
