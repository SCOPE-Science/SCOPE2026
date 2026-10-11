import itertools,math

def facets(q):
 V=[(a,b) for a in range(q) for b in range(q)]
 F=[tuple(i for i,(a,b) in enumerate(V) if a==x or b==y) for x in range(q) for y in range(q)]
 S=set()
 for f in F:
  for k in range(1,len(f)+1):
   for t in itertools.combinations(f,k):S.add(t)
 return S

def par(seq):return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def tr(S,q,s,t,sw):
 perm=[q*(s[b] if sw else s[a])+(t[a] if sw else t[b]) for a in range(q) for b in range(q)]
 z=-1
 for face in S:
  L=[perm[i] for i in face]
  if tuple(sorted(L))==face:z+=((-1)**(len(face)-1))*par(L)
 return z

def f_t(p):
 f=sum(i==v for i,v in enumerate(p));t=sum(i<p[i] and p[p[i]]==i for i in range(len(p)))
 return f,t

def pred(s,t,sw):
 q=len(s)
 if not sw:
  fs,ts=f_t(s); ft,tt=f_t(t)
  return 2*math.comb(fs,2)*math.comb(ft,2)+2*ts*tt-(fs-1)*(ft-1)
 k=tuple(s[t[i]] for i in range(q));f=f_t(k)[0]
 return -(f-1)**2
for q in (2,3,4):
 S=facets(q);perms=list(itertools.permutations(range(q)))
 for sw in [False,True]:
  ct=0
  for s in perms:
   for t in perms:
    z=tr(S,q,s,t,sw);w=pred(s,t,sw)
    if z!=w:print('WRONG',q,sw,s,t,z,w);raise SystemExit
    ct+=1
  assert ct == math.factorial(q)**2
# Check the exhaustive face partition behind the equivariant relative-cell proof.
for q in (2,3,4):
    X=facets(q)
    V=[(a,b) for a in range(q) for b in range(q)]
    rows=[set(q*a+b for b in range(q)) for a in range(q)]
    cols=[set(q*a+b for a in range(q)) for b in range(q)]
    A={face for face in X if any(set(face)<=s for s in rows+cols)}
    mixed_edges={face for face in X-A if len(face)==2}
    assert len(mixed_edges)==2*math.comb(q,2)**2
    triangles=set()
    for e in mixed_edges:
        ((a,b),(c,d))=(V[x] for x in e)
        for x in ((a,d),(c,b)):
            triangles.add(tuple(sorted(e+(q*x[0]+x[1],))))
    assert len(triangles)==2*len(mixed_edges)
    assert triangles<=X-A
    residual=(X-A)-mixed_edges-triangles
    assert len(residual)%2==0
    pairs=[]
    for face in residual:
        if len(face)<3: continue
        supports=[]
        for a in range(q):
            for b in range(q):
                cap=rows[a]|cols[b]
                if set(face)<=cap:supports.append((a,b))
        assert len(supports)==1
        a,b=supports[0]
        center=q*a+b
        if center not in face:
            upper=tuple(sorted(face+(center,)))
            assert upper in residual
            pairs.append((face,upper))
    lower={x for x,y in pairs};upper={y for x,y in pairs}
    assert not lower&upper and lower|upper==residual
print('VERIFY_OK')
