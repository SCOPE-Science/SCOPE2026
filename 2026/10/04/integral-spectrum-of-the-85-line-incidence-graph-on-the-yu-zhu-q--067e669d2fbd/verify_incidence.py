#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations, permutations
from collections import Counter

# Exact arithmetic in Q(a,b,i), a^4=2, b^4=3, i^2=-1.
# Elements are sparse dictionaries keyed by (a_exp,b_exp,i_exp), with
# 0<=a_exp,b_exp<4 and 0<=i_exp<2.
class E:
    __slots__=('d',)
    def __init__(self, d=None):
        self.d={k:Fraction(v) for k,v in (d or {}).items() if v}
    @staticmethod
    def q(v): return E({(0,0,0):Fraction(v)})
    @staticmethod
    def mon(pa=0,pb=0,pi=0,c=1):
        qa,pa=divmod(pa,4); qb,pb=divmod(pb,4); qi,pi=divmod(pi,2)
        c=Fraction(c)*(2**qa)*(3**qb)*((-1)**qi)
        return E({(pa,pb,pi):c}) if c else E()
    def __add__(self,o):
        if not isinstance(o,E): o=E.q(o)
        d=self.d.copy()
        for k,v in o.d.items():
            d[k]=d.get(k,Fraction(0))+v
            if not d[k]: del d[k]
        return E(d)
    __radd__=__add__
    def __neg__(self): return E({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return E.q(o)-self
    def __mul__(self,o):
        if not isinstance(o,E): o=E.q(o)
        out={}
        for (pa,pb,pi),x in self.d.items():
            for (qa,qb,qi),y in o.d.items():
                aa=pa+qa; bb=pb+qb; ii=pi+qi
                ca,aa=divmod(aa,4); cb,bb=divmod(bb,4); ci,ii=divmod(ii,2)
                z=x*y*(2**ca)*(3**cb)*((-1)**ci)
                k=(aa,bb,ii); out[k]=out.get(k,Fraction(0))+z
        return E(out)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        out=E.q(1); x=self
        while n:
            if n&1: out=out*x
            x=x*x; n//=2
        return out
    def __eq__(self,o):
        if not isinstance(o,E): o=E.q(o)
        return self.d==o.d
    def iszero(self): return not self.d

ONE=E.q(1); ZERO=E(); I=E.mon(pi=1); a=E.mon(pa=1); b=E.mon(pb=1)
sqrt3=b*b
q12=(a*a)*b
q18=a*(b*b)
q6=a*b

def ipow(k): return I**(k%4)

def addline(lines,n,r1,r2):
    assert n not in lines
    lines[n]=[r1,r2]

def build_lines():
    L={}
    addline(L,1,[ZERO,ZERO,ONE,ZERO],[ZERO,ZERO,ZERO,ONE])
    for j1,j2,j3 in product(range(2),repeat=3):
        n=2+4*j1+2*j2+j3
        r1=[ZERO,ZERO,ZERO,ZERO]; r1[3-j1]=ONE
        c=((-1)**(j1+j3))*ipow(j2)*q12
        r2=[sqrt3-((-1)**(j1+j2)), -c, ZERO, ZERO]
        addline(L,n,r1,r2)
    for j1,j2 in product(range(2),repeat=2):
        n=10+2*j2+j1
        c=((-1)**j1)*I*((I*sqrt3)**j2)
        addline(L,n,[ZERO,ZERO,ONE,E.q(2)],[ONE,-c,ZERO,ZERO])
    for j1,j3 in product(range(2),repeat=2):
        n=14+2*j1+j3
        r1=[ZERO,ZERO,-(ONE-I*sqrt3),E.q(4)]
        A=q12+((-1)**j3)*(ONE-I)
        B=((-1)**j1)*(((-1)**j3)*q12-(ONE+I)*sqrt3)
        addline(L,n,r1,[A,-B,ZERO,ZERO])
    for j1,j3 in product(range(2),repeat=2):
        n=18+2*j1+j3
        r1=[ZERO,ZERO,-(ONE+I*sqrt3),E.q(4)]
        A=q12-((-1)**(j1+j3))*(ONE+I)
        C=(((-1)**j3)*q12+((-1)**j1)*(ONE-I)*sqrt3)
        addline(L,n,r1,[A,C,ZERO,ZERO])
    for j1,j2,j3 in product(range(2),repeat=3):
      for k in range(4):
        n=22+16*j1+40*j2+4*j3+k
        z=ipow(k+(1-j2)*(1-j3))*(I-ONE)
        r1=[2*q18*((-1)**j1), -2*q18*((-1)**(j2+j3))*I, -z, -2*z]
        C=z*q6*(((-1)**j2)*q12+((-1)**j3)*ipow(1-j2)*(sqrt3-((-1)**j2)))
        r2=[4*((-1)**j1)*(sqrt3+((-1)**j2)),4*ipow(j2)*q12,-C,ZERO]
        addline(L,n,r1,r2)
    for j1,j2,j3 in product(range(2),repeat=3):
      for k in range(4):
        n=30+16*j1+24*j2+4*j3+k
        z=ipow(k+j2*(1-j3))*q6
        r1=[2*((-1)**(j1+j3))*sqrt3,6*((-1)**j2),-z,-2*z]
        A=((-1)**j1)*(((-I)**j2)*q12+((-1)**j3)*(ONE+((-1)**j2)*sqrt3))
        B=((-1)**j3)*((-I)**j2)*q12+3-((-1)**j2)*sqrt3
        C=ipow(k+j2*(3-j3))*q6
        addline(L,n,r1,[A,B,-C,ZERO])
    assert sorted(L)==list(range(1,86))
    return L

PERMS=[]
for p in permutations(range(4)):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    PERMS.append((p,-1 if inv%2 else 1))

def det4(M):
    s=ZERO
    for p,sgn in PERMS:
        t=E.q(sgn)
        for i in range(4): t=t*M[i][p[i]]
        s=s+t
    return s

def build_graph(lines):
    adj=[set() for _ in range(85)]
    for aa,bb in combinations(range(1,86),2):
        if det4(lines[aa]+lines[bb]).iszero():
            adj[aa-1].add(bb-1); adj[bb-1].add(aa-1)
    return adj

def right_mul_A(M,adj):
    n=len(adj); out=[[0]*n for _ in range(n)]
    # (M A)_ij = sum_{k~j} M_ik
    for i,row in enumerate(M):
        o=out[i]
        for j in range(n):
            o[j]=sum(row[k] for k in adj[j])
    return out

def sub_scalar(M,r):
    # Return M*A - r*M is handled outside; helper unused.
    return M

def poly_annihilates(adj,roots):
    n=len(adj)
    B=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for r in roots:
        BA=right_mul_A(B,adj)
        B=[[BA[i][j]-r*B[i][j] for j in range(n)] for i in range(n)]
    return all(x==0 for row in B for x in row)

def traces(adj,kmax):
    n=len(adj)
    P=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    ans=[]
    for k in range(kmax+1):
        ans.append(sum(P[i][i] for i in range(n)))
        P=right_mul_A(P,adj)
    return ans

def main():
    lines=build_lines()
    adj=build_graph(lines)
    deg=[len(x) for x in adj]
    assert set(deg)=={20}
    edges=sum(deg)//2
    assert edges==850
    assert adj[0]==set(range(1,21))

    roots=[20,3,-1,-3,-5,-9]
    mult=[1,46,6,16,10,6]
    assert poly_annihilates(adj,roots)
    tr=traces(adj,5)
    expected=[sum(m*(r**k) for r,m in zip(roots,mult)) for k in range(6)]
    assert tr==expected==[85,0,1700,3180,210644,2821740]

    # Distinct roots + real symmetry imply diagonalizability. The six trace
    # equations form a Vandermonde system, so these multiplicities are unique.
    # Shift by -3 for the line-intersection matrix on a quintic surface.
    shifted=[r-3 for r in roots]
    rank=sum(m for x,m in zip(shifted,mult) if x!=0)
    inertia=(sum(m for x,m in zip(shifted,mult) if x>0),
             sum(m for x,m in zip(shifted,mult) if x<0),
             sum(m for x,m in zip(shifted,mult) if x==0))
    assert rank==39 and inertia==(1,38,46)

    common_adj=Counter(len(adj[i]&adj[j]) for i in range(85) for j in adj[i] if i<j)
    assert common_adj==Counter({3:530,0:320})
    triangles=sum(common_adj.values() and k*v for k,v in common_adj.items())//3
    assert triangles==530

    print('LINES_OK 85')
    print('INCIDENCE_OK vertices=85 degree=20 edges=850')
    print('ADJACENT_COMMON_NEIGHBORS_OK 0:320 3:530 triangles=530')
    print('ANNIHILATING_POLYNOMIAL_OK (x-20)(x-3)(x+1)(x+3)(x+5)(x+9)')
    print('TRACES_OK',','.join(map(str,tr)))
    print('SPECTRUM_OK 20^1,3^46,(-1)^6,(-3)^16,(-5)^10,(-9)^6')
    print('LINE_INTERSECTION_MATRIX_OK rank=39 inertia=1,38,46')
    print('VERIFY_OK')

if __name__=='__main__': main()
