"""Direct finite checks for functional evolution-algebra idempotents.

Run with Python 3; no nonstandard packages required.  Operations use explicit
polynomial-basis finite fields and literal coordinatewise algebra products.
"""
from itertools import product
from collections import Counter
from math import gcd


class FiniteField:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = modulus
        self.degree = len(modulus)-1
        assert modulus[-1] == 1
        self.q = p**self.degree
        self.digits = [self.unpack(a) for a in range(self.q)]
        self.plus = [[self.pack([(x+y)%p for x,y in zip(self.digits[a],self.digits[b])])
                      for b in range(self.q)] for a in range(self.q)]
        self.times = [[self.multiply(a,b) for b in range(self.q)] for a in range(self.q)]
        self.squares = [self.times[a][a] for a in range(self.q)]
        assert all(self.power(a,self.q)==a for a in range(self.q))
        assert all(self.power(a,self.q-1)==1 for a in range(1,self.q))

    def unpack(self, a):
        digits=[]
        for _ in range(self.degree):
            digits.append(a%self.p);a//=self.p
        return digits

    def pack(self, digits):
        return sum(c*self.p**i for i,c in enumerate(digits))

    def multiply(self, a,b):
        p=self.p; d=self.degree
        x=self.digits[a];y=self.digits[b]
        prod=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):
                prod[i+j]=(prod[i+j]+x[i]*y[j])%p
        for j in range(2*d-2,d-1,-1):
            c=prod[j]
            for i in range(d):
                prod[j-d+i]=(prod[j-d+i]-c*self.modulus[i])%p
        return self.pack(prod[:d])

    def power(self,a,k):
        r=1
        while k:
            if k%2:r=self.times[r][a]
            a=self.times[a][a];k//=2
        return r


def cycles(f):
    seen=set(); lengths=[]
    for a in range(len(f)):
        if a in seen:continue
        path=[]; pos={};v=a
        while v not in seen and v not in pos:
            pos[v]=len(path);path.append(v);v=f[v]
        if v in pos:lengths.append(len(path)-pos[v])
        seen.update(path)
    return sorted(lengths)


def brute_idempotents(f, field):
    n=len(f); plus=field.plus; squares=field.squares; count=0
    for x in product(range(field.q),repeat=n):
        rhs=[0]*n
        for v in range(n):
            j=f[v];rhs[j]=plus[rhs[j]][squares[x[v]]]
        if rhs==list(x):count+=1
    return count


def predicted_count(lengths,q):
    ans=1
    for L in lengths:ans*=1+gcd(2**L-1,q-1)
    return ans


def mobius(n):
    prime_factors=0;p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:return 0
            prime_factors+=1
        p+=1
    if n>1:prime_factors+=1
    return -1 if prime_factors%2 else 1


def totient(n):
    return sum(1 for k in range(1,n+1) if gcd(k,n)==1)


def reconstruct(lengths, n):
    observations={m:sum(gcd(L,m) for L in lengths) for m in range(1,n+1)}
    multiple_counts={m:sum(mobius(m//d)*observations[d] for d in range(1,m+1) if m%d==0)//totient(m)
                     for m in range(1,n+1)}
    assert all(sum(mobius(m//d)*observations[d] for d in range(1,m+1) if m%d==0)%totient(m)==0
               for m in range(1,n+1))
    result={m:sum(mobius(j)*multiple_counts[m*j] for j in range(1,n//m+1))
            for m in range(1,n+1)}
    return sorted(k for k,v in result.items() for _ in range(v))


def main():
    fields=[('F2',FiniteField(2,[0,1])),
            ('F4',FiniteField(2,[1,1,1])),
            ('F8',FiniteField(2,[1,1,0,1])),
            ('F3',FiniteField(3,[0,1])),
            ('F5',FiniteField(5,[0,1])),
            ('F9',FiniteField(3,[1,0,1]))]
    stats=[]
    sizes={'F2':4,'F4':3,'F8':3,'F3':4,'F5':3,'F9':3}
    for name,field in fields:
        checks=0
        for n in range(1,sizes[name]+1):
            for f in product(range(n),repeat=n):
                lengths=cycles(f)
                actual=brute_idempotents(f,field)
                expected=predicted_count(lengths,field.q)
                assert actual==expected,(name,f,lengths,actual,expected)
                assert reconstruct(lengths,n)==lengths,(f,lengths)
                checks+=1
        stats.append((name,checks))
    import random
    random.seed(4109)
    field=fields[1][1]
    for _ in range(32):
        f=tuple(random.randrange(5) for _ in range(5))
        assert brute_idempotents(f,field)==predicted_count(cycles(f),field.q)
        assert reconstruct(cycles(f),5)==cycles(f)
    a,b=(0,0,0),(0,0,1)
    assert cycles(a)==cycles(b)==[1]
    assert len(set(a))==1 and len(set(b))==2
    # The reduction T^(2^L)-T is squarefree over char p exactly if p does not divide 2^L-1.
    # Check this directly through modular polynomial gcd with SymPy, when present.
    try:
        import sympy as sp
        T=sp.Symbol('T')
        checks=0
        for p in (2,3,5,7,11):
            for L in range(1,9):
                f=sp.Poly(T**(2**L)-T,T,modulus=p)
                squarefree=(sp.gcd(f,f.diff()).degree()==0)
                assert squarefree == ((2**L-1)%p!=0),(p,L,squarefree)
                checks+=1
        print('SCHEME_SQUAREFREE_GCD_CHECKS',checks)
    except ImportError:
        print('SCHEME_SQUAREFREE_GCD_CHECKS not run (sympy unavailable)')
    print('FINITE_FIELD_FULL_FUNCTION_GRAPHS',stats)
    print('ADDITIONAL_F4_DIMENSION5_GRAPHS',32)
    print('NONRECONSTRUCTION_TREE_WITNESS_IMAGE_DIMS',1,2)
    print('VERIFY_OK_FUNCTIONAL_EVOLUTION_IDEMPOTENTS')

if __name__=='__main__':
    main()
