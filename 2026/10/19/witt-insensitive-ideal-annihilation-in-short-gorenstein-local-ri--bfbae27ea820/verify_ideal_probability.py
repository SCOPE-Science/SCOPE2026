"""Standalone finite-field checks for ideal products in short local Gorenstein rings.

Ring multiplication is given by a residue-field unit and a maximal ideal
with basis e_1,...,e_d,w, where e_i e_j=B_ij w and w*m=0.
The script enumerates row-reduced subspaces of m, filters ring ideals using
multiplication (not the quotient-subspace ideal classification), and checks
ordered ideal-product counts directly.
"""
from itertools import combinations, product
from math import comb

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        p=0
        while b:
            if b&1:p^=a
            b>>=1
            a<<=1
            if a&4:a^=7
        return p
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q

def subspaces(dim,F):
    for k in range(dim+1):
        for pivs in combinations(range(dim),k):
            options=[(i,j) for i,p in enumerate(pivs) for j in range(p+1,dim) if j not in pivs]
            for vals in product(range(F.q),repeat=len(options)):
                rows=[[0]*dim for _ in range(k)]
                for i,p in enumerate(pivs):rows[i][p]=1
                for (i,j),v in zip(options,vals):rows[i][j]=v
                yield tuple(tuple(row) for row in rows),pivs

def contained(v,basis,piv,F):
    v=list(v)
    for row,p in zip(basis,piv):
        c=v[p]
        if c:
            for j in range(len(v)):
                v[j]=F.add(v[j],F.neg(F.mul(c,row[j])))
    return all(x==0 for x in v)

def bilinear(a,b,B,F):
    val=0
    for i in range(len(B)):
        for j in range(len(B)):
            val=F.add(val,F.mul(F.mul(a[i],B[i][j]),b[j]))
    return val

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=1; den=1
    for i in range(k):
        num*=q**(n-i)-1;den*=q**(i+1)-1
    assert num%den==0
    return num//den

def run(q,B,name):
    F=Field(q); d=len(B); m_dim=d+1
    all_ideals=[]
    for basis,pivs in subspaces(m_dim,F):
        is_ideal=True
        for a in basis:
            for i in range(d):
                scalar=0
                for j in range(d):scalar=F.add(scalar,F.mul(B[i][j],a[j]))
                v=[0]*d+[scalar]
                if not contained(v,basis,pivs,F):
                    is_ideal=False;break
            if not is_ideal:break
        if is_ideal:all_ideals.append((basis,pivs))
    # Distinct R counted separately (the only ideal outside maximal ideal).
    G=sum(gaussian(d,i,q) for i in range(d+1))
    J=G+2
    assert len(all_ideals)+1==J,(name,len(all_ideals)+1,J)
    O=sum(gaussian(d,a,q)*sum(gaussian(d-a,b,q) for b in range(d-a+1)) for a in range(d+1))
    z2=(2*J-1+O)
    # product of maximal ideals is zero iff each basis-basis product vanishes.
    z2_direct=0
    for ib,ip in all_ideals:
        for jb,jp in all_ideals:
            if all(bilinear(a,b,B,F)==0 for a in ib for b in jb):
                z2_direct+=1
    # 0 * R and R * 0 already not included in the restricted count.
    z2_direct+=2
    assert z2_direct==z2,(name,z2_direct,z2)
    A=G*G-O
    # Build the complete multiplication table of ideals from actual basis
    # products, then propagate product states for k=2,3,4.
    zeroindex=next(i for i,(basis,pivs) in enumerate(all_ideals) if len(basis)==0)
    socleindex=next(i for i,(basis,pivs) in enumerate(all_ideals)
                    if len(basis)==1 and all(x==0 for x in basis[0][:-1]) and basis[0][-1])
    ringindex=len(all_ideals)
    multip=[[ringindex]*J for _ in range(J)]
    for i,(ib,ip) in enumerate(all_ideals):
        for j,(jb,jp) in enumerate(all_ideals):
            multip[i][j]=socleindex if any(bilinear(a,b,B,F) for a in ib for b in jb) else zeroindex
    for i in range(J):
        multip[i][ringindex]=i
        multip[ringindex][i]=i
    nonzero_pairs=sum(not all(bilinear(a,b,B,F)==0 for a in ib for b in jb)
                      for ib,ip in all_ideals for jb,jp in all_ideals)
    assert nonzero_pairs==A
    states=[0]*J;states[ringindex]=1
    for k in (1,2,3,4):
        newstates=[0]*J
        for i,ct in enumerate(states):
            for j in range(J):newstates[multip[i][j]]+=ct
        states=newstates
        expected_nonzero=1+k*G+comb(k,2)*(G*G-O)
        actual_nonzero=sum(states)-states[zeroindex]
        assert sum(states)==J**k and actual_nonzero==expected_nonzero,(name,k,actual_nonzero,expected_nonzero)
    sq0=sum(all(bilinear(a,b,B,F)==0 for a in ib for b in ib) for ib,ip in all_ideals)
    print(name, 'q',q,'d',d,'ideals',J,'orth_pairs',O,'zero_pairs',z2,'squares_zero_in_m',sq0, 'Z3_numerator',J**3-(1+3*G+3*(G*G-O)))
    return (J,O,z2,sq0)



