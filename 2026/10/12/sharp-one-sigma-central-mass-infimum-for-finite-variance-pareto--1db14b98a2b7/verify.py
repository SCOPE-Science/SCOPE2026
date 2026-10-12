import math

def central(alpha):
    A=(alpha+math.sqrt(alpha/(alpha-2.0)))/(alpha-1.0)
    return 1.0-A**(-alpha)

target=1.0-math.exp(-2.0)
for alpha in [2.001,2.01,2.1,2.5,3.0,5.0,10.0,100.0,1000.0,1e6]:
    c=central(alpha)
    assert c>target, (alpha,c,target)

# First-order asymptotic defect: alpha*(C_alpha-target) -> exp(-2).
for alpha in [1e4,1e5,1e6]:
    scaled=alpha*(central(alpha)-target)
    assert abs(scaled-math.exp(-2.0)) < 3e-4, (alpha,scaled)

# Formula agrees with direct CDF evaluation at a representative scale.
for alpha in [2.1,3.0,7.0,50.0]:
    a=3.7
    mu=alpha*a/(alpha-1.0)
    sigma=a*math.sqrt(alpha)/((alpha-1.0)*math.sqrt(alpha-2.0))
    assert mu-sigma<a
    direct=1.0-(a/(mu+sigma))**alpha
    assert abs(direct-central(alpha)) < 2e-15
print('VERIFY_OK')
