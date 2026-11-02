import itertools, math

def brute(mods):
    X=list(itertools.product(*(range(m) for m in mods)))
    N=len(X)
    op=lambda a,b: tuple((2*b[i]-a[i])%mods[i] for i in range(len(mods)))
    mul=[[X.index(op(a,b)) for b in X] for a in X]
    ct=0
    for p in itertools.permutations(range(N)):
        if all(p[mul[i][j]]==mul[p[i]][p[j]] for i in range(N) for j in range(N)):
            ct+=1
    return ct

def aut_h(mods):
    # maps hom uniquely determined by images of generator. finite abelian group, brute bijective check
    X=list(itertools.product(*(range(m) for m in mods)))
    maps=[]
    for tup in itertools.product(X,repeat=len(mods)):
        if all(all((mods[j]*tup[j][i])%mods[i]==0 for i in range(len(mods))) for j in range(len(mods))):
            arr=[tuple(sum(x[j]*tup[j][i] for j in range(len(mods)))%mods[i] for i in range(len(mods))) for x in X]
            if len(set(arr))==len(X):maps.append(tup)
    return len(maps)

def formula(mods):
    H=[m//math.gcd(m,2) for m in mods]
    c2=sum(m%4==2 for m in mods if m%2==0)
    c4=sum(m%4==0 for m in mods if m%2==0)
    s=2**c2;d=2**c4
    return math.prod(mods)*aut_h(H)*math.factorial(s-1)*math.factorial(s)**(d-1)*d**(s*d-1)
for mods in [(2,2),(2,3),(2,4),(2,6),(3,3),(4,2),(2,2,2),(4,),(8,),(6,)]:
    a=brute(mods) if math.prod(mods)<=8 else None
    b=formula(mods)
    print(mods, a,b, 'OK' if a is None or a==b else 'FAIL')

# Independently construct all core-quandle automorphisms of C4 x C4
# from their action on the four translation-orbits and the displacement group.
def exhaustive_C4xC4():
    X=list(itertools.product(range(4), repeat=2))
    idx={x:i for i,x in enumerate(X)}
    H=[(0,0),(0,2),(2,0),(2,2)]
    classes=[(0,0),(0,1),(1,0),(1,1)]
    rep={c:c for c in classes}
    E=lambda x,y:tuple((2*y[i]-x[i])%4 for i in range(2))
    M=[[idx[E(x,y)] for y in X] for x in X]
    lam=[]
    for p in itertools.permutations(H):
        f=dict(zip(H,p))
        if f[(0,0)]==(0,0) and all(f[tuple((x[i]+y[i])%4 for i in range(2))]==tuple((f[x][i]+f[y][i])%4 for i in range(2)) for x in H for y in H):lam.append(f)
    assert len(lam)==6
    Fset=set()
    for a in X:
        ca=tuple(v%2 for v in a)
        for f in lam:
            opt=[]
            for c in classes[1:]:
                want=f[tuple((2*z)%4 for z in c)]
                co=tuple(((ca[i]+want[i]//2)%2) for i in range(2))
                bc=tuple((co[i]-ca[i])%2 for i in range(2))
                possibles=[b for b in X if tuple((2*b[i])%4 for i in range(2))==want and tuple((b[i]+ca[i])%2 for i in range(2))==co]
                assert len(possibles)==4
                opt.append(possibles)
            for choices in itertools.product(*opt):
                B={(0,0):(0,0),**dict(zip(classes[1:],choices))}
                images=[]
                for x in X:
                    c=tuple(v%2 for v in x)
                    h=tuple((x[i]-c[i])%4 for i in range(2))
                    images.append(idx[tuple((a[i]+B[c][i]+f[h][i])%4 for i in range(2))])
                p=tuple(images)
                assert len(set(p))==16
                assert all(p[M[i][j]]==M[p[i]][p[j]] for i in range(16) for j in range(16))
                Fset.add(p)
    assert len(Fset)==6144
    # Affine maps give exactly |A| |GL_2(Z4)|, checked independently.
    aff=set()
    for u in X:
        for v in X:
            arr=[tuple((x[0]*u[k]+x[1]*v[k])%4 for k in range(2)) for x in X]
            if len(set(arr))==16:
                for a in X:
                    aff.add(tuple(idx[tuple((a[k]+z[k])%4 for k in range(2))] for z in arr))
    assert len(aff)==1536 and aff<=Fset
    return len(Fset),len(aff)

assert exhaustive_C4xC4()==(6144,1536)
print('VERIFY_OK')
