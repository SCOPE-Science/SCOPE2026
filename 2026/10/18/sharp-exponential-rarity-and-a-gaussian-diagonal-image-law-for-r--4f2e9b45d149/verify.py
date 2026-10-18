"""Independent numerical and finite-magma checks for random-magma regularity."""
import itertools, math

def exact_count_formula(n):
    # integer occupancy: count full mappings of length t with image cardinality d
    a=[0]*(n+1); a[0]=1
    for t in range(n):
        b=[0]*(n+1)
        for d in range(t+1):
            if a[d]:
                b[d]+=d*a[d]
                b[d+1]+=(n-d)*a[d]
        a=b
    N=n*(n-1)//2
    return sum(a[d]*(n*n-n+d)**N for d in range(1,n+1))

def brute_count(n):
    total=0; distribution={}
    for xs in itertools.product(range(n),repeat=n*n):
        di={xs[i*n+i] for i in range(n)}
        valid=True
        for i in range(n):
            for j in range(i+1,n):
                if xs[i*n+j]==xs[j*n+i] and xs[i*n+j] not in di:
                    valid=False; break
            if not valid: break
        if valid:
            total+=1
            distribution[len(di)]=distribution.get(len(di),0)+1
    return total,distribution

def direct_semigroup_regular_count(n):
    tables=list(itertools.product(range(n), repeat=n*n))
    def combine(f,g):
        return tuple(g[f[i*n+j]*n+f[j*n+i]] for i in range(n) for j in range(n))
    regular=0
    for f in tables:
        exists=any(combine(combine(f,g),f)==f for g in tables)
        diagonal={f[i*n+i] for i in range(n)}
        criterion=all(f[i*n+j]!=f[j*n+i] or f[i*n+j] in diagonal
                      for i in range(n) for j in range(i+1,n))
        assert exists==criterion,(n,f)
        regular+=exists
    return regular

def prob_float(n):
    a=[0.0]*(n+1);a[0]=1.0
    for t in range(n):
        b=[0.0]*(n+1)
        for d in range(t+1):
            b[d]+=a[d]*d/n
            b[d+1]+=a[d]*(n-d)/n
        a=b
    N=n*(n-1)//2
    weights=[a[d]*(1-(n-d)/(n*n))**N for d in range(n+1)]
    total=sum(weights)
    expectation=sum(d*w for d,w in enumerate(weights))/(n*total)
    variance=sum((d-n*expectation)**2*w for d,w in enumerate(weights))/(n*total)
    return total,expectation,variance

def constants():
    a=.5;b=1.
    for _ in range(80):
        l=(a+b)/2
        if (l-1)*math.exp(l)+1>math.exp(-.5): b=l
        else: a=l
    l=(a+b)/2
    x=-math.expm1(-l)/l
    H=-x*math.log(x)-(1-x)*math.log1p(-x)
    h=H-1+x*math.log(math.expm1(l))-math.log(l)
    I=(1-x)/2-h
    v=(1/x)*(1+l-1/x)
    dx=((l+1)*math.exp(-l)-1)/(l*l)
    F2=-1/(x*(1-x))+(math.exp(l)/math.expm1(l))/dx
    C=math.exp((1-x*x)/4)/(x*math.sqrt((1-x)*v)*math.sqrt(-F2))
    return l,x,I,C,-1/F2

if __name__=='__main__':
    for n in (1,2,3):
        c,by=brute_count(n)
        formula=exact_count_formula(n)
        assert c==formula,(n,c,formula)
        print('exhaustive',n,'total',n**(n*n),'regular',c,'diagonal image histogram',by)
    assert direct_semigroup_regular_count(2)==14
    print('exhaustive direct monoid inner-inverse check n=2: 14 of 16')
    l,x,I,C,var=constants()
    assert .8281<l<.8282 and .6800<x<.6801 and .1718<I<.1720 and 1.25<C<1.27
    print('constants',l,x,I,C,var)
    for n in (10,20,40,80,160,320,640):
        P,mean,condvar=prob_float(n)
        rat=P/(C*math.exp(-I*n))
        print('n',n,'prob',P,'conditional_fraction',mean,'conditional_variance_over_n',condvar,'asympt_ratio',rat)
        if n>=160:
            assert abs(mean-x)<.015
            assert abs(rat-1)<.15
            assert abs(condvar-var)<.02
    print('VERIFY_OK')
