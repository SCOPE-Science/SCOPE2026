"""Standalone finite checks for the random evolution-algebra rigidity theorem.
Uses standard Python only; treats finite checks as illustrations, not proof.
"""
from itertools import product, permutations
from math import prod
from random import Random


def rank2(rows,n):
    b={}
    for x in rows:
        for i in range(n-1,-1,-1):
            if not ((x>>i)&1):continue
            if i in b:x^=b[i]
            else:
                b[i]=x;break
    return len(b)


def natural_change(M,P,n):
    for i in range(n):
        for j in range(i+1,n):
            z=P[i]&P[j]
            if z:
                res=0
                for k in range(n):
                    if z>>k&1: res^=M[k]
                if res:return False
    return True


def monomial(P):
    return all(x.bit_count()==1 for x in P) and len(set(P))==len(P)


def two_li(M):
    return all(x and M.count(x)==1 for x in M)


def graph_props(M,n):
    if not any((M[i]>>i)&1 for i in range(n)):
        return False
    for m in range(1,(1<<n)-1):
        if not any(M[i]&(~m&((1<<n)-1)) for i in range(n) if m>>i&1):
            return False
    for p in permutations(range(n)):
        if all(p[i]==i for i in range(n)):continue
        if all(((M[i]>>j)&1)==((M[p[i]]>>p[j])&1) for i in range(n) for j in range(n)):
            return False
    return True


def exact_2li_count(q,n):
    return prod(q**n-1-j*(q-1) for j in range(n))


def check_odd_field_two_dimensions():
    for q in (3,5):
        pairs=list(product(range(q),repeat=2))
        GL=[(u,v) for u in pairs for v in pairs if (u[0]*v[1]-u[1]*v[0])%q]
        two_li_total=0; unique_total=0
        for m1,m2 in product(pairs, repeat=2):
            # Avoid relying on a rank-one test when vectors are dependent:
            independent=bool((m1[0]*m2[1]-m1[1]*m2[0])%q)
            two_li_total+=int(independent)
            nonmon=False
            for u,v in GL:
                pair=[(u[0]*v[0])%q,(u[1]*v[1])%q]
                xy=[(pair[0]*m1[j]+pair[1]*m2[j])%q for j in range(2)]
                if xy==[0,0] and (u[0]*u[1]!=0 or v[0]*v[1]!=0):
                    nonmon=True;break
            unique_total+=int(not nonmon)
        assert two_li_total==exact_2li_count(q,2)
        assert unique_total>=two_li_total
        if q>3:assert unique_total==two_li_total
        print('ODD_FIELD_DIM_TWO',q,'two_LI',two_li_total,'unique',unique_total,'out_of',q**4)


def check_small():
    for n in (2,3):
        allrows=list(product(range(1<<n),repeat=n))
        count=0;count_by_formula=0
        ps=[P for P in allrows if rank2(P,n)==n]
        for M in allrows:
            if two_li(M):
                count+=1
                for P in ps:
                    if natural_change(M,P,n) and not monomial(P):
                        raise AssertionError(('2LI nonmonomial',n,M,P))
        count_by_formula=exact_2li_count(2,n)
        assert count==count_by_formula,(n,count,count_by_formula)
        print('2LI_EXACT',n,count,'/',len(allrows),'NATURAL_CHANGES_CHECKED',len(ps))
    return True


def find_witness():
    R=Random(10222026)
    for n in (5,6,7):
        for _ in range(200000):
            M=[R.randrange(1<<n) for _ in range(n)]
            if rank2(M,n)==n or not two_li(M):continue
            if graph_props(M,n):
                print('SINGULAR_RIGID_CRITERION_WITNESS',n, 'rank',rank2(M,n),'rows',M)
                return M
    raise AssertionError('no witness found in bounded reproducible search')

if __name__=='__main__':
    check_small()
    check_odd_field_two_dimensions()
    find_witness()
    print('VERIFY_OK')
