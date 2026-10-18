"""Independent finite verification of two-block partition orbit formulas.
Usage: python3 verify_orbit_formula.py. Python 3 standard library only.
"""
from collections import Counter
from math import factorial,comb


def bell(n):
    b=[1]
    for m in range(1,n+1): b.append(sum(comb(m-1,j)*b[j] for j in range(m)))
    return b[n]


def orbit_coefficient(a,b):
    coeff=[[0]*(b+1) for _ in range(a+1)];coeff[0][0]=1
    for u in range(a+1):
        for v in range(b+1):
            if not (u or v):continue
            for i in range(u,a+1):
                for j in range(v,b+1):
                    coeff[i][j]+=coeff[i-u][j-v]
    return coeff[a][b]


def partitions(n):
    def rec(vals,k):
        if len(vals)==n:
            buckets=[0]*(k+1)
            for idx,v in enumerate(vals):buckets[v]|=1<<idx
            yield tuple(buckets)
        else:
            for c in range(k+2):
                yield from rec(vals+[c],max(c,k))
    yield from rec([0],0)


def profiles(a,b):
    mask=(1<<a)-1
    counts=Counter()
    for blocks in partitions(a+b):
        p=tuple(sorted(((block&mask).bit_count(),(block&~mask).bit_count()) for block in blocks))
        counts[p]+=1
    return counts


def class_size(a,b,prof):
    mult=Counter(prof)
    den=1
    for (u,v),m in mult.items():den*=factorial(u)**m*factorial(v)**m*factorial(m)
    assert (factorial(a)*factorial(b))%den==0
    return (factorial(a)*factorial(b))//den


def moments(prof,a,b):
    return tuple(sum(comb(u,i)*comb(v,j) for u,v in prof)
                 for i in range(a+1) for j in range(b+1) if i+j>=2)


def main():
    cases=0;total=0
    for n in range(3,9):
        for a in range(n//2+1,n):
            b=n-a
            if a<=b:continue
            # n=8 is feasible here: just 4140 direct partitions.
            profs=profiles(a,b)
            assert orbit_coefficient(a,b)==len(profs),(a,b,'coefficient')
            assert sum(profs.values())==bell(n),(a,b,'total')
            assert all(class_size(a,b,key)==count for key,count in profs.items()),(a,b,'class size')
            signatures={}
            for key in profs:
                sig=(len(key),moments(key,a,b))
                assert sig not in signatures or signatures[sig]==key,(a,b,'binomial moment collision')
                signatures[sig]=key
            print(f'a={a}, b={b}, orbit_classes={len(profs)}, weight_total={sum(profs.values())}')
            cases+=1;total+=sum(profs.values())
    for a,b in [(6,4),(7,3),(8,2),(9,1),(7,4)]:
        print(f'coefficient({a},{b})={orbit_coefficient(a,b)}')
    print('VERIFY_ORBIT_FORMULA_OK',cases,total)


if __name__=='__main__': main()
