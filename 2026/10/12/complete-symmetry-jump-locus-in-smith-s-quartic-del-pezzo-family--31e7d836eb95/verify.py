import itertools
import sympy as sp

a=sp.symbols('a')
S=[sp.Integer(0),sp.Integer(1),sp.Integer(-1),a,-a]

def cr(p,q,r,s):
    return sp.cancel((p-r)*(q-s)/((p-s)*(q-r)))

def numdiff(u,v):
    return sp.factor(sp.together(u-v).as_numer_denom()[0])

base1=cr(S[0],S[1],S[2],S[3])
base2=cr(S[0],S[1],S[2],S[4])
conditions={}
generic=[]
for perm in itertools.permutations(range(5)):
    T=[S[perm[i]] for i in range(5)]
    n1=numdiff(base1,cr(T[0],T[1],T[2],T[3]))
    n2=numdiff(base2,cr(T[0],T[1],T[2],T[4]))
    if n1==0 and n2==0:
        generic.append(perm)
        conditions[perm]=None
        continue
    g=sp.factor(sp.gcd(sp.Poly(n1,a),sp.Poly(n2,a)).as_expr())
    # The family excludes collisions a=0, ±1.
    for h in (a,a-1,a+1):
        while sp.degree(g,a)>0 and sp.rem(sp.Poly(g,a),sp.Poly(h,a))==0:
            g=sp.factor(sp.div(sp.Poly(g,a),sp.Poly(h,a))[0].as_expr())
    conditions[perm]=(g if sp.degree(g,a)>0 else sp.Integer(0))

assert len(generic)==2
assert set(generic)=={(0,1,2,3,4),(0,2,1,4,3)} # id and x -> -x

special={
    a**2+1:4,
    a**2+3:6,
    3*a**2+1:6,
    a**2-4*a-1:10,
    a**2+4*a-1:10,
}
for f, expected in special.items():
    count=0
    for g in conditions.values():
        if g is None:
            count += 1
        elif g != 0 and sp.rem(sp.Poly(g,a),sp.Poly(f,a))==0:
            count += 1
    assert count==expected, (f,count)

# No other noncollision factor occurs.
seen=set()
for g in conditions.values():
    if g is None or g==0 or sp.degree(g,a)<=0:
        continue
    for f,e in sp.factor_list(g)[1]:
        f=sp.monic(sp.Poly(f,a)).as_expr()
        if sp.degree(f,a)>0:
            seen.add(sp.factor(f))
expected_seen={sp.factor(sp.monic(sp.Poly(f,a)).as_expr()) for f in special}
assert seen==expected_seen, (seen,expected_seen)

# The special stabilizer orders are 4, 6, and 10.  Among finite
# subgroups of PGL_2(C), an invariant five-point set rules out cyclic
# groups of orders 6 and 10 (away from the two common fixed points all
# orbits have full cyclic order) and rules out V_4 (its nontrivial
# point-orbits have even size). Thus the groups are C4, S3, and D5.
print("generic_stabilizer_order=2")
for f,n in special.items(): print(sp.factor(f),n)
print("VERIFY_OK")
