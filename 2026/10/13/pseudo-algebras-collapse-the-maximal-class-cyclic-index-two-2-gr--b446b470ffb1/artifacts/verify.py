from collections import Counter
from math import gcd

def order_char(N,k):
    return 1 if k%N==0 else N//gcd(N,k)

def maximal_formula(m,r):
    N=2**(m-1)
    C=Counter({1:1,2:3})
    seen=set(); fixed=[]
    for k in range(N):
        rk=(r*k)%N
        if rk==k:
            fixed.append(k); continue
        if k in seen: continue
        seen|={k,rk}
        d=order_char(N,k)
        assert d>=4
        C[d]+=1
    assert set(fixed)=={0,N//2}
    return dict(sorted(C.items()))

def expected_max(m):
    C={1:1,2:3}
    for j in range(2,m):
        C[2**j]=2**(j-2)
    return C

def modular_formula(m):
    N=2**(m-1); r=2**(m-2)+1
    assert [k for k in range(N) if (r*k-k)%N==0]==list(range(0,N,2))
    C=Counter({1:1,2:3})
    for j in range(2,m-1):
        C[2**j]=2**j
    seen=set(); top=0
    for k in range(1,N,2):
        if k in seen: continue
        rk=(r*k)%N
        seen|={k,rk}
        assert order_char(N,k)==N
        top+=1
    assert top==2**(m-3)
    C[N]=top
    return dict(sorted(C.items()))

def expected_mod(m):
    C={1:1,2:3}
    for j in range(2,m-1):
        C[2**j]=2**j
    C[2**(m-1)]=2**(m-3)
    return C

for m in range(4,13):
    N=2**(m-1)
    D=maximal_formula(m,-1%N)
    SD=maximal_formula(m,(2**(m-2)-1)%N)
    Q=expected_max(m)
    M=modular_formula(m)
    assert D==SD==Q==expected_max(m)
    assert M==expected_mod(m)
    assert 4+(2**(m-2)-1)*4==2**m
    assert 2**(m-1)+2**(m-3)*4==2**m
    print({"m":m,"order":2**m,"maximal_class":D,"modular":M})

assert expected_max(4)=={1:1,2:3,4:1,8:2}
assert expected_mod(4)=={1:1,2:3,4:4,8:2}
print("VERIFY_OK")