def test_mixed_characteristic():
    """Exhaust the actual ideals of a characteristic-four Gorenstein ring.

    R=(Z/4)[x,y]/(2x,2y,xy,x*x-2,y*y-2), represented by
    (a mod 4,b mod 2,c mod 2). No residue-field splitting is used.
    """
    elts=list(product(range(4),range(2),range(2)))
    zero=(0,0,0)
    one=(1,0,0)
    def add(a,b):return ((a[0]+b[0])%4,(a[1]+b[1])%2,(a[2]+b[2])%2)
    def mul(a,b):
        return ((a[0]*b[0]+2*(a[1]*b[1]+a[2]*b[2]))%4,
                ((a[0]%2)*b[1]+(b[0]%2)*a[1])%2,
                ((a[0]%2)*b[2]+(b[0]%2)*a[2])%2)
    for a in elts:
        for b in elts:
            for c in elts:
                assert mul(mul(a,b),c)==mul(a,mul(b,c))
                assert mul(add(a,b),c)==add(mul(a,c),mul(b,c))
    def subgroup_generated(H,g):
        T=set(H)|{g}
        while True:
            new=T|{add(a,b) for a in T for b in T}
            if len(new)==len(T):return frozenset(new)
            T=new
    seen={frozenset([zero])};todo=list(seen)
    while todo:
        H=todo.pop()
        for g in elts:
            if g in H:continue
            K=subgroup_generated(H,g)
            if K not in seen:seen.add(K);todo.append(K)
    ideals=[H for H in seen if all(mul(r,i) in H for r in elts for i in H)]
    assert len(ideals)==7,len(ideals)
    pair_zero=sum(all(mul(a,b)==zero for a in I for b in J) for I in ideals for J in ideals)
    assert pair_zero==25,pair_zero
    # Explicit products of ideals, computed as additive subgroups.
    idx={H:i for i,H in enumerate(ideals)}
    prod_idx=[]
    for I in ideals:
        row=[]
        for J in ideals:
            K=frozenset([zero])
            for a in I:
                for b in J:K=subgroup_generated(K,mul(a,b))
            assert K in idx
            row.append(idx[K])
        prod_idx.append(row)
    jone=idx[next(I for I in ideals if one in I)]
    jzero=idx[frozenset([zero])]
    states=[0]*len(ideals);states[jone]=1
    for k in (1,2,3,4):
        newstates=[0]*len(ideals)
        for i,cnt in enumerate(states):
            for j in range(len(ideals)):
                newstates[prod_idx[i][j]]+=cnt
        states=newstates
        G=5;O=12
        expected_nonzero=1+k*G+comb(k,2)*(G*G-O)
        assert sum(states)-states[jzero]==expected_nonzero,(k,states)
    print('mixed_characteristic_Z4_quotient','ideals',len(ideals),'zero_pairs',pair_zero)

if __name__=='__main__':
    results=[]
    results.append(run(2,[[1]],'chain_q2_d1'))
    results.append(run(3,[[1]],'chain_q3_d1'))
    results.append(run(2,[[1,0],[0,1]],'binary_diagonal_d2'))
    results.append(run(2,[[0,1],[1,0]],'binary_alternating_d2'))
    results.append(run(3,[[1,0],[0,1]],'ternary_anisotropic_d2'))
    results.append(run(3,[[1,0],[0,2]],'ternary_split_d2'))
    results.append(run(4,[[0,1],[1,0]],'quaternary_alternating_d2'))
    results.append(run(5,[[1,0],[0,1]],'quinary_binary_d2'))
    results.append(run(2,[[1,0,0],[0,1,0],[0,0,1]],'binary_d3'))
    results.append(run(3,[[1,0,0],[0,1,0],[0,0,1]],'ternary_d3'))
    results.append(run(2,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],'binary_d4'))
    results.append(run(2,[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]],'binary_alternating_d4'))
    assert results[4][:3]==results[5][:3]
    assert results[4][3]!=results[5][3]
    test_mixed_characteristic()
    print('VERIFY_OK',len(results),'split finite local algebra configurations plus 1 mixed-characteristic example')
