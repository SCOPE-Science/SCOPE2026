#!/usr/bin/env python3
"""Independent exact checks for cyclic sequential Rule-60 dynamics.
Only finite corroboration: see analytical argument for all lengths and times.
"""
from itertools import permutations
from math import gcd
from random import Random


def update(x, schedule, n):
    for i in schedule:
        x ^= ((x >> ((i-1) % n)) & 1) << i
    return x


def matrix_columns(schedule, n):
    return [update(1 << i, schedule, n) for i in range(n)]


def apply(cols, x):
    y = 0
    while x:
        bit = x & -x
        y ^= cols[bit.bit_length()-1]
        x -= bit
    return y


def rank(vs, n):
    basis = [0]*n
    count = 0
    for x in vs:
        while x:
            j = x.bit_length()-1
            if basis[j]: x ^= basis[j]
            else:
                basis[j] = x
                count += 1
                break
    return count


def poly_mul(a,b):
    ans=0
    while b:
        if b&1: ans^=a
        a <<= 1
        b >>= 1
    return ans


def polynomial_gcd(a,b):
    while b:
        r=a
        while r and r.bit_length()>=b.bit_length():
            r ^= b<<(r.bit_length()-b.bit_length())
        a,b=b,r
    return a


def charpoly(cols,n):
    # determinant over F2[t], using row/column permutation expansion DP
    dp={0:1}
    for i in range(n):
        new={}
        for mask,coef in dp.items():
            for j in range(n):
                if mask>>j&1: continue
                element=((cols[j]>>i)&1) | ((2) if i==j else 0)
                if element:
                    newmask=mask|(1<<j)
                    new[newmask]=new.get(newmask,0)^poly_mul(coef,element)
        dp=new
    return dp[(1<<n)-1]


def predicted_polynomial(n,a):
    # (t+1)^n + t^a via F2 polynomial multiplication
    x=1
    for _ in range(n): x=poly_mul(x,3)
    return x^(1<<a)


def period_census(cols,n):
    seen=set(); primitive={}
    for start in range(1<<n):
        if start in seen:continue
        path=[];x=start
        while x not in seen:
            seen.add(x);path.append(x);x=apply(cols,x)
        assert x==start  # invertible map
        primitive[len(path)]=primitive.get(len(path),0)+1
    return primitive


def run():
    rng=Random(20261020)
    charchecks=fixedchecks=orbitchecks=cyclicchecks=0
    for n in range(3,10):
        if n<=7: schedules=list(permutations(range(n)))
        else:
            schedules=[]
            for j in range(240):
                arr=list(range(n));rng.shuffle(arr);schedules.append(tuple(arr))
        profiles={}
        for p in schedules:
            a=sum(p.index((i-1)%n)<p.index(i) for i in range(n))
            assert 1<=a<=n-1
            cols=matrix_columns(p,n)
            predicted=predicted_polynomial(n,a)
            actual=charpoly(cols,n)
            assert actual==predicted,(n,p,a,bin(actual),bin(predicted))
            charchecks+=1
            profiles.setdefault(a,predicted)
            assert profiles[a]==predicted
            # At least one coordinate is cyclic, proved in unrestricted mathematics.
            if n<=7 or (charchecks%7==0):
                good=False
                for i in range(n):
                    v=1<<i; powers=[]
                    for k in range(n):
                        powers.append(v);v=apply(cols,v)
                    if rank(powers,n)==n:good=True;break
                assert good,(n,p,a)
                cyclicchecks+=1
            if n<=7 or charchecks%8==0:
                for m in (1,2,3,4,5,6,7,8,9,12):
                    fm=[]
                    for i in range(n):
                        x=1<<i
                        for _ in range(m):x=apply(cols,x)
                        fm.append(x^(1<<i))
                    actual_fixed=1<<(n-rank(fm,n))
                    expected_fixed=1<<(polynomial_gcd(predicted,(1<<m)|1).bit_length()-1)
                    assert actual_fixed==expected_fixed,(n,p,m,actual_fixed,expected_fixed)
                    fixedchecks+=1
            if n<=6 and (p[0]==0 or (a in (1,n-1) and p[0]==1)):
                orbits=period_census(cols,n)
                for d,count in orbits.items():
                    assert sum(q*c for q,c in orbits.items() if d%q==0)==sum(1 for x in range(1<<n) if apply_power(cols,x,d)==x)
                orbitchecks+=1
        if n <= 7:
            assert set(profiles)==set(range(1,n)),(n,set(profiles))
        assert len(set(profiles.values()))==len(profiles)
    print('VERIFY_OK', 'characteristic_polynomials',charchecks,'fixed_point_checks',fixedchecks,'cyclic_vectors',cyclicchecks,'orbit_censuses',orbitchecks)


def apply_power(cols,x,m):
    for _ in range(m):x=apply(cols,x)
    return x


if __name__=='__main__':run()
