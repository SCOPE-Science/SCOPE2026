#!/usr/bin/env python3
from fractions import Fraction

def block_lengths(mask, n):
    out=[]
    j=0
    while j<n:
        if (mask>>j)&1:
            k=j
            while k<n and ((mask>>k)&1):
                k+=1
            out.append(k-j)
            j=k
        else:
            j+=1
    return out

checks=0
for m in range(2,8):
    for n in range(2,8):
        N=m+n
        target2=Fraction(N*(N-1),4)

        # Rebuild the distinct simplex summands in Proposition 3.21.
        summands=set()
        for i in range(N):
            summands.add((i,))
        for i in range(m):
            for j in range(i+1,m):
                summands.add((i,j))
            for j in range(m,N):
                summands.add((i,j))
        for left in range(n):
            for right in range(left+1,n):
                # Intervals of length at least two in the right coordinate block.
                summands.add(tuple(range(m+left,m+right+1)))

        assert len(summands)==N*(N+1)//2

        minimum=None
        for mask in range(1, (1<<N)-1):
            S={i for i in range(N) if (mask>>i)&1}
            a=sum(1 for i in range(m) if i in S)
            rmask=sum((1<<j) for j in range(n) if m+j in S)
            blocks=block_lengths(rmask,n)
            b=sum(blocks)
            s=a+b

            # Direct Minkowski support count.
            z_direct=sum(1 for I in summands if set(I).issubset(S))

            gamma=sum(blocks[i]*blocks[j]
                      for i in range(len(blocks))
                      for j in range(i+1,len(blocks)))
            z_formula=(
                a*(a+1)//2
                + a*b
                + sum(t*(t+1)//2 for t in blocks)
            )
            assert z_direct==z_formula
            assert z_formula==s*(s+1)//2-gamma

            slack=Fraction(s*(N+1),2)-z_direct
            norm2=Fraction(s*(N-s),N)
            d2=slack*slack/norm2
            predicted=(
                Fraction(s*(N-s),2)+gamma
            )**2/norm2
            assert d2==predicted
            assert d2>=target2

            if d2==target2:
                assert s in (1,N-1)
                assert gamma==0
            if s in (1,N-1) and gamma==0:
                assert d2==target2

            minimum=d2 if minimum is None else min(minimum,d2)
            checks+=1

        assert minimum==target2

print(f"VERIFY_OK generalized-multiplihedron-facet-distance subset_checks={checks} m,n=2..7 exact=yes")
