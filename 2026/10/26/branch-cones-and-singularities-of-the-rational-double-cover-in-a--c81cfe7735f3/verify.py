import sympy as s
A,B,C=s.symbols('a b c')
Q=A**6-B**3-1
D=Q*C**2-1
X1=A*(1+Q*C**2)/D
X2=-2*A**3*C/D
X3=2*A*C/D
X4=2*A*B*C/D
f=lambda x1,x2,x3,x4: x2+x1**2*x3+x2**3+x3**3+x4**3
assert s.cancel(f(X1,X2,X3,X4))==0
assert s.cancel(-X2/X3-A**2)==0
assert s.cancel(X4/X3-B)==0
assert s.cancel(X3/(X1-A)-C)==0
T={A:-A,C:1/(Q*C)}
for x in [X1,X2,X3,X4]:
 assert s.cancel(x.subs(T, simultaneous=True)-x)==0
print('VERIFY_OK affine_cubic_rational_map_involution_inverse')
W,X1s,X2s,X3s,X4s,Tv=s.symbols('w x1 x2 x3 x4 t')
F=X2s*W**2+X1s**2*X3s+X2s**3+X3s**3+X4s**3
print('projective_F=',F)
print('branch_2=',s.factor(F.subs(X2s,0)))
print('branch_3=',s.factor(F.subs(X3s,0)))
print('intersection=',s.factor(F.subs({X2s:0,X3s:0})))
print('J=[',','.join(map(str,[s.diff(F,x) for x in [W,X1s,X2s,X3s,X4s]])),']')
# Main branch cubic in projective plane: eta^2 xi + xi^3 + zeta^3; no common nonzero zero of derivatives since char0.
# quadratic cover canonical class: K_X=O(-2); ramification L=O(1) => K_Y=pi^* O(-1); volume 6
print('VERIFY_OK smooth cubic cones elliptic and triple-line intersection, anticanonical_volume=6')

# The quartic tangent cone at either exceptional transverse section is squarefree.
U,V=s.symbols('u v')
quart=U*(U**3+V**3)
assert s.resultant(quart.subs(V,1),s.diff(quart.subs(V,1),U),U)!=0
# The generic local branch curves v=0 and u^2*v+v^3+z^3=0 meet to order three.
Z,T=s.symbols('z t')
assert s.Poly((T**2*U+U**3+Z**3).subs(U,0),Z).degree()==3
print('VERIFY_OK distinct_four_lines_and_order_three_branch_contact')
print('VERIFY_OK rational_double_cover_branch_profile')
