"""Direct finite-field tests of rank-refined square-root fibers.

No external packages. Enumerates ALL matrices in listed small cases;
uses no Jordan classification or group-order ratios in that enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def field(q):
    assert q in (2,3,4)
    if q == 4:
        add = [[a ^ b for b in range(4)] for a in range(4)]
        mul = [[0] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                t = 0
                for i in range(2):
                    for j in range(2):
                        if (a >> i) & (b >> j) & 1:
                            t ^= 1 << (i+j)
                if t & 8:  # not reached for degree <=2
                    t ^= 0b10110
                if t & 4:
                    t ^= 0b111  # x^2 = x+1
                mul[a][b] = t
    else:
        add = [[(a+b)%q for b in range(q)] for a in range(q)]
        mul = [[a*b%q for b in range(q)] for a in range(q)]
    inv = [0] + [next(b for b in range(1,q) if mul[a][b] == 1) for a in range(1,q)]
    return add,mul,inv


def square(mat,n,add,mul):
    out = []
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v = add[v][mul[mat[n*i+k]][mat[n*k+j]]]
            out.append(v)
    return tuple(out)


def rank(mat,n,add,mul,inv):
    a=[list(mat[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if a[i][col]),None)
        if pivot is None: continue
        a[pivot],a[r]=a[r],a[pivot]
        fac=inv[a[r][col]]
        for j in range(col,n):a[r][j]=mul[fac][a[r][j]]
        for i in range(n):
            if i == r or a[i][col] == 0:continue
            fac=a[i][col]
            # in odd char, additive inverse is (q-1)*v; use table.
            for j in range(col,n):
                v=mul[fac][a[r][j]]
                negative=next(t for t in range(len(add)) if add[t][v]==0)
                a[i][j]=add[a[i][j]][negative]
        r+=1
        if r==n:break
    return r


def centralizer_order(mult,q):
    dim=sum(sum(a for k,a in mult.items() if k>=j)**2
            for j in range(1,max(mult,default=0)+1))
    answer=Fraction(q**dim)
    for a in mult.values():
        for j in range(1,a+1): answer *= Fraction(q**j-1,q**j)
    assert answer.denominator==1
    return int(answer)


def theoretical(n,r,q):
    m=n-2*r
    if m<0:return {}
    target=centralizer_order({2:r,1:m},q)
    counts=Counter()
    for a in range(r//2+1):
        b=r-2*a
        for c in range(max(0,(m-b)//2+1)):
            d=m-b-2*c
            if d<0:continue
            source=centralizer_order({4:a,3:b,2:c,1:d},q)
            assert target % source==0
            counts[3*a+2*b+c] += target//source
    return dict(counts)


def target_matrix(n,r):
    a=[0]*(n*n)
    for i in range(r):a[(2*i)*n+2*i+1]=1
    return tuple(a)


def exhaustive(n,q):
    add,mul,inv=field(q)
    targets={target_matrix(n,r):r for r in range(n//2+1)}
    observed={r:Counter() for r in range(n//2+1)}
    for M in product(range(q),repeat=n*n):
        r=targets.get(square(M,n,add,mul))
        if r is not None:
            observed[r][rank(M,n,add,mul,inv)] += 1
    for r in range(n//2+1):
        got=dict(observed[r]); expected=theoretical(n,r,q)
        assert got==expected,(n,q,r,got,expected)
        print('CHECK',n,q,r,'rank_counts',dict(sorted(got.items())))


def limits_check():
    for q in (2,3,4,5,7):
        for n in range(1,16):
            for r in range(n//2+1):
                got=theoretical(n,r,q)
                if r%2 and n==2*r:
                    assert not got
                else:
                    assert sorted(got)==list(range((3*r+1)//2,(n+r)//2+1))
    print('FORMULA_AND_SHARP_BOUNDS_OK')

if __name__=='__main__':
    limits_check()
    for n,q in ((2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)):
        exhaustive(n,q)
    print('VERIFY_OK_NILPOTENT_SQUARE_ROOT_FIBERS')
