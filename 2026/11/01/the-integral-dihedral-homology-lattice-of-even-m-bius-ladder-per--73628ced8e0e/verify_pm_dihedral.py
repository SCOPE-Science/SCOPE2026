"""Independent finite checks of the cycle-tile model for Möbius perfect-matching complexes."""
from itertools import combinations

def permsign(order):
    return -1 if sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order))) % 2 else 1

def mod2_homology_of_facets(pm):
    from itertools import combinations
    faces={}
    for facet in pm:
        f=tuple(sorted(facet))
        for j in range(1,len(f)+1):
            faces.setdefault(j-1,set()).update(combinations(f,j))
    faces={j:sorted(fs) for j,fs in faces.items()}
    # Exact sparse elimination over the field with two elements.
    ranks={-1:0}
    for j,fs in sorted(faces.items()):
        if j==0:
            ranks[0]=1  # augmented boundary to degree minus one
            continue
        below={f:i for i,f in enumerate(faces[j-1])}
        pivots={}
        for face in fs:
            mask=0
            for a in range(j+1):
                mask^=1<<below[face[:a]+face[a+1:]]
            while mask:
                h=mask.bit_length()-1
                if h in pivots:mask^=pivots[h]
                else:pivots[h]=mask;break
        ranks[j]=len(pivots)
    return {j:len(fs)-ranks[j]-ranks.get(j+1,0) for j,fs in faces.items() if len(fs)-ranks[j]-ranks.get(j+1,0)}

def case(n):
    assert n % 2 == 0 and n >= 4
    N=2*n
    und=lambda a,b:tuple(sorted((a%N,b%N)))
    r=[und(i,i+n) for i in range(n)]
    h=[frozenset((und(i,i+1),und(i+n,i+n+1))) for i in range(n)]
    assert len(set(r))==n and len(set().union(*h))==2*n
    E=set(r).union(*h)
    nbr={i:[] for i in range(N)}
    for e in E:
        a,b=e
        nbr[a].append((b,e));nbr[b].append((a,e))
    pm=set()
    def rec(left, picked):
        if not left:
            pm.add(frozenset(picked));return
        a=min(left)
        for b,e in nbr[a]:
            if b in left:rec(left-{a,b},picked+[e])
    rec(set(range(N)),[])
    tilings=set()
    for k in range(n//2+1):
        for I in combinations(range(n),k):
            if any((i+1)%n in I for i in I):continue
            covered=set().union(*({i,(i+1)%n} for i in I)) if I else set()
            F=frozenset(set().union(*(h[i] for i in I))|{r[j] for j in range(n) if j not in covered})
            tilings.add(F)
    assert pm==tilings, ('tile model false',n,len(pm),len(tilings),len(pm-tilings),len(tilings-pm))
    # The rotation and reflection carry a horizontal-edge pair to the tile expected.
    for name,f,move in [('rotation',lambda v:v+1,lambda i:(i+1)%n),('reflection',lambda v:-v,lambda i:(-i-1)%n)]:
        image=lambda e:und(f(e[0]),f(e[1]))
        assert all({image(x) for x in h[i]}==set(h[move(i)]) for i in range(n)),(name,n,'tiles')
        assert all(image(r[i])==r[(i+1)%n if name=='rotation' else (-i)%n] for i in range(n))
    k=n//2
    Ev=tuple(range(0,n,2));Od=tuple(range(1,n,2))
    def action(f):
        out=[]
        for s in [Ev,Od]:
            im=[f(i) for i in s]
            targ=0 if set(im)==set(Ev) else 1
            sign=permsign(im)
            out.append((targ,sign))
        return tuple(out)
    R=action(lambda i:(i+1)%n)
    S=action(lambda i:(-i-1)%n)
    assert R==((1,1),(0,(-1)**(k-1)))
    assert S==((1,(-1)**(k*(k-1)//2)),(0,(-1)**(k*(k-1)//2)))
    # Every independent tile set outside the two special facets has a compatible rung.
    indep=[]
    for sz in range(n//2+1):
        for I in combinations(range(n),sz):
            if any((i+1)%n in I for i in I):continue
            indep.append(I)
            covered=set().union(*({i,(i+1)%n} for i in I)) if I else set()
            if set(I) not in (set(Ev),set(Od)):
                assert len(covered)<n
    output={'n':n,'perfect_matchings':len(pm),'tile_independent_sets':len(indep),'rotation_columns':R,'reflection_columns':S}
    if n<=10:
        betti=mod2_homology_of_facets(pm)
        assert betti=={k-1:2}, (n,betti)
        output['mod2_reduced_homology']=betti
    return output

if __name__=='__main__':
    for n in [4,6,8,10,12,14]: print(case(n),flush=True)
    print('VERIFY_OK')
