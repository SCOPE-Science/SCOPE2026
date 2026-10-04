#!/usr/bin/env python3
from itertools import combinations
from math import comb

PRIMES=(2,3,5,7,101)

def rank_mod(cols, nrows, p):
    rows=[[0]*len(cols) for _ in range(nrows)]
    for j,col in enumerate(cols):
        for i,v in col.items(): rows[i][j]=v%p
    r=0
    n=len(cols)
    for c in range(n):
        pivot=next((i for i in range(r,nrows) if rows[i][c]%p),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][c],-1,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(nrows):
            if i!=r and rows[i][c]%p:
                a=rows[i][c]%p
                rows[i]=[(x-a*y)%p for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==nrows: break
    return r

def add(col, idx, val):
    col[idx]=col.get(idx,0)+val
    if col[idx]==0: del col[idx]

def theta_column(S, triple_index):
    # S is increasing oriented 4-subset of {0,...,m-1}; base edge 0.
    a,b,c,d=S
    if a==0:
        return {triple_index[(b,c,d)]:1}
    # (e_b-e_a)^(e_c-e_a)^(e_d-e_a)
    # = b^c^d - a^c^d + a^b^d - a^b^c in basis e_i-e_0.
    col={}
    for tri,sgn in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
        add(col,triple_index[tri],sgn)
    return col

def boundary5_column(T, four_index):
    # oriented boundary of increasing 5-subset
    col={}
    T=list(T)
    for q in range(5):
        face=tuple(T[:q]+T[q+1:])
        add(col,four_index[face],(-1)**q)
    return col

def matvec(cols, x):
    out={}
    for j,a in x.items():
        if a:
            for i,v in cols[j].items(): add(out,i,a*v)
    return out

def main():
    for m in range(4,11):
        fours=list(combinations(range(m),4))
        fives=list(combinations(range(m),5))
        triples=list(combinations(range(1,m),3))
        ti={t:i for i,t in enumerate(triples)}
        fi={s:i for i,s in enumerate(fours)}
        Tcols=[theta_column(s,ti) for s in fours]
        Rcols=[boundary5_column(s,fi) for s in fives]

        # T * boundary = 0 exactly over Z.
        for rc in Rcols:
            assert matvec(Tcols,rc)=={}

        # Columns containing edge 0 are exactly the standard basis of Λ^3 A.
        base=[s for s in fours if 0 in s]
        assert len(base)==comb(m-1,3)
        for s in base:
            col=Tcols[fi[s]]
            assert col=={ti[s[1:]]:1}

        # Every non-base theta column obeys the explicit five-term reduction.
        for s in fours:
            if 0 in s: continue
            five=(0,)+s
            relation=boundary5_column(five,fi)
            # coefficient of s in boundary is +1 (remove 0); hence T(s) is
            # minus the combination of the four base-containing faces.
            assert relation[fi[s]]==1
            reduced={}
            for j,a in relation.items():
                if j!=fi[s]: add(reduced,j,-a)
            assert matvec(Tcols,{fi[s]:1})==matvec(Tcols,reduced)

        expected=comb(m-1,3)
        ker_expected=len(fours)-expected
        assert ker_expected==comb(m-1,4)
        for p in PRIMES:
            rt=rank_mod(Tcols,len(triples),p)
            rr=rank_mod(Rcols,len(fours),p)
            assert rt==expected,(m,p,rt,expected)
            assert rr==ker_expected,(m,p,rr,ker_expected)
        print(f"m={m} theta={len(fours)} basis={expected} relations_rank={ker_expected}")
    print("VERIFY_OK")

if __name__=='__main__':
    main()
