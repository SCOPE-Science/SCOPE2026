"""Exact full-state meeting-time checks and independent hazard-shape spot checks.
Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from math import exp


def gauss(matrix, rhs):
    n = len(rhs)
    aug = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = next((j for j in range(i, n) if aug[j][i]), None)
        if pivot is None:
            raise AssertionError('singular resolvent')
        aug[i], aug[pivot] = aug[pivot], aug[i]
        row_scale = aug[i][i]
        aug[i] = [v / row_scale for v in aug[i]]
        for j in range(n):
            if j != i and aug[j][i]:
                fac = aug[j][i]
                aug[j] = [aug[j][k] - fac * aug[i][k] for k in range(n+1)]
    return [row[-1] for row in aug]


def full_graph_transforms(m, n, a, b, s):
    size = m+n
    states = [(i, j) for i in range(size) for j in range(size) if i != j]
    index = {q: k for k, q in enumerate(states)}
    mat = [[F(0) for _ in states] for _ in states]
    rhs = [F(0) for _ in states]
    def neighbors(v):
        return range(m, size) if v < m else range(m)
    def rate(v):
        return a if v < m else b
    for z, (i, j) in enumerate(states):
        mat[z][z] = s + rate(i) + rate(j)
        for v, fixed, which in [(i, j, 0), (j, i, 1)]:
            for new in neighbors(v):
                r = rate(v)/len(neighbors(v))
                if new == fixed:
                    rhs[z] += r
                else:
                    q = (new, fixed) if which == 0 else (fixed, new)
                    mat[z][index[q]] -= r
    return dict(zip(states, gauss(mat, rhs)))


def reduced_transform(m, n, a, b, s, typ):
    p = b*F(m-1,m)
    q = a*F(n-1,n)
    h = b/F(m)+a/F(n)
    u = a+b
    denominator = ((s+u)*(s+2*a)*(s+2*b)
                   - 2*a*p*(s+2*b)-2*b*q*(s+2*a))
    numerator = {'A': 2*a*h*(s+2*b),
                 'B': 2*b*h*(s+2*a),
                 'D': h*(s+2*a)*(s+2*b)}[typ]
    return numerator/denominator


def exact_checks():
    checks = 0
    for m,n,a,b in [(2,2,F(1),F(2)),(2,3,F(2),F(1)),
                    (3,2,F(1),F(3)),(3,3,F(1),F(1)),
                    (2,4,F(3,2),F(2,3)),(4,2,F(2,3),F(5,2))]:
        for s in [F(0),F(1,2),F(2)]:
            vals = full_graph_transforms(m,n,a,b,s)
            for (i,j),v in vals.items():
                typ = ('A' if i<m and j<m else
                       'B' if i>=m and j>=m else 'D')
                want = reduced_transform(m,n,a,b,s,typ)
                assert v == want,(m,n,a,b,s,i,j,v,want)
                checks += 1
    return checks


def eig_roots(m,n,a,b):
    a,b = float(a),float(b)
    u = a+b
    p = b*(m-1)/m
    q = a*(n-1)/n
    assert a != b
    l,r = 2*min(a,b),2*max(a,b)
    def f(t):
        return u-t-2*a*p/(2*a-t)-2*b*q/(2*b-t)
    def bisect(left,right):
        vl=f(left)
        for _ in range(100):
            mid=(left+right)/2
            if mid==left or mid==right:break
            if (f(mid)>0)==(vl>0):left=mid
            else:right=mid
        return (left+right)/2
    eps = 1e-9*min(a,b)
    return [bisect(0,l-eps),bisect(l+eps,r-eps),
            bisect(r+eps,4*u)]


def coefficients(m,n,a,b,typ):
    u=a+b; p=b*(m-1)/m;q=a*(n-1)/n
    h=b/m+a/n
    vals=eig_roots(m,n,a,b)
    c=[]
    for lam in vals:
        s=-lam
        deriv=(s+2*a)*(s+2*b)+(s+u)*(2*s+2*a+2*b)-2*a*p-2*b*q
        num={'A': 2*a*h*(s+2*b),'B':2*b*h*(s+2*a),
             'D':h*(s+2*a)*(s+2*b)}[typ]
        c.append(num/(lam*deriv))
    assert abs(sum(c)-1)<1e-8,(m,n,a,b,typ,c)
    return vals,c


def hazard_slope(rates,cs,t):
    weights=[cs[i]*exp(-(rates[i]-rates[0])*t) for i in range(3)]
    den=sum(weights)
    h=sum(weights[i]*rates[i] for i in range(3))/den
    der=-sum(cs[i]*cs[j]*(rates[i]-rates[j])**2 *
             exp(-((rates[i]+rates[j])-2*rates[0])*t)
             for i in range(3) for j in range(i+1,3))/(den*den)
    return h,der


def shape_checks():
    count=0
    for m,n,a,b in [(2,2,2.,1.),(3,5,5.,.5),(5,2,.4,3.),
                    (3,4,1.,2.),(4,3,3.,1.),(2,6,1.,4.)]:
        for typ in ('A','B','D'):
            rates,cs=coefficients(m,n,a,b,typ)
            if typ=='D':
                assert all(x>0 for x in cs)
            else:
                assert cs[0]>0 and cs[2]<0
                if (a>b if typ=='A' else b>a):assert cs[1]>0
                else:assert cs[1]<0
            ts=[(i/100)*20/rates[0] for i in range(101)]
            slopes=[hazard_slope(rates,cs,t)[1] for t in ts]
            if typ=='D':assert all(x<1e-7 for x in slopes)
            elif (a>b if typ=='A' else b>a):
                assert slopes[0]>0 and slopes[-1]<1e-7
                assert sum(slopes[i]>0 and slopes[i+1]<0 for i in range(100))==1
            else:
                assert all(x>-1e-7 for x in slopes)
            count+=1
    return count

if __name__=='__main__':
    x=exact_checks();y=shape_checks()
    print('PASS: %d full-state exact-rational Laplace identities; %d spectral hazard classifications' %(x,y))
