from collections import defaultdict
n=273; d=12; poly=0x10ff; size=1<<d

def mul(a,b):
    z=0
    while b:
        if b&1: z^=a
        b>>=1; a<<=1
        if a&size: a^=poly
    return z

def exp(a,k):
    z=1
    while k:
        if k&1:z=mul(z,a)
        a=mul(a,a); k>>=1
    return z
# Exact irreducibility test for the degree-twelve defining polynomial.
def polyrem(a,b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def polygcd(a,b):
    while b:
        a,b=b,polyrem(a,b)
    return a

z=2
for i in range(1,13):
    z=mul(z,z)
    if i in (4,6): assert polygcd(z^2,poly)==1
assert z==2

# Independently find the first generator of multiplicative group.
q=size-1
p=[3,5,7,13]
g=next(a for a in range(2,size) if exp(a,q)==1 and all(exp(a,q//x)!=1 for x in p))
beta=exp(g,q//n)
H=[exp(beta,i) for i in range(n)]
assert len(set(H))==n and all(mul(H[i],H[(n-i)%n])==1 for i in range(n))
cubes=[mul(mul(x,x),x) for x in H]
pairs=defaultdict(list)
for i in range(1,n):
    for j in range(i+1,n):
        pairs[(H[i]^H[j],cubes[i]^cubes[j])].append((i,j))
quints=set()
for (s,t), v in pairs.items():
    rhs=(s^1,t^1)
    for i,j in v:
        for k,l in pairs.get(rhs,[]):
            if len({i,j,k,l})==4:
                quint=tuple(sorted((0,i,j,k,l)))
                assert 0==(H[0]^H[i]^H[j]^H[k]^H[l])
                assert 0==(cubes[0]^cubes[i]^cubes[j]^cubes[k]^cubes[l])
                quints.add(quint)
assert len(quints)==35,(len(quints),quints)
def norm(q):return min(tuple(sorted((v+r)%n for v in q)) for r in range(n))
reps=sorted({norm(x) for x in quints})
assert len(reps)==7,reps
for r in reps:
    assert len({tuple(sorted((x+t)%n for x in r)) for t in range(n)})==n
    assert any(tuple(sorted((x+t)%n for x in r)) in quints for t in range(n))
all_quints=set()
for r in reps:
    for k in range(n):all_quints.add(tuple(sorted((t+k)%n for t in r)))
assert len(all_quints)==1911 and {a for a in all_quints if 0 in a}==quints
print('generator',g,'root',beta, 'norm_samples',len(quints),'orbits',len(reps),'all',len(all_quints))
for i,r in enumerate(reps): print(i+1,','.join(map(str,r)))
print('frobenius perm',[[reps.index(norm(tuple(sorted(2*x%n for x in r)))) for r in reps]])
