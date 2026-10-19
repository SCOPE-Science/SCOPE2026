"""Exact ternary Fourier-minor characteristic-polynomial enumeration.

Run: python3 checker.py
Only Python's integer arithmetic is used. A primitive cube root z obeys z*z=-1-z.
"""
from itertools import combinations, permutations, product
from collections import Counter

ZPOW=((1,0),(0,1),(-1,-1))
ZERO=(0,0); ONE=(1,0)

def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def times(x,y):return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def minus(x):return(-x[0],-x[1])
def dot(x,y):return sum(a*b for a,b in zip(x,y))%3

def det(matrix):
    n=len(matrix); ans=ZERO
    for perm in permutations(range(n)):
        term=ONE
        for i,j in enumerate(perm):term=times(term,matrix[i][j])
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        ans=plus(ans,minus(term) if inversions%2 else term)
    return ans

def charpoly(A,B):
    gram=[]
    for a in A:
        row=[]
        for aa in A:
            val=ZERO
            for b in B:
                val=plus(val,ZPOW[(dot(a,b)-dot(aa,b))%3])
            row.append(val)
        gram.append(row)
    e=[]
    for k in range(1,5):
        val=ZERO
        for idx in combinations(range(4),k):
            val=plus(val,det([[gram[i][j] for j in idx] for i in idx]))
        assert val[1]==0,('coefficient not rational',val)
        e.append(val[0])
    return (1,-e[0],e[1],-e[2],e[3])

LINE=((0,0),(1,0),(2,0),(0,1))
CAP=((0,0),(1,0),(0,1),(1,1))
INDEPENDENT=((0,0,0),(1,0,0),(0,1,0),(0,0,1))
P_LINE=(1,-16,84,-162,81)
P_CAP=(1,-16,81,-144,81)
P_INDEPENDENT=(1,-16,90,-216,189)

expected_line={
    (1,-16,84,-162,81):36,
    (1,-16,72,-81,0):8,
    (1,-16,78,-108,0):12,
}
expected_cap={
    (1,-16,81,-144,81):16,
    (1,-16,78,-144,81):4,
    (1,-16,84,-162,81):16,
    (1,-16,78,-108,0):16,
    (1,-16,84,-144,0):4,
}

def census(A):
    d=len(A[0]); grid=list(product(range(3),repeat=d))
    count=Counter()
    for remaining in combinations(grid[1:],3):
        count[charpoly(A,(grid[0],)+remaining)]+=1
    return count

assert census(LINE)==expected_line
assert census(CAP)==expected_cap
third=census(INDEPENDENT)
assert sum(third.values())==2600
assert sum(num for polynomial,num in third.items() if polynomial[2]==90)==8
assert third[P_INDEPENDENT]==8
assert all(polynomial[2]<=90 for polynomial in third)
assert charpoly(INDEPENDENT,((0,0,0),(0,1,2),(1,0,2),(2,2,1)))==P_INDEPENDENT
assert charpoly(CAP,((0,0),(0,1),(1,0),(1,2)))==P_CAP
assert charpoly(LINE,((0,0),(0,1),(1,0),(2,0)))==P_LINE

print('CHECK_PASS')
print('line_normalized_good=36 cap_normalized_optimal=16 independent_normalized_optimal=8')
print('line_full=81 cap_full=36 independent_full=54')
