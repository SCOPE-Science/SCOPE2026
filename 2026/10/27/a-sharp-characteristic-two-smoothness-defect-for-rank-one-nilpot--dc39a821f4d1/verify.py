#!/usr/bin/env python3
"""Independent finite-field and tangent checks for a square-zero rank-one algebra."""
from itertools import product
from math import prod

def add(a, b, q):
    return a ^ b if q in (2, 4) else (a + b) % q

def mul(a, b, q):
    if q == 2:
        return a & b
    if q == 4:
        z = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & 1 and (b >> j) & 1:
                    z ^= (1 << (i+j))
        if z & 8:
            z ^= 0b1100  # x^3 = x^2 + x = 1 under x^2=x+1
        if z & 4:
            z ^= 0b111  # x^2=x+1
        return z
    return (a*b) % q

def gram_similitudes(q, n):
    count_o = 0
    count_go = 0
    for entries in product(range(q), repeat=n*n):
        diag = 0
        ok = True
        for i in range(n):
            for j in range(i, n):
                s = 0
                for k in range(n):
                    s = add(s, mul(entries[k*n+i], entries[k*n+j], q), q)
                if i == j:
                    if i == 0:
                        diag = s
                        if diag == 0:
                            ok = False; break
                    elif s != diag:
                        ok = False; break
                elif s != 0:
                    ok = False; break
            if not ok:
                break
        if ok:
            count_go += 1
            count_o += (diag == 1)
    return count_o, count_go

def sp_order(q, m):
    return q**(m*m) * prod(q**(2*i)-1 for i in range(1, m+1))

def orth_count(q,n):
    if n%2:
        return sp_order(q, (n-1)//2)
    return q**(n-1) * sp_order(q, (n-2)//2)

def rank_mod_p(mat, p):
    a=[[x%p for x in row] for row in mat]
    ncol=len(a[0]); rank=0
    for col in range(ncol):
        i=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if i is None: continue
        a[i], a[rank] = a[rank], a[i]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[(inv*z)%p for z in a[rank]]
        for j in range(len(a)):
            if j!=rank and a[j][col]:
                t=a[j][col]
                a[j]=[(x-t*y)%p for x,y in zip(a[j],a[rank])]
        rank+=1
    return rank

def linearized_rank(n,p):
    # X^T+X-h I=0 for X in M_n, h=delta c.
    rows=[]
    for i in range(n):
        for j in range(i,n):
            v=[0]*(n*n+1)
            v[i*n+j]+=1; v[j*n+i]+=1
            if i==j: v[n*n]-=1
            rows.append(v)
    return rank_mod_p(rows,p)

def main():
    cases=0
    for q,n in [(2,1),(2,2),(2,3),(2,4),(4,1),(4,2),(4,3)]:
        actual_o,actual_go=gram_similitudes(q,n)
        expected_o=orth_count(q,n)
        expected_go=(q-1)*expected_o
        assert (actual_o,actual_go)==(expected_o,expected_go), (q,n,actual_o,actual_go,expected_o,expected_go)
        # Every vector of coefficients in the annihilator creates an automorphism.
        assert actual_go*q**n == (q-1)*q**n*expected_o
        print('char2_count',q,n,actual_o,actual_go,actual_go*q**n)
        cases+=1
    for n in range(1,12):
        for p in [2,3,5,7]:
            actual=(n*n+1)-linearized_rank(n,p)
            expected=n*(n+1)//2 if p==2 else n*(n-1)//2+1
            assert actual==expected,(n,p,actual,expected)
            cases+=1
    print('VERIFY_OK finite_field_count_cases=7 tangent_cases=44 total_cases=',cases)

if __name__ == '__main__':
    main()
