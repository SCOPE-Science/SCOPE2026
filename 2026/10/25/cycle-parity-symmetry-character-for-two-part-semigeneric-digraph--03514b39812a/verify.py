#!/usr/bin/env python3
"""Exhaustively compare parity-matrix symmetries with closed fixed-point characters."""
import itertools
from math import factorial

def parity_matrices(a,b):
    for bits in itertools.product((0,1), repeat=a*b):
        M=tuple(tuple(bits[i*b+j] for j in range(b)) for i in range(a))
        if all(M[i][j]^M[ii][j]^M[i][jj]^M[ii][jj]==0
               for i in range(a) for ii in range(i+1,a)
               for j in range(b) for jj in range(j+1,b)):
            yield M

def cycles(p):
    seen=set();ls=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;length=0
            while j not in seen:
                seen.add(j);length+=1;j=p[j]
            ls.append(length)
    return ls

def fixing_preserving(M,s,t):
    a=len(M);b=len(M[0])
    return all(M[i][j]==M[s[i]][t[j]] for i in range(a) for j in range(b))

def fixing_swapping(M,s,t):
    n=len(M)
    return all(M[i][j]==1-M[t[j]][s[i]] for i in range(n) for j in range(n))

def theorem_pres(s,t):
    c=len(cycles(s))+len(cycles(t))
    flag=all(l%2==0 for l in cycles(s)+cycles(t))
    return 2**(c-1)*(1+int(flag))

def theorem_swap(s,t):
    theta=tuple(t[s[i]] for i in range(len(s)))
    ls=cycles(theta)
    return 2**len(ls) if all(x%2==0 for x in ls) else 0

checks=0
for a,b in [(1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4)]:
    Ms=list(parity_matrices(a,b))
    assert len(Ms)==2**(a+b-1)
    p=list(itertools.permutations(range(a)))
    q=list(itertools.permutations(range(b)))
    for s in p:
        for t in q:
            actual=sum(fixing_preserving(M,s,t) for M in Ms)
            assert actual==theorem_pres(s,t), (a,b,s,t,actual,theorem_pres(s,t))
            checks+=1
    if a==b:
        for s in p:
            for t in q:
                actual=sum(fixing_swapping(M,s,t) for M in Ms)
                assert actual==theorem_swap(s,t), (a,b,s,t,actual,theorem_swap(s,t))
                checks+=1
    total_pres=sum(sum(fixing_preserving(M,s,t) for M in Ms) for s in p for t in q)//(factorial(a)*factorial(b))
    expected_pres=((a+1)*(b+1)+int(a%2==0 and b%2==0))//2
    assert total_pres==expected_pres, (a,b,total_pres,expected_pres)
    if a==b:
        fixed_swaps=sum(sum(fixing_swapping(M,s,t) for M in Ms) for s in p for t in q)
        total_all=(total_pres*factorial(a)**2+fixed_swaps)//(2*factorial(a)**2)
        expected_all=((a+1)**2+3*int(a%2==0))//4
        assert total_all==expected_all,(a,total_all,expected_all)
    print('PASS',a,b,len(Ms),'preserving_orbits',total_pres,'full_orbits',expected_all if a==b else 'not applicable')
print('ALL_TESTS_PASS',checks)
