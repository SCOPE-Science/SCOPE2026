#!/usr/bin/env python3
"""Exact finite-state algebra for the four-site site-disordered exclusion chain.

Requires Python 3 and SymPy 1.12 or newer. Computations use rational integers,
not floating-point sampling. The code reconstructs all certificates from the
specified Markov generator, including boundary values and root-count signs.
"""
import json
import sympy as sp
from fractions import Fraction

u, v, rho, d, t, z = sp.symbols('u v rho d t z')
S = sp.Rational
RATES = (S(1), S(1, 4), S(1, 2), S(1))
Q = sp.zeros(16)
for x in range(16):
    occup = tuple((x >> i) & 1 for i in range(4))
    moves = [(x ^ 1, u if not occup[0] else 1-u),
             (x ^ 8, v if not occup[3] else 1-v)]
    for i in range(3):
        if occup[i] != occup[i+1]:
            moves.append((x ^ (3 << i), RATES[i] if occup[i] else RATES[i+1]))
    for y, rate in moves:
        Q[y, x] += rate
        Q[x, x] -= rate

A = Q.copy()
A[-1, :] = sp.ones(1, 16)
b = sp.zeros(16, 1)
b[-1] = 1
stationary = A.inv(method='DM') * b
assert all(sp.cancel(q) == 0 for q in (Q * stationary))
assert sp.cancel(sum(stationary) - 1) == 0
current = sp.factor(sum(
    stationary[x]*(RATES[1] if ((x >> 1)&3)==1
                   else -RATES[2] if ((x >> 1)&3)==2 else 0)
    for x in range(16)))
num, den = sp.fraction(current)
P = sp.cancel(num / (u-v))
assert sp.cancel(current - (u-v)*P/den) == 0
assert sp.Poly(P, u, v).total_degree() == 4
assert den.subs({u:0,v:0}) > 0

U, V = rho+d/2, rho-d/2
swap = lambda f, x, y: f.subs({u:x,v:y}, simultaneous=True)
# E=(u-v)*(P(u,v) D(v,u)-P(v,u) D(u,v))/(D(u,v)D(v,u)).
ex_num = sp.factor(d*(swap(P,U,V)*swap(den,V,U)-swap(P,V,U)*swap(den,U,V)))
f = sp.cancel(-ex_num/(4*d*d))
assert sp.Poly(f, rho, d).total_degree() <= 17
assert sp.cancel(ex_num + 4*d*d*f) == 0

R = (d/2+(1-d/2)*t)/(1+t)
h = sp.Poly(sp.cancel((1+t)**9*f.subs(rho, R)), t)
assert h.degree() == 9
cs = {k: sp.factor(h.nth(k)) for k in range(10)}

# Verify the accompanying human-readable polynomial certificate byte-content
# against independently regenerated exact symbolic expressions.
from pathlib import Path
certificate = json.loads((Path(__file__).parent / 'polynomial_certificate.json').read_text())
def from_terms(rows, variables):
    return sp.Add(*(sp.Rational(row['coefficient'])*sp.prod(
        var**int(deg) for var,deg in zip(variables,row['powers']))
        for row in rows))
assert sp.expand(from_terms(certificate['P_terms'],(u,v)) - P) == 0
assert sp.expand(from_terms(certificate['D_terms'],(u,v)) - den) == 0
assert sp.expand(from_terms(certificate['F_terms'],(rho,d)) - f) == 0
for k in range(10):
    assert sp.expand(from_terms(certificate['H_t_coefficients'][str(k)],(d,)) - cs[k]) == 0
# These coefficient inequalities prove strict positivity of the exact
# rational-current denominator and the polynomial numerator on [0,1]^2.
assert {mon: coeff for mon, coeff in sp.Poly(den,u,v).terms() if coeff<0} == {
    (3,3):sp.Integer(-6912), (2,3):sp.Integer(-23328)}
assert sp.Poly(den,u,v).coeff_monomial(u**2*v**2) == 651144
assert sp.Poly(den,u,v).coeff_monomial(1) > 0
assert all(c>0 for mon,c in sp.Poly(den,u,v).terms()
           if mon not in ((3,3),(2,3)))
assert {mon:coeff for mon,coeff in sp.Poly(P,u,v).terms() if coeff<0} == {
    (2,2):sp.Integer(-3408)}
assert sp.Poly(P,u,v).coeff_monomial(u**2*v) == 47258
assert sp.Poly(P,u,v).coeff_monomial(1) > 0
assert all(c>0 for mon,c in sp.Poly(P,u,v).terms() if mon != (2,2))
critical_poly = (413067648*d**6 + 18917449838*d**5 +
                 324236281277*d**4 + 2454897307300*d**3 +
                 6770005929628*d**2 - 1324169822640*d -
                 8093326579200)
