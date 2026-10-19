"""Independent state-construction and local-geometry checks for rectangular rook graphs.
Run: python italian_rook_check2.py. Uses the standard library only.
"""
from itertools import combinations_with_replacement, product
from math import factorial,comb
from collections import Counter

def good(x,m,n):
    for i in range(m):
        for j in range(n):
            if x[i][j]!=0:continue
            if sum(x[i][k] for k in range(n) if k!=j)+sum(x[k][j] for k in range(m) if k!=i)<2:
                return False
    return True

def local_states(n):
    ans=[]
    for a,b in combinations_with_replacement(range(n),2):
        v=[0]*n;v[a]+=1;v[b]+=1
        ans.append(tuple(v))
    return ans

def main():
    for m,n in [(2,5),(2,6),(2,8),(3,7),(3,8)]:
        local=local_states(n)
        histogram=Counter()
        sample=None
        count=0
        for rows in product(local,repeat=m):
            assert good(rows,m,n)
            deg=sum((n-1) if 2 in row else 2*(n-1) for row in rows)
            histogram[deg]+=1
            count+=1
            if sample is None:sample=rows
        assert count==comb(n+1,2)**m
        target={ (n-1)*(m+k):comb(m,k)*n**(m-k)*comb(n,2)**k for k in range(m+1)}
        assert dict(histogram)==target, (m,n,histogram,target)
        # Cartesian product distance is half the L1 distance, attained by within-row transfers.
        other=[]
        for row in sample:
            other.append(next(v for v in local if sum(min(a,b) for a,b in zip(row,v))==0))
        assert sum(sum(abs(a-b) for a,b in zip(row,v))//2 for row,v in zip(sample,other))==2*m
        print(f'product m={m} n={n}: functions={count}, degrees={sorted(histogram.items())}, radius=diameter={2*m}')
    # At equality the two families meet in equal-sized fibres of the column-to-row map.
    for m in [2,3,4]:
        n=2*m
        full=balanced=0
        for assignment in product(range(m),repeat=n):
            counts=[assignment.count(i) for i in range(m)]
            if all(counts):
                full+=1
                if all(c==2 for c in counts):balanced+=1
        A=sum((-1)**j*comb(m,j)*(m-j)**n for j in range(m+1))
        assert full==A and balanced==factorial(n)//2**m
        total=A+comb(n+1,2)**m-balanced
        print(f'critical m={m} n={n}: cover={A} balanced={balanced} total={total}')
    print('STRUCTURAL_CHECKS_OK')
if __name__=='__main__':main()
