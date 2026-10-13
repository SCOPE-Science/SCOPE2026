from math import isqrt

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def sigma(n):
    d=2; out=1
    while d*d<=n:
        if n%d==0:
            power=1; term=1
            while n%d==0:
                n//=d; power*=d; term+=power
            out*=term
        d+=1
    return out*(n+1) if n>1 else out

def repdigits(N):
    found=[]
    for g in range(2,isqrt(N)+1):
        U=1+g+g*g
        ell=3
        while U<=N:
            if N%U==0:
                c=N//U
                if 0<c<g:found.append((g,c,ell))
            U=U*g+1;ell+=1
    return found

families=[]
for p in range(2,17):
    q=2**p-1
    if prime(p) and prime(q):
        families += [('A',2**(p-1)*q*q)]
        families += [('B',2**(2*p-1)*q)]
for t in range(3,19):
    for k in range(t):
        q=2**t-2**k-1
        if prime(q):families.append(('C',2**(t-1)*q))
families.append(('EX',40))
found=[]
for typ,n in families:
    for triple in repdigits(n):found.append((typ,n,triple))
assert found==[('EX',40,(3,1,4))],found
assert sigma(40)==90
print('PASS checked',len(families),'classified near-perfect instances; long repdigits:',found)
for s in range(2,20):
    g=2**s-1;Q=(g*g+1)//2
    assert Q>g
    assert 2**(2*s-2)<Q<2**(2*s-1)
    if s>=3:
        v=2**s-2
        assert v&(v-1) !=0
print('PASS local inequalities for s=2..19')
