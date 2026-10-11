from sympy import symbols, factor, simplify, sqrt, diff, exp, Rational

a,b,w,x,h,t = symbols('a b w x h t', positive=True)
F = (x+b)*(2*a+b-x)
Ft = 2*x*(a-x)
Ftt = 2*x*(a-2*x)
G = a*x**2 + (4*a*b+2*b**2)*x - a*b*(2*a+b)
assert simplify(F*Ftt - Ft**2 + 2*x*G) == 0

s = sqrt(b*(2*a+b))
h1 = ((a+b)*s - b*(2*a+b))/a
h2 = a*s/(a+b+s)
assert simplify(h1-h2) == 0
assert simplify(G.subs(x,h2)) == 0

Fs = F.subs({a:3,b:2,x:exp(t)})
assert simplify(Fs - (16+6*exp(t)-exp(2*t))) == 0
assert simplify(h2.subs({a:3,b:2}) - Rational(4,3)) == 0
logcurv_num = simplify((F*Ftt-Ft**2).subs({a:3,b:2,x:1}))
assert logcurv_num == 26
assert simplify(F.subs({a:3,b:2,x:1})) == 21
print('OK: factorization, threshold identity, and published special case verified exactly.')
