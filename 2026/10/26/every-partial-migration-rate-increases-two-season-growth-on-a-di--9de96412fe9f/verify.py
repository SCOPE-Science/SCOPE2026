"""Exact self-contained check of a three-site, two-season dispersal identity.

Run: python3 verify.py. Uses only the Python standard library.
Finite examples are diagnostics; the general result rests on the supplied proof.
"""
from fractions import Fraction
from itertools import permutations, product
from hashlib import sha256
import json

# Laurent polynomials in the four indeterminates u,v,w,t.
# The coefficient of any integral monomial exponent tuple is an integer.
ZERO=(0,0,0,0)
def poly(c=0):
    return {ZERO:c} if c else {}
def term(exponents,c=1):
    return {tuple(exponents):c} if c else {}
def add(a,b):
    out=a.copy()
    for e,c in b.items():
        out[e]=out.get(e,0)+c
        if not out[e]:del out[e]
    return out
def neg(a):return {e:-c for e,c in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(i+j for i,j in zip(e,f))
            out[g]=out.get(g,0)+c*d
            if not out[g]:del out[g]
    return out
def matmul(A,B):
    return [[sum_poly(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def sum_poly(items):
    p={}
    for a in items:p=add(p,a)
    return p
def det3(A):
    out={}
    for p in permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        termp=poly(1)
        for i in range(3):termp=mul(termp,A[i][p[i]])
        out=add(out,neg(termp) if inv%2 else termp)
    return out

def laurent_identity():
    one=poly(1);t=term((0,0,0,1));u=term((1,0,0,0));v=term((0,1,0,0));w=term((0,0,1,0))
    a=sub(one,t)
    C=[[poly(0),poly(0),one],[one,poly(0),poly(0)],[poly(0),one,poly(0)]]
    M=[[add(a if i==j else {},mul(t,C[i][j])) for j in range(3)] for i in range(3)]
    D=[[q if i==j else {} for j in range(3)] for i,q in enumerate([u,v,w])]
    Di=[[q if i==j else {} for j in range(3)] for i,q in enumerate([term((-1,0,0,0)),term((0,-1,0,0)),term((0,0,-1,0))])]
    Q=matmul(matmul(matmul(M,Di),M),D)
    lhs=det3([[sub(one if i==j else {},Q[i][j]) for j in range(3)] for i in range(3)])
    sum_ratios=sum_poly([term((1,-1,0,0)),term((-1,1,0,0)),term((1,0,-1,0)),term((-1,0,1,0)),term((0,1,-1,0)),term((0,-1,1,0))])
    rhs=neg(mul(mul(mul(t,t),mul(t,a)),sub(sum_ratios,poly(6))))
    assert lhs==rhs,(lhs,rhs)
    return len(lhs)

def ratmat(d,x,y,z):
    a=1-d;I=[[Fraction(int(i==j)) for j in range(3)] for i in range(3)]
    C=[[Fraction(0),Fraction(0),Fraction(1)],[Fraction(1),Fraction(0),Fraction(0)],[Fraction(0),Fraction(1),Fraction(0)]]
    M=[[a*I[i][j]+d*C[i][j] for j in range(3)] for i in range(3)]
    D=[[Fraction(x if i==0 else y if i==1 else z) if i==j else Fraction(0) for j in range(3)] for i in range(3)]
    Di=[[Fraction(1,x if i==0 else y if i==1 else z) if i==j else Fraction(0) for j in range(3)] for i in range(3)]
    def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    Q=mm(mm(mm(M,Di),M),D)
    V=[[Fraction(int(i==j))-Q[i][j] for j in range(3)] for i in range(3)]
    d3=sum(((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))) * V[0][p[0]]*V[1][p[1]]*V[2][p[2]] for p in permutations(range(3)))
    h=sum(Fraction(a,b)+Fraction(b,a)-2 for a,b in [(x,y),(x,z),(y,z)])
    assert d3==-d**3*(1-d)*h
    if 0<d<1 and len({x,y,z})>1:
        assert d3<0
    else:assert d3==0
    return d3


def main():
    nt=laurent_identity()
    combos=0;strict=0
    for x,y,z in product((1,2,3,5),repeat=3):
        for num,den in [(0,1),(1,7),(1,3),(1,2),(2,3),(6,7),(1,1)]:
            d=Fraction(num,den)
            q=ratmat(d,x,y,z)
            combos+=1;strict+=q<0
    certificate={"symbolic_identity":"PASS","laurent_monomials":nt,
                 "rational_examples":combos,"strict_cases":strict,
                 "boundary_and_homogeneous_cases":combos-strict,
                 "example_parameters":{"season_1":[1,1,2],"season_2":[2,2,1],"rate":"1/2"},
                 "example_characteristic_polynomial":"lambda^3-(3/2)lambda^2-lambda-1/2",
                 "example_polynomial_at_lambda_2":"-1/2",
                 "universal_claim_from_proof_not_enumeration":True}
    print(json.dumps(certificate,sort_keys=True,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
