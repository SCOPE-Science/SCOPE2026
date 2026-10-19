#!/usr/bin/env python3
"""Checks explicit low-support dihedral convolution ranks in finite fields.

The general theorem is analytic. Residue-field tests are corroborative and
are not assertions about characteristic-zero ranks without the proof.
"""

def prime(q):
    if q < 2: return False
    for t in range(2, int(q**0.5)+1):
        if q%t==0: return False
    return True

def field(p):
    for k in range(10, 2000):
        q=k*p+1
        if prime(q):
            for g in range(2, q):
                z=pow(g,(q-1)//p,q)
                if z != 1 and pow(z,p,q)==1:
                    return q,z
    raise AssertionError("no field")

def mul(x,y,p):
    a,e=x; b,d=y
    return ((a+(-1 if e else 1)*b)%p,e^d)

def rank_mod(mat,q):
    a=[row[:] for row in mat]; n=len(a); m=len(a[0]); r=0
    for c in range(m):
        ix=next((i for i in range(r,n) if a[i][c]%q),None)
        if ix is None: continue
        a[r],a[ix]=a[ix],a[r]
        t=pow(a[r][c]%q,-1,q)
        a[r]=[(v*t)%q for v in a[r]]
        for i in range(r+1,n):
            h=a[i][c]%q
            if h: a[i]=[(u-h*v)%q for u,v in zip(a[i],a[r])]
        r+=1
        if r==n: break
    return r

def regular_rank(p,q,weights):
    pts=[(a,e) for e in range(2) for a in range(p)]
    loc={v:i for i,v in enumerate(pts)}
    mat=[[0]*(2*p) for _ in pts]
    for col,x in enumerate(pts):
        for g,v in weights.items():
            mat[loc[mul(g,x,p)]][col]=(mat[loc[mul(g,x,p)]][col]+v)%q
    return rank_mod(mat,q)

def cyclo_zero(coeffs):
    # An integer Laurent expression in a primitive p-th root is zero precisely
    # when all p folded coefficients are identical.
    return len(set(coeffs)) == 1

def profile_test(p):
    q,z=field(p)
    const=[{(0,0):1},
           {(0,0):1,(0,1):-1},
           {(0,0):pow(z,3,q),(1,0):-(z+z*z),(2,0):1},
           {(0,0):1,(1,0):-1,(0,1):-1,(1,1):1}]
    got=[regular_rank(p,q,w) for w in const]
    target=[2*p,p,2*p-4,p-1]
    assert got==target,(p,q,z,got,target)
    # Exact cyclotomic-integer verification of the three-tap interpolation.
    # Value at frequency j is zeta^(2j) - zeta^(1+j) -
    # zeta^(2+j) + zeta^3, reduced modulo zeta^p = 1.
    roots=[]
    for j in range(p):
        coeff=[0]*p
        for exponent,scalar in [(2*j,1),(1+j,-1),(2+j,-1),(3,1)]:
            coeff[exponent%p]+=scalar
        if cyclo_zero(coeff): roots.append(j)
    assert roots==[1,2],(p,roots)
    print(f'p={p}: residue field={q}, ranks={got}, exact cyclotomic zeros={roots}')

if __name__=='__main__':
    for p in (5,7,11,13,17): profile_test(p)
    print('CHECK_OK: examples, not an infinite verification')
