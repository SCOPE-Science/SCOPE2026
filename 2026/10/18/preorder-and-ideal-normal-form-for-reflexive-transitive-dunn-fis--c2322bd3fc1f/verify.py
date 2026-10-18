"""Verify enumeration of reflexive/transitive FSD relations on rooted star forests.

The independent methods are direct relational tests, quotient-poset counting,
canonical row permutation, and a cycle-index enumeration.
Run with Python 3.10+ and no third-party packages.
"""
from itertools import product, permutations
from fractions import Fraction
from math import factorial


def le(a, b):
    return a == 0 or a == b


def transitive(rows):
    n = len(rows)
    return all((rows[i] & (1 << j)) == 0 or (rows[j] & ~rows[i]) == 0
               for i in range(n) for j in range(n))


def direct_fsd(rows):
    n = len(rows)
    R = {(i,j) for i in range(n) for j in range(n) if rows[i] >> j & 1}
    E = {(i,j) for i in range(n) for j in range(n) if le(i,j)}
    G = {(j,i) for i,j in E}
    def comp(A,B):
        return {(i,k) for (i,j) in A for (h,k) in B if j == h}
    return (comp(E,R) <= comp(R,E)
            and comp(R,G) <= comp(G,R)
            and comp(G,R) <= comp(R,G))


def canonical_triple(rows):
    m = len(rows)-1
    full = (1<<m)-1
    Q = tuple(rows[i+1] >> 1 for i in range(m))
    B = sum(1<<i for i in range(m) if rows[i+1] & 1)
    T = rows[0] >> 1
    if rows[0] & 1 == 0:
        return False
    if not all(Q[i] & (1<<i) for i in range(m)) or not transitive(Q):
        return False
    if T:
        if any(not(Q[i]&(1<<t)) for i in range(m) for t in range(m) if T>>t&1):
            return False
        if any(Q[t] & ~T for t in range(m) if T>>t&1):
            return False
    if any(Q[i]&B and not (B>>i&1) for i in range(m)):
        return False
    return all(rows[i+1] == ((Q[i]<<1) | (B>>i&1)) for i in range(m))


def all_reflexive_rows(n):
    pairs = [(i,j) for i in range(n) for j in range(n) if i != j]
    for b in range(1 << len(pairs)):
        rows = [1<<i for i in range(n)]
        for index,(i,j) in enumerate(pairs):
            if b >> index & 1: rows[i] |= 1<<j
        yield tuple(rows)


def permute_rows(rows,p):
    out=[0]*len(rows)
    for i in range(len(rows)):
        out[p[i]]=sum(1<<p[j] for j in range(len(rows)) if rows[i]>>j&1)
    return tuple(out)


def direct_check(m):
    good=[]
    for rows in all_reflexive_rows(m+1):
        if not transitive(rows):continue
        a=direct_fsd(rows)
        b=canonical_triple(rows)
        assert a == b, ('classification discrepancy',m,rows,a,b)
        if a:good.append(rows)
    perms=[(0,)+tuple(j+1 for j in p) for p in permutations(range(m))]
    fixed=[sum(permute_rows(rows,p)==rows for rows in good) for p in perms]
    assert sum(fixed)%factorial(m)==0
    return len(good),sum(fixed)//factorial(m)


def posets(k):
    pairs=[(i,j) for i in range(k) for j in range(i+1,k)]
    for choices in product(range(3),repeat=len(pairs)):
        rows=[1<<i for i in range(k)]
        for (i,j),t in zip(pairs,choices):
            if t==1:rows[i]|=1<<j
            if t==2:rows[j]|=1<<i
        if transitive(rows):yield tuple(rows)


def ideals(P):
    k=len(P)
    return tuple(B for B in range(1<<k) if all(not(P[i]&B) or (B>>i&1) for i in range(k)))


def stirling(n,k):
    arr=[[0]*(n+1) for _ in range(n+1)]
    arr[0][0]=1
    for a in range(1,n+1):
        for b in range(1,a+1):arr[a][b]=b*arr[a-1][b]+arr[a-1][b-1]
    return arr[n][k]


def labelled_via_posets(n):
    nums=[]
    for k in range(n+1):
        allP=list(posets(k))
        P=len(allP)
        A=sum(len(ideals(X)) for X in allP)
        nums.append((P,A))
    for k in range(1,n+1):
        B=k*(nums[k-1][0]+nums[k-1][1])
        assert B==sum(len(ideals(P)) for P in posets(k)
                      if any(all(P[j]&(1<<i) for j in range(k)) for i in range(k)))
    return [sum(stirling(m,k)*(nums[k][1]+k*(nums[k-1][1]+nums[k-1][0]))
                for k in range(1,m+1)) for m in range(1,n+1)]


def cycles(p):
    seen=set();lengths=[]
    for a in range(len(p)):
        if a in seen:continue
        j=a;size=0
        while j not in seen:
            seen.add(j);size+=1;j=p[j]
        lengths.append(size)
    return lengths


def weight_coeffs(cyclesizes,n):
    coeff=[0]*(n+1);coeff[0]=1
    for length in cyclesizes:
        nxt=[0]*(n+1)
        for a,c in enumerate(coeff):
            if c:
                for b in range(length,n-a+1,length):nxt[a+b]+=c
        coeff=nxt
    return coeff


def unlabelled_via_cycles(n):
    totals=[Fraction(0) for _ in range(n+1)]
    for k in range(n+1):
        pp=list(permutations(range(k)))
        canon={}
        for P in posets(k):
            rep=min(permute_rows(P,p) for p in pp)
            canon[rep]=1
        for P in canon:
            aut=[p for p in pp if permute_rows(P,p)==P]
            Js=ideals(P)
            hasgreat=any(all(P[j] & (1<<i) for j in range(k)) for i in range(k))
            for p in aut:
                Jfixed=sum(all(bool(B&(1<<i))==bool(B&(1<<p[i]))
                               for i in range(k)) for B in Js)
                coef=weight_coeffs(cycles(p),n)
                for m in range(n+1):
                    totals[m]+=Fraction((1+hasgreat)*Jfixed*coef[m],len(aut))
    assert all(x.denominator==1 for x in totals)
    return [int(x) for x in totals]


def main():
    expected_lab=[4,20,189,3084,81536]
    expected_iso=[4,13,50,232,1303]
    for m in range(1,5):
        actual=direct_check(m)
        assert actual==(expected_lab[m-1],expected_iso[m-1]),(m,actual)
        print('DIRECT',m,actual)
    lab=labelled_via_posets(5)
    iso=unlabelled_via_cycles(5)[1:]
    assert lab==expected_lab,(lab,expected_lab)
    assert iso==expected_iso,(iso,expected_iso)
    print('QUOTIENT',lab,iso)
    print('VERIFY_OK')

if __name__=='__main__':main()
