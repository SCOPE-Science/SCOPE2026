"""Exhaustive finite-field checks for the null-filiform Leibniz derivation corank law.

Uses only the Python standard library. Each test enumerates every derivation via its
image of the cyclic generator; numerical tests support, but do not prove, the
arbitrary-field theorem.
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)
        self.m = len(modulus) - 1
        assert self.modulus[-1] == 1
        self.q = p ** self.m
        self.vectors = [self.digits(x) for x in range(self.q)]
        self.addition = [[self.encode([(a+b)%p for a,b in zip(self.vectors[x],self.vectors[y])])
                          for y in range(self.q)] for x in range(self.q)]
        self.multiplication = [[self.multiply_direct(x,y) for y in range(self.q)] for x in range(self.q)]
        self.inverses = [0] * self.q
        for x in range(1,self.q):
            for y in range(1,self.q):
                if self.multiplication[x][y] == 1:
                    self.inverses[x]=y
                    break
            assert self.inverses[x] != 0
        self.negatives = [next(y for y in range(self.q) if self.addition[x][y]==0)
                          for x in range(self.q)]

    def digits(self,x):
        v=[]
        for _ in range(self.m):
            v.append(x%self.p)
            x//=self.p
        return v

    def encode(self,v):
        return sum(a*self.p**i for i,a in enumerate(v))

    def multiply_direct(self,x,y):
        p,m=self.p,self.m
        a,b=self.vectors[x],self.vectors[y]
        v=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):
                v[i+j]=(v[i+j]+a[i]*b[j])%p
        for degree in range(2*m-2,m-1,-1):
            z=v[degree]
            for j in range(m):
                v[degree-m+j]=(v[degree-m+j]-z*self.modulus[j])%p
        return self.encode(v[:m])

    def add(self,a,b):
        return self.addition[a][b]

    def mul(self,a,b):
        return self.multiplication[a][b]

    def scale(self,k,x):
        return self.mul(k%self.p,x)

    def sub(self,a,b):
        return self.add(a,self.negatives[b])


def derivation_matrix(a,F):
    n=len(a)
    M=[[0]*n for _ in range(n)]
    for i in range(n):
        M[i][0]=a[i]
    for j in range(1,n):
        M[j][j]=F.scale(j+1,a[0])
        for i in range(j+1,n):
            M[i][j]=a[i-j]
    return M


def matrix_rank(M,F):
    rows=[r[:] for r in M]
    n=len(rows)
    pivot=0
    for j in range(n):
        r=next((i for i in range(pivot,n) if rows[i][j]),None)
        if r is None:
            continue
        rows[pivot],rows[r]=rows[r],rows[pivot]
        scale=F.inverses[rows[pivot][j]]
        rows[pivot]=[F.mul(scale,x) for x in rows[pivot]]
        for i in range(pivot+1,n):
            a=rows[i][j]
            if a:
                rows[i]=[F.sub(x,F.mul(a,y)) for x,y in zip(rows[i],rows[pivot])]
        pivot+=1
    return pivot


def predicted_corank_counts(n,q,p):
    z=n//p
    counts=Counter()
    counts[n]=1
    for nu in range(1,n):
        counts[nu]+=(q-1)*q**(n-nu-1)
    if z==0:
        counts[0]+=(q-1)*q**(n-1)
    else:
        for nu in range(1,z):
            counts[nu]+=(q-1)**2*q**(n-nu-1)
        counts[z]+=(q-1)*q**(n-z)
    assert sum(counts.values())==q**n
    return counts


def bracket_basis(i,j,n):
    # Right-Leibniz convention: [e_i,e_1]=e_(i+1) for i<n.
    return i+1 if j==0 and i<n-1 else None


def satisfies_derivation(M,F):
    n=len(M)
    for i in range(n):
        for j in range(n):
            b=bracket_basis(i,j,n)
            left=[M[r][b] if b is not None else 0 for r in range(n)]
            right=[0]*n
            for t in range(n):
                bj=bracket_basis(t,j,n)
                if bj is not None:
                    right[bj]=F.add(right[bj],M[t][i])
                bi=bracket_basis(i,t,n)
                if bi is not None:
                    right[bi]=F.add(right[bi],M[t][j])
            if left!=right:
                return False
    return True


def run_case(p,modulus,n):
    F=Field(p,modulus)
    actual=Counter()
    total=0
    for a in product(range(F.q),repeat=n):
        M=derivation_matrix(a,F)
        if total<100 or (n<=3):
            assert satisfies_derivation(M,F), (p,modulus,n,a)
        actual[n-matrix_rank(M,F)]+=1
        total+=1
    expected=predicted_corank_counts(n,F.q,p)
    assert actual==expected,(p,modulus,n,actual,expected)
    return total


def predicted_individual_nullity(a, F):
    """Independent p-curvature/resonance test for a nonzero leading parameter."""
    n = len(a)
    assert a[0] != 0
    z = n // F.p
    if z == 0:
        return 0
    inv = F.inverses[a[0]]
    f = [0] + [F.mul(x, inv) for x in a[1:]]
    for h in range(1,z):
        val = 1
        for _ in range(F.p):
            val = F.mul(val, f[h])
        if val != f[F.p * h]:
            return h
    return z


def check_individual_resonances():
    samples = [(2,[0,1],9),(2,[1,1,1],6),
               (2,[1,1,0,1],5),(3,[1,0,1],5),(5,[0,1],6)]
    tested=0
    for p,modulus,n in samples:
        F=Field(p,modulus)
        for a in product(range(F.q),repeat=n):
            if not a[0]:
                continue
            actual=n-matrix_rank(derivation_matrix(a,F),F)
            expected=predicted_individual_nullity(a,F)
            assert actual==expected,(p,modulus,n,a,actual,expected)
            tested+=1
    return tested


def main():
    cases=([(2,[0,1],n) for n in range(2,10)] +
           [(3,[0,1],n) for n in range(2,8)] +
           [(5,[0,1],n) for n in range(2,6)] +
           [(2,[1,1,1],n) for n in range(2,7)] +
           [(2,[1,1,0,1],n) for n in range(2,5)] +
           [(3,[1,0,1],n) for n in range(2,5)])
    total=0
    for p,modulus,n in cases:
        total+=run_case(p,modulus,n)
    print('FIELD_CASES',len(set((p,tuple(modulus)) for p,modulus,n in cases)))
    print('DIMENSION_CASES',len(cases))
    print('ENUMERATED_DERIVATIONS',total)
    print('INDIVIDUAL_RESONANCE_CASES',check_individual_resonances())
    print('VERIFY_OK')


if __name__=='__main__':
    main()
