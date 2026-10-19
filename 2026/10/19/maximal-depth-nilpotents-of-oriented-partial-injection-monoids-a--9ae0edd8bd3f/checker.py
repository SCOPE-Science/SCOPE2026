"""Independent finite checks for oriented partial-injection maximal nilpotents.
No external dependencies. Execute: python checker.py
"""
from itertools import permutations
from math import gcd

def phi(k):
    return sum(gcd(i,k)==1 for i in range(1,k+1))

def cyclic(t):
    return sum(t[i]>t[(i+1)%len(t)] for i in range(len(t)))<=1

def anticyclic(t):
    return sum(t[i]<t[(i+1)%len(t)] for i in range(len(t)))<=1

def brute(n):
    good=reverse=union=0
    # One directed Hamiltonian path is the unique form of a nilpotent of index n.
    for word in permutations(range(n)):
        pairs=sorted(zip(word[:-1],word[1:]))
        images=[y for x,y in pairs]
        a=cyclic(images)
        b=anticyclic(images)
        good+=a;reverse+=b;union+=(a or b)
    return good,reverse,union

def successor(b,d,m):
    return [i+b if i<=m-b else (i+b-d if i<d else i-d) for i in range(m+1)]

def cycles(p):
    seen=set(); c=0
    for x in range(len(p)):
        if x in seen:continue
        c+=1
        while x not in seen:
            seen.add(x);x=p[x]
    return c

for n in range(2,9):
    pos,neg,union=brute(n)
    expect=n*sum(phi(k) for k in range(1,n))
    assert pos==expect,(n,'cyclic',pos,expect)
    if n>=3:assert neg==2*n,(n,'anticyclic',neg,2*n)
    if n>=4:assert union==expect+2*n,(n,'union',union,expect+2*n)
    print(f'n={n} cyclic={pos} anti={neg} union={union}')
for m in range(1,31):
    count=0
    for b in range(1,m+1):
        for d in range(1,m+1):
            if b+d<=m:continue
            p=successor(b,d,m)
            assert sorted(p)==list(range(m+1))
            assert cycles(p)==gcd(b,d)
            count+=(gcd(b,d)==1)
    assert count==sum(phi(k) for k in range(1,m+1))
print('VERIFY_OK')
