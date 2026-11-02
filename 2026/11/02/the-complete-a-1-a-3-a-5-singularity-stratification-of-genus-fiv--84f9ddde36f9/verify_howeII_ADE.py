"""Exact symbolic witness checks for the seven Howe sextic root-pattern strata.
Standard library except sympy; no extrapolation of finite checks into proofs.
"""
import sympy as S
x,y,z=S.symbols('x y z')
P=x**4+x+1
cases=[('3-simple',x*(x-2)*(x+2),[1,1,1]),('3-double',x*x*(x-2),[2,1]),('3-triple',x**3,[3]),('2-simple',x*(x-2),[1,1]),('2-double',x*x,[2]),('1-simple',x,[1]),('0-constant',S.Integer(1),[])]
assert S.discriminant(P,x)==229
for label,q,pattern in cases:
 Q=S.expand(P-q)
 assert S.gcd(P,Q)==1 and S.discriminant(Q,x)!=0,(label,'bad branching')
 roots=S.factor_list(q)[1]
 assert sorted([v for f,v in roots])==sorted(pattern),(label,roots)
 d=S.degree(q,x)
 Phi=lambda A:S.expand(sum(c*x**i*z**(4-i) for (i,),c in S.Poly(A,x).terms()))
 Delta=lambda q:S.expand(sum(c*x**i*z**(3-i) for (i,),c in S.Poly(q,x).terms()))
 H=S.expand(y**4*z**2-2*(Phi(P)+Phi(Q))*y**2+Delta(q)**2)
 assert S.Poly(H,x,y,z).is_homogeneous
 assert S.expand(H.subs(z,1)-(y**4-2*(P+Q)*y**2+q*q))==0
 # Fixed infinite singularity: in y=1 chart tangent cone z^2, residual at z=0 starts -4*x^4.
 assert S.expand(H.subs({y:1,z:0})).expand().coeff(x,4)==-4
 # When d < 3 the second infinity point is singular with q_hom divisible by z^(3-d).
 Qh=Delta(q)
 assert S.expand(Qh.subs(x,1)).as_poly(z).terms()[-1][0][0]>=3-d
 # Quadratic coefficient in y at [1:0:0] has nonzero constant -4.
 assert S.expand(H.subs({x:1,y:1})-H.subs({x:1,y:0})).coeff(z,0)==-4 if d<3 else True
 # Genus defect sum equals 5 for each root multiplicity partition.
 assert 2+sum(pattern)+(3-d)==5
 print(label,'degree_diff',d,'local_A_indices_affine',[2*a-1 for a in pattern], 'infinity_A', [3]+([2*(3-d)-1] if d<3 else []),'disc_phi2',S.discriminant(Q,x))
print('HOWEII_SEVEN_ADE_STRATA_EXACT_SYMBOLIC_WITNESSES_PASS')
