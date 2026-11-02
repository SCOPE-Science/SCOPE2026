"""Cross-checks for the Thue--Morse shortest-absent recurrence.

Run with Python 3 standard library: python verify.py
"""
from itertools import product

L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
J = ((0, 1), (1, 0))

def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def transpose_comp(w):
    return ''.join('01' if c == '0' else '10' for c in w)

def tm_next(w):
    return transpose_comp(w)

def matrix_count(word):
    P=((1,0),(0,1))
    for c in word:
        P=mul(P, L if c=='0' else R)
    return sum(map(sum,P)),P

def absent_brute(word,length):
    count=0
    for x in product('01',repeat=length):
        p=0
        for ch in x:
            n=word.find(ch,p)
            if n<0:
                count+=1
                break
            p=n+1
    return count

def absent_dp(word,length):
    N=len(word)
    nxt=[[N+1,N+1] for _ in range(N+2)]
    for p in range(N-1,-1,-1):
        nxt[p]=nxt[p+1][:]
        nxt[p][int(word[p])]=p+1
    d={0:1}
    for _ in range(length):
        e={}
        for p,v in d.items():
            for sym in range(2):
                dest = N+1 if p==N+1 else nxt[p][sym]
                e[dest]=e.get(dest,0)+v
        d=e
    return d.get(N+1,0)

A,D=3,1
T='0'
checks=0
for m in range(9):
    W=tm_next(T)
    h=len(T)
    a,P=matrix_count(T)
    assert a==A,(m,a,A)
    assert P[0][0]*P[1][1]-P[0][1]*P[1][0]==1
    assert D==P[0][1]+P[1][0]
    assert absent_dp(W,h+1)==A,(m,W[:30],A)
    checks+=2
    if m<=3:
        assert absent_brute(W,h+1)==A
        checks+=1
    assert W.count('0') == h and W.count('1')==h
    assert A>D>0
    if m<8:
        A,D=2+A*D,D*(A-D)
        T=tm_next(T)

# Independently test the forbidden-transition characterization for all
# orientations through seven complementary pairs.
for h in range(1,8):
    for bits in product('01',repeat=h):
        b=''.join(bits)
        W=transpose_comp(b)
        a,_=matrix_count(b)
        assert absent_brute(W,h+1)==a,(b,W,a)
        checks+=1

print('VERIFY_OK',checks,'independent comparisons; exact quadratic recurrence to m=8')
