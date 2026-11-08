"""Exact transfer certificate for two-step majority dynamics on open ladders.
No external packages. Run: python transfer_verify.py
"""
from collections import Counter

N=16
alphabet=[(u,v) for u in range(4) for v in range(4)]
def bit(x,k): return (x>>k)&1

def majority(neighbors,old):
    count=sum(neighbors)
    return int(2*count>len(neighbors)) if 2*count!=len(neighbors) else old

def end_test(a,b):
    u,v=alphabet[a]; x,y=alphabet[b]
    for k in (0,1):
        j=1-k
        if majority((bit(u,j),bit(x,k)),bit(u,k))!=bit(v,k):return False
        if majority((bit(v,j),bit(y,k)),bit(v,k))!=bit(u,k):return False
    return True

def middle_test(a,b,c):
    u,v=alphabet[a]; x,y=alphabet[b]; z,w=alphabet[c]
    for k in (0,1):
        j=1-k
        if majority((bit(u,k),bit(x,j),bit(z,k)),bit(x,k))!=bit(y,k):return False
        if majority((bit(v,k),bit(y,j),bit(w,k)),bit(y,k))!=bit(x,k):return False
    return True

edges=[(a*16+b,b*16+c) for a in range(16) for b in range(16)
       for c in range(16) if middle_test(a,b,c)]
left=[int(end_test(a,b)) for a in range(16) for b in range(16)]
right=[int(end_test(b,a)) for a in range(16) for b in range(16)]

def transfer(vector):
    out=[0]*256
    for i,j in edges:out[i]+=vector[j]
    return out

# Verify the 256-coordinate identity (T^5-3T^4+T^3-T^2+3T-I)R=0.
vec=[right]
for _ in range(5):vec.append(transfer(vec[-1]))
observed=Counter(tuple(vec[k][i] for k in range(6)) for i in range(256))
expected={
 (0,0,0,0,0,0):190,
 (1,1,2,7,17,44):18,
 (0,1,3,6,17,45):18,
 (0,2,4,10,28,72):12,
 (1,1,4,11,27,72):12,
 (1,2,7,17,44,117):2,
 (1,1,1,1,1,1):2,
 (1,3,6,17,45,116):2,
}
assert observed==expected,(observed,expected)
coeff=(-1,3,-1,1,-3,1)
assert all(sum(coeff[k]*vec[k][i] for k in range(6))==0 for i in range(256))
print('Transfer identity: 256/256 entries verified, eight value patterns.')
print('Triple-state transitions:',len(edges),'left-end pairs:',sum(left))

def F(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def L(n):return F(n-1)+F(n+1) if n>=1 else 2

def theoretical(n):
    f=2*(F(n+1)+1)
    p=L(2*n)+1+3*(n%3==0)
    q=2*F(n-1)
    return f,p,q

# Transfer enumeration of fixed points and pure-flip configurations is a
# restriction on the same 16-letter alphabet, not the formula itself.
for n in range(2,81):
    # Backward vector evaluation; filters are diagonal at each letter.
    def restriction(mode):
        if mode=='fixed':return [int(u==v) for u,v in alphabet]
        if mode=='flip':return [int(u^v==3) for u,v in alphabet]
        return [1]*16
    def count(mode):
        allow=restriction(mode)
        d=[int(right[a*16+b] and allow[a] and allow[b]) for a in range(16) for b in range(16)]
        for _ in range(n-2):
            w=[0]*256
            for i,j in edges:
                a=i//16;b=i%16
                if allow[a]:w[i]+=d[j]
            d=w
        return sum(left[i]*d[i] for i in range(256))
    f,p,q=theoretical(n)
    assert (count('fixed'),count('all'),count('flip'))==(f,p,q),(n,f,p,q)
    assert p%2==f%2
    if n<=12:print('n',n,'fixed',f,'two_periodic_states',p,'pure_flip_states',q,'primitive_2cycles',(p-f)//2)
print('Exact transfer counts match Fibonacci-Lucas formulas for 2 <= n <= 80.')
