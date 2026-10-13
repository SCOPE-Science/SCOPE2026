"""Exact computational checks for the Möbius-ladder dissociation formulas.

Requires Python 3.10+ and SymPy 1.14. No network access or auxiliary data.
Run: python verify.py
"""
from collections import Counter
from math import comb
import sympy as sp

z, t = sp.symbols('z t')
STATES = tuple((a,b) for a in range(4) for b in range(4))
INDEX = {x:i for i,x in enumerate(STATES)}
def flip(a):
    return ((a&1)<<1)|((a>>1)&1)
def admissible(a,b,c):
    for j in (0,1):
        if (b>>j)&1:
            if ((a>>j)&1)+((b>>(1-j))&1)+((c>>j)&1)>1:
                return False
    return True

T=sp.zeros(16)
for a,b in STATES:
    for c in range(4):
        if admissible(a,b,c):
            T[INDEX[a,b],INDEX[b,c]] = z**b.bit_count()
F=sp.zeros(16)
for i,(a,b) in enumerate(STATES):
    F[i,INDEX[flip(a),flip(b)]]=1
assert T*F==F*T
assert sum(bool(x) for x in T)==41

# A literal symmetry basis, independently generated from the flip permutation.
fixed=[]; pairs=[]; used=set()
for i,(a,b) in enumerate(STATES):
    if i in used: continue
    j=INDEX[flip(a),flip(b)]
    used.add(i);used.add(j)
    (fixed if i==j else pairs).append(i if i==j else (i,j))
assert len(fixed)==4 and len(pairs)==6
P=sp.zeros(16);c=0
for i in fixed:
    P[i,c]=1; c+=1
for i,j in pairs:
    P[i,c]=1;P[j,c]=1;c+=1
assert c==10
for i,j in pairs:
    P[i,c]=1;P[j,c]=-1;c+=1
assert c==16
U=P.inv()*T*P
assert U[:10,10:]==sp.zeros(10,6)
assert U[10:,:10]==sp.zeros(6,10)
QP=1-(1+z)*t-(z+2*z*z)*t**2+(z**3-z*z)*t**3+z**4*t**4
QM=1+z*t+z*z*t*t
assert sp.expand((sp.eye(10)-t*U[:10,:10]).det(method='domain-ge')-QP)==0
assert sp.expand((sp.eye(6)-t*U[10:,10:]).det(method='domain-ge')-QM)==0

# Polynomial arithmetic is separate from SymPy's characteristic-polynomial machinery.
def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):out[i+j]+=x*y
    return out

def scalar(k,a):return [k*x for x in a]

def strip(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

# Newton trace recurrence: p_n=-nq_n-sum_{j=1}^{n-1}q_j p_{n-j}.
qp={1:[-1,-1],2:[0,-1,-2],3:[0,0,-1,1],4:[0,0,0,0,1]}
qm={1:[0,1],2:[0,0,1]}
def traces(q,N):
    p=[[0]]
    for n in range(1,N+1):
        ans=scalar(-n,q.get(n,[0]))
        for j in range(1,min(n,len(q))+1):
            ans=add(ans,scalar(-1,multiply(q[j],p[n-j])))
        p.append(strip(ans))
    return p

Pp=traces(qp,100)
Pm=traces(qm,100)
def predicted(n):return strip(add(Pp[n],scalar(-1,Pm[n])))
assert predicted(1)==[1,2]
assert predicted(2)==[1,4,6]

# Construct the same graph in an unrelated vertex labelling, Z/(2n).
def brute(n):
    N=2*n
    adj=[0]*N
    for i in range(N):
        for j in ((i-1)%N,(i+1)%N,(i+n)%N):adj[i]|=1<<j
    ans=[0]*(N+1)
    tests=0
    for mask in range(1<<N):
        tests+=1
        b=mask
        while b:
            vbit=b & -b
            v=vbit.bit_length()-1
            if (adj[v]&mask).bit_count()>1:break
            b-=vbit
        else:ans[mask.bit_count()]+=1
    return strip(ans),tests

checked=0
for n in range(3,11):
    vals,k=brute(n)
    checked+=k
    assert vals==predicted(n),(n,vals,predicted(n))

# Compute signed traces through 32 columns using sparse transfer DP.
arcs=[[] for _ in range(16)]
for i,(a,b) in enumerate(STATES):
    for c in range(4):
        if admissible(a,b,c):arcs[i].append((INDEX[b,c],b.bit_count()))
for n in range(3,33):
    output=[0]*(2*n+1)
    for start in range(16):
        d={start:[1]}
        for step in range(n):
            nxt={}
            for i,poly in d.items():
                for j,w in arcs[i]:
                    dest=nxt.setdefault(j,[0]*(2*n+1))
                    for a,v in enumerate(poly):
                        if v:dest[a+w]+=v
            d=nxt
        target=INDEX[flip(STATES[start][0]),flip(STATES[start][1])]
        if target in d:
            output=add(output,d[target])
    assert strip(output)==predicted(n),(n,strip(output),predicted(n))

lucas=[2,1]
for i in range(2,101):lucas.append(lucas[-1]+lucas[-2])
for n in range(3,101):
    p=predicted(n)
    assert len(p)==n+1
    expected=lucas[n]+1+2*(n%2==0)-3*(n%3==0)
    assert p[-1]==expected,(n,p[-1],expected)

print('VERIFY_OK flip_states=16 symmetry_dims=10+6 arcs=41 block_determinants=exact brute_orders=3..10 brute_masks='+str(checked)+' trace_orders=3..32 Lucas_top_orders=3..100')
