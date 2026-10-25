from itertools import product

def mul(x,y,p,lam):
    # natural e1, e2, e3 basis; e1^2=-u, e2^2=-2u+lam*v, e3^2=u
    a=(-x[0]*y[0]-2*x[1]*y[1]+x[2]*y[2])%p
    b=(lam*x[1]*y[1])%p
    return ((a)%p,b,(a+b)%p)

def rref(rows,p):
    a=[list(row) for row in rows if any(z%p for z in row)];i=0
    for col in range(3):
        j=next((j for j in range(i,len(a)) if a[j][col]%p),None)
        if j is None: continue
        a[i],a[j]=a[j],a[i]
        inv=pow(a[i][col],-1,p)
        a[i]=[(z*inv)%p for z in a[i]]
        for k in range(len(a)):
            if k!=i:
                mult=a[k][col]
                a[k]=[(a[k][c]-mult*a[i][c])%p for c in range(3)]
        i+=1
        if i==len(a):break
    return tuple(tuple(row) for row in a[:i])

def dimspan(rows,p):return len(rref(rows,p))

def subspace_set(p):
    vec=[x for x in product(range(p),repeat=3) if any(x)]
    subs={():()}
    for v in vec:subs[rref([v],p)]=1
    for v in vec:
      for w in vec:
        k=rref([v,w],p)
        if len(k)==2: subs[k]=2
    subs[rref([(1,0,0),(0,1,0),(0,0,1)],p)]=3
    return subs

def predicted(p,lam):
    u=(1,0,1);t=(1,0,-1);v=(0,1,1);w=(0,0,1)
    rows=[[],[u],[t],[u,v],[u,w],[u,v,w]]
    if lam!=2%p:
        a=pow((2-lam)%p,-1,p)
        ell=((a)%p,1,(a+1)%p)
        rows.append([ell])
    if lam==4%p:
        inv2=pow(2,-1,p)
        z=tuple((v[i]-inv2*u[i])%p for i in range(3))
        k=tuple((w[i]-inv2*u[i])%p for i in range(3))
        rows.append([z,k])
    return {rref(r,p) for r in rows}

for p in [3,5,7,11]:
    allspaces=subspace_set(p)
    for lam in range(1,p):
        actual=set()
        for space in allspaces:
            if all(dimspan(list(space)+[mul(x,y,p,lam)],p)==len(space) for x in space for y in space):
                actual.add(space)
        expected=predicted(p,lam)
        assert expected==actual,(p,lam,len(actual),len(expected),actual-expected,expected-actual)
        print('OK',p,lam,len(actual))
print('VERIFY_OK')
