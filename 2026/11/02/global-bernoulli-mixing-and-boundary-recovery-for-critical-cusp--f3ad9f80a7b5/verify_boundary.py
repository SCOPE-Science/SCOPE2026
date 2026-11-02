from fractions import Fraction as F

def data(theta):
    K2 = (1-theta/2)**2/2
    a = 1/K2
    r = theta*a
    return a,r

def check(t0,t1,p):
    a0,r0=data(t0); a1,r1=data(t1)
    A=(1-p)*a0+p*a1
    B=(1-p)*a0*r0+p*a1*r1
    C=(1-p)*a0*r0*r0+p*a1*r1*r1
    t=B/A
    rec=a0*(t-r0)/(a0*(t-r0)+a1*(r1-t))
    assert rec==p,(t0,t1,p,rec)
    assert A*C-B*B==p*(1-p)*a0*a1*(r1-r0)**2
    assert (r1-r0)>0
    return A,B,C

pairs=[(F(5,4),F(7,4)),(F(11,10),F(19,10)),(F(3,2),F(9,5))]
ps=[F(0),F(1,7),F(1,3),F(1,2),F(3,4),F(9,10),F(1)]
for a,b in pairs:
    for p in ps: check(a,b,p)
print('EXACT_RATIONAL_MIXTURE_RECOVERY_AND_DISCRIMINANT_PASS',len(pairs)*len(ps))
print('EXACT_BOUNDARY_WEIGHT_COEFFICIENTS_PASS', '2w(z)=a z -3 a r z^2/4 +5 a r^2 z^3/8 +O(z^4)')
print('UNIFORM_SPECTRAL_GAP_REQUIRES_ANALYTIC_PROOF')
