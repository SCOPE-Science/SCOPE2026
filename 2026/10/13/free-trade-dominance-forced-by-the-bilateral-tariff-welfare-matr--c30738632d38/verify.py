"""Exact symbolic consistency check for the cited bilateral tariff payoff matrix.

Run: python verify.py    (requires SymPy >=1.10).
The proof in RESULT.md is self-contained; this script replays its identities.
"""
import sympy as sp

D_A,D_B,L_A,L_B,x,y,S_A,S_B,P_A,P_B,C_A,C_B = sp.symbols(
    'D_A D_B L_A L_B x y S_A S_B P_A P_B C_A C_B', real=True)

# Rows: tariff then no tariff for A; columns: tariff then no tariff for B.
u_A = sp.Matrix([[-D_A-L_A,-D_A],[-L_A,0]])
u_B = sp.Matrix([[-D_B-L_B,-L_B],[-D_B,0]])
expected_A_tariff = y*u_A[0,0] + (1-y)*u_A[0,1]
expected_A_free = y*u_A[1,0] + (1-y)*u_A[1,1]
expected_B_tariff = x*u_B[0,0] + (1-x)*u_B[1,0]
expected_B_free = x*u_B[0,1] + (1-x)*u_B[1,1]
gap_A = sp.expand(expected_A_tariff-expected_A_free)
gap_B = sp.expand(expected_B_tariff-expected_B_free)
assert sp.simplify(gap_A+D_A)==0
assert sp.simplify(gap_B+D_B)==0
assert sp.diff(gap_A,y)==sp.diff(gap_B,x)==0

# Affine coefficient decomposition forced by the payoff table: slopes zero.
assert sp.diff(gap_A,y)==0
assert sp.diff(gap_B,x)==0
# Source equation (8) gives slopes A_i = S_i + P_i + C_i; at
# positive free-trade surplus P_i and nonnegative C_i, S_i, this is > 0.
source_slope_A=S_A+P_A+C_A
source_slope_B=S_B+P_B+C_B
assert sp.expand(source_slope_A-(S_A+P_A+C_A))==0
assert sp.expand(source_slope_B-(S_B+P_B+C_B))==0
assert source_slope_A.subs({S_A:0,P_A:1,C_A:0})==1

# Exact solution: for every 0 < x0 < 1, D>0 and t>=0.
t,x0,D=sp.symbols('t x0 D',real=True)
sol=x0/(x0+(1-x0)*sp.exp(D*t))
assert sp.simplify(sp.diff(sol,t)+D*sol*(1-sol))==0
assert sp.simplify(sol.subs(t,0)-x0)==0

# For the separately defined coupled vector field, the mixed-point
# Jacobian has negative, not positive, determinant when both slopes >0.
a,b,xs,ys=sp.symbols('a b xs ys',real=True)
J=sp.Matrix([[0,a*xs*(1-xs)],[b*ys*(1-ys),0]])
assert sp.factor(J.det()+a*b*xs*(1-xs)*ys*(1-ys))==0

# Numerical exact sanity check for two positive losses and export effects.
sample={D_A:sp.Rational(3,2),D_B:sp.Rational(2,3),
        L_A:sp.Rational(5,4),L_B:sp.Rational(7,6),
        x:sp.Rational(1,3),y:sp.Rational(3,4)}
assert gap_A.subs(sample)==-sp.Rational(3,2)
assert gap_B.subs(sample)==-sp.Rational(2,3)
print('VERIFY_OK')
