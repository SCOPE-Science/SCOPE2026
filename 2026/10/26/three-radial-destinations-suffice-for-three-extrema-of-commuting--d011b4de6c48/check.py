from sympy import symbols, factor, diff, Rational, simplify, Poly, count_roots

m, a, b = symbols('m a b', positive=True)
p1 = (m + 201)/(201*(m+1))
p2 = 100*m*(m+201)/(201*(m+1)*(m+101))
p3 = 100*m/(201*(m+101))
assert simplify(p1 + p2 + p3 - 1) == 0
mean = p1 + 2*p2 + 3*p3
variance = factor(p1 + 4*p2 + 9*p3 - mean**2)
expected_v = 500*m*(m+201)*(21*m*m+162*m+4141)/(40401*(m+1)**2*(m+101)**2)
assert simplify(variance-expected_v) == 0
expected_derivative = -500*(m*m-3858*m+4141)*(99*m*m-202*m-20301)/(40401*(m+1)**3*(m+101)**3)
assert simplify(diff(variance,m)-expected_derivative) == 0
A=m*m-3858*m+4141; B=99*m*m-202*m-20301
assert A.subs(m,1)>0 and A.subs(m,2)<0 and A.subs(m,20)<0 and A.subs(m,3858)>0
assert B.subs(m,2)<0 and B.subs(m,20)>0
assert count_roots(A, 0, 10000) == 2 and count_roots(B,0,10000) == 1
for t,sign in [(Rational(1,2),1),(2,-1),(20,1),(4000,-1)]:
    assert (expected_derivative.subs(m,t)>0) == (sign>0)
# Symbolic proof-check of the two-region monotone far-destination chance.
S=a+b
p=m*b/(S*(m+a))
assert simplify(diff(p,m)-a*b/(S*(m+a)**2)) == 0
print('PASS: normalization; exact variance and derivative; three positive root isolation; two-destination monotonicity')
