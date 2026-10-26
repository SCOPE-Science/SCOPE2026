"""Independent exact finite checks of conditional leaf-count distributions."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import factorial

def from_words(n):
    bydegree=defaultdict(Counter)
    for word in product(range(n), repeat=n-2):
        occ=Counter(word)
        d=1+occ[0]
        leaves=sum(occ[i]==0 for i in range(n))
        bydegree[d][leaves]+=1
    return {d:{v:Fraction(z,sum(c.values())) for v,z in c.items()} for d,c in bydegree.items()}

def expected_law(n,d):
    q=n-1;t=n-d-1
    counts=Counter()
    for w in product(range(q), repeat=t):
        leaves=q-len(set(w))+(d==1)
        counts[leaves]+=1
    return {L:Fraction(c,q**t) for L,c in counts.items()}

def tails(law,j): return sum((p for L,p in law.items() if L>=j),Fraction(0))

def mean(n,d):
    q=n-1;r=Fraction(q-1,q)
    return (d==1)+q*r**(n-d-1)

checks=0
for n in range(5,8):
    obs=from_words(n)
    for d in range(1,n):
        assert obs[d]==expected_law(n,d),(n,d,'law');checks+=1
    for a,b in [(2,1),(1,n-1)]+[(d,d+1) for d in range(2,n-1)]:
        assert all(tails(obs[a],j)<=tails(obs[b],j) for j in range(n+1)),(n,a,b)
        assert any(tails(obs[a],j)<tails(obs[b],j) for j in range(n+1));checks+=2
    for d in range(3,n-1):
        assert any(tails(obs[1],j)<tails(obs[d],j) for j in range(n+1)),(n,d,'a')
        assert any(tails(obs[1],j)>tails(obs[d],j) for j in range(n+1)),(n,d,'b')
        checks+=2
for n in range(5,41):
    assert (mean(n,3)>mean(n,1))==(n<=8),(n,'mean crossover');checks+=1
    assert all(mean(n,d)>mean(n,1) for d in range(4,n));checks+=1
print(f'PASS {checks} exact checks')
