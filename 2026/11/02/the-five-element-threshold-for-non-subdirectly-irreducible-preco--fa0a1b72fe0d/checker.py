"""Standalone finite checks of preconditional-chain congruence threshold.
Python >= 3.9; no external dependencies. Enumerates n<=5 algebra candidates,
checks P1-P5 literally and every interval-partition congruence.
"""
from itertools import product

def candidate_rows(n,a):
    if a == 0: return [(n-1,)*n]
    if a == n-1: return [tuple(range(n))]
    ret=[]
    for mids in product(*(range(b,n) for b in range(1,a))):
        row=(0,)+mids+(n-1,)*(n-a)
        if all(row[i]<=row[i+1] for i in range(n-1)):
            ret.append(row)
    return ret

def axioms(R):
    n=len(R); t=n-1
    for a,b,c in product(range(n), repeat=3):
        # Holliday's P1--P5 literally.
        if a==t and R[a][b]>b:return False
        if min(a,b)>R[a][b]:return False
        if R[a][b]>R[a][min(a,b)]:return False
        if R[a][min(b,c)]>R[a][b]:return False
        if R[a][R[min(a,b)][c]]>R[min(a,b)][c]:return False
    for a in range(n):
        if R[a][a]!=t:return False
        if min(a,R[a][0])!=0:return False
        if a>R[R[a][0]][0]:return False
    return True

def congruences(R):
    n=len(R)
    out=[]
    for cuts in range(1<<(n-1)):
        block=[0]
        for j in range(n-1):block.append(block[-1]+((cuts>>j)&1))
        seen={};ok=True
        for a,b in product(range(n), repeat=2):
            pair=(block[a],block[b]); val=block[R[a][b]]
            if pair in seen and seen[pair]!=val:ok=False;break
            seen[pair]=val
        if ok:out.append(cuts)
    return out

def is_si(congs,n):
    identity=(1<<(n-1))-1
    intersection_cuts=0
    for x in congs:
        if x!=identity:intersection_cuts|=x
    return intersection_cuts!=identity

def family(n):
    t=n-1
    R=[]
    for a in range(n):
        if a==0:R.append((t,)*n)
        elif a==2:R.append(tuple(0 if b==0 else t for b in range(n)))
        else:R.append(tuple(b if b<a else t for b in range(n)))
    return R

def single_merge(n,i):
    return ((1<<(n-1))-1) ^ (1<<i)

def check():
    expected={(2):(1,1),(3):(1,1),(4):(2,2),(5):(6,4)}
    for n,(all_count,si_count) in expected.items():
        found=[]
        for R in product(*(candidate_rows(n,a) for a in range(n))):
            if axioms(R):
                C=congruences(R)
                found.append((R,C,is_si(C,n)))
        assert len(found)==all_count,(n,len(found),all_count)
        assert sum(x[2] for x in found)==si_count,(n,sum(x[2] for x in found))
        if n==5:
            assert sum(not x[2] for x in found)==2
            for R,C,si in found:
                assert (not si)==(list(R)[2][1]==4 and list(R)[3][1] in (1,4) and list(R)[3][2] in (2,4) and (list(R)[3][1],list(R)[3][2]) in ((1,2),(4,4)))
        print('n',n,'F_expansions',len(found),'subdirectly_irreducible',sum(x[2] for x in found))
    for n in range(5,13):
        R=family(n); assert axioms(R),(n,'axioms')
        C=congruences(R)
        assert single_merge(n,1) in C,(n,'edge1')
        assert single_merge(n,n-2) in C,(n,'topedge')
        assert not is_si(C,n),(n,'SI')
    print('INFINITE_FAMILY_FINITE_TESTS_OK; ALL_CHECKS_OK')
if __name__=='__main__':check()
