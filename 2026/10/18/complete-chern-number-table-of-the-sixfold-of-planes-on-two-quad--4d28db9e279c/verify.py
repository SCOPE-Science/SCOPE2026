from itertools import combinations
from fractions import Fraction
from math import prod

# Exponents of (c2,c3,c4,c5,c6,H) for all degree-six monomials.
MONOMIALS = [(0,0,0,0,0,6),(1,0,0,0,0,4),(0,1,0,0,0,3),
 (0,0,1,0,0,2),(0,0,0,1,0,1),(0,0,0,0,1,0),
 (2,0,0,0,0,2),(1,1,0,0,0,1),(3,0,0,0,0,0),
 (1,0,1,0,0,0),(0,2,0,0,0,0)]
EXPECTED = (3904,3072,1664,896,384,256,2880,1728,5248,1792,1088)

def integrate(weights):
    out=[Fraction(0)]*len(MONOMIALS)
    for I in combinations(range(9),3):
        J=[j for j in range(9) if j not in I]
        tangent=[weights[j]-weights[i] for i in I for j in J]
        normal=[-(weights[I[a]]+weights[I[b]]) for a in range(3) for b in range(a,3)]*2
        h=-sum(weights[i] for i in I)
        c=[1]+[0]*6
        for w in tangent:
            c=[c[0]]+[c[k]+w*c[k-1] for k in range(1,7)]
        for w in normal:
            nxt=[c[0]]+[0]*6
            for k in range(1,7):nxt[k]=c[k]-w*nxt[k-1]
            c=nxt
        factor=Fraction(prod(normal),prod(tangent))
        for n,(a,b,c4,d,e,f) in enumerate(MONOMIALS):
            out[n]+=factor*(c[2]**a)*(c[3]**b)*(c[4]**c4)*(c[5]**d)*(c[6]**e)*(h**f)
    return tuple(out)

def independent_degree():
    # Multiply sparse three-variate polynomials, then take coefficient [x^8 y^7 z^6].
    def product(P,Q):
        D={}
        for a,ca in P.items():
            for b,cb in Q.items():
                e=tuple(a[k]+b[k] for k in range(3));D[e]=D.get(e,0)+ca*cb
        return D
    def linear(terms):
        return {(int(i==0),int(i==1),int(i==2)):v for i,v in terms}
    L=[{(1,0,0):1}, {(0,1,0):1}, {(0,0,1):1}]
    add=lambda i,j: {**L[i], **{k:L[i].get(k,0)+v for k,v in L[j].items()}}
    A={(0,0,0):1}
    for i in range(3):
        for j in range(i,3):
            for _ in range(2):A=product(A,add(i,j))
    for _ in range(6):A=product(A,{(1,0,0):1,(0,1,0):1,(0,0,1):1})
    for i,j in [(0,1),(0,2),(1,2)]:A=product(A,{**L[i],**{k:-v for k,v in L[j].items()}})
    return A.get((8,7,6),0)

if __name__=='__main__':
    assert integrate(list(range(1,10)))==EXPECTED
    assert integrate([1,3,7,13,21,31,43,57,73])==EXPECTED
    assert independent_degree()==3904
    print('VERIFY_OK fixed_points=84 anticanonical_volume=3904 euler=256 full_chern_table=11')
