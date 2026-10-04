import sympy as sp
x0,x1,x2,u,v=sp.symbols('x0 x1 x2 u v')
A0=sp.Matrix([[0,0,0],[0,0,0],[0,0,1]])
A1=sp.Matrix([[0,1,2],[1,3,4],[2,4,5]])
A2=sp.Matrix([[0,6,7],[6,8,9],[7,9,10]])
A=x0*A0+x1*A1+x2*A2
F=sp.expand(A.det())
F_expected=-x0*x1**2-12*x0*x1*x2-36*x0*x2**2-x1**3+2*x1**2*x2+7*x1*x2**2+4*x2**3
assert sp.expand(F-F_expected)==0
# singular locus: Fx0=-(x1+6x2)^2, and after x1=-6x2, Fx1=-125x2^2
partials=[sp.diff(F,z) for z in (x0,x1,x2)]
assert sp.expand(partials[0]+(x1+6*x2)**2)==0
assert sp.expand(partials[1].subs(x1,-6*x2)+125*x2**2)==0
# local A2 coordinates s=x1+6x2,t=x2, X=x0+s-20t
s,t,X=sp.symbols('s t X')
Floc=sp.expand(F.subs({x1:s-6*t,x2:t,x0:X-s+20*t}))
assert sp.expand(Floc-(-X*s**2-125*s*t**2+250*t**3))==0
# in affine X=1 quadratic part -s^2 and restriction s=0 has 250t^3: A2 by splitting lemma
# normalization
Xpar=125*v**2*(2*v-u)
spar=u**3
tpar=u**2*v
x0p=sp.expand(Xpar-spar+20*tpar)
x1p=sp.expand(spar-6*tpar)
x2p=tpar
assert sp.expand(F.subs({x0:x0p,x1:x1p,x2:x2p}))==0
assert sp.gcd(sp.gcd(x0p,x1p),x2p)==1
# inverse off cusp: [s:t]=[u:v]
assert sp.expand((x1p+6*x2p)*v-x2p*u)==0
# Cayley quadrics
a,b,c=sp.symbols('a b c')
y=sp.Matrix([a,b,c])
Qs=[sp.expand((y.T*M*y)[0]) for M in (A0,A1,A2)]
assert Qs[0]==c**2
assert sp.expand(Qs[1]-(2*a*b+4*a*c+3*b**2+8*b*c+5*c**2))==0
assert sp.expand(Qs[2]-(12*a*b+14*a*c+8*b**2+18*b*c+10*c**2))==0
# local at q (a=1): linear coefficient matrix in b,c has det -20
L=sp.Matrix([[sp.diff(Qs[1].subs(a,1),b).subs({b:0,c:0}),sp.diff(Qs[1].subs(a,1),c).subs({b:0,c:0})],[sp.diff(Qs[2].subs(a,1),b).subs({b:0,c:0}),sp.diff(Qs[2].subs(a,1),c).subs({b:0,c:0})]])
assert L.det()==-20
# set-theoretic uniqueness in char 0: c=0 and two equations force b=0; resultant/gcd in r=a/b if b!=0 are inconsistent
# adjugate factorization along normalization
Ap=sp.simplify(A.subs({x0:x0p,x1:x1p,x2:x2p}))
adj=Ap.adjugate().applyfunc(sp.expand)
ypar=sp.Matrix([2*(u-5*v)**2,-u*(2*u-5*v),u**2])
assert all(sp.expand(adj[i,j]+u**2*ypar[i]*ypar[j])==0 for i in range(3) for j in range(3))
# kernel identity and conic
assert all(sp.expand(z)==0 for z in (Ap*ypar))
Y0,Y1,Y2=sp.symbols('Y0 Y1 Y2')
conic=Y0*Y2-2*(Y1+Y2)**2
assert sp.expand(conic.subs({Y0:ypar[0],Y1:ypar[1],Y2:ypar[2]}))==0
# conic smooth: gradient cannot vanish projectively over char 0
cg=[sp.diff(conic,z) for z in (Y0,Y1,Y2)]
sol=sp.solve(cg+[conic],[Y0,Y1,Y2], dict=True)
assert sol==[{Y0:0,Y1:0,Y2:0}]
# cusp preimage maps to q
assert [sp.expand(z.subs(u,0)) for z in ypar]==[50*v**2,0,0]
print('F=',F)
print('Floc=',Floc)
print('Cayley=',Qs)
print('Jac_q_det=',L.det())
print('normalization=',[x0p,x1p,x2p])
print('kernel=',list(ypar))
print('conic=',conic)
print('VERIFY_OK')
