"""Exact independent verification of four-coordinate Walsh-sketch rank laws.

Uses Python standard library only. All probabilities are computed as Fractions.
The finite checks are corroboration; the all-size theorem follows from the
character and inclusion-exclusion proof in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def sign_row(t, columns):
    return tuple(1 if ((t & col).bit_count() & 1) == 0 else -1 for col in columns)


def projective(t, columns):
    r = sign_row(t, columns)
    return tuple(x*r[0] for x in r)


def exact_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    rk = 0
    for j in range(len(a[0])):
        piv = next((i for i in range(rk, len(a)) if a[i][j]), None)
        if piv is None:
            continue
        a[piv], a[rk] = a[rk], a[piv]
        pv = a[rk][j]
        for i in range(rk+1,len(a)):
            if a[i][j]:
                t = a[i][j]/pv
                for h in range(j,len(a[0])):
                    a[i][h] -= t*a[rk][h]
        rk += 1
        if rk == len(a):
            break
    return rk


def closed(m, dependent, N=None):
    if m < 1:
        raise ValueError('requires positive sketch size')
    if N is None:
        if dependent:
            return 4*Fraction(3,4)**m-6*Fraction(1,2)**m+4*Fraction(1,4)**m
        return (12*Fraction(1,2)**m + 8*Fraction(3,8)**m
                -68*Fraction(1,4)**m+72*Fraction(1,8)**m)
    def c(num):
        return comb(num,m) if 0 <= m <= num else 0
    if dependent:
        numerator = 4*c(3*N//4)-6*c(N//2)+4*c(N//4)
    else:
        numerator = (12*c(N//2)+8*c(3*N//8)
                     -68*c(N//4)+72*c(N//8))
    return Fraction(numerator,comb(N,m))


def check_all_column_quads(d):
    N=1<<d
    seen = {True:0,False:0}
    for cols in combinations(range(N),4):
        dep=(cols[0]^cols[1]^cols[2]^cols[3])==0
        patterns={projective(t,cols) for t in range(N)}
        assert len(patterns)==(4 if dep else 8)
        assert all(sum(projective(t,cols)==pat for t in range(N))==N//len(patterns)
                   for pat in patterns)
        seen[dep]+=1
    assert sum(seen.values())==comb(N,4)
    print('all column supports in N=',N,':',seen)
    return seen


def check_iid(N, cols):
    pats=tuple(sorted({projective(t,cols) for t in range(N)}))
    dep=cols[0]^cols[1]^cols[2]^cols[3]==0
    r=[exact_rank([pats[j] for j in range(len(pats)) if mask>>j&1])
       for mask in range(1<<len(pats))]
    dp=[0]*(1<<len(pats));dp[0]=1
    for m in range(1,29):
        new=[0]*len(dp)
        for mask, v in enumerate(dp):
            if v:
                for j in range(len(pats)):
                    new[mask |(1<<j)]+=v
        dp=new
        bad=sum(v for mask,v in enumerate(dp) if r[mask]<4)
        got=Fraction(bad,len(pats)**m)
        want=closed(m,dep)
        assert got==want,(m,dep,got,want)
    print('iid sketch exact 28 lengths checked; dependent:',dep)


def check_without_replacement(N, cols):
    dep=cols[0]^cols[1]^cols[2]^cols[3]==0
    pats=tuple(sorted({projective(t,cols) for t in range(N)}))
    ids=[pats.index(projective(t,cols)) for t in range(N)]
    ranks=[exact_rank([pats[j] for j in range(len(pats)) if mask>>j&1])
           for mask in range(1<<len(pats))]
    bad_by_size=[0]*(N+1)
    # Exactly enumerates every row subset, including every size.
    pms=[0]*(1<<N)
    for mask in range(1,1<<N):
        low=mask & -mask
        i=low.bit_length()-1
        pms[mask]=pms[mask ^ low] | (1<<ids[i])
        if ranks[pms[mask]]<4:
            bad_by_size[mask.bit_count()]+=1
    for m in range(1,N+1):
        got=Fraction(bad_by_size[m],comb(N,m))
        want=closed(m,dep,N)
        assert got==want,(N,m,dep,got,want)
    print('without replacement all row subsets checked; N=',N,'dependent:',dep,
          'rank failure at m=4:',closed(4,dep,N),
          'last failing m=',max((m for m in range(1,N+1) if bad_by_size[m]),default=0))


def check_cube_coplanarity():
    pats=[(1,x,y,z) for x in (-1,1) for y in (-1,1) for z in (-1,1)]
    bad=[I for I in combinations(range(8),4) if exact_rank([pats[i] for i in I])<4]
    assert len(bad)==12
    assert all(exact_rank([pats[i] for i in I])==4 for I in combinations(range(8),5))
    print('four-vertex cube coplanar subsets:',len(bad),
          'all five-vertex sets full-rank')


def main():
    check_all_column_quads(3)
    check_all_column_quads(4)
    check_cube_coplanarity()
    for N in (8,16):
        for cols in ((0,1,2,3),(0,1,2,4)):
            check_iid(N,cols)
            check_without_replacement(N,cols)
    assert closed(4,True)==Fraction(29,32)
    assert closed(4,False)==Fraction(169,256)
    assert closed(4,True,8)==Fraction(27,35)
    assert closed(4,False,8)==Fraction(6,35)
    for m in range(4,300):
        assert closed(m,True)>closed(m,False)
    print('all exact checks passed: 2 sampling models; 2 affine classes')


if __name__=='__main__':
    main()
