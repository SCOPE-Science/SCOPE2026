import itertools, math
from fractions import Fraction


def H(k, power=1):
    return sum(Fraction(1, i**power) for i in range(1,k+1))

def apk(bits):
    k=len(bits); s=0; out=Fraction(0)
    for i,b in enumerate(bits,1):
        s += b
        if b:
            out += Fraction(s,i)
    return out/k

def eta(k,m):
    h=H(k)
    return Fraction(m,1)*h/(k*k) + Fraction(m*(m-1),1)*(k-h)/(k*k*(k-1)) if k>1 else Fraction(m,1)

def mu(k,p):
    h=float(H(k)); return p*p+p*(1-p)*h/k

def source_var(k,p):
    h=float(H(k)); h2=float(H(k,2))
    return 5*p**3*(1-p)/k + p*(1-p)/k**2*(p*(1-2*p)*(3*h+h*h)+(1-p)*(1-3*p)*h2)

# Exact conditional means by exhaustive enumeration.
for k in range(2,9):
    for m in range(k+1):
        vals=[apk(b) for b in itertools.product([0,1], repeat=k) if sum(b)==m]
        ex=sum(vals, Fraction(0))/len(vals)
        assert ex == eta(k,m), (k,m,ex,eta(k,m))

# Exact Bernoulli mean/variance against source formulas at rational p values.
for k in range(2,8):
    for p in [0.2,0.37,0.5,0.8]:
        vals=[]; probs=[]
        for b in itertools.product([0,1], repeat=k):
            m=sum(b); pr=p**m*(1-p)**(k-m)
            vals.append(float(apk(b))); probs.append(pr)
        ex=sum(v*w for v,w in zip(vals,probs))
        va=sum((v-ex)**2*w for v,w in zip(vals,probs))
        assert abs(ex-mu(k,p)) < 2e-12
        assert abs(va-source_var(k,p)) < 2e-12, (k,p,va,source_var(k,p))

# Check exact linear + degenerate quadratic decomposition numerically.
for k in range(2,8):
    p=0.37; hks=[sum(1/j for j in range(1,i+1)) for i in range(1,k+1)]
    hk=hks[-1]
    cs=[p+(1-p)/(i+1)+p*(hk-hks[i]) for i in range(k)]
    ea=mu(k,p)
    for b in itertools.product([0,1], repeat=k):
        xs=[z-p for z in b]
        lin=sum(c*x for c,x in zip(cs,xs))/k
        quad=sum(xs[j]*xs[i]/(i+1) for i in range(1,k) for j in range(i))/k
        assert abs(float(apk(b))-ea-lin-quad) < 5e-12

# Asymptotic coefficient constants: 5 before prevalence adjustment, 1 after.
for k in [1000,10000,100000]:
    p=0.37
    hs=[]; cur=0.0
    for i in range(1,k+1):
        cur += 1/i; hs.append(cur)
    hk=hs[-1]
    cs=[p+(1-p)/i+p*(hk-hs[i-1]) for i in range(1,k+1)]
    d=2*p+(1-2*p)*hk/k
    v1=sum(c*c for c in cs)/k/p**2
    v2=sum((c-d)**2 for c in cs)/k/p**2
    if k==100000:
        assert abs(v1-5) < 0.01, v1
        assert abs(v2-1) < 0.01, v2

# Check eta - plug-in mean exact algebra numerically for all m.
for k in range(2,50):
    h=float(H(k))
    for m in range(k+1):
        lhs=float(eta(k,m))-mu(k,m/k)
        rhs=m*(k-m)*(h-k)/(k**3*(k-1))
        assert abs(lhs-rhs)<1e-12
print('VERIFY_OK')
