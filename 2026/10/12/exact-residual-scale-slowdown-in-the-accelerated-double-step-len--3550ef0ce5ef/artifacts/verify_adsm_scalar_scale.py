import math, random

random.seed(34)

def source_lhs_rhs(a, eta, w1, w2, chi, s, alpha):
    B=eta+1.0
    q=-eta*s
    sn=(1.0-B*alpha)*s
    h=lambda z: 0.5*(a*z)**2
    lhs=h(sn)-h(s)
    rhs=-(w1*((alpha+alpha/eta)*a*s)**2
          +w2*((alpha+alpha/eta)*q)**2)+chi*h(s)
    return lhs, rhs

def poly(a, eta, w1, w2, chi, alpha):
    B=eta+1.0
    A=B*B*(0.5+w1/(eta*eta)+w2/(a*a))
    return A*alpha*alpha-B*alpha-0.5*chi

def amax(a, eta, w1, w2, chi):
    B=eta+1.0
    A=B*B*(0.5+w1/(eta*eta)+w2/(a*a))
    return (B+math.sqrt(B*B+2.0*A*chi))/(2.0*A)

def abar(a, eta, w1, w2):
    return 1.0/((eta+1.0)*(0.5+w1/(eta*eta)+w2/(a*a)))

def mind(r, threshold):
    m=0
    while r**m > threshold:
        m+=1
    return m

# Exact secant calibration: v=a*u makes the scalar update equal a.
for _ in range(200):
    a=10**random.uniform(-3,2)
    eta=random.uniform(1.01,1.99)
    delta=10**random.uniform(-2,2)
    s=random.choice([-1.0,1.0])*10**random.uniform(-2,2)
    alpha=10**random.uniform(-3,0)
    q=-eta/delta*a*s
    u=(alpha+alpha/eta)*q
    assert u != 0.0
    v=a*u
    dnew=v*v/((alpha+alpha/eta)*v*q)
    assert abs(dnew-a) <= 2e-12*max(1.0,a)

# Direct source inequality and reduced polynomial have identical truth values.
for _ in range(1000):
    a=10**random.uniform(-3,2)
    eta=random.uniform(1.01,1.99)
    w1=10**random.uniform(-3,0)
    w2=10**random.uniform(-3,0)
    chi=10**random.uniform(-5,-1)
    s=random.choice([-1.0,1.0])*10**random.uniform(-2,2)
    alpha=10**random.uniform(-4,0)
    lhs,rhs=source_lhs_rhs(a,eta,w1,w2,chi,s,alpha)
    p=poly(a,eta,w1,w2,chi,alpha)
    scale=max(1.0,abs(lhs),abs(rhs))
    if abs(lhs-rhs)>1e-11*scale and abs(p)>1e-11:
        assert (lhs<=rhs)==(p<=0.0)
    am=amax(a,eta,w1,w2,chi)
    assert (alpha<=am)==(p<=0.0)

# Stabilization for a positive summable sequence chi_k=1/(k+2)^2.
eta=1.5; w1=0.1; w2=0.2; r=0.5
for a in [1.0,0.3,0.1,0.03,0.01]:
    ms=mind(r,abar(a,eta,w1,w2))
    tail=[]
    for k in range(200,600):
        chi=1.0/(k+2.0)**2
        tail.append(mind(r,amax(a,eta,w1,w2,chi)))
    assert set(tail)=={ms}

# Small-scale laws: contraction gap is comparable to a^2 and m grows logarithmically.
vals=[]
for a in [1e-2,3e-3,1e-3,3e-4,1e-4]:
    ba=abar(a,eta,w1,w2)
    m=mind(r,ba)
    al=r**m
    B=eta+1.0
    rho=abs(1.0-B*al)
    assert m>0 and 0.0 < B*al < 1.0
    assert r*ba < al <= ba
    gap=1.0-rho
    assert gap/(a*a) > 0.5
    assert gap/(a*a) < 10.0
    vals.append((a,m,gap))
# m - 2 log(1/a)/|log r| stays bounded on the tested scales.
offsets=[m-2.0*math.log(1.0/a)/abs(math.log(r)) for a,m,_ in vals]
assert max(offsets)-min(offsets) < 2.1

print('VERIFY_OK')
