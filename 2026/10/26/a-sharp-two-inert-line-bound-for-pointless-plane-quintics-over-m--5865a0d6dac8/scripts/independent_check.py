"""Independent exact binary-plane-quintic verification with GF(2) Buchberger and polynomial gcd."""
import json,itertools, collections,time
START=time.monotonic()
MS=[(a,b,5-a-b) for a in range(6) for b in range(6-a)]

# Enumerate all 2**21 quintics rather than use an affine parametrization.
E=[]
for p in range(1,8):
    E.append(sum(1<<j for j,(a,b,c) in enumerate(MS)
                 if ((a==0 or p&1) and (b==0 or p&2) and (c==0 or p&4))))
pointless=[f for f in range(1<<21) if all((f&e).bit_count()%2 for e in E)]
assert len(pointless)==16384

def gf2_poly_divrem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

def gf2_gcd(a,b):
    while b:a,b=b,gf2_poly_divrem(a,b)
    return a

def mult_binary(p,q):
    out=0
    while p:
        one=p&-p;i=one.bit_length()-1;p^=one
        tmp=q
        while tmp:
            one2=tmp&-tmp;j=one2.bit_length()-1;tmp^=one2
            out^=1<<(i+j)
    return out

def binary_linear_power(a,b,n):
    result=1
    for _ in range(n):result=mult_binary(result, a|(b<<1))
    return result

lines=[]
for ell in range(1,8):
    pts=[p for p in range(1,8) if not ((ell&p).bit_count()%2)]
    A,B=pts[:2]
    words=[]
    for a,b,c in MS:
        z=1
        for idx,ex in ((0,a),(1,b),(2,c)):
            bit1=(A>>idx)&1;bit2=(B>>idx)&1
            z=mult_binary(z,binary_linear_power(bit1,bit2,ex))
        words.append(z)
    lines.append(words)

def restrict(f, words):
    out=0
    for i in range(21):
        if f>>i&1:out^=words[i]
    return out

def kfactor(f):
    count=0
    for words in lines:
        r=restrict(f,words)
        # The binary homogeneous quintic r has no rational linear factor.
        # z^4+z is the product of the monic irreducibles of degrees 1 and 2.
        # degree=5 and no linear factors => reducible iff quadratic factor exists.
        if gf2_gcd(r,0b10010)==1: count+=1
    return count
hist_all=collections.Counter(kfactor(f) for f in pointless)
assert sum(hist_all.values())==16384

# Buchberger in GF(2)[u,v], with graded-lex leading-term order.
def lt(poly):return max(poly,key=lambda m:(m[0]+m[1],m[0]))
def divide_reduce(f,G):
    f=set(f); remainder=set()
    while f:
        top=lt(f)
        for g in G:
            h=lt(g)
            if top[0]>=h[0] and top[1]>=h[1]:
                shift=top[0]-h[0],top[1]-h[1]
                f.symmetric_difference_update((i+shift[0],j+shift[1]) for i,j in g)
                break
        else:
            f.remove(top);remainder.add(top)
    return remainder

def gb_unit(f,du,dv):
    G=[]
    for p in (f,du,dv):
        if not p:continue
        q=divide_reduce(p,G)
        if q=={(0,0)}:return True
        if q:G.append(q)
    pairs=[(i,j) for i in range(len(G)) for j in range(i)]
    while pairs:
        i,j=pairs.pop()
        a,b=lt(G[i]),lt(G[j])
        ll=max(a[0],b[0]),max(a[1],b[1])
        S={(v[0]+ll[0]-a[0],v[1]+ll[1]-a[1]) for v in G[i]}
        S.symmetric_difference_update((v[0]+ll[0]-b[0],v[1]+ll[1]-b[1]) for v in G[j])
        h=divide_reduce(S,G)
        if h=={(0,0)}:return True
        if h:
            new=len(G)
            pairs.extend((new,k) for k in range(new))
            G.append(h)
    return False

def smooth_projective(f):
    for chart in range(3):
        poly=set()
        for i,(a,b,c) in enumerate(MS):
            if f>>i&1:
                ex=[a,b,c];ex.pop(chart)
                poly.add(tuple(ex))
        du={(i-1,j) for i,j in poly if i&1}
        dv={(i,j-1) for i,j in poly if j&1}
        if not gb_unit(poly,du,dv):return False
    return True

from pathlib import Path
certificate=json.load(open(Path(__file__).resolve().parent.parent/'certificates'/'orbits.json'))
# Independently enumerate all 168 invertible 3x3 matrices and verify orbit coverage.
def polynomial_product(P,Q):
    out=set()
    for a in P:
        for b in Q:
            c=(a[0]+b[0],a[1]+b[1],a[2]+b[2])
            if c in out:out.remove(c)
            else:out.add(c)
    return out

def monomial_images(rows):
    powers=[]
    for row in rows:
        linear={(int((row>>0)&1),0,0)} if row&1 else set()
        if row&2:linear.add((0,1,0))
        if row&4:linear.add((0,0,1))
        products=[{(0,0,0)}]
        for k in range(5):products.append(polynomial_product(products[-1],linear))
        powers.append(products)
    images=[]
    for a,b,c in MS:
        poly=polynomial_product(polynomial_product(powers[0][a],powers[1][b]),powers[2][c])
        images.append(sum(1<<MS.index(ex) for ex in poly))
    return images

def invertible(r0,r1,r2):
    combos={0,r0,r1,r2,r0^r1,r0^r2,r1^r2,r0^r1^r2}
    return len(combos)==8
matrices=[monomial_images((r,s,t)) for r in range(1,8) for s in range(1,8) for t in range(1,8) if invertible(r,s,t)]
assert len(matrices)==168
def action(f,m):
    out=0
    for j in range(21):
        if (f>>j)&1:out^=m[j]
    return out
all_orbit_elements=set()
for entry in certificate:
    rep=entry['representative_mask']
    orbit={action(rep,m) for m in matrices}
    assert len(orbit)==entry['orbit_size'],(rep,len(orbit),entry['orbit_size'])
    assert not (all_orbit_elements & orbit),rep
    all_orbit_elements.update(orbit)
assert all_orbit_elements==set(pointless)

smooth={}
for item in certificate:
    rep=item['representative_mask']
    sm=smooth_projective(rep)
    assert sm==item['geometrically_smooth'],(rep,sm,item)
    assert kfactor(rep)==item['irreducible_line_sections'],rep
    smooth[rep]=sm
weighted=collections.Counter()
for item in certificate:
    if smooth[item['representative_mask']]:weighted[item['irreducible_line_sections']]+=item['orbit_size']
print(json.dumps({'direct_enumeration':len(pointless),
                  'all_irreducible_line_sections_histogram':dict(sorted(hist_all.items())),
                  'projective_orbits':len(certificate),
                  'smooth_orbits':sum(smooth.values()),
                  'smooth_equations':sum(weighted.values()),
                  'smooth_histogram':dict(sorted(weighted.items())),
                  'seconds':round(time.monotonic()-START,4)},sort_keys=True))
