import sympy as s
from itertools import combinations

x0,x1,x2,x3,t,a,b,u,w = s.symbols('x0 x1 x2 x3 t a b u w')
vars4=(x0,x1,x2,x3)
A1=s.Matrix([
[0,x0,4*x1,2*x2],
[x0,4*x3,2*x1-2*x3,0],
[4*x1,2*x1-2*x3,-4*x1,-x2],
[2*x2,0,-x2,x3]])
A2=s.Matrix([
[0,x0-8*x3,4*x3,2*x2],
[x0-8*x3,4*x1+8*x3,-2*x1-6*x3,-2*x2],
[4*x3,-2*x1-6*x3,4*x3,x2],
[2*x2,-2*x2,x2,-x1]])
F=s.expand(A1.det())
assert s.expand(A2.det()-F)==0
expected=(4*x0**2*x1*x3+x0**2*x2**2+16*x0*x1**2*x3+8*x0*x1*x2**2
          -16*x0*x1*x3**2-8*x0*x2**2*x3+16*x1**2*x2**2
          -64*x1**2*x3**2-32*x1*x2**2*x3+16*x2**2*x3**2)
assert s.expand(F-expected)==0
G=[s.factor(s.diff(F,v)) for v in vars4]
assert s.factor(G[2]-2*x2*(x0+4*x1-4*x3)**2)==0
ell=x0+4*x1-4*x3
subell={x0:-4*x1+4*x3}
assert s.factor(G[0].subs(subell)+16*x1*x3*(x1-x3))==0
assert s.factor(G[1].subs(subell)+64*x1*x3*(x1+x3))==0
assert s.factor(G[3].subs(subell)+64*x1*x3*(x1+x3))==0
subx2={x2:0}
assert s.factor(G[0].subs(subx2)-8*x1*x3*(x0+2*x1-2*x3))==0
assert s.factor(G[1].subs(subx2)-4*x3*(x0+8*x1)*(x0-4*x3))==0
assert s.factor(G[3].subs(subx2)-4*x1*(x0+4*x1)*(x0-8*x3))==0

# Four isolated singular points are ordinary nodes.
H=s.hessian(F,vars4)
nodes=[(1,0,0,0),(0,1,0,0),(0,0,0,1),(-4,1,0,-1)]
for P in nodes:
    M=H.subs(dict(zip(vars4,P)))
    assert M.rank()==3
    assert all(g.subs(dict(zip(vars4,P)))==0 for g in G)

# Two singular lines and Hessian drop exactly at t^2+1=0 away from their intersection.
La={x0:4,x1:0,x2:t,x3:1}
Lb={x0:-4,x1:1,x2:t,x3:0}
for L in (La,Lb):
    MH=H.subs(L)
    minors=[s.factor(MH.extract(rs,cs).det()) for rs in combinations(range(4),2) for cs in combinations(range(4),2)]
    nz=[m for m in minors if m!=0]
    assert s.factor(s.gcd_list(nz)/(t**2+1)) in (256,-256,1024,-1024,4096,-4096,1,-1)
    assert MH.subs(t,2).rank()==2
    assert MH.subs(t,s.I).rank()==1
    assert MH.subs(t,-s.I).rank()==1

# Exact pinch-point completion on each line: discriminant is a square times a simple parameter.
Ga=s.expand(F.subs({x3:1,x0:4+w,x1:a,x2:t}))
Pa=s.Poly(Ga,w)
Aa,Ba,Ca=Pa.coeff_monomial(w**2),Pa.coeff_monomial(w),Pa.coeff_monomial(1)
assert s.factor(Ba**2-4*Aa*Ca-256*a**2*(a**2+2*a+t**2+1))==0
Gb=s.expand(F.subs({x1:1,x0:-4+w,x3:b,x2:t}))
Pb=s.Poly(Gb,w)
Ab,Bb,Cb=Pb.coeff_monomial(w**2),Pb.coeff_monomial(w),Pb.coeff_monomial(1)
assert s.factor(Bb**2-4*Ab*Cb-256*b**2*(b**2+2*b+t**2+1))==0

# At the line intersection [0:0:1:0], completing the square gives U^2-(8ab)^2 times a unit.
Gp=s.expand(F.subs({x2:1,x0:u-4*a+4*b,x1:a,x3:b}))
Pp=s.Poly(Gp,u)
Ap,Bp,Cp=Pp.coeff_monomial(u**2),Pp.coeff_monomial(u),Pp.coeff_monomial(1)
assert s.factor(Ap-(1+4*a*b))==0
assert s.factor(Bp-16*a*b*(b-a))==0
assert s.factor(Bp**2-4*Ap*Cp-256*a**2*b**2*(1+(a+b)**2))==0

# Representation-dependent matrix rank along the same intrinsic double curves.
def three_minors(M):
    return [s.factor(M.extract(rs,cs).det()) for rs in combinations(range(4),3) for cs in combinations(range(4),3)]
for name,A,Lrank3,Lrank2 in [('A1',A1,La,Lb),('A2',A2,Lb,La)]:
    m3=three_minors(A.subs(Lrank3)); nz=[m for m in m3 if m!=0]
    assert nz and s.factor(s.gcd_list(nz)/(t**2+1)) in (4,-4,8,-8,16,-16,1,-1)
    assert A.subs(Lrank3).subs(t,2).rank()==3
    assert A.subs(Lrank3).subs(t,s.I).rank()==2
    assert A.subs(Lrank3).subs(t,-s.I).rank()==2
    assert all(m==0 for m in three_minors(A.subs(Lrank2)))
    assert A.subs(Lrank2).subs(t,2).rank()==2

print('VERIFY_OK')
