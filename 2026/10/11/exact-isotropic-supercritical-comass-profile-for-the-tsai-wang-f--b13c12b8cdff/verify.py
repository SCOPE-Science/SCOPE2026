import sympy as sp

r = sp.symbols("r", integer=True, positive=True)
lam = sp.symbols("lam", positive=True)
Q,u,v,d = sp.symbols("Q u v d", positive=True, real=True)

# Pairwise smoothing identity.
lhs = Q*sp.cos(u)**2 + d*sp.sin(2*u)
rhs = Q*sp.cos(u+v)*sp.cos(u-v) + d*sp.sin(2*u)
assert sp.trigsimp(lhs-rhs-Q*sp.sin(v)**2) == 0

x = lam**2
C = (1+x)**(r/sp.Integer(2))
dd = lam/(1+x)

# Subcritical branch.
q_sub = (1-(r-1)*x)/(1+x)
t_sub = lam
crit_sub = sp.simplify(dd-q_sub*t_sub-(r-1)*dd*t_sub**2)
assert crit_sub == 0
h_sub = sp.simplify(C*(q_sub+r*dd*t_sub)/(1+t_sub**2)**(r/sp.Integer(2)))
assert h_sub == 1

# Supercritical branch.
q_sup = ((r-1)*x-1)/(1+x)
t_sup = 1/((r-1)*lam)
crit_sup = sp.simplify(dd-q_sup*t_sup-(r-1)*dd*t_sup**2)
assert crit_sup == 0

h_sup = sp.simplify(C*(q_sup+r*dd*t_sup)/(1+t_sup**2)**(r/sp.Integer(2)))
target = (
    (r-1)**(r-1)
    * lam**r
    * (1+x)**((r-2)/sp.Integer(2))
    / (1+(r-1)**2*x)**((r-2)/sp.Integer(2))
)
assert sp.simplify(h_sup/target) == 1

# Boundary continuity and representative exact replays.
for rr in range(2, 11):
    lb = sp.sqrt(sp.Rational(1, rr-1))
    boundary = sp.simplify(target.subs({r:rr, lam:lb}))
    assert boundary == 1

    # Representative supercritical rational-square choice lambda^2=4/(r-1).
    ll = sp.sqrt(sp.Rational(4, rr-1))
    tt = sp.simplify(t_sup.subs({r:rr, lam:ll}))
    closed = sp.simplify(target.subs({r:rr, lam:ll}))
    a = sp.simplify((1-(rr-1)*ll**2)/(1+ll**2))
    de = sp.simplify(ll/(1+ll**2))
    Ce = sp.simplify((1+ll**2)**(sp.Rational(rr,2)))
    direct = sp.simplify(
        Ce*abs(a-rr*de*tt)/(1+tt**2)**(sp.Rational(rr,2))
    )
    assert sp.simplify(direct-closed) == 0

# Rank-three specialization.
r3 = sp.simplify(target.subs(r,3))
r3_target = 4*lam**3*sp.sqrt(1+lam**2)/sp.sqrt(1+4*lam**2)
assert sp.simplify(r3-r3_target) == 0

print("VERIFY_OK")
print("pairwise_smoothing=true")
print("subcritical_comass=1")
print("supercritical_formula=true")
print("boundary_continuity=true")
print("rank3_specialization=true")
