"""Exact finite certificates for uniqueness of three-stratum zero-envy lotteries.

Run with Python 3; only the standard library is required.
"""
from fractions import Fraction as Q
from itertools import combinations, product, permutations

SHAPES = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (3, 1, 1))

def outcomes(blocks, k):
    return tuple(v for v in product(*(range(m + 1) for m in blocks)) if sum(v) == k)

def matrix(blocks, k):
    states = outcomes(blocks, k)
    return [[Q(1) for _ in states]] + [
        [Q(v[j] >= blocks[j] - rank) for v in states]
        for j in range(3) for rank in range(blocks[j])]

def rank(rows):
    m=[r[:] for r in rows]
    if not m: return 0
    nr,nc=len(m),len(m[0]); i=0
    for j in range(nc):
        s=next((t for t in range(i,nr) if m[t][j]),None)
        if s is None:continue
        m[i],m[s]=m[s],m[i]
        c=m[i][j]
        for h in range(j,nc):m[i][h]/=c
        for t in range(nr):
            if t!=i and m[t][j]:
                c=m[t][j]
                for h in range(j,nc):m[t][h]-=c*m[i][h]
        i+=1
        if i==nr:break
    return i

def determinant(square):
    x=[r[:] for r in square]
    size=len(x); ans=Q(1)
    for i in range(size):
        z=next((j for j in range(i,size) if x[j][i]),None)
        if z is None:return Q(0)
        if z!=i:
            x[i],x[z]=x[z],x[i]
            ans=-ans
        piv=x[i][i];ans*=piv
        for j in range(i+1,size):
            q=x[j][i]/piv
            for l in range(i+1,size):x[j][l]-=q*x[i][l]
            x[j][i]=0
    return ans

def test_lottery(weights):
    assert sum(weights.values(),Q(0))==1
    expected=[Q(0)]*6
    for state,p in weights.items():
        assert sum(state)==3 and p>=0
        for g,n in enumerate(state):
            for pos in range(2):
                expected[2*g+pos] += p*Q(n>=2-pos)
    assert expected==[Q(1,5),Q(4,5)]*3,expected

if __name__=='__main__':
    certificates=[]
    for blocks in SHAPES:
        n=sum(blocks)
        for k in range(n+1):
            a=matrix(blocks,k)
            states=outcomes(blocks,k)
            assert rank(a)==len(states),(blocks,k)
            if 0<k<n:
                witness=next(( (sel,determinant([a[i] for i in sel]))
                    for sel in combinations(range(n+1),len(states))
                    if determinant([a[i] for i in sel])!=0),None)
                assert witness is not None
                sel,det=witness
                assert abs(det)==1,(blocks,k,sel,det)
                certificates.append((blocks,k,len(states),sel,int(det)))
    a6=matrix((2,2,2),3)
    assert len(a6[0])==7 and rank(a6)==6
    all_perms=set(permutations((0,1,2)))
    uniform={s:Q(1,10) for s in all_perms}
    uniform[(1,1,1)]=Q(2,5)
    cycle={s:Q(1,5) for s in ((0,1,2),(1,2,0),(2,0,1))}
    cycle[(1,1,1)]=Q(2,5)
    assert uniform!=cycle
    test_lottery(uniform)
    test_lottery(cycle)
    for b,k,n,rows,det in certificates:
        print(f'shape={b} k={k} columns={n} rows={rows} det={det}')
    print(f'PASS: {len(certificates)} exact nonzero minors, all boundary k, rank 6 of 7 at six parties, two distinct rational lotteries.')
