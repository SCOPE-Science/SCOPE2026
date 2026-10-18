# Exact reproducible classification of smooth plane-filling quintics over F2.
from collections import Counter
from itertools import product
D=5
mons=[(i,j,D-i-j) for i in range(D+1) for j in range(D-i+1)]
assert len(mons)==21
pts=[tuple(int(bool(v)) for v in p) for p in product((0,1),repeat=3) if p!=(0,0,0)]
# rref GF2

def nullspace(rows,n):
  piv={}
  for r in rows:
    r=int(r)
    while r:
      j=r.bit_length()-1
      if j not in piv: piv[j]=r; break
      r^=piv[j]
  free=[j for j in range(n) if j not in piv]
  ns=[]
  for j in free:
    v=1<<j
    # Pivot columns increase; all contributions from smaller pivots are known.
    for k in sorted(piv):
      if (piv[k]&v).bit_count()%2:v^=1<<k
    ns.append(v)
  for r in rows:
    assert all((r&b).bit_count()%2==0 for b in ns)
  return ns

def evalmon(m,p):
  a,b,c=m;x,y,z=p
  return (x**a)*(y**b)*(z**c)
base_rows=[sum(evalmon(m,p)<<i for i,m in enumerate(mons)) for p in pts]
basis=nullspace(base_rows,len(mons))
n=len(basis); assert n==14, n
# coeff mask to monomials
polys=[0]*(1<<n)
for m in range(1,1<<n):
    v=m&-m;j=v.bit_length()-1;polys[m]=polys[m^v]^basis[j]
lookup={p:i for i,p in enumerate(polys)}

def gf_mul(a,b,dd,poly):
    out=0;mask=(1<<dd)-1
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&(1<<dd):a^=poly
    return out&mask

def field_data(dd,poly):
    q=1<<dd;mul=[[gf_mul(a,b,dd,poly) for b in range(q)] for a in range(q)]
    powers=[[1]*6 for _ in range(q)]
    for a in range(q):
        for i in range(1,6):powers[a][i]=mul[powers[a][i-1]][a]
    return mul,powers

def singular_kernel_at(p, mul, powers,dd):
    # compute gradients for basis polynomials over GF(2^dd)
    evals=[]
    for m in mons:
        a,b,c=m;x,y,z=p
        dx=mul[mul[powers[x][a-1]][powers[y][b]]][powers[z][c]] if a&1 else 0
        dy=mul[mul[powers[x][a]][powers[y][b-1]]][powers[z][c]] if b&1 else 0
        dz=mul[mul[powers[x][a]][powers[y][b]]][powers[z][c-1]] if c&1 else 0
        evals.append((dx,dy,dz))
    grow=[]
    for v in basis:
        idx=[i for i in range(len(mons)) if (v>>i)&1]
        grow.append(tuple(__import__('functools').reduce(lambda a,b:a^b,(evals[i][j] for i in idx),0) for j in range(3)))
    rows=[]
    for j in range(3):
        for bit in range(dd):
            row=sum(((grow[i][j]>>bit)&1)<<i for i in range(n))
            if row:rows.append(row)
    return nullspace(rows,n)

bad=bytearray(1<<n)
bad[0]=1
polys_irred={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
counts={}
for dd in range(1,7):
    mul,powers=field_data(dd,polys_irred[dd]);q=1<<dd
    changed=0; active=0; maxnul=0
    for p in [(1,y,z) for y in range(q) for z in range(q)]+[(0,1,z) for z in range(q)]+[(0,0,1)]:
        kernel=singular_kernel_at(p,mul,powers,dd)
        dim=len(kernel);maxnul=max(maxnul,dim)
        if dim==0:continue
        active+=1
        kspace=[0]
        for b in kernel:kspace += [v^b for v in kspace]
        for v in kspace:
            if not bad[v]:bad[v]=1;changed+=1
    counts[dd]=(changed,active,maxnul)
    print('degree <=',dd,'new_bad',changed,'survivors',len(bad)-sum(bad),flush=True)

smooth={i for i in range(1<<n) if not bad[i]}
# transform via f(M(x,y,z)) over F2
# poly multiplication GF2 monoms degree up to 5

def pmul(p,q):
    coeff=set()
    for a in p:
        for b in q:
            c=tuple(a[i]+b[i] for i in range(3))
            if c in coeff:coeff.remove(c)
            else:coeff.add(c)
    return list(coeff)

def pmap(M):
    L=[]
    for row in M:L.append([e for i,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]) if row[i]])
    trans=[]
    for a,b,c in mons:
        p=[(0,0,0)]
        for Lcur,deg in zip(L,(a,b,c)):
            for _ in range(deg):p=pmul(p,Lcur)
        trans.append(sum(1<<mons.index(e) for e in p))
    f=[]
    for B in basis:
        t=0
        for j in range(21):
            if (B>>j)&1:t^=trans[j]
        assert t in lookup
        f.append(lookup[t])
    return f

Ms=[[(0,1,0),(1,0,0),(0,0,1)],[(1,0,0),(0,0,1),(0,1,0)],[(1,1,0),(0,1,0),(0,0,1)]]
trans=[pmap(M) for M in Ms]

def linear_img(v,tr):
    out=0
    while v:
        bit=v&-v;out^=tr[bit.bit_length()-1];v^=bit
    return out

orbits=[];seen=set()
for m in sorted(smooth):
    if m in seen:continue
    stack=[m];O={m}
    while stack:
        x=stack.pop()
        for tr in trans:
            y=linear_img(x,tr)
            assert y in smooth
            if y not in O:O.add(y);stack.append(y)
    seen|=O;orbits.append((m,len(O)))
assert counts[1][0]==14196 and counts[2][0]==147 and counts[3][0]==24 and counts[4][0]==420 and counts[5][0]==0 and counts[6][0]==84
assert len(smooth)==1512 and len(orbits)==10 and Counter(sz for _,sz in orbits)=={168:8,84:2}
assert orbits==[(157,168),(159,168),(174,84),(251,168),(410,84),(413,168),(417,168),(433,168),(463,168),(684,168)]
print('smooth_count',len(smooth),'orbits',len(orbits),'group_orbit_sizes',dict(sorted(Counter(sz for _,sz in orbits).items())))

# Independent algebraic-closure smoothness certificate for the ten representatives.
# On each projective affine chart, the three partial derivatives generate the unit ideal.
import sympy as sp
x,y,z=sp.symbols('x y z')
T=sp.symbols('T')
for d,p in polys_irred.items():
  field_polynomial=sum((p>>i&1)*T**i for i in range(d+1))
  assert sp.Poly(field_polynomial,T,modulus=2).is_irreducible
for mask,size in orbits:
  F=sum((polys[mask]>>i&1)*x**a*y**b*z**c for i,(a,b,c) in enumerate(mons))
  grads=[sp.diff(F,w) for w in (x,y,z)]
  for variables,sub in [((y,z),{x:1}),((x,z),{y:1}),((x,y),{z:1})]:
    gb=sp.groebner([g.subs(sub) for g in grads],*variables,modulus=2,order='grevlex')
    assert len(gb.polys)==1 and gb.polys[0].total_degree()==0 and int(gb.polys[0].as_expr())%2==1
  print('Certified smooth representative',mask,'orbit size',size,flush=True)
print('All finite witnesses, projective orbits and algebraic-closure smoothness certificates PASS')
