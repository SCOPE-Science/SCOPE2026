import math

def gamma_m(m):
    return (m*math.sqrt(2.0)+1.0)/(((2*m+1)*math.sqrt(2.0))+2.0)

def continued_fraction_denominators(m, count=10):
    a=[0,2,m,1]+[2]*(count+5)
    qm1=0
    q=1
    qs=[q]
    for j in range(1,count):
        qn=a[j]*q+qm1
        qs.append(qn)
        qm1,q=q,qn
    return qs

def source_values(m, K):
    g=gamma_m(m)
    h=math.pi*(0.5-g)
    R=1.0/math.sin(h)
    assert abs(h-math.pi/(2*(2*m+1+math.sqrt(2)))) < 5e-15
    qs=continued_fraction_denominators(m,8)
    assert qs[2]==2*m+1
    assert qs[3]==2*m+3
    assert qs[4]==6*m+7

    def G(x):
        return math.atan(math.sqrt(x*x-1.0))-math.atan(math.sqrt(R*R-1.0))
    def Fminus(a):
        return -G(R*math.cos(a))
    def Fplus(a,b):
        x=R*math.sin(a-b)/(math.sin(a)-math.sin(b))
        return G(x)

    ds=[]
    for k in range(1,K+2):
        x=(2*k-1)*g
        ds.append(math.pi*abs(x-round(x)))

    for k in range(2,K+1):
        a,b=sorted(ds[:k])[:2]
        fm=Fminus(a)
        fp=Fplus(a,b)
        if not (fm < ds[k] + 2e-12 and fp < ds[k] + 2e-12):
            raise AssertionError((m,k,a,b,ds[k],fm,fp))

    # Exact prefix formulas from the proof, numerically cross-checked.
    for k in range(2,m+2):
        alpha=math.pi/2-(2*k-1)*h
        beta=math.pi/2-(2*k-3)*h
        fm_exact=math.asin(math.sin(h)/math.sin((2*k-1)*h))-h
        fp_exact=h-math.asin(math.tan(h)*math.sin(2*(k-1)*h))
        assert abs(Fminus(alpha)-fm_exact) < 2e-12
        assert abs(Fplus(alpha,beta)-fp_exact) < 2e-12

    # Source bounded-tail criterion at j0=3.
    q3,q4=qs[3],qs[4]
    lhs=4*math.pi/(math.cos(math.pi/q3)*math.sqrt(R*R*math.cos(math.pi/q4)**2-1))
    assert lhs < q3

for m in range(2,101):
    source_values(m, min(5000, max(200,m+20)))

# Deep-tail stress tests.
for m in [2,3,4,10,25,100]:
    source_values(m,5000)

# Growth sanity checks.
for m in [1000,10000]:
    h=math.pi/(2*(2*m+1+math.sqrt(2)))
    R=1/math.sin(h)
    A=4*math.pi/3*(1/math.tan(h))**3
    assert abs(R/(4*m/math.pi)-1) < 0.003
    assert abs(A/(256*m**3/(3*math.pi**2))-1) < 0.01

print("VERIFY_OK family_m=2..100 deep_tail=5000")
