import itertools,random

def det(u,v,p): return (u[0]*v[1]-u[1]*v[0])%p

def solve_cycle(w,p):
    # Prescribe det(v_i,v_{i+1})=w_i on a cyclic sequence.
    L=len(w);w=[int(x)%p for x in w]
    assert L>=3
    z=(0,0);e1=(1,0);e2=(0,1);e3=(1,1)
    vs=[None]*L
    def solve_middle(a,b,x,y):
        d=det(a,b,p)
        assert d
        inv=pow(d,-1,p)
        return ((y*a[0]+x*b[0])*inv%p,(y*a[1]+x*b[1])*inv%p)
    if L==3 and w[2]==0:
        if w[0]:
            vs=[e1,(0,w[0]),(-w[1]*pow(w[0],-1,p)%p,0)]
        elif w[1]:
            vs=[z,e1,(0,w[1])]
        else: vs=[z,z,z]
    elif L%2==0:
        r=L//2
        if r%2==0: c=[i%2 for i in range(r)]
        else: c=[i%2 for i in range(r-1)]+[2]
        colors=[e1,e2,e3]
        for j in range(r):vs[2*j]=colors[c[j]]
        for j in range(r):
            a=vs[2*j];b=vs[(2*j+2)%L]
            vs[2*j+1]=solve_middle(a,b,w[2*j],w[2*j+1])
    else:
        r=(L-1)//2
        vs[0]=e1;vs[-1]=(0,-w[-1]%p) if w[-1] else e1
        if r>=2:
            # Choose three projective colors on a path with given endpoints.
            endpoint=1 if w[-1] else 0
            def path(prefix):
                if len(prefix)==r:
                    return prefix+[endpoint] if prefix[-1]!=endpoint else None
                for c in range(3):
                    if c!=prefix[-1]:
                        ans=path(prefix+[c]);
                        if ans is not None:return ans
                return None
            c=path([0]);assert c is not None,(L,w)
            for j in range(1,r):vs[2*j]=[e1,e2,e3][c[j]]
        for j in range(r):
            vs[2*j+1]=solve_middle(vs[2*j],vs[2*j+2],w[2*j],w[2*j+1])
    assert all(det(vs[i],vs[(i+1)%L],p)==w[i] for i in range(L)),(L,p,w,vs)
    return vs

def all_elem(sizes):return list(itertools.product(*[range(s) for s in sizes]))
def neg(x,ns):return tuple(-a%n for a,n in zip(x,ns))
def T(x,ns):return tuple(-2*a%n for a,n in zip(x,ns))
def primitive_root_order(n,p):
 for x in range(1,p):
  if pow(x,n,p)==1 and all(pow(x,n//d,p)!=1 for d in range(2,n+1) if n%d==0 and all(d%j for j in range(2,int(d**.5)+1))):
   return x
 raise ValueError((n,p))

def check(ns,p,trials,seed=10):
 rng=random.Random(seed)
 A=all_elem(ns);N=len(A);assert (p-1)%max(ns)==0 or all((p-1)%n==0 for n in ns)
 roots=[primitive_root_order(n,p) for n in ns]
 def chi(k,x):
  v=1
  for r,a,b,n in zip(roots,k,x,ns):v=v*pow(r,a*b%n,p)%p
  return v
 C=[[chi(k,x) for x in A] for k in A]
 target_idx={a:i for i,a in enumerate(A)}
 orb=[];seen=set()
 for x in A:
  if x in seen:continue
  o=[];y=x
  while y not in seen:
   o.append(y);seen.add(y);y=T(y,ns)
  assert y==x
  orb.append(o)
 assert all(len(o)==1 or len(o)>=3 for o in orb)
 nonfixed=[x for x in A if T(x,ns)!=x]
 for sample in range(trials):
  desired={x:(rng.randrange(p) if x in nonfixed else 0) for x in A}
  ac={x:0 for x in A};bc={x:0 for x in A}
  for o in orb:
   if len(o)==1:continue
   ww=[desired[neg(x,ns)]*pow(N,-1,p)%p for x in o]
   vs=solve_cycle(ww,p)
   for x,v in zip(o,vs):ac[x],bc[x]=v
  aa=[sum(ac[k]*C[i][j] for i,k in enumerate(A))%p for j in range(N)]
  bb=[sum(bc[k]*C[i][j] for i,k in enumerate(A))%p for j in range(N)]
  value=[0]*N
  for i,x in enumerate(A):
   for j,y in enumerate(A):
    out=tuple((2*y0-x0)%n for x0,y0,n in zip(x,y,ns))
    value[target_idx[out]]+=(aa[i]*bb[j]-bb[i]*aa[j])
  value=[z%p for z in value]
  right=[sum(desired[k]*C[i][j] for i,k in enumerate(A))%p for j in range(N)]
  assert value==right,(ns,p,sample)
 print('OK',ns,p,'N',N,'roots',roots,'orbits',sorted(set(map(len,orb))),'commutator_dimension',len(nonfixed),'trials',trials)

if __name__=='__main__':
 for p in (2,3,5,7,11):
  for L in range(3,15):
   rng=random.Random(100*L+p)
   for t in range(300):solve_cycle([rng.randrange(p) for _ in range(L)],p)
 print('CYCLE_SOLVER_OK')
 for ns,p,trials in [((5,),11,120),((7,),29,120),((9,),19,120),((3,5),31,120),((5,5),11,50),((3,3),7,40),((15,),31,120)]:check(ns,p,trials)
 print('VERIFY_OK')
