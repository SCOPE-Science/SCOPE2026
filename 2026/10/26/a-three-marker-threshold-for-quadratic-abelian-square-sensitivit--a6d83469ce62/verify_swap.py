"""Exact sparse-word Abelian-square census and local-swap checks.

Uses direct substring enumeration independently of the gap formula.
"""
from itertools import product

def count_direct(w):
    found=set()
    n=len(w)
    for i in range(n):
        for j in range(i+2,n+1,2):
            f=w[i:j]
            h=len(f)//2
            if f[:h].count('1')==f[h:].count('1'):
                found.add(f)
    return len(found)

def K(a,b,c):
    return sum(1 for x in range(a+1) for y in range(c+1)
               if abs(x-y)<=b and (x+y-b)%2==0)

def formula3(a,b,c,d):
    overlap=K(min(a,b),b,min(c,d)) if b==c else 0
    return max(a,b,c,d)//2+K(a,b,c)+K(b,c,d)-overlap

def word3(a,b,c,d):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d

def word2(a,b,c):
    return '0'*a+'1'+'0'*b+'1'+'0'*c

for m in range(0,11):
    for a in range(m+1):
        for b in range(m-a+1):
            for c in range(m-a-b+1):
                d=m-a-b-c
                w=word3(a,b,c,d)
                assert count_direct(w)==formula3(a,b,c,d),(a,b,c,d)
for k in range(1,35):
    w=word3(k,k,k,k)
    v=word3(k,k+1,k-1,k)
    assert len(w)==len(v)==4*k+3
    assert w[:2*k+2]+w[2*k+2:] ==w
    assert sum(x!=y for x,y in zip(w,v))==2
    qw=(k+1)*(k+2)//2-(k%2)
    qv=k*(k+2)+(k+1)//2
    assert formula3(k,k,k,k)==qw,(k,qw)
    assert formula3(k,k+1,k-1,k)==qv,(k,qv)
    if k<=14:
        assert count_direct(w)==qw and count_direct(v)==qv,(k,qw,qv)
# Fixed weight two formula direct verification and low-weight swap census.
for m in range(0,14):
    for a in range(m+1):
        for b in range(m-a+1):
            c=m-a-b
            assert count_direct(word2(a,b,c))==max(a,b,c)//2+K(a,b,c),(a,b,c)
for n in range(2,12):
    for bits in product('01',repeat=n):
        if min(bits.count('0'),bits.count('1'))>2: continue
        w=''.join(bits)
        for i in range(n-1):
            if w[i]==w[i+1]:continue
            v=w[:i]+w[i+1]+w[i]+w[i+2:]
            # Safety check: the claimed O(n) low-support gap is not contradicted at small lengths.
            assert abs(count_direct(w)-count_direct(v))<=4*n,(n,w,v)
print('PASS: all three-one gap quadruples with <=10 zeros; all k<=34 formula tests; direct length<=59 samples; all two-one triples with <=13 zeros; all low-minority adjacent swaps through length 11.')
