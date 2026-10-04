from fractions import Fraction
import sympy as sp

s,u,v = sp.symbols('s u v')
M = [
    [sp.Rational(1),0,0,0],
    [sp.Rational(14351,10000),sp.Rational(6797,10000),sp.Rational(39435,10000),sp.Rational(77238,10000)],
    [-sp.Rational(13085,10000),sp.Rational(46694,10000),sp.Rational(131949,10000),sp.Rational(51509,10000)],
    [sp.Rational(11573,10000),sp.Rational(12007,10000),sp.Rational(57272,10000),sp.Rational(86591,10000)],
]
EXPECTED = [
4097057871858200718399710457050029783860448093883227674718933457227000000000000,
886550574980216626763495644940579931850647416367114988341240632505000000000000,
-14583445523408363563043807155529990819517874422341082510349311651322000000000000,
-5275699128677051945839235006808320077582295289599096827353598942811453300000000,
17554592606358550297152133225066058371683785754779718519967513497275130300000000,
8606156808171959940381182770903055017106302150492576001858996085131852000000000,
-6999255125012068183983935339635630280233270657536727356116586004108299033030000,
-4299485645818848556385308962411578844253286727339888981739646169646110507450000,
-143456610277323149419672668802489602321319249963404595109173337004241260620000,
4519935476335806902498900300573315260877836169182856532548525582293189114273,
30338654869700262466652210847156386094220876251571377982129917845522862489,
]

def primitive_integer(poly):
    poly = sp.Poly(poly, u, domain=sp.QQ)
    den = 1
    for c in poly.all_coeffs(): den = sp.ilcm(den, c.q)
    cs = [int(c*den) for c in poly.all_coeffs()]
    g = 0
    for c in cs: g = sp.igcd(g, abs(c))
    cs = [c//g for c in cs]
    if cs[0] < 0: cs = [-c for c in cs]
    return cs

assert sp.det(sp.Matrix(M)) != 0
p = [sum(row[j]*s**j for j in range(4)) for row in M]
A = sp.expand(p[2] - u*p[1] + v*p[0])
B = sp.expand(p[3] - (u**2-v)*p[1] + u*v*p[0])
subs = sp.subresultants(A,B,s)
S1 = [r for r in subs if sp.degree(r,s)==1][-1]
a = sp.Poly(S1,s).coeff_monomial(s)
b = sp.Poly(S1,s).coeff_monomial(1)
R = sp.resultant(a,b,v)
factors = sp.factor_list(R)[1]
deg10 = [f for f,m in factors if sp.degree(f,u)==10]
assert len(deg10) == 1
assert primitive_integer(deg10[0]) == EXPECTED
# The only other u-factor is the leading-coefficient degeneration, with multiplicity 3.
other = [(sp.factor(f),m,sp.degree(f,u)) for f,m in factors if sp.degree(f,u)!=10]
assert len(other)==1 and other[0][1]==3 and other[0][2]==1
assert primitive_integer(other[0][0]) == [77238,-51509]
print('M_DETERMINANT_NONZERO')
print('SUBRESULTANT_LINEAR_CONDITION_OK')
print('DEGREE10_ELIMINATION_POLYNOMIAL_OK')
print('ONLY_OTHER_U_FACTOR_77238u-51509_CUBED_OK')
print('ELIMINATION_OK')
