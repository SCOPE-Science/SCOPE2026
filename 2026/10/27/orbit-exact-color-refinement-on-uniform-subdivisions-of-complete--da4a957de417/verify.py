import itertools,random,collections,math

def instance(n,L):
    vertices=[('b',i) for i in range(n)]+[('e',a,b,t) for a in range(n) for b in range(a+1,n) for t in range(1,L)]
    ix={x:i for i,x in enumerate(vertices)}; adj=[[] for _ in vertices]
    for a in range(n):
      for b in range(a+1,n):
        path=[('b',a)]+[('e',a,b,t) for t in range(1,L)]+[('b',b)]
        for x,y in zip(path,path[1:]):
          u,v=ix[x],ix[y];adj[u].append(v);adj[v].append(u)
    return vertices,adj

def ref(adj,marked):
    c=[0]*len(adj)
    for j,v in enumerate(marked): c[v]=j+1
    for steps in range(len(adj)+1):
        profiles=[(c[i],tuple(sorted(c[j] for j in adj[i]))) for i in range(len(adj))]
        uniq={v:z for z,v in enumerate(sorted(set(profiles)))}; nc=[uniq[x] for x in profiles]
        if len(set(nc))==len(set(c)):
            return c,steps
        c=nc
    raise RuntimeError('no stabilize')

def orbit(n,L,verts,marked):
    loc={v:i for i,v in enumerate(verts)}; pp=[]
    for p in itertools.permutations(range(n)):
        vm=[]
        for v in verts:
            if v[0]=='b': im=('b',p[v[1]])
            else:
                a,b,t=v[1:]; x,y=p[a],p[b];im=('e',min(x,y),max(x,y),t if x<y else L-t)
            vm.append(loc[im])
        if all(vm[i]==i for i in marked): pp.append(vm)
    sig=[tuple(sorted({perm[i] for perm in pp})) for i in range(len(verts))]
    return sig, len(pp)

def parts_equal(c, sig):
    return all((c[i]==c[j])==(sig[i]==sig[j]) for i in range(len(c)) for j in range(i))

def group_formula(n,L,verts,marked):
    E=collections.defaultdict(set); forced=set()
    for i in marked:
        v=verts[i]
        if v[0]=='b': forced.add(v[1])
        else:
            a,b,t=v[1:]; E[(a,b)].add(t)
            if 2*t!=L: forced|={a,b}
    incident=collections.defaultdict(set)
    for (a,b) in E:
        incident[a].add((a,b));incident[b].add((a,b))
    for a in range(n):
        if len(incident[a])>=2: forced.add(a)
    changed=True
    while changed:
        nf=set(forced)
        for (a,b) in E:
            if a in forced or b in forced: nf|={a,b}
        changed=(nf!=forced);forced=nf
    p=0
    for (a,b),locations in E.items():
        if a not in forced and b not in forced:
            assert len(incident[a])==len(incident[b])==1 and locations=={L//2} and L%2==0
            p+=1
    u=sum(1 for a in range(n) if a not in forced and not incident[a]);f=len(forced)
    assert f+2*p+u==n,(f,p,u,n)
    t=f+p+(u>0)
    count=t+(t*(t-1)//2)*(L-1)+(p+(u>=2))*(L//2)
    return f,p,u,count

def predicted_class_sizes(f,p,u,L):
    sizes=[1]*f+[2]*p+([u] if u else [])
    out=list(sizes)
    for i in range(len(sizes)):
      for j in range(i+1,len(sizes)):
        out.extend([sizes[i]*sizes[j]]*(L-1))
    for m in sizes:
      if m>=2:
        for d in range(1,L//2+1):
          out.append((m*(m-1)//2)*(1 if 2*d==L else 2))
    return sorted(out)

if __name__=='__main__':
 random.seed(1208304)
 totals=[]
 for n,L,N in [(4,2,1024),(4,3,2000),(4,4,2000),(4,5,2000),(5,2,2000),(5,3,1300),(5,4,1200),(6,2,500),(6,3,400)]:
    vs,adj=instance(n,L);tot=0;maxsteps=0
    subs = [tuple(i for i in range(len(vs)) if mask>>i&1) for mask in range(1<<len(vs))] if n==4 and L==2 else []
    if not subs:
      subs=[tuple(random.sample(range(len(vs)),random.randrange(len(vs)+1))) for _ in range(N)]
    for marked in subs:
        c,steps=ref(adj,marked); orb,nperm=orbit(n,L,vs,marked)
        f,p,u,count=group_formula(n,L,vs,marked)
        if (not parts_equal(c,orb) or len(set(c))!=count or sorted(collections.Counter(c).values())!=predicted_class_sizes(f,p,u,L)
            or steps>2*L-2 or nperm != 2**p*math.factorial(u)):
            print('FAIL',n,L,marked,[vs[x] for x in marked],'wl classes',len(set(c)),'orbit',len(set(orb)),'formula',count,'fpu',f,p,u,'steps',steps)
            raise SystemExit(1)
        maxsteps=max(maxsteps,steps); tot+=1
    totals.append((n,L,tot,maxsteps))
 print('ALL_TESTS_PASS')
 print('cases',totals)
 print('total_configurations',sum(x[2] for x in totals))
