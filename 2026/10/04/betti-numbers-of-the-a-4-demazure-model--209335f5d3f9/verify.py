import itertools, math

def permute(v,p):
    w=[0]*5
    for i,a in enumerate(v):
        w[p[i]]=a
    return tuple(w)

def act(v,g):
    p,s=g
    return tuple(s*x for x in permute(v,p))

G=[(p,s) for p in itertools.permutations(range(5)) for s in (1,-1)]
assert len(G)==240

def sIJ(I,J):
    a,b=len(I),len(J)
    d=math.gcd(a,b)
    v=[0]*5
    for i in I:
        v[i]+=b//d
    for j in J:
        v[j]-=a//d
    assert sum(v)==0
    return tuple(v)

ray_specs=[(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)]
ray_reps=[]
for r,t in ray_specs:
    ray_reps.append(sIJ(set(range(r)),set(range(r,r+t))))
v1=(1,2,-1,-1,-1)
v2=(2,2,-2,-1,-1)
v3=(2,3,-2,-2,-1)
ray_reps += [v1,v2,v3]

ray_orbits=[{act(v,g) for g in G} for v in ray_reps]
ray_sizes=[len(o) for o in ray_orbits]
assert ray_sizes == [20,60,40,10,30,20,40,60,120]
for i in range(len(ray_orbits)):
    for j in range(i):
        assert ray_orbits[i].isdisjoint(ray_orbits[j])
assert sum(ray_sizes)==400

C0=[
    sIJ({0},{1}),
    sIJ({0},{1,2}),
    sIJ({0},{1,2,3}),
    sIJ({0},{1,2,3,4}),
]
C1=[
    sIJ({1},{2}),
    sIJ({1},{2,3}),
    sIJ({1},{2,3,4}),
    sIJ({0,1},{2,3,4}),
]
C2=[
    sIJ({1},{2}),
    sIJ({0,1},{2}),
    sIJ({0,1},{2,3}),
    sIJ({0,1},{2,3,4}),
]
C3=[
    sIJ({1},{2}),
    sIJ({1},{2,3}),
    sIJ({0,1},{2,3}),
    sIJ({0,1},{2,3,4}),
]

cones=[
    C0,
    [C1[0],C1[1],C1[2],v1],
    [C1[0],C1[1],v1,C1[3]],
    [C2[0],C2[1],C2[2],v2],
    [C2[0],v2,C2[2],C2[3]],
    [C3[0],C3[1],C3[2],v3],
    [C3[0],C3[1],v3,C3[3]],
    [C3[0],v3,C3[2],C3[3]],
]

def cone_image(C,g):
    return frozenset(act(v,g) for v in C)

cone_orbits=[]
stab_sizes=[]
for C in cones:
    Cset=frozenset(C)
    stab=[g for g in G if cone_image(C,g)==Cset]
    stab_sizes.append(len(stab))
    cone_orbits.append({cone_image(C,g) for g in G})

assert stab_sizes == [1]*8
assert [len(o) for o in cone_orbits] == [240]*8
for i in range(8):
    for j in range(i):
        assert cone_orbits[i].isdisjoint(cone_orbits[j])

maximal_cones=sum(len(o) for o in cone_orbits)
assert maximal_cones==1920

picard_rank=400-4
euler=maximal_cones
b0=b8=1
b2=b6=picard_rank
b4=euler-(b0+b2+b6+b8)
assert picard_rank==396
assert b4==1126
assert [b0,b2,b4,b6,b8]==[1,396,1126,396,1]

print("group_order=240")
print("ray_orbit_sizes="+",".join(map(str,ray_sizes)))
print("ray_count=400")
print("maximal_cone_stabilizers="+",".join(map(str,stab_sizes)))
print("maximal_cone_orbit_sizes="+",".join(str(len(o)) for o in cone_orbits))
print("maximal_cone_count=1920")
print("picard_rank=396")
print("euler_characteristic=1920")
print("even_betti=1,396,1126,396,1")
print("VERIFY_OK")
