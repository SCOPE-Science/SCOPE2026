"""Pure-Python numerical corroboration of Pareto-reset SSEP scaling.

Usage: python3 check_stdlib.py
No external packages; numerical checks complement, but do not replace, proof.
"""
import itertools
import math

passed = 0

def verify(condition, label):
    global passed
    if not condition:
        raise AssertionError(label)
    passed += 1


def h(y, u):
    return 0.5*math.erfc(y/(2*math.sqrt(u)))


def integrate_01(fn, n=4000):
    # Composite Simpson quadrature; n is even.
    total = fn(0.)+fn(1.)
    for j in range(1,n):
        total += (4 if j%2 else 2)*fn(j/n)
    return total/(3*n)


def weighted(alpha, fn):
    c=(alpha-1)/alpha
    small=integrate_01(lambda s: fn(max(s,1e-300)))
    # Transform u=1/(s**8) for u>=1; integrable for alpha>=1.5.
    tail=integrate_01(lambda s: 0 if s==0 else 8*s**(8*(alpha-1)-1)*fn(s**-8))
    return c*(small+tail)


def kernel(alpha,y,z):
    a=weighted(alpha,lambda u:h(y,u))
    b=weighted(alpha,lambda u:h(z,u))
    c=weighted(alpha,lambda u:h(y,u)*h(z,u))
    return c-a*b

for alpha in (1.5,2.,3.,5.):
    verify(abs(weighted(alpha,lambda u:1.)-1.)<5e-10,'age normalization')
    verify(abs(weighted(alpha,lambda u:h(0.,u))-.5)<5e-10,'center density')
    verify(kernel(alpha,1.,2.)>0,'same-side positive')
    verify(kernel(alpha,-1.,-2.)>0,'same-side negative-half positive')
    verify(kernel(alpha,1.,-2.)<0,'opposite-side negative')
    verify(abs(kernel(alpha,0.,2.))<2e-9,'center zero')
    verify(abs(kernel(alpha,2.,1.)-kernel(alpha,1.,2.))<2e-9,'symmetry')

# Independent exact enumeration of all SSEP occupation states on a four-cycle.
L=4
configs=list(itertools.combinations(range(L),2))
index={config:i for i,config in enumerate(configs)}

def generator(states):
    where={state:i for i,state in enumerate(states)}
    Q=[[0.]*len(states) for _ in states]
    for i,state in enumerate(states):
        occupied=set(state)
        for x in state:
            for y in ((x-1)%L,(x+1)%L):
                if y in occupied:continue
                nxt=tuple(sorted((occupied-{x})|{y}))
                # Each undirected bond swaps particles at rate 1.
                # Iterating occupied particles finds each enabled swap once.
                Q[i][where[nxt]]+=1.
                Q[i][i]-=1.
    return Q

# Uniformization computes the distribution e^(t Q) from a point mass.
def law(Q,at,t):
    m=len(Q)
    rate=max(-Q[i][i] for i in range(m))
    if rate==0:return [float(i==at) for i in range(m)]
    P=[[float(i==j)+Q[i][j]/rate for j in range(m)] for i in range(m)]
    prob=[float(i==at) for i in range(m)]
    p=math.exp(-rate*t)
    out=[p*z for z in prob]
    for k in range(1,150):
        prob=[sum(prob[i]*P[i][j] for i in range(m)) for j in range(m)]
        p*=rate*t/k
        for j in range(m):out[j]+=p*prob[j]
        if p<1e-16 and k>rate*t+15:break
    return out

Q=generator(configs)
init=index[(0,1)]
for t in (0.2,0.9,2.3,5.0):
    p=law(Q,init,t)
    verify(abs(sum(p)-1)<2e-13,'law normalization')
    rho=[sum(prob*(j in state) for prob,state in zip(p,configs)) for j in range(L)]
    check_cov=[]
    for i in range(L):
        for j in range(i+1,L):
            pair=sum(prob*(i in state and j in state) for prob,state in zip(p,configs))
            check_cov.append(pair-rho[i]*rho[j])
    verify(max(check_cov)<1e-12,'conditional SSEP negative pair covariances')
    verify(abs(sum(rho)-2.)<2e-13,'mass conserved')

# Independent one-particle dual and two-particle dual generator results.
one=[(i,) for i in range(L)]
Aone=generator(one) # With one particle moves on the same ring.
Atwo=generator(configs)
for t in (0.3,1.2,3.0):
    p=law(Q,init,t)
    for j in range(L):
        expectation=sum(prob*(j in state) for prob,state in zip(p,configs))
        q=law(Aone,j,t)
        dual=sum(q[i]*float(one[i][0]<2) for i in range(L))
        verify(abs(expectation-dual)<5e-13,'one-site dual')
    for j,(x,y) in enumerate(configs):
        expectation=sum(prob*(x in state and y in state) for prob,state in zip(p,configs))
        q=law(Atwo,j,t)
        dual=sum(q[i]*float(set(configs[i]).issubset({0,1})) for i in range(len(configs)))
        verify(abs(expectation-dual)<5e-13,'two-site dual')

print(f'PASS: {passed} deterministic checks (standard library only)')
for alpha in (1.5,2.,3.):
    print('alpha=',alpha,'K(1,2)=',format(kernel(alpha,1.,2.),'.12g'),
          'K(-1,2)=',format(kernel(alpha,-1.,2.),'.12g'))
