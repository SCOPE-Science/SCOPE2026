#!/usr/bin/env python3
"""Exact arithmetic checks of the metric complete-split P1 projection theorem.
Run: python verify_split_spline.py (requires SymPy >= 1.10).
The polynomial coefficient checks certify identities for all integer parameters,
not merely the finite matrix examples.
"""
import sympy as S

def abs_affine(a,b):
    a,b=S.Rational(a),S.Rational(b)
    if a>=0 and b>=0: return (a+b)/2
    if a<=0 and b<=0: return -(a+b)/2
    return (a*a+b*b)/(2*S.Abs(a-b))

def direct(m,k):
    n=m+k
    edges=[(i,m+j) for i in range(m) for j in range(k)] + [(m+i,m+j) for i in range(k) for j in range(i+1,k)]
    B=S.zeros(n)
    for u,v in edges:
        B[u,u]+=2; B[v,v]+=2; B[u,v]+=1; B[v,u]+=1
    I=6*B.inv()
    return tuple(S.factor(sum(abs_affine(I[u,a],I[v,a]) for u,v in edges)) for a in (0,m))

def formulas(m,k):
    m,k=S.Rational(m),S.Rational(k)
    L=m+2*k-2; a=2*m+2*k-3
    va=-2/(k*L)
    vs=4/(k*L)+6*(k-1)/(k*a)
    vo=2*(m-2*k)/(k*a*L)
    def I(x,y):
        if x*y>=0: return S.Abs(x+y)/2
        return (x*x+y*y)/(2*S.Abs(x-y))
    A=(7*m*m+26*m*k+24*k*k-23*m-44*k+20)/(3*L*(L+1))
    B=m*I(vs,va)+m*(k-1)*I(vo,va)+(k-1)*I(vs,vo)+S.binomial(k-1,2)*S.Abs(vo)
    return S.factor(A),S.factor(B)

n=0
for m in range(2,11):
    for k in range(2,10):
        direct_values=direct(m,k)
        expected=formulas(m,k)
        assert direct_values==expected,(m,k,direct_values,expected)
        assert direct_values[0]>direct_values[1]
        assert (direct_values[0]>2)==(m>=4)
        n+=1
print('EXACT_INDEPENDENT_MASS_INVERSES_AND_KERNEL_INTEGRALS_OK',n)

m,k,x,y=S.symbols('m k x y',integer=True)
L=m+2*k-2;a=2*m+2*k-3
C=(7*m*m+26*m*k+24*k*k-23*m-44*k+20)/(3*L*(L+1))
u=-2/(k*L);v=4/(k*L)+6*(k-1)/(k*a);w=2*(m-2*k)/(k*a*L)
I=lambda s,t:(s*s+t*t)/(2*(s-t))
Bminus=m*I(v,u)+m*(k-1)*(-u-w)/2+(k-1)*I(v,w)+((k-1)*(k-2)/2)*(-w)
Bplus=m*I(v,u)+m*(k-1)*I(w,u)+(k-1)*(v+w)/2+((k-1)*(k-2)/2)*w
for name,formula,shifts in [('NONPOSITIVE_OTHER_CLIQUE_KERNEL',Bminus,[(m,x+2),(k,y+2)]),('POSITIVE_OTHER_CLIQUE_KERNEL',Bplus,[(m,2*k+x),(k,y+2)])]:
    D=S.factor(C-formula)
    num,den=S.fraction(D)
    assert S.simplify(D-num/den)==0
    # Products in factored numerators have strictly positive denominators on the claimed domains.
    pol=S.expand(num)
    for vname,replace in shifts: pol=pol.subs(vname,replace)
    pol=S.Poly(S.expand(pol),x,y)
    assert all(int(z)>0 for z in pol.coeffs()),(name,[z for z in pol.coeffs() if z<=0])
    print('ALL_PARAMETER_POSITIVE_COEFFICIENT_CERTIFICATE_OK',name,len(pol.terms()))

assert S.simplify(C-2-(m*m+2*k*m-5*m-8*k+8)/(3*L*(L+1)))==0
assert S.limit(C,m,S.oo)==S.Rational(7,3)
assert S.limit(C,k,S.oo)==2
print('EXACT_TWO_THRESHOLD_AND_LIMIT_IDENTITIES_OK')
print('ALL_SPLIT_METRIC_GRAPH_P1_PROJECTION_CHECKS_OK')
