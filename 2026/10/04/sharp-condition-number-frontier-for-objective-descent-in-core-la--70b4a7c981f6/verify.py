import math, random

def rho_star(k):
    return 3*math.sqrt(3)*k*(k+1)/(k*k+k+1)**1.5

def p_star(k):
    return (2*k+1)/((k+1)*(k*k+k+1))

def threshold(vals,w):
    A=sum(q*l*l for q,l in zip(w,vals))
    B=sum(q*l*l*l for q,l in zip(w,vals))
    return 2*A**1.5/B

def obj_ratio(vals,w,rho):
    A=sum(q*l*l for q,l in zip(w,vals))
    E=sum(q*l for q,l in zip(w,vals))
    s=rho/math.sqrt(A)
    En=sum(q*l*(1-s*l)**2 for q,l in zip(w,vals))
    return En/E

for k in (1,1.2,2,5,20,100):
    a=1/k
    p=p_star(k)
    r=rho_star(k)
    assert abs(threshold([a,1],[1-p,p])-r)<3e-12
    assert abs(obj_ratio([a,1],[1-p,p],r)-1)<4e-12
    assert obj_ratio([a,1],[1-p,p],r*(1+1e-6))>1

for k in (1.1,2,3,10,50):
    a=1/k
    r=rho_star(k)
    best=10
    bp=None
    for j in range(20001):
        p=j/20000
        t=threshold([a,1],[1-p,p])
        if t<best:
            best,bp=t,p
    assert best>=r-2e-8
    assert abs(bp-p_star(k))<2e-4

random.seed(1)
for k in (1.5,3,10,30):
    a=1/k
    r=rho_star(k)
    for _ in range(5000):
        n=random.randrange(2,9)
        vals=[a+(1-a)*random.random() for _ in range(n)]
        raw=[random.random()+1e-4 for _ in range(n)]
        z=sum(raw)
        w=[q/z for q in raw]
        assert threshold(vals,w)>=r-1e-12

assert abs(rho_star(1)-2)<1e-12
assert abs(1e5*rho_star(1e5)-3*math.sqrt(3))<1e-4
print("verification passed")
