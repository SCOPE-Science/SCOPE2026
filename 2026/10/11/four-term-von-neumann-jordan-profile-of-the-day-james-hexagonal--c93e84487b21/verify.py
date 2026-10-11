from fractions import Fraction as Q

V=[(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)]

def N(z):
    s,t=z
    return max(abs(s),abs(t),abs(s-t))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(c,a): return (c*a[0],c*a[1])

def F(x,y,m):
    one=Q(1)
    a=m; b=one-m
    return Q(1,2)*(N(add(scale(a,x),scale(b,y)))**2+
                   N(sub(scale(a,x),scale(b,y)))**2+
                   a*b*N(sub(x,y))**2+
                   a*b*N(add(x,y))**2)

def R(z):
    s,t=z
    return (t,t-s)

def S(z):
    s,t=z
    return (t,s)

assert all(N(v)==1 for v in V)
assert [R(v) for v in V] == V[1:]+V[:1]
assert all(N(R(v))==N(v) and N(S(v))==N(v) for v in V)

# Pair orbits under simultaneous rotations/reflection and y -> -y.
pairs={(i,j) for i in range(6) for j in range(6)}
def gens(pair):
    i,j=pair
    yield ((i+1)%6,(j+1)%6)
    yield ((-i)%6,(-j)%6)
    yield (i,(j+3)%6)

def orbit(seed):
    seen={seed}; todo=[seed]
    while todo:
        p=todo.pop()
        for q in gens(p):
            if q not in seen:
                seen.add(q); todo.append(q)
    return seen
O0=orbit((0,0)); O1=orbit((0,1))
assert len(O0)==12 and len(O1)==24 and O0|O1==pairs and not (O0&O1)

# Exact values on rational checkpoints; the proof in RESULT.md identifies the
# active norm branches analytically on the entire interval 0 <= m <= 1/2.
for m in [Q(0),Q(1,8),Q(1,4),Q(3,8),Q(1,2)]:
    vals=[F(V[i],V[j],m) for i,j in pairs]
    target=Q(1)+Q(3,2)*m-Q(2)*m*m
    assert max(vals)==target

assert F(V[0],V[1],Q(3,8))==Q(41,32)
print('VERIFY_OK')
