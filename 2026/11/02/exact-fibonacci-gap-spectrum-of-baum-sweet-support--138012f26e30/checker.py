from collections import Counter
from itertools import product

def valid(n):
    if n==0: return True
    return all(len(block)%2==0 for block in bin(n)[2:].split('1'))

def fibonacci(N):
    f=[0,1]
    while len(f)<=N:
        f.append(f[-1]+f[-2])
    return f

def theorem(M):
    f=fibonacci(M+3)
    predicted={1:1+(M-1)//2, 2:M//2, 3:f[M+1]-2}
    for r in range(3,M-1):
        d=(1<<(r-1))+(2 if r%2 else 1)
        predicted[d]=f[M-r+1]-1
    return Counter({k:v for k,v in predicted.items() if v})

def actual(M):
    seq=[n for n in range(1<<M) if valid(n)]
    return Counter(y-x for x,y in zip(seq,seq[1:])),seq

for M in range(2,17):
    h,s=actual(M)
    p=theorem(M)
    assert h==p,(M,h,p)
    assert len(s)==fibonacci(M+3)[M+2],(M,len(s))
    assert sum(h.values())==len(s)-1
    assert sum(d*num for d,num in h.items())==(1<<M)-1
    print(M,len(s),len(h),max(h), 'ok')
print('ALL TESTS PASSED')
