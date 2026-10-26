#!/usr/bin/env python3
"""Exact-rational cross-checks of affine finite-element projection formulae.
Requires only Python's standard library. Run: python check_exact.py
"""
from fractions import Fraction as Q
from math import comb

def inverse(matrix):
    n=len(matrix)
    a=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j])
        a[j],a[k]=a[k],a[j]
        z=a[j][j]
        a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j]
                a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]

def gram(d,q):
    n=d+2
    a=[[Q(0) for _ in range(n)] for _ in range(n)]
    for mass,ids in [(q,tuple(range(d))+(d,)),(1-q,tuple(range(d))+(d+1,))]:
        for i in ids:
            for j in ids:
                a[i][j]+=mass*Q(1+int(i==j),(d+1)*(d+2))
    return a

def beta_abs_direct(d,c,b):
    """Integrates |c*u-b| against density d(1-u)^(d-1), via polynomial expansion."""
    assert c>b>0
    h=b/c
    neg=Q(0)
    for k in range(d):
        neg+=Q(d*((-1)**k)*comb(d-1,k))*(b*h**(k+1)/Q(k+1)-c*h**(k+2)/Q(k+2))
    return c/Q(d+1)-b+2*neg

def row_norm(d,q,inv,i):
    ans=Q(0)
    for mass,ids in [(q,tuple(range(d))+(d,)),(1-q,tuple(range(d))+(d+1,))]:
        vals=[inv[i][j] for j in ids]
        low=min(vals)
        high=max(vals)
        assert vals.count(high)==1 and vals.count(low)==d, (d,q,i,vals)
        ans+=mass*beta_abs_direct(d,high-low,-low)
    return ans

def formula(d,q):
    b=Q(d,d+2)
    return -1+Q(d+2)*((1+q)*(1-Q(2)*q/Q(d+2)/(1+q))**(d+1)+(1-q)*b**(d+1))

def shared(d):
    return -1+Q(2*(d+2))*Q(d+1,d+2)**(d+1)

def predicted_row(d,q,i):
    n=d+2
    vals=[]
    for j in range(n):
        if i<d:
            # Shared vertex: on its own vertex (d+1)^2 and every other vertex -(d+1)
            vals.append(Q((d+1)**2) if i==j else Q(-(d+1)))
        elif i==d:
            if j<d: vals.append(Q(-(d+1)))
            elif j==d: vals.append(Q(-(d+1))+Q((d+1)*(d+2),2)*(1+1/q))
            else: vals.append(Q(-(d+1))+Q((d+1)*(d+2),2))
        else:
            if j<d: vals.append(Q(-(d+1)))
            elif j==d: vals.append(Q(-(d+1))+Q((d+1)*(d+2),2))
            else: vals.append(Q(-(d+1))+Q((d+1)*(d+2),2)*(1+1/(1-q)))
    return vals

def main():
    cases=[Q(1,2),Q(1,3),Q(2,3),Q(1,11),Q(7,13),Q(1,100)]
    verified=0
    for d in range(2,11):
        for q in cases:
            inv=inverse(gram(d,q))
            for i in range(d+2):
                assert inv[i]==predicted_row(d,q,i),(d,q,i,inv[i],predicted_row(d,q,i))
                actual=row_norm(d,q,inv,i)
                expected=shared(d) if i<d else formula(d,q if i==d else 1-q)
                assert actual==expected,(d,q,i,actual,expected)
                verified+=1
            exact=max(row_norm(d,q,inv,i) for i in range(d+2))
            assert exact==formula(d,min(q,1-q))
    assert formula(2,Q(1,2))==Q(49,18)
    assert formula(2,Q(0))==Q(7,2)
    assert shared(2)==Q(19,8)
    print(f'PASS: {verified} exact independent row-integral and Gram-inverse checks; '
          '54 exact whole-operator comparisons; planar 49/18, 7/2, 19/8 checked.')

if __name__=='__main__':
    main()
