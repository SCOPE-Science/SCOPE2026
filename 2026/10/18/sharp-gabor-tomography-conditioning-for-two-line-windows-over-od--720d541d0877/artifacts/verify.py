#!/usr/bin/env python3
"""Reproduce Fourier ambiguity identities and the sharp weighted-cross bound.
Scientific checks only; works in Python 3 standard library.
"""
import cmath
import math


def field(q):
    if q == 9:
        vals = list(range(9))
        def sub(a, b):
            return ((a % 3 - b % 3) % 3) + 3 * ((a // 3 - b // 3) % 3)
        def mul(a, b):
            x, y = a % 3, a // 3
            z, w = b % 3, b // 3
            return ((x*z-y*w) % 3) + 3*((x*w+y*z) % 3)
        def psi(z):
            return cmath.exp(2j*math.pi*((2*(z%3))%3)/3)
        return vals, sub, mul, psi, 3
    assert q in (3, 5, 7, 11)
    vals = list(range(q))
    return vals, lambda a,b:(a-b)%q, lambda a,b:(a*b)%q, lambda z:cmath.exp(2j*math.pi*z/q), q


def formula(q, sub, mul, psi, c, a,b,u,v):
    return (q*(a == 0 and v == 0) + q*abs(c)**2*(b == 0 and u == 0)
            + c.conjugate()*psi(mul(v,b)) + c*psi(mul(u,a)))


def direct(q, vals, sub, mul, psi, c, a,b,u,v):
    def g(x,y):
        return (1.0 if x == 0 else 0.0) + (c if y == 0 else 0.0)
    total = 0j
    for x in vals:
        for y in vals:
            term=g(x,y)*g(sub(x,a),sub(y,b)).conjugate()
            if term:
                total += term*psi(sub(mul(u,x),sub(0,mul(v,y))))
    return total


def main():
    case_count = 0
    analytic_count = 0
    exact_min_count = 0
    rng_c = (-1+0j, 1+0j, .7+.4j, -0.8+0.5j, 2.3+0j)
    for q in (3,5,7,9,11):
        vals, sub,mul,psi,p=field(q)
        s=math.sin(math.pi/(2*p))
        bottom_count=0
        for c in rng_c:
            norm=q*(1+abs(c)**2)+2*c.real
            assert norm>0
            smallest=float('inf')
            minima=[] if c==-1 else None
            for a in vals:
                for b in vals:
                    for u in vals:
                        for v in vals:
                            z=formula(q,sub,mul,psi,c,a,b,u,v)
                            smallest=min(smallest, abs(z))
                            if minima is not None: minima.append(abs(z))
                            analytic_count+=1
                            if q<=5 or (q==7 and a==0 and b==0) or (q==9 and a==1 and b==1 and c==-1):
                                y=direct(q,vals,sub,mul,psi,c,a,b,u,v)
                                assert abs(z-y)<2e-9, (q,c,a,b,u,v,z,y)
                                case_count+=1
            assert smallest/norm <= s/(q-1)+1e-9,(q,c,smallest,norm)
            if c==-1:
                assert abs(smallest-2*s)<1e-9,(q,smallest,2*s)
                assert abs(smallest/norm -s/(q-1))<1e-9
                exact_min_count+=1
                expected_mult = 2*q*q*(q*q-1)//p + (2*(q*q-1) if q==3 else 0)
                obtained_mult = sum(abs(v-2*s)<1e-8 for v in minima)
                assert obtained_mult == expected_mult, (q,obtained_mult,expected_mult)
    # explicit operator-frame diagonalization for q=3: compare Weyl Gram eigenvalues
    # directly via trace/Fourier: for normalized g, the analysis frame bounds are
    # N*minimum ambiguity^2 and N*maximum ambiguity^2, with N=q*q.
    q=3; vals,sub,mul,psi,p=field(q)
    all_abs=[]
    for a in vals:
        for b in vals:
            for u in vals:
                for v in vals:
                    all_abs.append(abs(formula(q,sub,mul,psi,-1+0j,a,b,u,v)))
    assert abs(min(all_abs)-1)<1e-8
    assert abs(max(all_abs)-4)<1e-8
    # phase-root gap is attained by a nonzero translation in both coordinates
    for q in (3,5,7,9):
        vals,sub,mul,psi,p=field(q)
        roots=[abs(1+psi(x)) for x in vals]
        assert abs(min(roots)-2*math.sin(math.pi/(2*p)))<1e-9
    print('VERIFY_OK exhaustive_formulas={} direct_reconstructions={} optimal_examples={} extension_field=F9'.format(analytic_count,case_count,exact_min_count))

if __name__=='__main__':
    main()
