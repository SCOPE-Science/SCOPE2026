"""Exact finite-state and rational-function checks for Stern residues modulo 7."""
from fractions import Fraction
from math import gcd

P = 7

def poly_add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def poly_sub(a,b):
    return [ (a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def L(t):
    if t==7:return 1
    if t==6:return 7
    return t*pow(t+1,-1,P)%P

def R(t):
    if t==7:return 7
    return (t+1)%P

D=poly_mul(poly_mul([1,-2],[1,-1]),[1,1,0,2,4])
H=[[1,-1,-2,2,0,-4],
   [0,0,0,0,4,-4],
   [0,0,0,2,-2],
   [0,0,1,-1],
   [0,0,0,2,-2],
   [0,0,1,-1],
   [0,1,-1,-2,2],
   [0,0,0,0,0,4]]
for t in range(8):
    rhs=poly_add(D if t==0 else [0],[0]+poly_add(H[L(t)],H[R(t)]))
    assert trim(H[t])==trim(rhs),(t,H[t],rhs)

def pgcd(a,b):
    a=list(map(Fraction,trim(a)));b=list(map(Fraction,trim(b)))
    while any(b):
        rem=a[:]
        while any(rem) and len(rem)>=len(b):
            shift=len(rem)-len(b)
            c=rem[-1]/b[-1]
            for i in range(len(b)):rem[i+shift]-=c*b[i]
            rem=trim(rem)
        a,b=b,rem
    return trim([v/a[-1] for v in a])
assert pgcd(H[0],D)==[Fraction(1)]

# Direct Stern recurrence, distinct from projective transfer route.
nmax=2**18
s=[0]*(nmax+1);s[1]=1
for n in range(2,nmax+1):
    s[n]=s[n//2] if n%2==0 else s[n//2]+s[n//2+1]

counts=[1]
states=[1]+[0]*7
for r in range(1,301):
    new=[0]*8
    for t,num in enumerate(states):
        new[L(t)]+=num;new[R(t)]+=num
    states=new
    counts.append(states[0])
    if r<=18:
        assert counts[r]==sum(x%7==0 for x in s[:2**r]),r
    if r>=6:
        assert counts[r]==(2*counts[r-1]+counts[r-2]-4*counts[r-3]
                           +2*counts[r-4]+8*counts[r-5]-8*counts[r-6])
assert counts[:16]==[1,1,1,1,1,5,9,21,33,61,121,245,529,1037,2089,4069]
print('VERIFY_OK projective_polynomial_identities=8 rational_coprimality=1 '
      'direct_indices=262144 state_levels=300 minimal_order=6')
