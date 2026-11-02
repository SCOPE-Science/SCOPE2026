#!/usr/bin/env python3
"""Exact four-periodic BDF3 Schur certificate; Python standard library only."""
from fractions import Fraction
from pathlib import Path
from itertools import product
import hashlib

N = 4
ZERO_EXP = (0, 0, 0, 0)

def const(v):
    return {} if v == 0 else {ZERO_EXP: int(v)}

def variable(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): 1}

def add(*args):
    out = {}
    for p in args:
        for m, c in p.items():
            out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}

def neg(p):
    return {m: -c for m, c in p.items()}

def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            exp = tuple(x+y for x,y in zip(ma,mb))
            out[exp] = out.get(exp, 0) + ca*cb
    return {m: c for m,c in out.items() if c}

def square(a):
    return mul(a,a)

def scale(p,v):
    return {m:c*v for m,c in p.items()}

def matmul(A,B):
    return [[add(mul(A[i][0], B[0][j]), mul(A[i][1],B[1][j]))
             for j in range(2)] for i in range(2)]

def schur_polynomials():
    h = [variable(i) for i in range(4)]
    one, zero = const(1), const(0)
    F = [[one,zero],[zero,one]]
    delta, eps = one,one
    for i in range(4):
        a,b,c = h[i],h[(i-1)%4],h[(i-2)%4]
        d = add(scale(square(a),3),scale(mul(a,b),4),scale(mul(a,c),2),square(b),mul(b,c))
        D = mul(mul(mul(b,c),add(b,c)),d)
        K = add(square(a),scale(mul(a,b),4),scale(mul(a,c),2),
                scale(square(b),3),scale(mul(b,c),3),square(c))
        P = mul(mul(square(a),c),K)
        U = mul(mul(square(a),b),square(add(a,b)))
        F = matmul([[P,neg(U)],[D,zero]],F)
        delta = mul(delta,D)
        eps = mul(eps,U)
    trace = add(F[0][0],F[1][1])
    return {'minus':add(delta,neg(trace),eps),
            'plus':add(delta,trace,eps),
            'det':add(delta,neg(eps))}

def export_rows(polys):
    rows=['inequality\texp_x\texp_y\texp_z\texp_w\tcoefficient']
    for name in ('minus','plus','det'):
        for expo,c in sorted(polys[name].items(),reverse=True):
            rows.append(name+'\t'+'\t'.join(map(str,expo))+'\t'+str(c))
    return '\n'.join(rows)+'\n'

def direct_lagrange_pq(a,b,c):
    t=[Fraction(0),-a,-a-b,-a-b-c]
    alpha=[]
    for j in range(4):
        if j==0:
            alpha.append(sum((Fraction(1,-t[k]) for k in (1,2,3)),Fraction(0)))
        else:
            num=Fraction(1)
            den=Fraction(1)
            for k in range(4):
                if k!=j:
                    den*=t[j]-t[k]
                if k>0 and k!=j:
                    num*=-t[k]
            alpha.append(num/den)
    return ((alpha[2]+alpha[3])/alpha[0],alpha[3]/alpha[0])

def closed_pq(a,b,c):
    d=3*a*a+4*a*b+2*a*c+b*b+b*c
    D=b*c*(b+c)*d
    P=a*a*c*(a*a+4*a*b+2*a*c+3*b*b+3*b*c+c*c)
    U=a*a*b*(a+b)*(a+b)
    return P/D,-U/D

def main():
    polys=schur_polynomials()
    expected={'minus':(271,6),'plus':(267,6),'det':(271,3)}
    for name,(count,mincoef) in expected.items():
        p=polys[name]
        assert len(p)==count,(name,len(p))
        assert min(p.values())==mincoef,(name,min(p.values()))
        assert all(c>0 for c in p.values()),name
        assert {sum(e) for e in p}=={20},name
    content=export_rows(polys).encode('utf-8')
    path=Path(__file__).resolve().parent/'certificates'/'schur_coefficients.tsv'
    assert path.read_bytes()==content,'Coefficient certificate differs from exact expansion'
    # The coefficient check is exhaustive, not sampling.  The following
    # rational checks independently test the interpolation normalization.
    samples=[(1,1,1),(2,3,5),(5,1,7),(1,17,2),(3,29,1),(11,13,17),
             (1,1,23),(31,1,1)]
    for h in samples:
        x=tuple(map(Fraction,h))
        assert direct_lagrange_pq(*x)==closed_pq(*x),h
    print('PASS: three homogeneous degree-20 Schur polynomials')
    for name in ('minus','plus','det'):
        print(f'  {name}: {len(polys[name])} coefficients, all positive, min {min(polys[name].values())}')
    print('PASS: exhaustive coefficient table, eight rational interpolation tests')
    print('certificate_sha256='+hashlib.sha256(content).hexdigest())

if __name__=='__main__':
    main()
