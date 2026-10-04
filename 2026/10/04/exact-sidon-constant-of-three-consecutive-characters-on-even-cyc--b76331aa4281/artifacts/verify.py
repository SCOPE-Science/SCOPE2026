import cmath, math, random

def theorem_constant(N):
    return math.sqrt(1.0 + 1.0/(math.cos(math.pi/N)**2))

def witness(N):
    a=math.pi/N
    q=math.cos(a)**2
    c0=1+0j
    c2=cmath.exp(2j*a)
    c1=2*q*cmath.exp(1j*(a+math.pi/2))
    vals=[]
    for k in range(N):
        z=cmath.exp(2j*math.pi*k/N)
        vals.append(abs(c0+c1*z+c2*z*z))
    return (abs(c0)+abs(c1)+abs(c2))/max(vals)

def random_check(N, trials=200):
    C=theorem_constant(N)
    for _ in range(trials):
        cs=[complex(random.uniform(-1,1),random.uniform(-1,1)) for _ in range(3)]
        l1=sum(abs(c) for c in cs)
        if l1==0: continue
        M=0.0
        for k in range(N):
            z=cmath.exp(2j*math.pi*k/N)
            M=max(M,abs(cs[0]+cs[1]*z+cs[2]*z*z))
        assert l1/M <= C + 2e-12

for N in range(4,202,2):
    C=theorem_constant(N)
    W=witness(N)
    assert abs(C-W) < 5e-12, (N,C,W)
    random_check(N)
print('VERIFY_OK')
