#!/usr/bin/env python3
"""Independent small finite-field checks of the commutator-fiber formulas.

Run: python verify.py
Uses only Python's standard library, including an explicit GF(4) model.
"""
from collections import Counter
from itertools import product


def field_ops(q):
    if q in (2, 3, 5):
        return (lambda a,b:(a+b)%q), (lambda a,b:(a-b)%q), (lambda a,b:a*b%q), (q if q != 4 else 2)
    assert q in (4,9)
    if q == 9:
        def add9(a,b): return (a%3+b%3)%3+3*((a//3+b//3)%3)
        def sub9(a,b): return (a%3-b%3)%3+3*((a//3-b//3)%3)
        def mul9(a,b): return ((a%3)*(b%3)-(a//3)*(b//3))%3 + 3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        return add9,sub9,mul9,3
    def mul(a,b):
        x=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):
                    x ^= (1 << (i+j))
        if x&8:
            x ^= 0b1100   # z^3=z^2+z, relation z^2=z+1
        if x&4:
            x ^= 0b111
        return x
    return (lambda a,b:a^b), (lambda a,b:a^b), mul, 2


def make_ring(q,n):
    add, sub, mul, p=field_ops(q)
    elems=list(product(range(q),repeat=n))
    nums={x:i for i,x in enumerate(elems)}
    zero=nums[(0,)*n]
    plus=[[0]*len(elems) for _ in elems]
    minus=[[0]*len(elems) for _ in elems]
    times=[[0]*len(elems) for _ in elems]
    for i,a in enumerate(elems):
        for j,b in enumerate(elems):
            plus[i][j]=nums[tuple(add(a[t],b[t]) for t in range(n))]
            minus[i][j]=nums[tuple(sub(a[t],b[t]) for t in range(n))]
            c=[0]*n
            for k in range(n):
                for r in range(k+1):
                    c[k]=add(c[k],mul(a[r],b[k-r]))
            times[i][j]=nums[tuple(c)]
    val=[next((t for t in range(n) if a[t]),n) for a in elems]
    scalar2=nums[(2%p,)+(0,)*(n-1)] if p!=2 else zero
    return elems,plus,minus,times,val,zero,scalar2,p


def formula_fiber(q,n,p,z_val,z_central=True):
    if p!=2:
        if z_val==n:
            return q**(3*n-2)*((q*q+q+1)*q**n-(q+1))
        return q**(3*n-2)*(q+1)*(q**(z_val+1)-1)
    if not z_central:
        return 0
    if z_val==n:
        return q**(4*n-1)*((q+1)*q**n-1)
    # Equivalent integral form of (q+1)*q^(5n-1)*(1-q^(-z_val-1)).
    return (q*q-1)*sum(q**(5*n-2-i) for i in range(z_val+1))


def verify(q,n):
    es,plus,minus,times,val,zero,two,p=make_ring(q,n)
    R=len(es)
    elems=list(product(range(R),repeat=3))
    hist=Counter()
    images={}
    for x in elems:
        a,b,c=x
        xs=set()
        for y in elems:
            A,B,C=y
            # sl2 structure: [h,e]=2e, [h,f]=-2f, [e,f]=h
            E=times[two][minus[times[c][A]][times[a][C]]]
            F=times[two][minus[times[b][C]][times[c][B]]]
            H=minus[times[a][B]][times[b][A]]
            z=(E,F,H)
            hist[z]+=1
            xs.add(z)
        images[x]=len(xs)
    for z in elems:
        v=min(val[t] for t in z)
        exp=formula_fiber(q,n,p,v,z[0]==zero and z[1]==zero)
        assert hist[z]==exp,(q,n,z,hist[z],exp)
    for x in elems:
        if p != 2:
            i=min(val[t] for t in x)
            predicted=q**(2*(n-i))
        else:
            i=min(val[x[0]],val[x[1]])
            predicted=q**(n-i)
        assert images[x]==predicted,(q,n,x,images[x],predicted)
    assert sum(hist.values())==q**(6*n)
    zero_z=(zero,zero,zero)
    num_nonzero=sum(1 for z in elems if z!=zero_z and hist[z])
    print(f'PASS q={q} n={n} characteristic={p} pairs={q**(6*n)} '
          f'nonzero_target_vectors={num_nonzero} commuting_pairs={hist[zero_z]}')


def verify_integer_ring(p,n):
    """Directly enumerate matrices over Z/(p**n), a mixed-char chain ring."""
    modulus=p**n
    R=range(modulus)
    E=list(product(R,repeat=3))
    counts=Counter()
    images={}
    def valuation(a):
        if a==0:return n
        v=0
        while a%p==0:
            a//=p;v+=1
        return v
    for x in E:
        a,b,c=x
        outputs=set()
        for y in E:
            A,B,C=y
            z=(2*(c*A-a*C)%modulus,2*(b*C-c*B)%modulus,(a*B-b*A)%modulus)
            counts[z]+=1
            outputs.add(z)
        images[x]=len(outputs)
    for z in E:
        v=min(valuation(t) for t in z)
        expected=formula_fiber(p,n,p,v)
        assert counts[z]==expected,('mixed',p,n,z,counts[z],expected)
    for x in E:
        v=min(valuation(t) for t in x)
        assert images[x]==p**(2*(n-v)),('mixed image',p,n,x)
    print(f'PASS mixed-characteristic Z/{modulus}Z pairs={modulus**6} '
          f'commuting_pairs={counts[(0,0,0)]}')


def main():
    for q,n in ((2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(5,1),(9,1)):
        verify(q,n)
    for p,n in ((3,2),(3,1),(5,1)):
        verify_integer_ring(p,n)
    print('TAKIFF_SL2_COMMUTATOR_FIBERS_OK')

if __name__=='__main__':
    main()
