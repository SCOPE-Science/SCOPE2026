import sympy as sp

t,u = sp.symbols("t u")

A = sp.Matrix([
    [0,-1,-2,0,-2, 3],
    [0,-3,-1,-1,-2,-1],
])
Q = A.T * (A*A.T).inv() * A

assert Q*Q == Q
assert Q.rank() == 2
assert sp.trace(Q) == 2
assert Q == Q.T

v = sp.Matrix([[1,t,t**2]])
s = 1+t**2+t**4

G = sp.factor((v*Q[:3,:3]*v.T)[0] + (v*Q[3:,3:]*v.T)[0])
assert sp.simplify(G - (128*t**4 + 8*t**3 + 151*t**2 + 24*t + 9)/sp.Integer(126)) == 0

F = sp.cancel(G/s)
H = sp.factor(sp.diff(G,t)*s - G*sp.diff(s,t))
h = 4*t**6 + 23*t**5 + 32*t**4 - 238*t**3 - 142*t - 12
assert sp.simplify(H + h/sp.Integer(63)) == 0
assert sp.degree(h,t) == 6

disc = sp.discriminant(h,t)
assert disc == 6779465482547678036224
assert disc != 0

# The two-by-six matrix for the model ruling line.
B = sp.Matrix([
    [1,t,t**2,0,0,0],
    [0,0,0,1,t,t**2],
])

# P(t) lies in cut(Q) iff Q restricted to row(B) is singular.
cut_det = sp.factor((B*Q*B.T).det())
cut_factor = t*(5*t**3 + 12*t**2 - 2*t + 1)
assert sp.simplify(cut_det - cut_factor**2/sp.Integer(252)) == 0

res_cut = sp.resultant(h, cut_factor, t)
assert res_cut == -1358879507628
assert res_cut != 0

res_poles = sp.resultant(h, s, t)
assert res_poles == 2875220721
assert res_poles != 0

# Check the point t=infinity by u=1/t.
F_u = sp.cancel(F.subs(t,1/u))
dF_u = sp.cancel(sp.diff(F_u,u))
infinity_derivative = sp.limit(dF_u,u,0)
assert infinity_derivative == sp.Rational(4,63)
assert infinity_derivative != 0

# The source's ED formula for S(2,2): L=s, delta=4, ED=2*delta-2.
delta = sp.degree(s,t)
ed_degree = 2*delta-2
assert delta == 4 and ed_degree == 6

print("Q_rank=2")
print("Q_trace=2")
print("critical_polynomial=" + str(h))
print("critical_degree=6")
print("critical_discriminant=" + str(disc))
print("cut_factor=" + str(cut_factor))
print("resultant_critical_cut=" + str(res_cut))
print("resultant_critical_poles=" + str(res_poles))
print("infinity_derivative=" + str(infinity_derivative))
print("ED_degree_S22=6")
print("GD_degree_S22=6")
print("VERIFY_OK")
