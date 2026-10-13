import math

def cdf(x, alpha, theta, beta):
    if x < 0:
        return 0.0
    return 1.0 - alpha/(alpha-1.0) * (
        1.0 - alpha ** (-(theta ** ((x+1.0)**beta)))
    )

def pmf(x, alpha, theta, beta):
    return cdf(x,alpha,theta,beta)-cdf(x-1,alpha,theta,beta)

def lower_like_source(records, alpha, theta, beta):
    out = pmf(records[0],alpha,theta,beta)
    for i in range(1,len(records)):
        out *= pmf(records[i],alpha,theta,beta)/cdf(records[i-1],alpha,theta,beta)
    return out

def lower_like_strict(records, alpha, theta, beta):
    out = pmf(records[0],alpha,theta,beta)
    for i in range(1,len(records)):
        out *= pmf(records[i],alpha,theta,beta)/cdf(records[i-1]-1,alpha,theta,beta)
    return out

alpha,theta,beta = 2.0,0.5,1.0

# Basic PMF checks.
mass = sum(pmf(x,alpha,theta,beta) for x in range(200))
assert abs(mass-1.0) < 1e-12
assert all(pmf(x,alpha,theta,beta)>0 for x in range(15))

# Correct strict-lower transition normalizes.
for ell in range(1,8):
    s = sum(pmf(j,alpha,theta,beta)/cdf(ell-1,alpha,theta,beta) for j in range(ell))
    assert abs(s-1.0) < 1e-13
    spub = sum(pmf(j,alpha,theta,beta)/cdf(ell,alpha,theta,beta) for j in range(ell))
    assert spub < 1.0
    assert abs(spub - cdf(ell-1,alpha,theta,beta)/cdf(ell,alpha,theta,beta)) < 1e-13

records=(2,1,0)
lp=lower_like_source(records,alpha,theta,beta)
lc=lower_like_strict(records,alpha,theta,beta)
ratio=lp/lc

assert abs(lp-0.029669639318996233) < 1e-15
assert abs(lc-0.05973903647945523) < 1e-15
assert abs(ratio-0.4966541321636461) < 1e-15

print("VERIFY_OK")
print("F0",repr(cdf(0,alpha,theta,beta)))
print("F1",repr(cdf(1,alpha,theta,beta)))
print("F2",repr(cdf(2,alpha,theta,beta)))
print("source_likelihood",repr(lp))
print("strict_likelihood",repr(lc))
print("ratio",repr(ratio))
