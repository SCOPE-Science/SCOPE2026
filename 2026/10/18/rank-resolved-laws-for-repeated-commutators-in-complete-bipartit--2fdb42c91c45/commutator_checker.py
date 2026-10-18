"""Standalone exhaustive finite-field checks for complete-bipartite graphical-group commutator fibers.

Run: python commutator_checker.py
No external packages or source files are needed.
"""
from collections import Counter, defaultdict
from itertools import product


def mul(x, y, q):
    if q == 4:
        a0,a1=x&1,(x>>1)&1
        b0,b1=y&1,(y>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0|(c1<<1)
    return x*y % q


def add(x, y, q):
    return (x ^ y) if q == 4 else (x+y) % q


def neg(x, q):
    return x if q == 4 else (-x) % q


def rank(rows, q):
    if not rows:
        return 0
    mat = [list(row) for row in rows]
    n = len(mat)
    m = len(mat[0])
    r = 0
    for c in range(m):
        pivot = next((i for i in range(r,n) if mat[i][c]), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        inv = next(z for z in range(1,q) if mul(z,mat[r][c],q)==1)
        mat[r] = [mul(inv,z,q) for z in mat[r]]
        for i in range(n):
            if i != r and mat[i][c]:
                coeff = mat[i][c]
                mat[i] = [add(mat[i][j],neg(mul(coeff,mat[r][j],q),q),q) for j in range(m)]
        r += 1
        if r == n: break
    return r


def typ(u,v):
    return ('M' if any(u) and any(v) else
            'U' if any(u) else 'V' if any(v) else 'Z')


def formulas(q,a,b):
    A,B = q**a,q**b
    gl2 = (q*q-1)*(q*q-q)
    return (
        A*A + B*B + (q+1)*A*B-(q+1)*(A+B)+q,
        (q*q-1)*(A+B-q), gl2
    )


def check(q,a,b):
    vs = list(product(range(q),repeat=a+b))
    types = {x:typ(x[:a],x[a:]) for x in vs}
    counts = defaultdict(Counter)
    ranks = {}
    for x in vs:
        u,v = x[:a],x[a:]
        for y in vs:
            s,t = y[:a],y[a:]
            z = tuple(add(mul(u[i],t[j],q), neg(mul(s[i],v[j],q),q),q)
                      for i in range(a) for j in range(b))
            counts[(types[x],types[y])][z]+=1
    buckets = defaultdict(set)
    for z in product(range(q),repeat=a*b):
        r = rank([z[i*b:(i+1)*b] for i in range(a)],q)
        ranks[z]=r
        buckets[r].add(z)
    total = Counter()
    for key,table in counts.items():
        for z,n in table.items(): total[z]+=n
    N=formulas(q,a,b)
    for z,r in ranks.items():
        assert total[z] == (N[r] if r<=2 else 0), (q,a,b,z,r,total[z],N)
    A,B=q**a,q**b
    t={'Z':1,'U':A-1,'V':B-1,'M':(A-1)*(B-1)}
    # Each pair of support types has a target-independent count within rank strata.
    for pair,table in counts.items():
        for r,bucket in buckets.items():
            vals = {table[z] for z in bucket}
            assert len(vals)==1,(q,a,b,pair,r,vals)
            n=next(iter(vals))
            x,y=pair
            expect=0
            if r==0:
                if x=='Z': expect=t[y]
                elif y=='Z': expect=t[x]
                elif x==y=='U': expect=t['U']**2
                elif x==y=='V': expect=t['V']**2
                elif x==y=='M': expect=(q-1)*t['M']
            if r==1:
                if (x,y) in [('U','V'),('V','U')]: expect=q-1
                elif set((x,y))=={'U','M'}: expect=(q-1)*(A-1)
                elif set((x,y))=={'V','M'}: expect=(q-1)*(B-1)
                elif x==y=='M': expect=(q-1)**2*(A+B-q-2)
            if r==2 and x==y=='M': expect=(q*q-1)*(q*q-q)
            assert n==expect,(q,a,b,pair,r,n,expect)
    # Every possible target is accounted for, including rank >=3 zero fibers.
    expected_rank_counts={r:len(zs) for r,zs in buckets.items()}
    assert sum(expected_rank_counts[r]* (N[r] if r<=2 else 0)
               for r in expected_rank_counts)==q**(2*(a+b))
    print('PASS',f'q={q} a={a} b={b}', 'N=',N,'target_ranks=',dict(expected_rank_counts))

def gaussian(n, k, q):
    if k < 0 or k > n: return 0
    num=den=1
    for i in range(k):
        num *= q**(n-i)-1
        den *= q**(k-i)-1
    return num//den


def rank_character_sum(q,a,b,r,s):
    # Additive-character sum of rank-s maps from F_q^a into F_q^b
    total=0
    for j in range(s+1):
        total += ((-1)**(s-j) * q**((s-j)*(s-j-1)//2+a*j)
                  * gaussian(b-r,j,q) * gaussian(b-j,s-j,q))
    return total


def kfold_fiber(q,a,b,k,r):
    assert k>=0
    numerator = sum(q**(2*k*(a+b-s))*rank_character_sum(q,a,b,r,s)
                    for s in range(min(a,b)+1))
    assert numerator % q**(a*b)==0,(q,a,b,k,r,numerator)
    return numerator//q**(a*b)


def independent_convolution_check(q,a,b,max_k):
    targets=list(product(range(q),repeat=a*b))
    zero=(0,)*(a*b)
    rank_by_target={z:rank([z[i*b:(i+1)*b] for i in range(a)],q)
                    for z in targets}
    N=formulas(q,a,b)
    curr={z:(N[rank_by_target[z]] if rank_by_target[z]<3 else 0)
          for z in targets}
    one=curr.copy()
    for k in range(1,max_k+1):
        for z in targets:
            expect=kfold_fiber(q,a,b,k,rank_by_target[z])
            assert curr[z]==expect,(q,a,b,k,z,rank_by_target[z],curr[z],expect)
        assert sum(curr.values())==q**(2*k*(a+b))
        print('CONVOLUTION PASS',f'q={q} a={a} b={b} k={k}',
              'values by rank=',{r:curr[z] for z,r in rank_by_target.items()})
        if k<max_k:
            new={z:0 for z in targets}
            for z,n in curr.items():
                if not n: continue
                for y,m in one.items():
                    if m:
                        w=tuple(add(zi,yi,q) for zi,yi in zip(z,y))
                        new[w]+=n*m
            curr=new

if __name__ == '__main__':
    for case in [(2,1,1),(2,2,2),(2,3,3),(2,2,4),(3,1,2),(3,2,2),(3,2,3),(4,1,2),(4,2,2)]:
        check(*case)
    for case in [(2,2,2,4),(2,3,3,3),(3,2,2,3),(4,2,2,3)]:
        independent_convolution_check(*case)
    print('ALL_EXACT_CHECKS_PASSED 9 one-step cases + 4 multi-step cases')
