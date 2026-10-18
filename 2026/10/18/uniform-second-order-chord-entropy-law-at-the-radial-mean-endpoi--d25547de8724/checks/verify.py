"""Independent analytic/numeric checks of chord endpoint formulas.
No reliance on unpublished datasets.
"""
import math

def upper(d,eps):
    m=d-1
    logbin=math.lgamma(d+eps)-math.lgamma(d)-math.lgamma(1+eps)
    return math.exp((logbin-eps*math.log(d))/(1-eps))

def cone_ratio(d,eps):
    # Z=d*T, T~Beta(1,d-1)
    logEZ=eps*math.log(d)+math.lgamma(1+eps)+math.lgamma(d)-math.lgamma(d+eps)
    return math.exp(logEZ/(eps-1))

def log_ratio_from_moments(eps,log_mom,mean):
    return (log_mom-eps*math.log(mean))/(eps-1)

for d in range(2,20):
    H=sum(1.0/k for k in range(1,d))
    H2=sum(1.0/(k*k) for k in range(1,d))
    J=H-math.log(d)
    for e in [.001,.01,.07,.2,.45,.8]:
        assert abs(upper(d,e)-cone_ratio(d,e))<1e-10
        assert 1<=upper(d,e)+1e-12
        lr=math.log(cone_ratio(d,e))
        if e<=.07:
            approximation=e*J+e*e*(J-.5*H2)
            assert abs(lr-approximation)<4*e**3
print('PASS: 18 dimensions, cone sharpness and second-order expansions')

# Planar unit disk: transversal chord lengths L(y)=2sqrt(1-y^2).
mean=math.pi/2
j_disk=1+math.log(math.pi/8)
var_disk=1-math.pi**2/12
assert 0<j_disk<1-math.log(2)
for e in [.003,.02,.05]:
    logEL=e*math.log(2)+.5*math.log(math.pi)-math.log(2)+math.lgamma(1+e/2)-math.lgamma(1.5+e/2)
    logR=log_ratio_from_moments(e,logEL,mean)
    asym=e*j_disk+e*e*(j_disk-.5*var_disk)
    assert abs(logR-asym)<2*e**3, (e,logR,asym)
    assert logR > 0 and math.exp(logR)<upper(2,e)
print('PASS: nonextremal disk chord profile and sharp planar Jensen gap')

# Check raw chord-integral identity at nonzero p for generic rectangle direction:
# square sides 2,2, axis length L=2 constant, |K|=4, B=2.
for p in [-.9,-.5,-.2,.2,.75,2.]:
    radial=(2**(p+1)*2/(4*(p+1)))**(1/p)
    norm=(p+1)**(1/p)*radial
    assert abs(norm-2)<1e-12
print('PASS: cylinder equality for every sampled nonzero p>-1')

# Planar square diagonal direction: length tent on projected interval ->
# normalized chord Z=2(1-|Y|/a), distribution Z=2*T with T uniform (0,1).
for e in [.01,.2,.7]:
    EZ=2**e/(1+e)
    r=EZ**(1/(e-1))
    assert abs(r-upper(2,e))<2e-12
print('PASS: planar-square diagonal achieves universal sharp upper bound')
