"""Independent finite-field checks for ranks of endomorphisms of free class-two Lie algebras.
Run: python verify.py. Pure Python 3, no external dependencies.
"""
from collections import Counter
from itertools import product
from math import prod, comb


def gaussian(n, k, q):
    if k < 0 or k > n: return 0
    val=1
    for i in range(k):
        numerator = q**(n-i)-1
        denominator = q**(k-i)-1
        val *= numerator
        # defer exact division to end using rational products
    den=prod(q**(k-i)-1 for i in range(k))
    return val//den


def rank_count(m, n, r, q):
    # m rows, n columns, rank r
    return gaussian(m,r,q)*prod(q**n-q**i for i in range(r))


def predicted(d,q):
    c0=comb(d,2)
    out=Counter()
    for a in range(d+1):
        b=comb(a,2)
        c=c0-b
        t=d-a
        numA=rank_count(d,d,a,q)
        for j in range(min(c,t)+1):
            numB=q**(c0*a+b*t)*rank_count(c,t,j,q)
            out[a+b+j]+=numA*numB
    return out


def rank_binary(columns):
    pivot={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k in pivot:
                x^=pivot[k]
            else:
                pivot[k]=x; break
    return len(pivot)


def brute_binary(d):
    pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
    C=len(pairs)
    hist=Counter()
    for abin in range(1<<(d*d)):
        acol=[(abin>>(i*d)) & ((1<<d)-1) for i in range(d)]
        wedges=[]
        for i,j in pairs:
            u,v=acol[i],acol[j]
            z=0
            for k,(s,t) in enumerate(pairs):
                z|=(((u>>s & 1)*(v>>t & 1) ^ (u>>t & 1)*(v>>s & 1))<<k)
            wedges.append(z<<(d))
        for bbin in range(1<<(C*d)):
            first=[acol[i] | (((bbin>>(i*C))&((1<<C)-1))<<d) for i in range(d)]
            hist[rank_binary(first+wedges)]+=1
    return hist


def mod_rank(cols, rows, q):
    matrix=[[c[i]%q for c in cols] for i in range(rows)]
    rk=0
    for j in range(len(cols)):
        ix=next((i for i in range(rk,rows) if matrix[i][j]),None)
        if ix is None: continue
        matrix[rk],matrix[ix]=matrix[ix],matrix[rk]
        inv=pow(matrix[rk][j],-1,q)
        matrix[rk]=[(x*inv)%q for x in matrix[rk]]
        for i in range(rows):
            if i!=rk:
                f=matrix[i][j]
                matrix[i]=[(x-f*y)%q for x,y in zip(matrix[i],matrix[rk])]
        rk+=1
        if rk==rows: break
    return rk


def brute_ternary_d2():
    d=2; q=3
    hist=Counter()
    for vals in product(range(q),repeat=4):
        a0=(vals[0],vals[1]);a1=(vals[2],vals[3])
        wedge=(a0[0]*a1[1]-a0[1]*a1[0])%q
        for b in product(range(q),repeat=2):
            cols=[a0+(b[0],),a1+(b[1],),(0,0,wedge)]
            hist[mod_rank(cols,3,3)]+=1
    return hist


def assert_equal(tag,d,q,computed):
    pred=predicted(d,q)
    assert computed==pred,(tag,pred,computed)
    assert sum(pred.values())==q**(d*(d+comb(d,2)))
    print(f'{tag} d={d} q={q}: total={sum(pred.values())}; ranks={sorted(pred.items())}')


def test_rank_support():
    for d in range(3,16):
        pred=predicted(d,2)
        C=comb(d,2)
        target=set()
        for a in range(d+1):
            target.update(range(a*(a+1)//2,d+a*(a-1)//2+1))
        assert set(pred)==target
        assert max(k for k in pred if k<d+C)==d+C-(d-1)
        for a in range(d//2+1,d):
            start=d+a*(a-1)//2+1
            end=(a+1)*(a+2)//2
            assert end-start==2*a-d
            assert not set(range(start,end))&set(pred)
    print('RANK_GAPS_OK dimensions 3..15')


if __name__=='__main__':
    assert_equal('EXHAUSTIVE_GF2',2,2,brute_binary(2))
    assert_equal('EXHAUSTIVE_GF2',3,2,brute_binary(3))
    assert_equal('EXHAUSTIVE_GF3',2,3,brute_ternary_d2())
    test_rank_support()
    print('VERIFY_OK')
