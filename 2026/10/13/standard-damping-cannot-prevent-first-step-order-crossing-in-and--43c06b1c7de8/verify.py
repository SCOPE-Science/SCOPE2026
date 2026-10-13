from fractions import Fraction as F

def aa_first(lams, e, omega):
    a=[F(1)-x for x in lams]
    num=sum(ai**3*ei**2 for ai,ei in zip(a,e))
    den=sum(ai**4*ei**2 for ai,ei in zip(a,e))
    beta=num/den
    tau=den/num
    pred=[ei*(F(1)-beta*ai) for ai,ei in zip(a,e)]
    out=[(F(1)-omega*ai)*pi for ai,pi in zip(a,pred)]
    return a,beta,tau,pred,out

def objective_coeffs(lams,e):
    # Q(beta)=c0-2*c1*beta+c2*beta^2
    a=[F(1)-x for x in lams]
    c0=sum(ai**2*ei**2 for ai,ei in zip(a,e))
    c1=sum(ai**3*ei**2 for ai,ei in zip(a,e))
    c2=sum(ai**4*ei**2 for ai,ei in zip(a,e))
    return c0,c1,c2

# Exact witness.
lams=[F(1,2),F(3,4)]
e=[F(35),F(35)]
a,beta,tau,pred,out0=aa_first(lams,e,F(0))
_,_,_,_,out1=aa_first(lams,e,F(1))
assert beta==F(36,17)
assert tau==F(17,36)
assert pred[0]==-F(35,17)
assert pred[1]==F(280,17)
# x*=1 coordinate shift
assert F(1)+out0[0]==-F(18,17)
assert F(1)+out1[0]==-F(1,34)
# Picard images from x0=(36,36) are positive.
xstar=[F(1),F(1)]
x0=[F(36),F(36)]
x1=[xs+la*(x-xs) for xs,la,x in zip(xstar,lams,x0)]
x2=[xs+la*(x-xs) for xs,la,x in zip(xstar,lams,x1)]
assert x1==[F(37,2),F(109,4)]
assert x2==[F(39,4),F(331,16)]
assert all(v>0 for v in x1+x2)

# Rational family: independently recover beta from quadratic coefficients,
# verify tau is inside the active gap range, and verify the sign formula for several omegas.
vals=[F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)]
errs=[F(1),F(2),F(3)]
for la1 in vals:
  for la2 in vals:
    if la1==la2: continue
    for e1 in errs:
      for e2 in errs:
        l=[la1,la2]
        ee=[e1,e2]
        a,beta,tau,pred,_=aa_first(l,ee,F(0))
        c0,c1,c2=objective_coeffs(l,ee)
        assert beta==c1/c2
        assert min(a)<tau<max(a)
        signs=[(F(1)-ai/tau) for ai in a]
        assert signs[0]*signs[1] < 0
        for om in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            _,_,_,pred,out=aa_first(l,ee,om)
            for ai,pi,oi in zip(a,pred,out):
                assert oi==(F(1)-om*ai)*pi
                assert F(1)-om*ai>0
                assert (oi>0)==(pi>0)

# One dimension: exact prediction to the fixed point.
for la in vals:
    a,beta,tau,pred,out=aa_first([la],[F(7)],F(1))
    assert pred==[F(0)] and out==[F(0)]

print('VERIFY_OK')
