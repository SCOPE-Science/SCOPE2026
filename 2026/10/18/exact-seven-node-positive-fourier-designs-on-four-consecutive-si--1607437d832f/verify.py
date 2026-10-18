"""Exact rational-interval certificate for prime-eleven positive Fourier cubature.
Python 3 standard library; no floating-point arithmetic is used.
Every trigonometric entry is enclosed using Machin's arctangent identity,
Taylor remainder bounds, and outward-rounded integer intervals.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
from collections import Counter

Q = 10 ** 44

def lower(x):
    return x.numerator * Q // x.denominator

def upper(x):
    return -(-x.numerator * Q // x.denominator)

def exact(x):
    x = Fraction(x)
    return (lower(x), upper(x))

def add(a,b): return a[0]+b[0], a[1]+b[1]
def neg(a): return -a[1], -a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    z=[a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]]
    return min(z)//Q,-(-max(z)//Q)
def inv(a):
    assert a[0]*a[1]>0, ('division interval contains zero',a)
    x,y=Fraction(Q*Q,a[0]),Fraction(Q*Q,a[1])
    return min(x.numerator//x.denominator,y.numerator//y.denominator),max(-(-x.numerator//x.denominator),-(-y.numerator//y.denominator))
def div(a,b):return mul(a,inv(b))

def atan_bounds(den, count=68):
    term=Fraction(1,den); acc=Fraction(0)
    # 68 terms (last negative) and 67 terms (last positive) bracket atan.
    vals=[]
    for k in range(count):
        acc+=(-1 if k%2 else 1)*Fraction(1,(2*k+1)*den**(2*k+1))
        if k in (count-2,count-1): vals.append(acc)
    return min(vals),max(vals)

b5=atan_bounds(5);b239=atan_bounds(239)
PI=(lower(16*b5[0]-4*b239[1]),upper(16*b5[1]-4*b239[0]))
assert 3*Q < PI[0] < PI[1] < 4*Q

def trig(j):
    # return rigorous cosine and sine intervals for 2*pi*j/11
    if j<0:
        c,s=trig(-j)
        return c,neg(s)
    x=div(mul(exact(2*j),PI),exact(11))
    x2=mul(x,x)
    st=exact(0);ct=exact(0)
    ts=x;tc=exact(1)
    K=31
    for k in range(K):
        st=add(st,ts);ct=add(ct,tc)
        ts=div(neg(mul(ts,x2)),exact((2*k+2)*(2*k+3)))
        tc=div(neg(mul(tc,x2)),exact((2*k+1)*(2*k+2)))
    # Uniform Lagrange-Taylor bound valid because |x|<4 and derivatives <=1.
    err=Fraction(4**(2*K-1),factorial(2*K-1))
    radius=upper(err)
    return add(ct,(-radius,radius)),add(st,(-radius,radius))

TR={j:trig(j) for j in range(-5,6)}

def mat_value(h,t):
    k=(h*t)%11
    if k>5:k-=11
    return TR[k]

def moments(support, include_constant):
    m=[]
    if include_constant:m.append([exact(1) for _ in support])
    for k in range(1,4):
        m.append([mat_value(k,t)[0] for t in support])
        m.append([mat_value(k,t)[1] for t in support])
    return m

def eliminate(a, rhs=None):
    n=len(a)
    a=[[tuple(v) for v in row] for row in a]
    if rhs is not None: a=[row+[tuple(rhs[i])] for i,row in enumerate(a)]
    det=exact(1)
    for i in range(n):
        k=max(range(i,n),key=lambda j: abs(a[j][i][0]+a[j][i][1]))
        if k!=i:
            a[k],a[i]=a[i],a[k]
            det=neg(det)
        piv=a[i][i]
        assert piv[0]*piv[1]>0,('uncertified pivot',i,piv)
        det=mul(det,piv)
        for j in range(i+1,n):
            fac=div(a[j][i],piv)
            for l in range(i+1,len(a[j])):
                a[j][l]=sub(a[j][l],mul(fac,a[i][l]))
            a[j][i]=exact(0)
    if rhs is None: return det
    x=[None]*n
    for i in range(n-1,-1,-1):
        val=a[i][-1]
        for j in range(i+1,n):val=sub(val,mul(a[i][j],x[j]))
        x[i]=div(val,a[i][i])
    return x


def translate_key(s):
    return min(tuple(sorted((t+a)%11 for t in s)) for a in range(11))

if __name__=='__main__':
    min_lower_det=None
    for s in combinations(range(11),6):
        det=eliminate(moments(s,False))
        assert det[0]>0 or det[1]<0,('uncertified nonsingularity',s,det)
        mag=min(abs(det[0]),abs(det[1]))
        min_lower_det=mag if min_lower_det is None else min(min_lower_det,mag)
    count=0
    patterns=Counter()
    min_positive=None;max_negative=None
    for s in combinations(range(11),7):
        w=eliminate(moments(s,True),[exact(1)]+[exact(0)]*6)
        if all(v[0]>0 for v in w):
            count+=1;patterns[translate_key(s)]+=1
            mm=min(v[0] for v in w)
            min_positive=mm if min_positive is None else min(min_positive,mm)
        else:
            assert any(v[1]<0 for v in w),('uncertified sign',s,w)
            v=min(v[1] for v in w)
            max_negative=v if max_negative is None else max(max_negative,v)
    wanted={
        (0,1,2,3,5,7,9):11,
        (0,1,2,4,6,7,9):11,
        (0,1,3,4,6,7,9):11,
    }
    assert count==33 and dict(patterns)==wanted
    print('pi_certified_interval_scaled',PI)
    print('six_site_moment_min_abs_determinant_lower_bound',float(Fraction(min_lower_det,Q)))
    print('six_site_sets_certified',462)
    print('seven_site_sets_certified',330)
    print('positive_seven_site_sets',count)
    print('positive_translation_orbits',sorted(patterns.items()))
    print('least_positive_weight_lower_bound',float(Fraction(min_positive,Q)))
    print('largest_negative_witness_upper_bound',float(Fraction(max_negative,Q)))
    print('CERTIFICATE_PASS')
