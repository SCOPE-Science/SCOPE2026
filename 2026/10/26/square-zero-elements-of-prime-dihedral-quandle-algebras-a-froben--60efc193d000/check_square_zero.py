#!/usr/bin/env python3
"""Self-contained finite-field and quandle-algebra square-zero checks.

For a prime p not dividing q, compare the exact Fourier-orbit census
against exhaustive coefficient-vector enumeration in F_q[R_p].
"""
from itertools import product
from math import comb

# Small finite fields use base-prime polynomial-coordinate encodings.
FIELDS = {
    2: (2, (0, 1)), 3: (3, (0, 1)), 5: (5, (0, 1)),
    7: (7, (0, 1)), 11: (11, (0, 1)),
    4: (2, (1, 1, 1)),       # a^2+a+1
    8: (2, (1, 1, 0, 1)),    # a^3+a+1
    9: (3, (1, 0, 1)),       # a^2+1
}

def tables(q):
    prime, modulus = FIELDS[q]
    degree = len(modulus)-1
    assert prime**degree == q and modulus[-1] == 1
    def digits(x):
        d=[]
        for _ in range(degree): d.append(x%prime); x//=prime
        return d
    def pack(ds): return sum(v*(prime**i) for i,v in enumerate(ds))
    vec=[digits(i) for i in range(q)]
    add=[[pack([(vec[a][i]+vec[b][i])%prime for i in range(degree)])
          for b in range(q)] for a in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            c=[0]*(2*degree-1)
            for i in range(degree):
                for j in range(degree): c[i+j]=(c[i+j]+vec[a][i]*vec[b][j])%prime
            for k in range(len(c)-1,degree-1,-1):
                w=c[k]
                for j in range(degree): c[k-degree+j]=(c[k-degree+j]-w*modulus[j])%prime
            row.append(pack(c[:degree]))
        mul.append(row)
    assert all(mul[a][0]==0 and mul[a][1]==a for a in range(q))
    return add,mul

def ord_mod(x,p):
    x%=p
    value=1
    for i in range(1,p):
        value=value*x%p
        if value==1: return i
    raise AssertionError('order not found')

def predicted(p,q):
    d=ord_mod(q,p)
    subgroup={pow(q,j,p) for j in range(d)}
    x=(-2)%p
    ell=next(j for j in range(1,p) if pow(x,j,p) in subgroup)
    assert (p-1)%(d*ell)==0
    ncyc=(p-1)//(d*ell)
    w=q**d-1
    cyc=0
    for j in range(ell//2+1):
        cyc+= (ell*comb(ell-j,j)//(ell-j)) * w**j
    return cyc**ncyc, (d,ell,ncyc)

def direct_count(p,q):
    add,mul=tables(q)
    # i*j := 2*j - i modulo p.
    ix=[[ (2*j-i)%p for j in range(p)] for i in range(p)]
    count=0
    for a in product(range(q),repeat=p):
        s=[0]*p
        for i in range(p):
            if a[i]:
                for j in range(p):
                    if a[j]: s[ix[i][j]]=add[s[ix[i][j]]][mul[a[i]][a[j]]]
        if not any(s): count+=1
    return count

def run():
    tests=[(3,2),(3,4),(3,5),(5,2),(5,3),(5,4),(5,7),(5,8),(5,11),
           (7,2),(7,3),(7,4),(11,2),(13,2)]
    for p,q in tests:
        want,params=predicted(p,q)
        got=direct_count(p,q)
        print(f'R_{p} over F_{q}: direct={got}, formula={want}, (d,ell,cycles)={params}')
        assert got==want, (p,q,want,got)
    print('ALL_DIHEDRAL_SQUARE_ZERO_TESTS_PASSED',len(tests))

if __name__=='__main__': run()
