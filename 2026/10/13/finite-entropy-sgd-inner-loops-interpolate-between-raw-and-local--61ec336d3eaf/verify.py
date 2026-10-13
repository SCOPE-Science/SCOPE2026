import random

def S(K, alpha, z):
    r=1.0-alpha
    return alpha*sum((r**(K-j))*(1.0-(1.0-z)**j) for j in range(1,K+1))

def phi(h,gamma,eta,K,alpha):
    return gamma*h/(h+gamma)*S(K,alpha,eta*(h+gamma))

def direct(h,gamma,eta,K,alpha,x=1.7):
    y=x; mu=x
    for _ in range(K):
        y=y-eta*(h*y+gamma*(y-x))
        mu=(1.0-alpha)*mu+alpha*y
    return gamma*(x-mu)/x

random.seed(350069)
for _ in range(2500):
    h=10.0**random.uniform(-3,3); gamma=10.0**random.uniform(-3,3)
    eta=random.uniform(1e-8,1.0/(h+gamma)); K=random.randint(1,35); alpha=random.uniform(0.01,1.0)
    a=direct(h,gamma,eta,K,alpha); b=phi(h,gamma,eta,K,alpha)
    assert abs(a-b)<=3e-11*max(1.0,abs(a),abs(b))
for _ in range(500):
    mu=10.0**random.uniform(-3,1); M=mu*10.0**random.uniform(0.01,3); gamma=10.0**random.uniform(-3,2)
    eta=random.uniform(1e-8,1.0/(M+gamma)); alpha=random.uniform(0.01,1.0)
    ratio=phi(M,gamma,eta,1,alpha)/phi(mu,gamma,eta,1,alpha)
    assert abs(ratio-M/mu)<8e-11*(M/mu)
for _ in range(3000):
    mu=10.0**random.uniform(-3,1); kappa=10.0**random.uniform(0.01,3); M=mu*kappa; gamma=10.0**random.uniform(-3,2)
    eta=random.uniform(1e-7,0.999999/(M+gamma)); K=random.randint(2,30); alpha=random.uniform(0.01,1.0)
    kfin=phi(M,gamma,eta,K,alpha)/phi(mu,gamma,eta,K,alpha)
    kideal=kappa*(mu+gamma)/(M+gamma)
    assert kfin>kideal*(1.0-3e-12)
    assert kfin<kappa*(1.0+3e-12)
for mu,M,gamma,eta,alpha in [(1.0,100.0,1.0,1/101,0.75),(0.3,7.0,2.0,0.08,0.4),(2.0,9.0,0.5,0.05,1.0)]:
    kideal=(M/mu)*(mu+gamma)/(M+gamma)
    kfin=phi(M,gamma,eta,1500,alpha)/phi(mu,gamma,eta,1500,alpha)
    assert abs(kfin-kideal)<4e-7*max(1.0,kideal)
mu,M,gamma,K,alpha=1.0,40.0,3.0,7,0.75
raw=M/mu
eta=1e-8
kfin=phi(M,gamma,eta,K,alpha)/phi(mu,gamma,eta,K,alpha)
assert abs(kfin-raw)<5e-5
print('verification passed')
