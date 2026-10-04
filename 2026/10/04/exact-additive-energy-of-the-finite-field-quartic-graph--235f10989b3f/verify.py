from collections import defaultdict


def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def energy_prime(p):
    fib=defaultdict(int)
    for a in range(p):
        a4=pow(a,4,p)
        for b in range(p):
            fib[((a+b)%p,(a4+pow(b,4,p))%p)] += 1
    return sum(v*v for v in fib.values())


def formula(q, eps):
    return 3*q*q-q-1-(q-1)*(1+eps)**2


def find_nonsquare(p):
    for d in range(2,p):
        if legendre(d,p)==-1:
            return d
    raise RuntimeError


def add(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)

def neg(x,p):
    return ((-x[0])%p,(-x[1])%p)

def mul(x,y,p,d):
    a,b=x; c,e=y
    return ((a*c+b*e*d)%p,(a*e+b*c)%p)

def pw(x,n,p,d):
    r=(1,0)
    while n:
        if n&1: r=mul(r,x,p,d)
        x=mul(x,x,p,d); n//=2
    return r

def chi2(x,p,d):
    if x==(0,0): return 0
    q=p*p
    y=pw(x,(q-1)//2,p,d)
    if y==(1,0): return 1
    if y==((p-1)%p,0): return -1
    raise AssertionError((p,d,x,y))

def energy_p2(p):
    d=find_nonsquare(p)
    els=[(a,b) for a in range(p) for b in range(p)]
    fourth={x:pw(x,4,p,d) for x in els}
    fib=defaultdict(int)
    for a in els:
        for b in els:
            fib[(add(a,b,p),add(fourth[a],fourth[b],p))]+=1
    q=p*p
    minus3=((p-3)%p,0)
    eps=chi2(minus3,p,d)
    return q,eps,sum(v*v for v in fib.values())

# Prime fields: broad exact census.
prime_checks=0
for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]:
    eps=legendre(-3,p)
    got=energy_prime(p)
    want=formula(p,eps)
    assert got==want,(p,got,want,eps)
    # Equivalent mod-3 form.
    if p%3==1:
        assert eps==1 and want==3*p*p-5*p+3
    else:
        assert p%3==2 and eps==-1 and want==3*p*p-p-1
    prime_checks+=1

# Quadratic extensions test the prime-power statement beyond prime fields.
ext_checks=0
for p in [5,7,11]:
    q,eps,got=energy_p2(p)
    want=formula(q,eps)
    assert eps==1  # q == 1 (mod 3) for p != 3
    assert got==want,(q,got,want)
    ext_checks+=1

# Algebraic factorization used in the proof, checked symbolically at integer samples.
for s in range(-4,5):
    for u in range(-4,5):
        for v in range(-4,5):
            lhs=(s**4-4*u*s*s+2*u*u)-(s**4-4*v*s*s+2*v*v)
            rhs=2*(u-v)*(u+v-2*s*s)
            assert lhs==rhs

print(f"VERIFY_OK prime_fields={prime_checks} quadratic_extensions={ext_checks} max_prime=101")
