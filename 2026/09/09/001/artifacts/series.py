"""Exact series + dissection audit for G(q)=prod_{3 not| m}(1+q^m)/(1-q^m)."""
import json

N = 120
# S(n) by exact DP: for each m not div by 3: d = c * 1/(1-q^m); e = d*(1+q^m)
c = [0]*(N+1); c[0]=1
for m in range(1,N+1):
    if m % 3 == 0:
        continue
    d = [0]*(N+1)
    for n in range(N+1):
        s = 0
        k = n
        while k >= 0:
            s += c[k]
            k -= m
        d[n]=s
    e = [0]*(N+1)
    for n in range(N+1):
        e[n]=d[n]+(d[n-m] if n>=m else 0)
    c = e
S = c

def t(n):
    # #{odd divisors of n not divisible by 3}
    if n<=0: return 0
    return sum(1 for d in range(1,n+1,2) if n%d==0 and d%3!=0)

def oddpart(n):
    while n%2==0: n//=2
    return n

# 1) mod-2 family
mod2ok = all(S[n]%2==0 for n in range(1,N+1))
# 2) R(q)=G(q)/G(q^2) series: R = prod over odd m not div 3 of (1+q^m)/(1-q^m)
R=[0]*(N+1); R[0]=1
for m in range(1,N+1,2):
    if m%3==0: continue
    d=[0]*(N+1)
    for n in range(N+1):
        s=0; k=n
        while k>=0:
            s+=R[k]; k-=m
        d[n]=s
    e=[0]*(N+1)
    for n in range(N+1):
        e[n]=d[n]+(d[n-m] if n>=m else 0)
    R=e
# dissection identity: R = 1+2T mod 4, T(n)=t(n)
disc = [(R[n]-(1 if n==0 else 0)-2*t(n))%4 for n in range(N+1)]
discok = all(v==0 for v in disc)
# G = G(q^2)*R mod 4 check
G2=[0]*(N+1)
for n in range(N+1):
    if n%2==0: G2[n]=S[n//2]
conv=[0]*(N+1)
for n in range(N+1):
    conv[n]=sum(G2[j]*R[n-j] for j in range(n+1))
gok = all((conv[n]-S[n])%4==0 for n in range(N+1))
# 3) odd dichotomy S(2n+1) = 2 t(2n+1) mod 4
oddok = all((S[m]-2*t(m))%4==0 for m in range(1,N+1,2))
# 4) even lift S(2n)=S(n)+2 t(2n) mod 4
evenok = all((S[2*n]-S[n]-2*t(2*n))%4==0 for n in range(1,N//2+1))
# 5) characterization: S(odd m)=0 mod4 iff m/3^v3 non-square
def v3strip(m):
    while m%3==0: m//=3
    return m
def issq(m):
    r=int(m**0.5)
    return any((r+k)**2==m for k in (-2,-1,0,1,2))
charok=True
for m in range(1,N+1,2):
    expect2 = issq(v3strip(m))  # True -> S=2 mod4
    got = S[m]%4
    if expect2 and got!=2: charok=False
    if (not expect2) and got!=0: charok=False
# prime family
def primes(lo,hi):
    out=[]
    for p in range(lo,hi+1):
        if p>1 and all(p%d for d in range(2,int(p**0.5)+1)): out.append(p)
    return out
primezero=[p for p in primes(2,N) if p!=3 and S[p]%4!=0]
# doubling closure sample: p=5: S(5*2^k)
dbl=[(5*(2**k), S[5*(2**k)]%4) for k in range(7) if 5*(2**k)<=N]

print("mod2 all even:",mod2ok)
print("dissection R=1+2T mod4 to N:",discok)
print("G=G(q2)R mod4 to N:",gok)
print("odd dichotomy:",oddok)
print("even lift:",evenok)
print("square characterization:",charok)
print("primes p!=3 with S(p) not 0 mod4:",primezero)
print("doubling orbit of 5 (n, S mod4):",dbl)
print("S(1..30):",S[1:31])
print("S mod4 (1..40):",[s%4 for s in S[1:41]])
json.dump({"S":S,"N":N},open("series.json","w"))
