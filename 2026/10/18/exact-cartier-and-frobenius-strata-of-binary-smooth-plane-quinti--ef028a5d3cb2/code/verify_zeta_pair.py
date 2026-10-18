"""Independent exact checks for two genus-six plane quintics over F_2.

Requires only Python 3 standard library; verifies geometric smoothness by
Buchberger's algorithm in three affine charts and all point counts to degree 6.
"""
from itertools import chain
from functools import reduce

A = {(0,0,5),(0,3,2),(0,5,0),(1,2,2),(1,4,0),(2,0,3),(2,1,2),(2,2,1),(5,0,0)}
B = {(0,0,5),(0,1,4),(0,3,2),(0,4,1),(0,5,0),(1,3,1),(1,4,0),(2,0,3),(2,1,2),(2,2,1),(5,0,0)}
I=[(i,j,5-i-j) for i in range(1,4) for j in range(1,5-i) if 5-i-j>=1]
mods={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def gf_mul(a,b,mod,n):
    r=0
    while b:
        if b&1:r^=a
        b>>=1; a<<=1
        if a&(1<<n):a^=mod
    return r

def translate_plane_poly(monomials,chart):
    # Set one variable to one; return sparse polynomial over F_2 in the other two.
    out=set()
    rem=[k for k in range(3) if k!=chart]
    for exponents in monomials:
        term=(exponents[rem[0]],exponents[rem[1]])
        if term in out:out.remove(term)
        else:out.add(term)
    return out

def d(poly,variable):
    return {(a-1,b) for a,b in poly if a%2} if variable==0 else {(a,b-1) for a,b in poly if b%2}

def mulmon(poly,offset):
    a,b=offset
    return {(i+a,j+b) for i,j in poly}

def normal_form(poly,basis):
    poly=set(poly);remainder=set()
    while poly:
        pivot=max(poly)
        for g in basis:
            l=max(g)
            if pivot[0]>=l[0] and pivot[1]>=l[1]:
                poly.symmetric_difference_update(mulmon(g,(pivot[0]-l[0],pivot[1]-l[1])))
                break
        else:
            poly.remove(pivot); remainder.add(pivot)
    return remainder

def ideal_unit(gens):
    G=[set(g) for g in gens if g]
    if not G:return False
    pairs=[(i,j) for i in range(len(G)) for j in range(i)]
    while pairs:
        i,j=pairs.pop()
        a,b=max(G[i]),max(G[j])
        c=(max(a[0],b[0]),max(a[1],b[1]))
        S=mulmon(G[i],(c[0]-a[0],c[1]-a[1]))
        S.symmetric_difference_update(mulmon(G[j],(c[0]-b[0],c[1]-b[1])))
        R=normal_form(S,G)
        if not R:continue
        if R=={(0,0)}:return True
        size=len(G)
        G.append(R)
        pairs.extend((size,k) for k in range(size))
    return any(g=={(0,0)} for g in G)

def matrix_rank(rows):
    basis={}
    for v in rows:
        while v:
            pivot=v.bit_length()-1
            if pivot not in basis:
                basis[pivot]=v;break
            v^=basis[pivot]
    return len(basis)

def matmul(a,b):
    return [reduce(int.__xor__,(b[j] for j in range(6) if a[i]>>j&1),0) for i in range(6)]

def verify(name,monomials):
    for chart in range(3):
        f=translate_plane_poly(monomials,chart)
        assert ideal_unit([f,d(f,0),d(f,1)]),('singular',name,chart)
    H=[]
    for U in I:
        bits=0
        for j,V in enumerate(I):
            m=tuple(2*a-b for a,b in zip(U,V))
            if m in monomials:bits|=1<<j
        H.append(bits)
    a=6-matrix_rank(H);power=H
    for _ in range(5):power=matmul(power,H)
    p=matrix_rank(power)
    counts=[]
    for n in range(1,7):
        q=1<<n;mod=mods[n]
        powers=[[1]*6 for _ in range(q)]
        for e in range(q):
            for k in range(1,6):powers[e][k]=gf_mul(powers[e][k-1],e,mod,n)
        pts=chain(((1,u,v) for u in range(q) for v in range(q)),((0,1,v) for v in range(q)),((0,0,1),))
        num=0
        for X,Y,Z in pts:
            val=0
            for i,j,k in monomials:
                val^=gf_mul(gf_mul(powers[X][i],powers[Y][j],mod,n),powers[Z][k],mod,n)
            num+=(val==0)
        counts.append(num)
    print(f'{name} smooth=YES p_rank={p} a_number={a} point_counts={counts}')
    return counts,a,p

if __name__=='__main__':
    na,aa,pa=verify('A',A);nb,ab,pb=verify('B',B)
    assert na==nb==[0,2,6,14,60,74]
    assert (pa,pb)==(3,3) and (aa,ab)==(3,1)
    S=[2**n+1-na[n-1] for n in range(1,7)]
    coeff=[1]
    for k in range(1,7):
        numerator=-sum(coeff[k-j]*S[j-1] for j in range(1,k+1))
        assert numerator%k==0
        coeff.append(numerator//k)
    L=coeff+[0]*6
    for j in range(6):L[12-j]=2**(6-j)*coeff[j]
    assert L==[1,-3,3,-1,0,6,-16,12,0,-8,48,-96,64]
    print('common_L_coefficients=',L)
    print('Groebner_smoothness_checks=6; extension_counts=12; checks=PASS')
