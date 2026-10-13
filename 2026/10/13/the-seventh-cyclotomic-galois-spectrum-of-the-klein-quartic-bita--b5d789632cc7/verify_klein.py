import sympy as s
from math import gcd
z=s.symbols('z'); phi=sum(z**i for i in range(7))
# field ops sympy polynomial as list rational
Z=(0,)*6; ONE=(1,0,0,0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c=[0]*11
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[i+j]+=x*y
 for i in range(10,5,-1):
  if c[i]:
   x=c[i]
   for j in range(6):c[i-6+j]-=x
 return tuple(c[:6])
def pl(a):return sum(a[i]*z**i for i in range(6))
def tup(e):
 p=s.Poly(s.rem(e,phi,z),z);return tuple(p.nth(i) for i in range(6))
def inv(a):
 x=s.invert(pl(a),phi,z);return tup(x)
def div(a,b):return mul(a,inv(b))
def zp(k):return tup(z**(k%7))
A=zp(1);B=zp(2);C=zp(4)
u=sub(zp(1),zp(6));v=sub(zp(2),zp(5));w=sub(zp(4),zp(3))
I=[[A,Z,Z],[Z,C,Z],[Z,Z,B]] # diag exponents 1,4,2
T=[[Z,Z,ONE],[ONE,Z,Z],[Z,ONE,Z]]
U=[[u,v,w],[v,w,u],[w,u,v]]
def mm(l,M):return tuple(sumel([mul(l[i],M[i][j]) for i in range(3)]) for j in range(3))
def sumel(xs):
 a=Z
 for x in xs:a=add(a,x)
 return a
def norm(l):
 for x in l:
  if x!=Z:sc=inv(x);return tuple(mul(y,sc) for y in l)
 raise ValueError

# Enumerate the orbit of the rational bitangent under three explicit collineations.
base=norm((ONE,ONE,ONE))
orbit=[base]
for l in orbit:
    for M in (I,T,U):
        y=norm(mm(l,M))
        if y not in orbit:
            orbit.append(y)
        assert len(orbit)<=28, 'orbit larger than genus-three bitangent bound'
assert len(orbit)==28
assert all(l[0]==ONE for l in orbit)

# Homogeneous polynomial arithmetic for exact pullbacks of the quartic.
def padd(p,q):
    ans=dict(p)
    for e,c in q.items(): ans[e]=add(ans.get(e,Z),c)
    return {e:c for e,c in ans.items() if c!=Z}
def pmul(p,q):
    ans={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(e[i]+f[i] for i in range(3))
            ans[k]=add(ans.get(k,Z),mul(a,b))
    return {e:c for e,c in ans.items() if c!=Z}
def ppow(p,n):
    ans={(0,0,0):ONE}
    for _ in range(n): ans=pmul(ans,p)
    return ans
def pullback(M):
    v=[]
    for i in range(3):
        v.append({tuple(int(k==j) for k in range(3)):M[i][j]
                  for j in range(3) if M[i][j]!=Z})
    return padd(padd(pmul(ppow(v[0],3),v[1]),
                     pmul(ppow(v[1],3),v[2])),
                pmul(ppow(v[2],3),v[0]))
quartic_terms=((3,1,0),(0,3,1),(1,0,3))
for M,scalar in ((I,1),(T,1),(U,49)):
    result=pullback(M)
    assert len(result)==3
    assert all(result.get(k)==(scalar,0,0,0,0,0) for k in quartic_terms)


# Nonzero determinant establishes U invertible (away from characteristic seven).
from itertools import permutations
udet=Z
for perm in permutations(range(3)):
    term=ONE
    for i in range(3): term=mul(term,U[i][perm[i]])
    inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    udet=sub(udet,term) if inversions%2 else add(udet,term)
assert udet==tup(7*(1+2*z+2*z**2+2*z**4))
assert int(s.resultant(phi,pl(udet),z))==7**9

# Each line is represented in the form X+bY+cZ=0 in Z[zeta7].
# Determine all primes allowing a pair to coalesce via exact resultant norms.
from collections import Counter
from sympy import factorint
from math import gcd
norm_hist=Counter(); collision_hist=Counter()
for i in range(28):
    for j in range(i):
        d=sub(orbit[i][1],orbit[j][1])
        e=sub(orbit[i][2],orbit[j][2])
        norms=[0 if t==Z else int(s.resultant(phi,pl(t),z)) for t in (d,e)]
        common=gcd(*norms)
        assert common>0
        norm_hist[common]+=1
        for p in factorint(common):
            gp=s.gcd(s.gcd(s.Poly(phi,z,modulus=p),
                             s.Poly(pl(d),z,modulus=p)),
                      s.Poly(pl(e),z,modulus=p))
            if gp.degree()>0: collision_hist[p]+=1
assert sum(norm_hist.values())==378
assert norm_hist==Counter({7:84,43:42,64:42,29:42,203:42,448:42,497:42,1:21,49:21})
assert collision_hist==Counter({7:231,2:84})

# Six exact automorphisms of the cyclotomic extension.
def conjugate(k,e):return tup(sum(e[i]*z**(k*i) for i in range(6)))
fixed={}
for k in range(1,7):
    fixed[k]=sum(norm(tuple(conjugate(k,e) for e in l))==l for l in orbit)
assert fixed=={1:28,2:1,3:1,4:1,5:1,6:4}

unseen=set(range(28));galois_orbits=[]
while unseen:
    j=min(unseen)
    indices={orbit.index(norm(tuple(conjugate(k,e) for e in orbit[j])))
             for k in range(1,7)}
    assert indices<=unseen
    unseen-=indices
    galois_orbits.append(sorted(indices))
assert sorted(map(len,galois_orbits))==[1,3,6,6,6,6]
assert norm((ONE,zp(3),zp(1))) in orbit

# The orbit is exactly all bitangents because a smooth plane quartic in
# characteristic not two has 28 geometric odd theta characteristics.
print('VERIFY_OK: 28 exact bitangents, 1+3+6+6+6+6 Galois orbits,')
print('all-prime distinctness outside 2,7, and fixed counts',fixed)

# Independently enumerate all rational projective lines over eight small fields.
# A line is a bitangent iff its restricted binary quartic is a square over F_p.
X,Y,W,t=s.symbols('X Y W t')
F=X**3*Y+Y**3*W+W**3*X
for prime,expected in ((3,1),(5,1),(11,1),(13,4),(17,1),(19,1),(23,1),(29,28)):
    lines=[(1,a,b) for a in range(prime) for b in range(prime)]
    lines +=[(0,1,b) for b in range(prime)]+[(0,0,1)]
    count=0
    for a,b,c in lines:
        if a:
            restrict=s.Poly(F.subs({X:(-b*t-c)*pow(a,-1,prime),Y:t,W:1},simultaneous=True),t,modulus=prime)
        elif b:
            restrict=s.Poly(F.subs({X:t,Y:(-a*t-c)*pow(b,-1,prime),W:1},simultaneous=True),t,modulus=prime)
        else:
            restrict=s.Poly(F.subs({X:t,Y:1,W:0},simultaneous=True),t,modulus=prime)
        assert not restrict.is_zero
        if restrict.degree()%2==0 and all(m%2==0 for _,m in s.factor_list(restrict,modulus=prime)[1]):
            count+=1
    assert count==expected,(prime,count,expected)
print('VERIFY_OK: direct rational-bitangent census at eight primes')
