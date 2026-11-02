#!/usr/bin/env python3
"""A self-contained integer interval certificate for a parking-gap inequality.
Every interval endpoint represents a fixed-point rational with denominator 10**38.
All operations round outwards; Taylor remainders are bounded by alternation.
"""
S = 10**38

def c(n,d=1):
    assert (n*S)%d==0
    q=n*S//d
    return q,q

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def div(a,d):
    assert d>0
    return a[0]//d,-((-a[1])//d)
def times(a,n):
    if n>=0:return (a[0]*n,a[1]*n)
    return (-a[1]*(-n),-a[0]*(-n))
def mul(a,b):
    products=[v*w for v in a for w in b]
    return min(products)//S,-((-max(products))//S)

def j_bounds(x):
    if x==(0,0):return c(0)
    term=x
    total=term
    lower=None
    for j in range(2,82):
        term=div(times(mul(term,x),-(j-1)),j*j)
        total=add(total,term)
        if j==80:lower=total[0]
    return lower,total[1]

def exp_bounds(y):
    term=c(1);total=term
    upper=None
    for j in range(1,102):
        term=div(neg(mul(term,y)),j)
        total=add(total,term)
        if j==100: upper=total[1]
    return total[0],upper

def cert():
    ds=[]
    for i in range(751):
        x=c(i,50)
        jlo,jhi=j_bounds(x)
        # Logarithm exponent y = x + 2J(x).
        y=(x[0]+2*jlo,x[1]+2*jhi)
        assert 0<=y[0]<=y[1]<=23*S
        # The exponential is decreasing in y.  The direct interval-Taylor
        # evaluation is also valid (all polynomial operations enclose values).
        d=exp_bounds(y)
        assert 0<d[0]<=d[1]<=S,(i,d)
        ds.append(d)
    pos=0;neg_sum=0
    for i in range(750):
        # Step is 1/50.  Rectangle bounds use monotonicity of exp(-x-2J(x)).
        if i<50:
            pos += i*(49-i)*ds[i+1][0] // (50**3)
        else:
            neg_sum += ((i+1)*(i-49)*ds[i][1]+50**3-1) // (50**3)
    # Integral beyond 15 is at most 241 exp(-15).
    tail=241*exp_bounds(c(15))[1]
    lower=pos-neg_sum-tail
    assert lower> S//1000,(lower/S)
    print('CERTIFICATE_OK', 'strict_integral_lower_bound',f'{lower/S:.9f}', 'grid_cells',750)

if __name__=='__main__':cert()
