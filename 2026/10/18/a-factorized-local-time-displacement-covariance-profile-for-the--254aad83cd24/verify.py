"""Numerical consistency checks for a zero-local-time / displacement law."""
import math
import mpmath as mp

mp.mp.dps = 43


def gaussian_joint_moment(t):
    """Integrate the Gaussian conditional-on-zero covariance density."""
    t = mp.mpf(t)
    left = mp.sqrt(1-t)/mp.pi * mp.quad(
        lambda s: mp.sqrt(t-s)/(mp.sqrt(s)*(1-s)), [0,t]
    )
    right = mp.sqrt(t)/mp.pi * mp.quad(
        lambda s: mp.sqrt(s-t)/(s*mp.sqrt(1-s)), [t,1]
    )
    return left + right


def overshoot_mean(u,r):
    u,r = mp.mpf(u),mp.mpf(r)
    return mp.quad(lambda z: mp.exp(-z*z/(2*u)-r*z/u),[0,mp.inf])


for s in ['.01','.05','.1','.25','.333333333333','.5','.75','.9','.95','.99']:
    t = mp.mpf(s)
    direct=gaussian_joint_moment(t)
    expected=mp.sqrt(t)+mp.sqrt(1-t)-1
    cov_expected=-(1-mp.sqrt(t))*(1-mp.sqrt(1-t))
    independent_cov=direct-mp.sqrt(t*(1-t))
    assert abs(direct-expected)<mp.mpf('1e-19'),(s,'joint moment',direct,expected)
    assert abs(independent_cov-cov_expected)<mp.mpf('1e-19'),(s,'covariance',independent_cov,cov_expected)

# Conditional local time is a sum of two independent exponential overshoots.
# Compare direct survival integrations against Mills ratio formula at six points.
for u in ['.1','.5','.9']:
  for r in ['0','.75']:
    u,r=mp.mpf(u),mp.mpf(r)
    exact=mp.sqrt(u)*mp.sqrt(2*mp.pi)*mp.exp(r*r/(2*u))*mp.erfc(r/mp.sqrt(2*u))/2
    direct=overshoot_mean(u,r)
    assert abs(direct-exact)<mp.mpf('1e-28'),(u,r,direct,exact)

# Strict ordering under the same exponential variables at every positive r.
for u in [.11,.5,.89]:
 for e in [0.01,0.5,1,6]:
    vals=[math.sqrt(r*r+2*u*e)-r for r in [0,.1,.3,.9,2,6]]
    assert all(vals[i]>vals[i+1] for i in range(len(vals)-1)),(u,e,vals)

area=mp.quad(lambda t:-(1-mp.sqrt(t))*(1-mp.sqrt(1-t)),[0,.5,1])
assert abs(area-(mp.mpf(1)/3-mp.pi/8))<mp.mpf('1e-38')
print('PASS: 10 Gaussian joint-moment checks, 6 independent overshoot-integral checks,')
print('      12 strict conditional-coupling checks, 1 area-integral check.')
print('Exact unweighted area covariance:',mp.nstr(area,26))
