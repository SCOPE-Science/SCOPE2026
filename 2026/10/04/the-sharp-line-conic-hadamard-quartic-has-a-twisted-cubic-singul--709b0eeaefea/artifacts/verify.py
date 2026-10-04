import sympy as s
z0,z1,z2,z3,p,q,u,v,U,W=s.symbols('z0 z1 z2 z3 p q u v U W')
# source parametrizations
X=[-(5*p+q),3*(p-q),2*p,2*q]
Y=[-9*u**2-16*u*v-4*v**2,2*u**2,2*u*v,5*u**2+10*u*v+4*v**2]
assert s.expand(X[0]+X[1]+X[2]+2*X[3])==0
assert s.expand(X[0]-X[1]+4*X[2]-X[3])==0
y0,y1,y2,y3=Y
assert s.expand(y0+2*y1+3*y2+y3)==0
assert s.expand(y0**2+2*y0*y2+2*y0*y3+y1**2+2*y1*y2-2*y1*y3+y2**2+2*y2*y3+y3**2)==0
Z=[s.expand(X[i]*Y[i]) for i in range(4)]
F=(360*z0**3*z1-3120*z0**2*z1**2-9360*z0**2*z1*z2-2304*z0**2*z1*z3-2700*z0**2*z2**2+3160*z0*z1**3+24780*z0*z1**2*z2+5448*z0*z1**2*z3+46998*z0*z1*z2**2+57816*z0*z1*z2*z3+2034*z0*z1*z3**2+16200*z0*z2**3+22680*z0*z2**2*z3-75*z1**4-1550*z1**3*z2-3654*z1**3*z3-8535*z1**2*z2**2-66594*z1**2*z2*z3-3267*z1**2*z3**2-14310*z1*z2**3-263034*z1*z2**2*z3-13338*z1*z2*z3**2-486*z1*z3**3-4860*z2**4-106920*z2**3*z3-43740*z2**2*z3**2)
assert s.expand(F.subs(dict(zip([z0,z1,z2,z3],Z))))==0
q1=294*z0*z1-494*z1**2-2655*z1*z2-147*z1*z3-1080*z2**2
q2=1110*z0*z1+1800*z0*z2+230*z1**2+957*z1*z2+1209*z1*z3-9720*z2*z3
q3=32400*z0**2+152346*z0*z1+88200*z0*z2-191160*z0*z3+10334*z1**2+23079*z1*z2+491835*z1*z3+87480*z3**2
P=[6*(U+4*W)*(225*U**2+1070*U*W+1269*W**2),36*(5*U+11*W)*W**2,(5*U+11*W)*(49*U+115*W)*W,(2*U+5*W)*(125*U**2+850*U*W+1409*W**2)]
for Q in [q1,q2,q3]: assert s.expand(Q.subs(dict(zip([z0,z1,z2,z3],P))))==0
# coefficient rank = 4 binary cubics
mons=[U**3,U**2*W,U*W**2,W**3]
C=s.Matrix([[s.Poly(pi,U,W).coeff_monomial(m) for m in mons] for pi in P])
assert C.rank()==4
D=[s.diff(F,x) for x in [z0,z1,z2,z3]]
Qv=s.Matrix([q1,q2,q3])
M=[
[s.Rational(3,49)*(60*z0-120*z1-245*z2-226*z3),-(100*z1+39*z2)/s.Integer(49),0],
[-(15564*z0-10450*z1-38955*z2-109212*z3)/s.Integer(2940),-(50666*z0-55830*z1-202275*z2-12103*z3)/s.Integer(8820),(2*z0-z3)/s.Integer(180)],
[-(2010*z0-835*z1-1764*z2-16146*z3)/s.Integer(98),-(294*z0-1133*z1-1440*z2-882*z3)/s.Integer(98),0],
[-(768*z0-703*z1-9702*z2-972*z3)/s.Integer(98),-(47*z1-774*z2)/s.Integer(98),0]]
for i in range(4): assert s.expand(sum(M[i][j]*Qv[j] for j in range(3))-D[i])==0
G=s.groebner(D,z0,z1,z2,z3,order='grevlex')
for Q in [q1,q2,q3]:
    assert G.reduce(s.expand(Q**3))[1]==0
print('VERIFY_OK')
