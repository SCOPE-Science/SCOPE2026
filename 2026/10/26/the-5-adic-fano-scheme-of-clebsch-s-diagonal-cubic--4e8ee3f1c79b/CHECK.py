"""Exact finite-field checks for the Clebsch cubic's characteristic-five line geometry.

This checks all F_5-rational projective lines in its ambient hyperplane, their
incidence with the special node, and Zariski tangent dimensions. The general
geometric completeness and relative scheme assertions require the proof.
"""
from itertools import combinations, permutations, product

P = 5

def echelon_subspaces():
    for piv in combinations(range(4), 2):
        places = [(i,j) for i,p in enumerate(piv)
                  for j in range(p+1,4) if j not in piv]
        for values in product(range(P), repeat=len(places)):
            a = [[0]*4 for _ in range(2)]
            for i,p in enumerate(piv): a[i][p] = 1
            for (i,j),value in zip(places, values): a[i][j] = value
            yield a

def full(v):
    return list(v) + [(-sum(v))%P]

def cubic(v):
    return sum(x**3 for x in v)%P

def on_surface(u,v):
    u=full(u); v=full(v)
    return (cubic(u)==0 and cubic(v)==0 and
            sum(x*x*y for x,y in zip(u,v))%P==0 and
            sum(x*y*y for x,y in zip(u,v))%P==0)

def rank(a):
    a=[[x%P for x in row] for row in a];nr=len(a);nc=len(a[0]);r=0
    for j in range(nc):
        ip=next((i for i in range(r,nr) if a[i][j]),None)
        if ip is None: continue
        a[r],a[ip]=a[ip],a[r]
        iv=pow(a[r][j],-1,P); a[r]=[x*iv%P for x in a[r]]
        for i in range(nr):
            if i!=r and a[i][j]:
                z=a[i][j];a[i]=[(x-z*y)%P for x,y in zip(a[i],a[r])]
        r+=1
        if r==nr: break
    return r

def reduced_rows(vectors):
    a=[list(v) for v in vectors];r=0
    for j in range(4):
        ix=next((i for i in range(r,2) if a[i][j]%P),None)
        if ix is None:continue
        a[r],a[ix]=a[ix],a[r]
        inv=pow(a[r][j]%P,-1,P);a[r]=[x*inv%P for x in a[r]]
        for i in range(2):
            if i!=r:
                t=a[i][j];a[i]=[(x-t*y)%P for x,y in zip(a[i],a[r])]
        r+=1
        if r==2: break
    assert r==2
    return tuple(map(tuple,a))

def tangent_dimension(L):
    u=full(L[0]);v=full(L[1]);cols=[]
    for side in range(2):
        for j in range(4):
            e=[0]*4;e[j]=1;w=full(e)
            if side==0:
                c=[3*sum(u[t]**2*w[t] for t in range(5)),
                   2*sum(u[t]*w[t]*v[t] for t in range(5)),
                   sum(w[t]*v[t]**2 for t in range(5)),0]
            else:
                c=[0,sum(u[t]**2*w[t] for t in range(5)),
                   2*sum(u[t]*v[t]*w[t] for t in range(5)),
                   3*sum(v[t]**2*w[t] for t in range(5))]
            cols.append(c)
    # Eight basis perturbations minus four basis changes on the line.
    return 8-rank([list(row) for row in zip(*cols)])-4

lines=[L for L in echelon_subspaces() if on_surface(*L)]
assert len(lines)==21
on=[L for L in lines if rank(L+[[1,1,1,1]])==2]
off=[L for L in lines if rank(L+[[1,1,1,1]])==3]
assert (len(on),len(off))==(6,15)
assert all(tangent_dimension(L)==1 for L in on)
assert all(tangent_dimension(L)==0 for L in off)

paired=set()
for singleton in range(5):
    rem=[j for j in range(5) if j!=singleton]
    for left in combinations(rem,2):
        right=[j for j in rem if j not in left]
        u=[0]*5;v=[0]*5
        u[left[0]]=1;u[left[1]]=P-1
        v[right[0]]=1;v[right[1]]=P-1
        paired.add(reduced_rows([u[:4],v[:4]]))
assert len(paired)==15 and all([list(a),list(b)] in off for a,b in paired)

node_lines={reduced_rows([[1]*4,list(perm[:4])])
            for perm in permutations(range(5))}
assert len(node_lines)==6 and all([list(a),list(b)] in on for a,b in node_lines)

# In the ramified quadratic ring t^2+t-1=0, t^2=1-t.
# The normalized Pluecker ratios for the standard cyclotomic line
# p_(0,2)/p_(0,1)=t and the special fiber satisfies (t-2)^2=0.
assert ((2*2+2-1)%5)==0
assert ((-4)%5)==1   # (t-2)^2 = t^2+t-1 over F_5
print('VERIFY_OK: 806 Grassmannian F5-lines enumerated; 21 cubic lines = 15 simple + 6 tangent-dimensional-one; all 15 pairing and 6 node lines identified; ramified quadratic polynomial checked')
