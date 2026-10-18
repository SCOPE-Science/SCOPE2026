from itertools import product, permutations

def potentials(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]+[(n+i,n+j) for i in range(n) for j in range(i+1,n)]+[(i,n+i) for i in range(n)]
    seen=set()
    for av in product((-1,0,1), repeat=n-1):
        a=(0,)+av
        if max(a)-min(a)>1:continue
        for delta in product((-1,0,1),repeat=n):
            b=tuple(a[i]+delta[i] for i in range(n))
            if max(b)-min(b)>1:continue
            f=a+b
            tight=[(u,v) for u,v in edges if abs(f[u]-f[v])==1]
            par=list(range(2*n))
            def find(u):
                while par[u]!=u:u=par[u]
                return u
            for u,v in tight:
                x,y=find(u),find(v)
                par[y]=x
            if len({find(v) for v in range(2*n)})==1:seen.add(f)
    return seen

def group_transform(f,n,perm,flip,neg):
    a=f[:n];b=f[n:]
    if flip:a,b=b,a
    nf=tuple(a[perm[i]] for i in range(n))+tuple(b[perm[i]] for i in range(n))
    if neg:nf=tuple(-x for x in nf)
    return tuple(x-nf[0] for x in nf)

def orbits(n, fs):
    perms=list(permutations(range(n)))
    todo=set(fs);orb=[]
    while todo:
        f=min(todo)
        orbit={group_transform(f,n,p,flip,neg) for p in perms for flip in (0,1) for neg in (0,1)}
        if not orbit<=fs:raise RuntimeError('symmetry violation')
        assert orbit<=todo
        todo.difference_update(orbit)
        orb.append((min(orbit),len(orbit)))
    return sorted(orb,key=lambda a: (a[1],a[0]))

def predicted(n):
    return 4**n+2*3**n-9*2**n+8

def orbitpred(n):
    return sum(t//2*((n-t)//2+1) for t in range(2,n+1))+sum(s//2 for s in range(2,n))+n*n//4

if __name__=='__main__':
  for n in range(2,7):
    fs=potentials(n)
    print('n',n,'facet_count',len(fs),'predicted',predicted(n))
    assert len(fs)==predicted(n)
    if 3<=n<=5:
      o=orbits(n,fs)
      print('orbit count',len(o),'predicted',orbitpred(n),'sizes',[size for _,size in o]);assert len(o)==orbitpred(n)
  print('ALL EXACT CHECKS PASSED')
