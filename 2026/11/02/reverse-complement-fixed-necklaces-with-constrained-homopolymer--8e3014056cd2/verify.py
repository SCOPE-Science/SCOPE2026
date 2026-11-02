"""Reproduce exact reverse-complement necklace counts and generating function tests.
Python 3 standard library only.
"""
from collections import defaultdict
from itertools import product
from math import comb, gcd

COMP = (1, 0, 3, 2)
GC = (0, 0, 1, 1)

def reverse_complement(word):
    return tuple(COMP[x] for x in reversed(word))

def representative(word):
    return min(word[k:]+word[:k] for k in range(len(word)))

def cyclic_valid(word, max_run):
    n = len(word)
    return all(any(word[(i+j)%n]!=word[i] for j in range(1,max_run+1)) for i in range(n))

def linear_counts(length, max_run):
    if length == 0:
        return {0:1}
    states = {(x, 1,GC[x]):1 for x in range(4)}
    for _ in range(1,length):
        new = defaultdict(int)
        for (x,run,g),v in states.items():
            for y in range(4):
                if x==y and run>=max_run: continue
                new[(y,run+1 if x==y else 1,g+GC[y])] +=v
        states=new
    out=defaultdict(int)
    for (_,_,g),v in states.items():out[g]+=v
    return out

def moebius(n):
    if n==1:return 1
    m=0; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; m+=1
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:m+=1
    return -1 if m%2 else 1

def divisors(n):return [d for d in range(1,n+1) if n%d==0]

def predicted(n,g,m):
    if n%2 or g%2:return 0
    return linear_counts(n//2,m).get(g//2,0)//2

def primitive_prediction(n,g,m):
    return sum(moebius(d)*predicted(n//d,g//d,m) for d in divisors(gcd(n,g)))

def brute(m,n):
    sets=defaultdict(set)
    for w in product(range(4),repeat=n):
        if cyclic_valid(w,m):sets[sum(GC[x] for x in w)].add(representative(w))
    fixed=defaultdict(int); primitive=defaultdict(int)
    for g,words in sets.items():
        for w in words:
            if representative(reverse_complement(w))==w:
                fixed[g]+=1
                if all(w!=w[d:]+w[:d] for d in range(1,n)):
                    primitive[g]+=1
    return fixed,primitive

def multiply(a,b,limit):
    out=defaultdict(int)
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+k<=limit:out[i+k,j+l]+=x*y
    return out

def test_rational_identity(m,limit=12):
    a={(j,0):1 for j in range(1,m+1)}
    b={(j,j):1 for j in range(1,m+1)}
    ab=multiply(a,b,limit)
    num=defaultdict(int)
    den={(0,0):1}
    for poly,factor in ((a,2),(b,2),(ab,4)):
        for k,v in poly.items():num[k]+=factor*v
    for poly,factor in ((a,-1),(b,-1),(ab,-3)):
        for k,v in poly.items():den[k]=den.get(k,0)+factor*v
    series={(0,0):0}
    for length in range(1,limit+1):
        for g,v in linear_counts(length,m).items():series[length,g]=v
    prod=multiply(den,series,limit)
    for length in range(limit+1):
        for g in range(length+1):
            assert prod.get((length,g),0)==num.get((length,g),0),(m,length,g)

def main():
    for m in (1,2,3,4):
        test_rational_identity(m)
    tested=0
    for m in (1,2,3):
        for n in range(1,9):
            f,p=brute(m,n)
            for g in range(n+1):
                assert f[g]==predicted(n,g,m),(m,n,g,'fixed',f[g],predicted(n,g,m))
                assert p[g]==primitive_prediction(n,g,m),(m,n,g,'primitive',p[g],primitive_prediction(n,g,m))
                tested+=1
    for m in (1,2,3,4):
        for n in range(1,81):
            for g in range(n+1):
                assert predicted(n,g,m)>=0
                if n%2 or g%2: assert predicted(n,g,m)==0
                v=primitive_prediction(n,g,m)
                assert v>=0 and v<=predicted(n,g,m),(m,n,g,v)
    assert [predicted(n,n//2,3) for n in (4,8,12,16,20,24)] == [4,48,640,8804,124180,1781696]
    assert [primitive_prediction(n,n//2,3) for n in (4,8,12,16,20,24)] == [4,44,636,8756,124176,1781012]
    print('VERIFY_OK; rational identities m=1..4, n<=12; direct necklaces/primitive n<=8, m<=3:', tested,'composition cells; larger DP m<=4,n<=80')

if __name__=='__main__':main()
