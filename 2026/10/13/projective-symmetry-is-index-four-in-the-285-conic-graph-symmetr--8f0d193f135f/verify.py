from math import gcd

# Discriminant form of T = <6> + <20> on A_T = Z/6 + Z/20.
# q(a,b)=a^2/6+b^2/20 mod 2Z.  We encode 120*q modulo 240.
A=[(a,b) for a in range(6) for b in range(20)]
def add(x,y): return ((x[0]+y[0])%6,(x[1]+y[1])%20)
def mul(n,x): return ((n*x[0])%6,(n*x[1])%20)
def q120(x): return (20*x[0]*x[0]+6*x[1]*x[1])%240
def b120(x,y): return (20*x[0]*y[0]+6*x[1]*y[1])%120

e1=(1,0); e2=(0,1)
U=[x for x in A if mul(6,x)==(0,0) and q120(x)==q120(e1)]
V=[x for x in A if mul(20,x)==(0,0) and q120(x)==q120(e2)]
autos=[]
for u in U:
    for v in V:
        if b120(u,v):
            continue
        image={add(mul(a,u),mul(b,v)) for a in range(6) for b in range(20)}
        if len(image)==120:
            autos.append((u,v))
assert len(autos)==8
assert set(U)=={(1,0),(5,0)}
assert set(V)=={(0,1),(0,9),(0,11),(0,19)}

# O(T) for diag(6,20): the only norm-6 primitive vectors are +-e1,
# hence every integral isometry is a diagonal sign change.  The
# orientation-preserving subgroup is {+I,-I}.
short=[]
for a in range(-3,4):
    for b in range(-3,4):
        if 6*a*a+20*b*b==6:
            short.append((a,b))
assert set(short)=={(1,0),(-1,0)}
O_T=[(s1,s2) for s1 in (-1,1) for s2 in (-1,1)]
O_plus=[x for x in O_T if x[0]*x[1]==1]
assert set(O_plus)=={(1,1),(-1,-1)}

# Their images in O(q_T) are +I and -I, so the Hodge-compatible image has size 2.
hodge_disc={((1,0),(0,1)),((5,0),(0,19))}
assert len(hodge_disc)==2
assert hodge_disc.issubset(set(autos))

# Degtyarev gives |Aut(Fn_2(N_285,h))|=2880 and surjectivity onto Aut(discr N_285).
# Primitive unimodular gluing identifies the latter with O(q_T), of order 8.
graph_aut=2880
disc_aut=len(autos)
hodge_image=len(hodge_disc)
kernel=graph_aut//disc_aut
projective_aut=kernel*hodge_image
assert graph_aut%disc_aut==0
assert kernel==360
assert projective_aut==720
assert graph_aut//projective_aut==4
print('VERIFY_OK', {'disc_aut':disc_aut,'kernel':kernel,'projective_aut':projective_aut,'index':4})
