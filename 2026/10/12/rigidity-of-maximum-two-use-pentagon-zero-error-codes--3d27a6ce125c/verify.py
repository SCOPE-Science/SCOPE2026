from itertools import combinations, product, permutations
V=list(product(range(5), repeat=2))
idx={v:i for i,v in enumerate(V)}

def conf(u,v):
    if u==v: return False
    return all(a==b or (a-b)%5 in (1,4) for a,b in zip(u,v))

def independent(C):
    return all(not conf(V[i],V[j]) for i,j in combinations(C,2))
max5=[]
for C in combinations(range(25),5):
    if independent(C): max5.append(tuple(C))
assert len(max5)==10
assert not any(independent(C) for C in combinations(range(25),6))
expected=set()
for a in range(5):
    for s in (2,-2):
        C=tuple(sorted(idx[(x,(a+s*x)%5)] for x in range(5)))
        expected.add(C)
assert set(max5)==expected and len(expected)==10
# natural isometry group D10 x D10, with optional coordinate swap
Ds=[]
for eps in (1,-1):
    for a in range(5):
        Ds.append(lambda x,eps=eps,a=a:(eps*x+a)%5)
def apply(C,f,g,swap):
    out=[]
    for i in C:
        x,y=V[i]
        z=(f(x),g(y))
        if swap: z=(z[1],z[0])
        out.append(idx[z])
    return tuple(sorted(out))
canon=next(iter(expected))
orbit=set()
stab=0
for f in Ds:
  for g in Ds:
    for swap in (False,True):
      im=apply(canon,f,g,swap)
      orbit.add(im)
      if im==canon: stab+=1
assert orbit==expected
assert len(orbit)==10 and stab==20
print('VERIFY_OK maximum=5 labeled_maxima=10 natural_orbits=1 orbit_size=10 stabilizer=20')
