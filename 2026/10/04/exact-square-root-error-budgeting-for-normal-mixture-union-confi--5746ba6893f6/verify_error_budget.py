import math


def boundary(V, a, eta):
    return math.sqrt((V + eta**-2) * math.log((1.0 + eta*eta*V)/(a*a)))


def objective(Vs, alloc, eta):
    return sum(boundary(V,a,eta) for V,a in zip(Vs,alloc))


def optimum(Vs, alpha, eta):
    s=[math.sqrt(V+eta**-2) for V in Vs]
    S=sum(s)
    a=[alpha*x/S for x in s]
    W=S*math.sqrt(math.log(eta*eta*S*S/(alpha*alpha)))
    return a,W


def second_derivative(V,a,eta):
    Q=V+eta**-2
    L=math.log((1+eta*eta*V)/(a*a))
    b=math.sqrt(Q*L)
    return Q/(a*a*b)*(1.0-1.0/L)


def check_case(Vs, alpha, eta):
    alloc,W=optimum(Vs,alpha,eta)
    direct=objective(Vs,alloc,eta)
    assert abs(direct-W) <= 2e-12*max(1.0,W)
    s=[math.sqrt(V+eta**-2) for V in Vs]
    ratios=[a/x for a,x in zip(alloc,s)]
    assert max(ratios)-min(ratios) < 1e-14
    for V in Vs:
        for frac in (0.05,0.2,0.5,0.8,0.95):
            a=alpha*frac
            assert second_derivative(V,a,eta) > 0
    if len(Vs)==2:
        best=W
        for k in range(1,5000):
            a0=alpha*k/5000
            val=objective(Vs,[a0,alpha-a0],eta)
            assert val >= best-1e-10*max(1.0,best)
    if len(Vs)==3:
        best=W
        for i in range(1,150):
            for j in range(1,150-i):
                a0=alpha*i/150
                a1=alpha*j/150
                a2=alpha-a0-a1
                val=objective(Vs,[a0,a1,a2],eta)
                assert val >= best-1e-10*max(1.0,best)


for Vs,alpha,eta in [
    ([10.0,100.0],0.05,1.0),
    ([100.0,10.0],0.10,2.0),
    ([0.0,0.0],0.05,0.7),
    ([2.0,20.0,200.0],0.05,1.3),
]:
    check_case(Vs,alpha,eta)

# Equal allocation is optimal exactly for equal clocks in the two-arm examples.
a,_=optimum([25.0,25.0],0.05,1.0)
assert abs(a[0]-0.025)<1e-14 and abs(a[1]-0.025)<1e-14
a,_=optimum([25.0,100.0],0.05,1.0)
assert a[1]>a[0]

# Entropy/KL coefficient identity.
v=[1.0,4.0,9.0]
s=[math.sqrt(x) for x in v]
S=sum(s)
q=[x/S for x in s]
m=len(q)
H=-sum(x*math.log(x) for x in q)
D=sum(x*math.log(m*x) for x in q)
assert abs(D-(math.log(m)-H))<1e-14
assert D>0

print('VERIFY_OK')
