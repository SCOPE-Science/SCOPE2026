"""Exact audit of determinant polynomials for a weighted theta graphical zonotope.
Python 3 standard library; no floating-point arithmetic or external files.
"""
from itertools import combinations, permutations
from collections import defaultdict
from fractions import Fraction

# Columns: 03,04,05,12,13,15,24. Rows: vertices 0,1,2,3,4.
A = ((1,1,1,0,0,0,0),
     (0,0,0,1,1,1,0),
     (0,0,0,-1,0,0,1),
     (-1,0,0,0,-1,0,0),
     (0,-1,0,0,0,0,-1))
X=(1,-1,0,0,0)
Y=(0,0,1,-1,1)
# a on 03 and 13, b on 05 and 15, c on 04,12,24.
VARIABLE=(0,2,1,2,0,1,2)

def det(matrix):
    n=len(matrix)
    assert all(len(row)==n for row in matrix)
    # Exact integer Leibniz determinant, <= 120 terms per 5x5 minor.
    total=0
    for perm in permutations(range(n)):
        t=1
        for i in range(n): t *= matrix[i][perm[i]]
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        total += (-1 if inversions%2 else 1)*t
    return total

def coefficients(extra):
    dim=5
    needed=dim-len(extra)
    output=defaultdict(int)
    multiplicities=defaultdict(int)
    for indices in combinations(range(7),needed):
        columns=tuple(extra)+tuple(tuple(A[row][idx] for row in range(5)) for idx in indices)
        matrix=tuple(tuple(col[row] for col in columns) for row in range(5))
        d=abs(det(matrix))
        multiplicities[d]+=1
        powers=tuple(sum(VARIABLE[j]==k for j in indices) for k in range(3))
        output[powers]+=d
    return {k:v for k,v in sorted(output.items()) if v},{k:v for k,v in sorted(multiplicities.items())}

EXPECTED=(
    {(1,1,3):4,(1,2,2):6,(2,1,2):6},
    {(1,1,2):12},
    {(0,1,3):2,(0,2,2):3,(1,0,3):2,(1,1,2):10,(1,2,1):8,(2,0,2):3,(2,1,1):8},
    {(0,1,2):6,(1,0,2):6,(1,1,1):16},
)
# We intentionally compute and compare *every coefficient*, not only samples.
if __name__=='__main__':
    all_coeffs=[]
    for label,extras in [('V',()),('P',(X,)),('Q',(Y,)),('W',(X,Y))]:
        coeff,count=coefficients(extras)
        print(label,'coefficients:',coeff,'determinant counts:',count)
        all_coeffs.append(coeff)
    assert tuple(all_coeffs)==EXPECTED, ('polynomial mismatch',all_coeffs,EXPECTED)
    assert [sum(c.values()) for c in all_coeffs]==[16,12,36,28]
    # Check all coefficient identities as exact symbolic polynomial multiplications.
    def mul(left,right):
        out=defaultdict(int)
        for mon,coef in left.items():
            for mon2,coef2 in right.items():
                out[tuple(mon[i]+mon2[i] for i in range(3))] += coef*coef2
        return {k:v for k,v in out.items() if v}
    def minus(left,right):
        out=defaultdict(int,left)
        for k,v in right.items():out[k]-=v
        return {k:v for k,v in out.items() if v}
    # V*W - P*Q = 16*a^2*b^2*c^4.
    assert minus(mul(all_coeffs[0],all_coeffs[3]),mul(all_coeffs[1],all_coeffs[2]))=={(2,2,4):16}
    # At a=b=1,c=2: V=80, P=48, Q=128, W=80.
    def evaluate(poly,a,b,c):return sum(v*a**i*b**j*c**k for (i,j,k),v in poly.items())
    for triple in [(1,1,1),(1,1,2),(1,2,3),(3,7,2),(1,1,10)]:
        a,b,c=triple
        v,p,q,w=[evaluate(z,a,b,c) for z in all_coeffs]
        assert Fraction(v*w,p*q)==1+Fraction(4*a*b*c,3*(8*a*b*(a+b)+3*c*(a+b)**2+4*a*b*c+2*c*c*(a+b)))
        print(triple,'ratio=',Fraction(v*w,p*q))
    assert Fraction(evaluate(all_coeffs[0],1,1,2)*evaluate(all_coeffs[3],1,1,2),evaluate(all_coeffs[1],1,1,2)*evaluate(all_coeffs[2],1,1,2)) == Fraction(25,24)
    print('PASS: four full determinant polynomials, exact cancellation, source specialization, and rational samples')
