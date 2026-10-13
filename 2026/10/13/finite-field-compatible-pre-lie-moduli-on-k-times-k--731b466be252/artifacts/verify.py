from itertools import product

def dot(x,y,q):
    return ((x[0]*y[0])%q,(x[1]*y[1])%q)

def star(x,y,p,q):
    a,b,c,d,e,f,g,h=p
    x1,x2=x; y1,y2=y
    return (
        (x1*y1*a + x1*y2*c + x2*y1*e + x2*y2*g)%q,
        (x1*y1*b + x1*y2*d + x2*y1*f + x2*y2*h)%q,
    )

def add(x,y,q): return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def sub(x,y,q): return ((x[0]-y[0])%q,(x[1]-y[1])%q)

def assoc_left(op,x,y,z,q):
    return sub(op(op(x,y,q),z,q),op(x,op(y,z,q),q),q)

def prelie(op,x,y,z,q):
    return assoc_left(op,x,y,z,q)==assoc_left(op,y,x,z,q)

def compatible(p,q):
    basis=((1,0),(0,1))
    # star is pre-Lie
    sop=lambda x,y,qq: star(x,y,p,qq)
    if not all(prelie(sop,x,y,z,q) for x in basis for y in basis for z in basis):
        return False
    # dot+star is pre-Lie; since both separately pre-Lie this tests compatibility directly.
    def sumop(x,y,qq): return add(dot(x,y,qq),star(x,y,p,qq),qq)
    return all(prelie(sumop,x,y,z,q) for x in basis for y in basis for z in basis)

def predicted(p,q):
    a,b,c,d,e,f,g,h=p
    if e%q!=c%q or f%q!=(-b)%q or g%q!=(-c)%q or d%q!=(-b)%q:
        return False
    return (b*(a+b+c-h))%q==0 and (c*(a+b+c-h))%q==0

def mat_vec(M,x,q):
    return ((M[0][0]*x[0]+M[0][1]*x[1])%q,(M[1][0]*x[0]+M[1][1]*x[1])%q)
def det(M,q): return (M[0][0]*M[1][1]-M[0][1]*M[1][0])%q

def automorphism(M,q):
    if det(M,q)==0: return False
    basis=((1,0),(0,1))
    return all(mat_vec(M,dot(x,y,q),q)==dot(mat_vec(M,x,q),mat_vec(M,y,q),q) for x in basis for y in basis)

def swap_product(p,q):
    # Direct parameter transform under basis swap tau: tau * (tau x star tau y)
    a,b,c,d,e,f,g,h=p
    return (h%q,g%q,f%q,e%q,d%q,c%q,b%q,a%q)

for q in (2,3,5):
    allp=list(product(range(q),repeat=8))
    good=[p for p in allp if compatible(p,q)]
    pred=[p for p in allp if predicted(p,q)]
    assert set(good)==set(pred), (q,len(good),len(pred),len(set(good)^set(pred)))
    assert len(good)==q**3+q**2-q

    mats=[((a,b),(c,d)) for a,b,c,d in product(range(q),repeat=4)]
    aut=[M for M in mats if automorphism(M,q)]
    I=((1,0),(0,1)); S=((0,1),(1,0))
    assert set(aut)=={I,S}, (q,aut)

    goodset=set(good)
    fixed=[p for p in good if swap_product(p,q)==p]
    assert len(fixed)==q**2

    rem=set(good)
    orbits=[]
    while rem:
        p=next(iter(rem))
        orb={p,swap_product(p,q)}
        assert orb<=goodset
        orbits.append(orb)
        rem-=orb
    assert len(orbits)==q*(q*q+2*q-1)//2
    assert sum(1 for o in orbits if len(o)==1)==q**2
    assert sum(1 for o in orbits if len(o)==2)==q*(q*q-1)//2
    print({"q":q,"products":len(good),"classes":len(orbits),"fixed":len(fixed),"two_orbits":sum(len(o)==2 for o in orbits)})
print('VERIFY_OK')
