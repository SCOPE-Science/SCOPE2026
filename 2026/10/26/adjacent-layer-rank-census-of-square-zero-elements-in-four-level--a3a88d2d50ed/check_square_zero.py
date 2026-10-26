"""Direct check of the four-level square-zero rank-refined census.
Use: python3 check_square_zero.py
No external dependencies.
"""
from itertools import product
from collections import Counter
from math import prod


def add(x,y,q):
    return x ^ y if q==4 else (x+y)%q

def mul(x,y,q):
    if q!=4: return x*y%q
    z=0
    while y:
        if y&1: z ^= x
        y >>= 1
        x <<= 1
        if x&4: x ^= 7
    return z

def power(x,n,q):
    z=1
    for _ in range(n): z=mul(z,x,q)
    return z

def inverse(x,q):
    assert x
    return power(x,q-2,q)

def rank(M,q):
    if not M: return 0
    a=[list(r) for r in M]
    m,n=len(a),len(a[0]); pivot=0
    for j in range(n):
        k=next((i for i in range(pivot,m) if a[i][j]),None)
        if k is None:continue
        a[pivot],a[k]=a[k],a[pivot]
        inv=inverse(a[pivot][j],q)
        a[pivot]=[mul(inv,v,q) for v in a[pivot]]
        for i in range(pivot+1,m):
            if a[i][j]:
                t=a[i][j]
                a[i]=[add(v,mul(t,w,q),q) if q==4 else (v-t*w)%q for v,w in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==m:break
    return pivot

def mat(values,rows,cols):
    return [list(values[i*cols:(i+1)*cols]) for i in range(rows)]

def mm(A,B,q):
    n=len(A); m=len(B); c=len(B[0]) if B else 0
    return [[sum(mul(A[i][k],B[k][j],q) for k in range(m))%q if q!=4
              else xor_prod(A[i], [B[k][j] for k in range(m)],q)
              for j in range(c)] for i in range(n)]

def xor_prod(x,y,q):
    z=0
    for u,v in zip(x,y):z^=mul(u,v,q)
    return z

def zero(A):return all(v==0 for row in A for v in row)

def sum_mat(A,B,q):
    return [[add(x,y,q) for x,y in zip(aa,bb)] for aa,bb in zip(A,B)]

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    numerator=prod(q**(n-j)-1 for j in range(k))
    denominator=prod(q**(k-j)-1 for j in range(k))
    assert numerator%denominator==0
    return numerator//denominator

def matrix_rank_count(m,n,r,q):
    if r<0 or r>min(m,n):return 0
    return gaussian(m,r,q)*prod(q**n-q**i for i in range(r))

def predicted(a,b,c,d,q):
    ans=Counter()
    for t in range(min(b,c)+1):
        nb=matrix_rank_count(b,c,t,q)
        for r in range(min(a,b-t)+1):
            na=matrix_rank_count(a,b-t,r,q)
            for s in range(min(c-t,d)+1):
                nc=matrix_rank_count(c-t,d,s,q)
                ans[(r,t,s)]+= nb*na*nc*q**(a*d+a*c+b*d-a*s-r*d+r*s)
    return ans

def direct(a,b,c,d,q):
    sizes=[a*b,a*c,a*d,b*c,b*d,c*d]
    blocks=[None]*6
    ans=Counter()
    import itertools
    allchoices=[list(product(range(q),repeat=s)) for s in sizes]
    for A,D,F,B,E,C in itertools.product(*allchoices):
        AA=mat(A,a,b);BB=mat(B,b,c);CC=mat(C,c,d)
        if not zero(mm(AA,BB,q)):continue
        if not zero(mm(BB,CC,q)):continue
        DD=mat(D,a,c);EE=mat(E,b,d)
        if not zero(sum_mat(mm(AA,EE,q),mm(DD,CC,q),q)):continue
        ans[(rank(AA,q),rank(BB,q),rank(CC,q))]+=1
    return ans



def same_flag_different_adjacent_witness():
    # Four antichain levels of sizes (1,2,1,1); index ranges 0,1:3,3,4.
    # One map from the last level to the third, or from the last to the second.
    n1=[[0]*5 for _ in range(5)]
    n2=[[0]*5 for _ in range(5)]
    n1[3][4]=1
    n2[2][4]=1
    prefixes=(1,3,4,5)
    assert [rank([row[:k] for row in n1[:k]],2) for k in prefixes] == [0,0,0,1]
    assert [rank([row[:k] for row in n2[:k]],2) for k in prefixes] == [0,0,0,1]
    assert zero(mm(n1,n1,2)) and zero(mm(n2,n2,2))
    assert rank([[n1[3][4]]],2)==1 and rank([[n2[3][4]]],2)==0
    print('OK prefix-Jordan witness: equal prefix ranks, distinct adjacent C ranks')

def main():
    same_flag_different_adjacent_witness()
    configs=[(1,1,1,1,2),(1,1,1,1,3),(1,1,1,1,4),(1,1,1,1,5),
             (2,1,1,1,2),(1,2,1,1,2),(1,1,2,1,2),(1,1,1,2,2),
             (2,2,1,1,2),(1,2,2,1,2),(1,1,1,1,7)]
    for a,b,c,d,q in configs:
        expected=predicted(a,b,c,d,q)
        if q==7:  # 7^6 is ~117k, still exhaustive
            pass
        actual=direct(a,b,c,d,q)
        assert actual==expected,(a,b,c,d,q,actual,expected)
        print('OK',q,(a,b,c,d),'count',sum(actual.values()),'strata',len(actual))
    for q in (2,3,4,5):
        for m in range(0,7):
            for n in range(0,7):
                assert sum(matrix_rank_count(m,n,r,q) for r in range(min(m,n)+1)) == q**(m*n)
    print('ALL_FOUR_LAYER_SQUARE_ZERO_CHECKS_PASSED',len(configs),'and 196 rank-count identities')

if __name__=='__main__':main()
