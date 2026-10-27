"""Independent validation by cyclic ternary column words (0=empty, 1/2=layer).
Unlike bitmask enumeration, this builds configurations column by column.
"""
from itertools import product

def words(n,k):
    return [a for a in product((0,1,2),repeat=n)
            if sum(v!=0 for v in a)==k
            and all(a[i]==0 or a[(i+1)%n]==0 or a[i]!=a[(i+1)%n]
                    for i in range(n))]

def swaps(a,b):
    A={(i,v) for i,v in enumerate(a) if v}
    B={(i,v) for i,v in enumerate(b) if v}
    return len(A-B)==len(B-A)==1

def connected(a):
    if not a:return False
    seen={0};stack=[0]
    while stack:
        p=stack.pop()
        for q,b in enumerate(a):
            if q not in seen and swaps(a[p],b):seen.add(q);stack.append(q)
    return len(seen)==len(a)

def main():
    for n in range(3,11):
        top=n if n%2==0 else n-1
        maxima=words(n,top)
        assert len(maxima)==(2 if n%2==0 else 2*n)
        if n%2:
            assert not words(n,n)
            assert connected(maxima)
            assert all(sum(swaps(w,t) for t in maxima)==2 for w in maxima)
        else:
            assert not swaps(maxima[0],maxima[1])
            near1=words(n,n-1)
            assert len(near1)==2*n
            S0=[w for w in near1 if all(w[i]==0 or w[i]==1+(i%2) for i in range(n))]
            S1=[w for w in near1 if w not in S0]
            assert len(S0)==len(S1)==n
            assert all(swaps(w,t) for w in S0 for t in S0 if w!=t)
            assert all(swaps(w,t) for w in S1 for t in S1 if w!=t)
            assert not any(swaps(w,t) for w in S0 for t in S1)
        near2=words(n,n-2)
        assert len(near2)==2*n*(n-2) and connected(near2)
        print('n=%d top=%d maxstates=%d near2states=%d connected=yes' %
              (n,top,len(maxima),len(near2)))

if __name__=='__main__':main()
