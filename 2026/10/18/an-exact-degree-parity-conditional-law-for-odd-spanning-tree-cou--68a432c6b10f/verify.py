from collections import defaultdict
from math import prod

def detmod2(rows,m):
    rank=0
    for col in range(m):
        p=next((k for k in range(rank,m) if (rows[k]>>col)&1),None)
        if p is None:continue
        rows[rank],rows[p]=rows[p],rows[rank]
        for k in range(m):
            if k!=rank and ((rows[k]>>col)&1):rows[k]^=rows[rank]
        rank+=1
    return rank==m

def alpha(k):
 from fractions import Fraction
 return prod((Fraction(2**(2*j-1)-1,2**(2*j-1)) for j in range(1,k+1)),start=Fraction(1))
for n in range(2,7):
 pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
 groups=defaultdict(lambda:[0,0])
 for mask in range(1<<len(pairs)):
  adj=[0]*n; d=0
  for k,(i,j) in enumerate(pairs):
   if mask>>k&1:
    adj[i]^=1<<j;adj[j]^=1<<i;d^=(1<<i)|(1<<j)
  B=[adj[i]&((1<<(n-1))-1) for i in range(n-1)]
  for i in range(n-1):
   if d>>i&1:B[i]^=1<<i
  odd=detmod2(B,n-1)
  groups[d][0]+=1;groups[d][1]+=odd
 expect=alpha((n-1)//2) if n%2 else alpha((n-2)//2)
 assert all((odd==0 if n%2==0 and d==0 else odd*expect.denominator==total*expect.numerator) for d,(total,odd) in groups.items())
 print(n,len(pairs),'degree_classes',len(groups),'per_class','range',sorted(set((a,b) for a,b in groups.values())),'pred',expect)

# Exhaustive fixed-diagonal symmetric matrices, sizes 1,...,5.
from collections import defaultdict
for m in range(1,6):
    matrix_counts=defaultdict(lambda:[0,0]); pos=[(i,j) for i in range(m) for j in range(i+1,m)]
    for b in range(1<<m):
        for mask in range(1<<len(pos)):
            rr=[((b>>i)&1)<<i for i in range(m)]
            for k,(i,j) in enumerate(pos):
                if mask>>k&1:
                    rr[i]^=1<<j;rr[j]^=1<<i
            matrix_counts[b][0]+=1
            matrix_counts[b][1]+=detmod2(rr,m)
    target=alpha(m//2) if m%2==0 else alpha((m-1)//2)
    for b,(total,odd) in matrix_counts.items():
        if b==0 and m%2==1:
            assert odd==0
        else:
            assert odd*target.denominator==total*target.numerator, (m,b,total,odd,target)
    print('fixed-diagonal matrices',m,'diagonals',len(matrix_counts),'all validated')
print('PASS exact finite enumerations')
