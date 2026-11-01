#!/usr/bin/env python3
"""Finite checks for the crown-graph minimal edge-domination enumerator.

Pure standard-library verification. Finite checks supplement the mathematical
proof; they do not certify its all-parameter assertions.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, factorial


def derangement(n):
    return sum((-1)**j * comb(n,j)*factorial(n-j) for j in range(n+1))


def a_term(n):
    return sum(comb(n,s) * sum((-1)**(s-j)*comb(s,j) *
               (j-1)**j * j**(n-j) for j in range(s+1))
               for s in range(2,n-1))


def b_term(n):
    if n < 4:
        return 0
    return n*(n-1)*comb(n-2,2) * sum(
        (-1)**j*comb(n-4,j)*factorial(n-2-j)
        for j in range(n-3))


def plus(a,b,scale=1):
    out=dict(a)
    for key,v in b.items():
        out[key]=out.get(key,0)+scale*v
    return {key:v for key,v in out.items() if v}


def multiply(a,b,t):
    out=defaultdict(Fraction)
    for (i,j,k),av in a.items():
        for (p,q,r),bv in b.items():
            if i+p<=t and j+q<=t:
                out[(i+p,j+q,k+r)]+=av*bv
    return {key:v for key,v in out.items() if v}


def power(p,k,t):
    out={(0,0,0):Fraction(1)}
    for _ in range(k):
        out=multiply(out,p,t)
    return out


def exponential_star_components(t):
    # exp[zxy+x(exp(zy)-1-zy)+y(exp(zx)-1-zx)]
    w={(1,1,1):Fraction(1)}
    for r in range(2,t+1):
        w[(1,r,r)]=Fraction(1,factorial(r))
        w[(r,1,r)]=Fraction(1,factorial(r))
    out={(0,0,0):Fraction(1)}
    p={(0,0,0):Fraction(1)}
    for k in range(1,2*t+1):
        p=multiply(p,w,t)
        if not p:
            break
        out=plus(out,{key:v/factorial(k) for key,v in p.items()})
    return out


def star_forest_crown(t):
    E=exponential_star_components(t)
    out=Counter()
    for j in range(t+1):
        r=t-j
        # z(exp(zx)+exp(zy)-1), the component containing one forced edge.
        forced={(0,0,1):Fraction(1)}
        for k in range(1,r+1):
            forced[(k,0,k+1)]=Fraction(1,factorial(k))
            forced[(0,k,k+1)]=Fraction(1,factorial(k))
        product=multiply(E,power(forced,j,r),r)
        for (p,q,k),v in product.items():
            if (p,q)==(r,r):
                integer=v*factorial(r)**2
                assert integer.denominator==1
                out[k]+=(-1)**j * comb(t,j) * int(integer)
    assert all(v>=0 for v in out.values())
    return +out


def formula(n):
    out=Counter({n:derangement(n)+2*(a_term(n)+b_term(n))})
    for degree,count in star_forest_crown(n-1).items():
        out[degree]+=n*count
    return +out


def direct_crown(n,also_check_classification=True):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    m=len(edges)
    adj=[]
    for i,j in edges:
        adj.append(sum(1<<k for k,(p,q) in enumerate(edges)
                       if p==i or q==j))
    all_edges=(1<<m)-1
    covered=[0]*(1<<m)
    out=Counter()
    class_counts=Counter()
    for mask in range(1,1<<m):
        low=mask & -mask
        covered[mask]=covered[mask^low] | adj[low.bit_length()-1]
        is_min=False
        if covered[mask]==all_edges:
            temp=mask
            is_min=True
            while temp:
                low=temp & -temp
                if covered[mask^low]==all_edges:
                    is_min=False
                    break
                temp^=low
        if also_check_classification:
            da=[0]*n; db=[0]*n
            for k,(i,j) in enumerate(edges):
                if (mask>>k)&1:
                    da[i]+=1;db[j]+=1
            ua={i for i,d in enumerate(da) if not d}
            ub={j for j,d in enumerate(db) if not d}
            classification=False
            if not ua and not ub:
                classification=all(da[i]==db[j]==1 for k,(i,j) in enumerate(edges) if (mask>>k)&1)
                kind='perfect matching'
            elif not ua and ub:
                # One edge per occupied row; for a unique missing b_j,
                # the row j must be a singleton preimage under the map.
                classification=(all(d==1 for d in da) and
                    (len(ub)>=2 or (len(ub)==1 and
                     db[next(iter(ub))]==0 and
                     sum(db[j]==1 for k,(i,j) in enumerate(edges)
                         if (mask>>k)&1 and i==next(iter(ub)))==1)))
                kind='row-function'
            elif not ub and ua:
                classification=(all(d==1 for d in db) and
                    (len(ua)>=2 or (len(ua)==1 and
                     sum(da[i]==1 for k,(i,j) in enumerate(edges)
                         if (mask>>k)&1 and j==next(iter(ua)))==1)))
                kind='column-function'
            elif ua==ub and len(ua)==1:
                classification=all(da[i]==1 or db[j]==1 for k,(i,j) in enumerate(edges) if (mask>>k)&1)
                kind='paired-hole star forest'
            else:
                kind='no admissible class'
            assert classification==is_min,(n,mask,classification,is_min,kind)
        if is_min:
            out[mask.bit_count()]+=1
            if also_check_classification:
                class_counts[kind]+=1
    return +out,class_counts


def directly_count_star_forests(t):
    ed=[(i,j) for i in range(t) for j in range(t) if i!=j]
    out=Counter()
    for mask in range(1<<len(ed)):
        da=[0]*t;db=[0]*t
        for k,(i,j) in enumerate(ed):
            if mask>>k&1:
                da[i]+=1;db[j]+=1
        if not da or min(da+db)==0:
            continue
        if all(da[i]==1 or db[j]==1 for k,(i,j) in enumerate(ed) if mask>>k&1):
            out[mask.bit_count()]+=1
    return +out


def main():
    totals=0
    for n in range(2,6):
        actual,kinds=direct_crown(n)
        predicted=formula(n)
        assert actual==predicted,(n,actual,predicted)
        print('n=',n,'minimal-edge counts=',dict(sorted(actual.items())),
              'classes=',dict(kinds))
        totals+=1<< (n*(n-1))
    for t in range(1,5):
        assert star_forest_crown(t)==directly_count_star_forests(t)
    for t in range(3,9):
        p=star_forest_crown(t)
        assert p[t]==derangement(t)
        assert p[2*t-2]==t
        assert all(t<=k<=2*t-2 for k in p)
    assert formula(6)==Counter({5:264,6:31405,7:1200,8:30})
    print('EXHAUSTIVE_MASKS=',totals)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
