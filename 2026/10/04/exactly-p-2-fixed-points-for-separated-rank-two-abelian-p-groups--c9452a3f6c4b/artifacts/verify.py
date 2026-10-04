from itertools import product
from math import gcd

def vp(n,p):
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def units(mod):
    return [x for x in range(mod) if gcd(x,mod)==1]

def fixed_order_from_minors(p,a,b,alpha,beta,gamma,delta):
    h=b-a
    u=(alpha-1) % (p**a)
    z=(delta-1) % (p**b)
    # Integer representatives of the six 2x2 minors.
    minors=[
        p**(a+b),
        (p**b)*gamma,
        (p**a)*z,
        (p**b)*u,
        (p**b)*beta,
        u*z-(p**h)*beta*gamma,
    ]
    g=0
    for m in minors:
        g=gcd(g,abs(m))
    return g

def direct_fixed_order(p,a,b,alpha,beta,gamma,delta):
    pa=p**a
    pb=p**b
    h=b-a
    count=0
    for x in range(pa):
        for y in range(pb):
            xx=(alpha*x + beta*y) % pa
            yy=((p**h)*gamma*x + delta*y) % pb
            if xx==x and yy==y:
                count += 1
    return count

def theta_formula(p,a,b):
    assert b-a>=2 and not (a==1 and b==3)
    if a==1:
        return 2*p**(b-1)*(p-1)**2
    if a==2 and b==4:
        return p**5*(3*p**3-6*p**2+p+1)
    if a==2:
        return p**(b+2)*(3*p**2-7*p+3)
    if b==a+2:
        return p**(3*a+b-5)*(p-1)*(3*p**2-4*p-1)
    return p**(3*a+b-4)*(p-1)*(3*p-5)

def count_theta_p2(p,a,b,direct=False):
    pa=p**a
    pb=p**b
    total=0
    for alpha in units(pa):
        for beta in range(pa):
            for gamma in range(pa):
                for delta in units(pb):
                    fo=fixed_order_from_minors(p,a,b,alpha,beta,gamma,delta)
                    if direct:
                        fd=direct_fixed_order(p,a,b,alpha,beta,gamma,delta)
                        assert fo==fd,(p,a,b,alpha,beta,gamma,delta,fo,fd)
                    if fo==p**2:
                        total += 1
    return total

# Every formula branch is represented.
cases=[
    (2,1,4,True),
    (3,1,4,True),
    (2,2,4,True),
    (3,2,4,False),
    (2,2,5,False),
    (3,2,5,False),
    (2,3,5,False),
    (2,3,6,False),
]
for p,a,b,direct in cases:
    got=count_theta_p2(p,a,b,direct=direct)
    want=theta_formula(p,a,b)
    assert got==want,(p,a,b,got,want)

# Published separated boundary pair (1,3), deliberately excluded from theorem.
for p in (2,3,5):
    got=count_theta_p2(p,1,3,direct=(p<=3))
    known=p*(2*p**3-3*p**2+1)
    assert got==known,(p,got,known)

print("VERIFY_OK")