assert sp.factor(cs[0] + critical_poly/2) == 0
assert sp.expand(from_terms(certificate['critical_polynomial_terms'],(d,))-critical_poly)==0

# For a polynomial p(d), the substitution d=z/(1+z) transfers roots
# in (0,1) to positive roots in z. Descartes counts these roots exactly
# when the sign variation is 0 or 1 and endpoint signs differ.
def transformed_signs(expr):
    p=sp.Poly(expr, d)
    N=p.degree()
    q=sp.Poly(sum(c*z**i*(1+z)**(N-i) for (i,),c in p.terms()), z)
    signs=[int(sp.sign(c)) for c in q.all_coeffs()]
    nonzero=[sgn for sgn in signs if sgn]
    changes=sum(nonzero[i]!=nonzero[i-1] for i in range(1,len(nonzero)))
    return signs, changes

bounds={5:(930915,930917),4:(974592,974595),
        3:(984394,984397),2:(988735,988738),
        1:(991185,991189),0:(992760,992763)}
for k in range(9,5,-1):
    signs, changes = transformed_signs(cs[k])
    assert changes == 0 and set(signs)=={-1}, (k,signs)
for k in range(5,-1,-1):
    signs, changes = transformed_signs(cs[k])
    assert changes == 1, (k,signs)
    assert cs[k].subs(d,0)>0 and cs[k].subs(d,1)<0
    lo,hi=bounds[k]
    assert cs[k].subs(d,S(lo,1000000))>0
    assert cs[k].subs(d,S(hi,1000000))<0
assert all(bounds[k][1] < bounds[k-1][0] for k in range(5,0,-1))
assert {str(k):list(bounds[k]) for k in bounds} == certificate['ordered_root_brackets_millionths']

# Exact endpoint under maximal contrast.
J10=sp.cancel(current.subs({u:1,v:0}))
J01=sp.cancel(current.subs({u:0,v:1}))
assert J10+J01 == S(3246744814,54087920537585)
assert J10+J01 == sp.Rational(certificate['maximal_contrast_even_current'])

# An independent exact-Fraction stationary calculation, with no symbolic inversion.
def exact_numeric(U,V):
    A=[[Fraction(0) for _ in range(16)] for _ in range(16)]
    for x in range(16):
        occ=[(x>>i)&1 for i in range(4)]
        rr=[Fraction(1), Fraction(1,4), Fraction(1,2), Fraction(1)]
        moves=[(x^1,U if not occ[0] else 1-U),
               (x^8,V if not occ[3] else 1-V)]
        for i in range(3):
            if occ[i] != occ[i+1]:
                moves.append((x^(3<<i),rr[i] if occ[i] else rr[i+1]))
        for y,rate in moves:
            A[y][x]+=rate
            A[x][x]-=rate
    A[-1]=[Fraction(1)]*16
    rhs=[Fraction(0)]*15+[Fraction(1)]
    for i in range(16):
        piv=next(j for j in range(i,16) if A[j][i])
        A[i],A[piv]=A[piv],A[i]
        rhs[i],rhs[piv]=rhs[piv],rhs[i]
        scale=A[i][i]
        for j in range(i,16):A[i][j]/=scale
        rhs[i]/=scale
        for k in range(i+1,16):
            mult=A[k][i]
            if mult:
                for j in range(i,16):A[k][j]-=mult*A[i][j]
                rhs[k]-=mult*rhs[i]
    x=[Fraction(0)]*16
    for i in range(15,-1,-1):
        x[i]=rhs[i]-sum(A[i][j]*x[j] for j in range(i+1,16))
    return sum(x[i]*(Fraction(1,4) if ((i>>1)&3)==1
                     else -Fraction(1,2) if ((i>>1)&3)==2
                     else Fraction(0)) for i in range(16))

for left,right in ((Fraction(7,10),Fraction(2,10)),
                   (Fraction(2,10),Fraction(7,10)),
                   (Fraction(1),Fraction(0)),
                   (Fraction(31,100),Fraction(11,100)),
                   (Fraction(19,20),Fraction(1,20))):
    direct=exact_numeric(left,right)
    symbolic=sp.cancel(current.subs({u:sp.Rational(left.numerator,left.denominator),
                                      v:sp.Rational(right.numerator,right.denominator)}))
    assert sp.Rational(direct.numerator,direct.denominator)==symbolic

print('PASS: generator stationarity, exact current, rational sign certificate,')
print('      six ordered crossing thresholds and independent rational calculations')
print('critical contrast lies in (0.992760, 0.992763)')
print('threshold signs (highest powers first):')
for k in range(9,-1,-1):
    signs,changes=transformed_signs(cs[k])
    print(k,'changes',changes,'interval',bounds.get(k,'uniformly negative'))
