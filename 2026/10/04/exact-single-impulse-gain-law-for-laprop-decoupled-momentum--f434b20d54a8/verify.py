import math

def laprop_terms(mu,nu,eps,G,T):
    m=0.0
    n=0.0
    out=[]
    for t in range(1,T+1):
        g=G if t==1 else 0.0
        n=nu*n+(1.0-nu)*g*g
        cn=1.0-nu**t
        z=g/(math.sqrt(n/cn)+eps)
        m=mu*m+(1.0-mu)*z
        cm=1.0-mu**t
        u=m/cm if cm>0.0 else z
        out.append(u)
    return out

def closed_term(mu,eps,G,t):
    if mu==0.0:
        return G/(abs(G)+eps) if t==1 else 0.0
    return (G/(abs(G)+eps))*(1.0-mu)*mu**(t-1)/(1.0-mu**t)

def gain(mu,tol=1e-16):
    if mu==0.0:
        return 1.0
    s=0.0
    t=1
    while True:
        term=(1.0-mu)*mu**(t-1)/(1.0-mu**t)
        s+=term
        if t>100 and term<tol:
            return s
        t+=1
        assert t<5000000

for mu in (0.0,0.2,0.8,0.9,0.99):
    for nu in (0.0,0.2,0.95,0.999):
        for eps in (1e-12,1e-8,1e-3):
            vals=laprop_terms(mu,nu,eps,2.5,200)
            for t,u in enumerate(vals,1):
                c=closed_term(mu,eps,2.5,t)
                assert abs(u-c)<=3e-12*max(1.0,abs(c))

assert abs(gain(0.8)-2.389264347082911)<2e-13
assert abs(gain(0.9)-3.0096094482297993)<2e-13
assert abs(gain(0.99)-5.205993946942028)<3e-12
vals=[gain(x) for x in (0.0,0.2,0.5,0.8,0.9,0.95,0.99)]
assert all(b>a for a,b in zip(vals,vals[1:]))
assert gain(0.999)>7.0

def adam_term(mu,nu,t):
    return ((1.0-mu)*mu**(t-1)/(1.0-mu**t))*math.sqrt((1.0-nu**t)/((1.0-nu)*nu**(t-1)))

nu=0.81
root=math.sqrt(nu)
sub=[adam_term(0.8,nu,t) for t in range(1,500)]
assert sub[-1]<1e-20 and sum(sub)<20.0
crit=[adam_term(root,nu,t) for t in (300,500,700)]
assert max(crit)-min(crit)<1e-10
sup=[adam_term(0.95,nu,t) for t in (40,60,80)]
assert sup[2]>sup[1]>sup[0]

print("verification passed")
