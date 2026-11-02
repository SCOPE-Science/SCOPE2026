"""Independent exact-field enumeration for a quintic value-set identity.

Run: python3 verify.py
Uses only Python standard library and arithmetic in GF(p) and GF(p^2).
The predicted formula is evaluated separately from direct image enumeration.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree, self.q = p, degree, p**degree
        if degree == 2:
            self.d = next(z for z in range(2,p) if pow(z,(p-1)//2,p)==p-1)
        else:
            self.d = None
        q = self.q
        self.add = [[0]*q for _ in range(q)]
        self.mul = [[0]*q for _ in range(q)]
        for x in range(q):
            a,b = x%p,x//p
            for y in range(q):
                c,e = y%p,y//p
                self.add[x][y] = (a+c)%p + p*((b+e)%p)
                if degree==1:
                    self.mul[x][y] = (a*c)%p
                else:
                    self.mul[x][y] = (a*c+self.d*b*e)%p + p*((a*e+b*c)%p)
        self.pow2=[self.mul[x][x] for x in range(q)]
        self.pow3=[self.mul[self.pow2[x]][x] for x in range(q)]
        self.pow4=[self.mul[self.pow2[x]][self.pow2[x]] for x in range(q)]
        self.pow5=[self.mul[self.pow4[x]][x] for x in range(q)]
        sq=set(self.pow2)
        self.nonsq=next(z for z in range(1,q) if z not in sq)
        self.sq=sq

    def chi(self,x):
        return 0 if x==0 else (1 if x in self.sq else -1)

    def scalar(self,a):
        return a%self.p

    def pred(self,B):
        q=self.q
        chi=self.chi
        c5=chi(self.scalar(5))
        c15=chi(self.scalar(-15))
        base=Fraction(19*q,30)+Fraction(1,6)
        if B==0:
            return base-Fraction(c5,30)+Fraction(5+c5-5*c15,30*q)+Fraction(1+5*c15,30*q*q)
        c5B=chi(self.mul[self.scalar(5)][B])
        cm15B=chi(self.mul[self.scalar(-15)][B])
        return base+Fraction(5+c5+5*c5B,30*q)+Fraction(-5+5*c15-5*cm15B,30*q*q)

    def actual_sum(self,B,a=0):
        q=self.q; A=self.add;M=self.mul
        if a==0:
            base=[A[self.pow5[x]][M[B][self.pow3[x]]] for x in range(q)]
        else:
            raise ValueError('use direct_coefficients for nonzero quartic coefficient')
        total=0
        for u in range(q):
            partial=[A[base[x]][M[u][self.pow2[x]]] for x in range(q)]
            for v in range(q):
                total += len({A[partial[x]][M[v][x]] for x in range(q)})
        return total

    def direct_coefficients(self,a,b):
        q=self.q; A=self.add;M=self.mul
        base=[A[self.pow5[x]][A[M[a][self.pow4[x]]][M[b][self.pow3[x]]]] for x in range(q)]
        total=0
        for u in range(q):
            partial=[A[base[x]][M[u][self.pow2[x]]] for x in range(q)]
            for v in range(q):
                total+=len({A[partial[x]][M[v][x]] for x in range(q)})
        return total

    def depressed_parameter(self,a,b):
        # B=b-(2/5)a^2 in GF(p^k); p>5
        p=self.p; M=self.mul; A=self.add
        scalar=(-2*pow(5,-1,p))%p
        return A[b][M[scalar][M[a][a]]]


def test():
    count=0; evaluations=0
    for p,deg in [(7,1),(11,1),(13,1),(17,1),(19,1),(23,1),(29,1),(31,1),(7,2),(11,2)]:
        f=Field(p,deg)
        cases=list(range(f.q)) if f.q<=49 else [0,1,f.nonsq]
        for B in cases:
            total=f.actual_sum(B)
            expect=f.q*f.q*f.pred(B)
            assert expect.denominator==1 and total==expect, (p,deg,B,total,expect)
            count+=1; evaluations+=f.q**3
        print('PASS', 'field',f.q,'cases',len(cases),'nonsquare',f.nonsq)
    # Test the non-depressed coefficients independently over the full prime field.
    for p in (7,11):
        f=Field(p)
        for a in range(p):
            for b in range(p):
                B=f.depressed_parameter(a,b)
                total=f.direct_coefficients(a,b)
                expect=f.q*f.q*f.pred(B)
                assert total==expect, (p,a,b,total,expect)
                count+=1; evaluations+=f.q**3
        print('PASS all original leading-coefficient pairs over GF(',p,')',sep='')
    # A second, independently structured replay checks the 4- and 5-subset
    # interpolation conditions (no polynomial evaluations in this check).
    subsets_checked=0
    for p in (7,11,13,17):
        f=Field(p)
        n4=[0]*p; n5=[0]*p
        inv2=pow(2,-1,p)
        for seq in combinations(range(p),4):
            s=sum(seq)%p
            z=(sum(t*t for t in seq)+s*s)%p
            B=(-inv2*z)%p
            n4[B]+=1
            subsets_checked+=1
        for seq in combinations(range(p),5):
            subsets_checked+=1
            if sum(seq)%p: continue
            B=(-inv2*sum(t*t for t in seq))%p
            n5[B]+=1
        for B in range(p):
            predicted_total=p**3-p*comb(p,2)+comb(p,3)-n4[B]+n5[B]
            assert predicted_total==p*p*f.pred(B),(p,B,predicted_total)
        print('PASS interpolation subsets',p)
    print('VERIFY_OK configurations=',count,'input_evaluations=',evaluations,'subset_tests=',subsets_checked)

if __name__=='__main__':test()
