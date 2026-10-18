"""Self-contained exact finite-field check of nonsplit almost-abelian Lie automorphism distributions."""
from itertools import product
from collections import Counter

class FiniteField:
    def __init__(self, q):
        self.q = q
        assert q in (2, 3, 4, 5, 7, 11)
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a+b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def sub(self, a, b):
        return self.add(a,self.neg(b))
    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        result = 0
        for _ in range(2):
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # quotient by x^2+x+1
        return result
    def inverse(self, a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:
                return b
        raise AssertionError('non-field operation')
    def det2(self, M):
        return self.sub(self.mul(M[0][0],M[1][1]),self.mul(M[0][1],M[1][0]))

def rank(M, F):
    a=[list(row) for row in M]; m=len(a);n=len(a[0]); r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=F.inverse(a[r][j]);a[r]=[F.mul(x,inv) for x in a[r]]
        for k in range(m):
            if k!=r and a[k][j]:
                t=a[k][j]
                a[k]=[F.sub(a[k][l],F.mul(t,a[r][l])) for l in range(n)]
        r+=1
        if r==m:break
    return r

def matrix_product(A,B,F):
    return [[F.add(F.mul(A[i][0],B[0][j]),F.mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]

def run_case(q, trace_kind):
    F=FiniteField(q); E=range(q)
    # Irreducible X^2 - tX - d: no root in F_q.
    cases=[]
    for t,d in product(E,E):
        if (t==0)!=(trace_kind=='zero'):continue
        if all(F.sub(F.sub(F.mul(x,x),F.mul(t,x)),d) != 0 for x in E):
            cases.append((t,d))
    assert cases, (q,trace_kind)
    t,d=cases[0]
    A=[[0,d],[1,t]]
    assert F.det2(A)
    count=Counter(); aut_ct=0; valid_T=Counter()
    for entries in product(E,repeat=4):
        T=[list(entries[:2]),list(entries[2:])]
        if F.det2(T)==0:continue
        TA=matrix_product(T,A,F);AT=matrix_product(A,T,F)
        for c in range(1,q):
            if TA!=[[F.mul(c,x) for x in row] for row in AT]:continue
            valid_T[c]+=1
            for w in product(E,repeat=2):
                M=[[F.sub(c,1),0,0], [w[0],F.sub(T[0][0],1),T[0][1]], [w[1],T[1][0],F.sub(T[1][1],1)]]
                count[3-rank(M,F)] +=1
                aut_ct+=1
    expected=(
       {0:0,1:q*q*(q*q-2),2:q*q-1,3:1}
       if t!=0 else
       {0:q*q*(q+1)*(q-2),1:q*q*(q*q+q-1),2:q*q-1,3:1}
    )
    assert all(count[i]==expected[i] for i in range(4)),(q,trace_kind,t,d,count,expected)
    assert aut_ct==q*q*(q*q-1)*(2 if t==0 else 1)
    assert valid_T[1]==q*q-1
    if t==0:assert valid_T[F.neg(1)]==q*q-1
    print(f'q={q:2} {trace_kind:7} companion=(tr={t},d={d}) automorphisms={aut_ct:6} fixedspace_counts={[count[i] for i in range(4)]}')

if __name__=='__main__':
    num=0
    for q in (2,3,4,5,7,11):
        for kind in (('nonzero',) if q in (2,4) else ('zero','nonzero')):
            run_case(q,kind); num+=1
    print('VERIFY_OK: exhaustive automorphisms and fixed-vector nullities for',num,'nonsplit finite-field Lie algebra configurations')
