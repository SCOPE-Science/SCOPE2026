"""Independent arithmetic checks of fixed-support Pythagorean pairs."""
from math import isqrt
from itertools import combinations

def lengths(A,B):
    return [max(0,min(B-1,w//2)-max(0,(w-A+2)//2)+1) for w in range(A+2*B-2)]

def independent_formula(A,B):
    ll=lengths(A,B)
    v=sum((n+1)//2 for n in ll)
    c=1
    for n in ll:
        if n and n%2==0:
            c*=n//2+1
    return v,c

def square(N):
    return [(N*(N+1)//2),(N*(N+2)//2),((2*N*N+3*N-1)//4),((2*N*N+3*N+1)//4)][N%4==2 and 1 or N%4==1 and 2 or N%4==3 and 3 or 0]

def tested_edges(A,B):
    pts=[(a,b) for a in range(A) for b in range(B)]
    nums=[2**a*3**b for a,b in pts]
    found=set()
    for i,j in combinations(range(len(nums)),2):
        x=nums[i]*nums[i]+nums[j]*nums[j]
        if isqrt(x)**2==x: found.add((i,j))
    expected=set()
    index={p:i for i,p in enumerate(pts)}
    for a,b in pts:
        if a+2<A and b>0:
            i,j=sorted((index[(a,b)],index[(a+2,b-1)]))
            expected.add((i,j))
    assert found==expected,(A,B,found^expected)
    return pts,found

def brute(A,B):
    pts,edges=tested_edges(A,B)
    if len(pts)>16: return
    best=0;count=0
    for mask in range(1<<len(pts)):
        if mask.bit_count()<best:continue
        if any((mask>>i)&1 and (mask>>j)&1 for i,j in edges): continue
        z=mask.bit_count()
        if z>best:best,count=z,0
        if z==best:count+=1
    assert (best,count)==independent_formula(A,B),(A,B,(best,count),independent_formula(A,B))

for A in range(1,11):
    for B in range(1,11):
        tested_edges(A,B)
        if A*B<=16:brute(A,B)
for N in range(1,201):
    assert independent_formula(N,N)[0]==square(N),(N,independent_formula(N,N),square(N))
print('VERIFY_OK rectangular_cases=100 exact_maximizers_for_boxes_up_to_16=true square_formulas_through_200=true')
