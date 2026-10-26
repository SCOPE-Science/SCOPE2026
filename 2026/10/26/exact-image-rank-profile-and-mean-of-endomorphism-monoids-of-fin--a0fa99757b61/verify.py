from itertools import product
from math import comb

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def trace_power_path(s,n):
    if s<1:return 0
    A=[[int(abs(i-j)==1) for j in range(s)] for i in range(s)]
    P=[[int(i==j) for j in range(s)] for i in range(s)]
    for _ in range(n):P=matmul(P,A)
    return sum(P[i][i] for i in range(s))

def counts_formula(n):
    m=n//2
    t=[trace_power_path(s,n) for s in range(m+2)]
    d={r:n*(t[r]-2*t[r-1]+t[r-2]) for r in range(2,m+2)}
    d[n]=2*n
    return d

def counts_brute(n):
    result={}
    for start in range(n):
        for signs in product((1,-1),repeat=n):
            if sum(signs)%n!=0:continue
            vals=[start]
            for s in signs[:-1]:vals.append((vals[-1]+s)%n)
            r=len(set(vals));result[r]=result.get(r,0)+1
    return result

for n in range(4,13,2):
    formula=counts_formula(n)
    brute=counts_brute(n)
    assert formula==brute,(n,formula,brute)
    total=sum(formula.values())
    expected_numer=sum(r*c for r,c in formula.items())
    m=n//2
    assert total==n*(comb(n,m)+2)
    assert expected_numer==n*(4**m+2*n)
    print(n,formula,'total',total,'mean=',f'{expected_numer}/{total}', 'mean formula=', f'({4**m}+{2*n})/({comb(n,m)}+2)')
print('VERIFY_OK')
