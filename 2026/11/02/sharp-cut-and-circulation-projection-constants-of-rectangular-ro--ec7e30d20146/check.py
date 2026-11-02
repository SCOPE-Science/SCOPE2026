from fractions import Fraction as F

def edges(m,n):
 h=[('h',i,k,j) for j in range(n) for i in range(m) for k in range(i+1,m)]
 v=[('v',j,k,i) for i in range(m) for j in range(n) for k in range(j+1,n)]
 return h+v

def col(m,n,src,t,typ):
 E=edges(m,n); out=[]
 if src[0]=='h':
  _,a,b,c=src
  u=lambda x: int(x==b)-int(x==a)
  d=lambda y: int(y==c)-F(1,n)
  for e in E:
   if e[0]=='h':
    _,i,k,y=e
    val=(u(k)-u(i))*(F(1,m*n)+t/F(m)*d(y))
   else:
    _,j,l,x=e
    vcoef=t/F(m) if typ=='cut' else (1-t)/F(n)
    val=u(x)*vcoef*(int(l==c)-int(j==c))
   out.append(val)
 else:
  _,a,b,c=src
  u=lambda y: int(y==b)-int(y==a)
  d=lambda x: int(x==c)-F(1,m)
  for e in E:
   if e[0]=='h':
    _,i,k,y=e
    hcoef=(1-t)/F(n) if typ=='cut' else t/F(m)
    val=u(y)*hcoef*(int(k==c)-int(i==c))
   else:
    _,j,l,x=e
    val=(u(l)-u(j))*(F(1,m*n)+(1-t)/F(n)*d(x))
   out.append(val)
 if typ=='cycle':
  out=[int(e==src)-x for e,x in zip(E,out)]
 return out

def mat(m,n,t,typ):
 E=edges(m,n)
 return [col(m,n,e,t,typ) for e in E] # columns

def c_norm(m,n):
 A=m*(m-1)+n*(n-1)
 t=F(m*m-2*m+n,A)
 lam=F(2*(m*m+m*n-3*m+n*n-3*n+3),A)
 return t,lam

def z_norm(m,n):
 A=(m-1)*(n+2);B=(n-1)*(m+2);S=A+B
 t=F(A,S)
 lam=F(5,1)-F(2*(m+n+2),m*n)-F(2*A*B,m*n*S)
 return t,lam

def div(m,n,x):
 res=[F(0) for i in range(m*n)]
 for e,v in zip(edges(m,n),x):
  if e[0]=='h':
   _,a,b,c=e; res[a*n+c]-=v;res[b*n+c]+=v
  else:
   _,a,b,c=e;res[c*n+a]-=v;res[c*n+b]+=v
 return res

def grad(m,n,p):
 return [p[b*n+c]-p[a*n+c] if typ=='h' else p[c*n+b]-p[c*n+a] for typ,a,b,c in edges(m,n)]

def run():
 cases=0; checks=0
 for m in range(2,8):
  for n in range(2,8):
   Ec=edges(m,n);N=len(Ec)
   tC,lamC=c_norm(m,n);tZ,lamZ=z_norm(m,n)
   for typ,t,lam in [('cut',tC,lamC),('cycle',tZ,lamZ)]:
    M=mat(m,n,t,typ)
    norms=[sum(abs(y) for y in column) for column in M]
    assert max(norms)==lam, (m,n,typ,t,lam,max(norms))
    checks+=len(norms)
    assert sum(z==lam for z in norms)>=1
    for x in M:
     if typ=='cycle': assert not any(div(m,n,x))
     else:
      edge_ix={e:i for i,e in enumerate(Ec)}
      potential=[F(0) for _ in range(m*n)]
      for ii in range(m):
       for jj in range(n):
        hh=x[edge_ix[('h',0,ii,0)]] if ii else F(0)
        vv=x[edge_ix[('v',0,jj,ii)]] if jj else F(0)
        potential[ii*n+jj]=hh+vv
      assert grad(m,n,potential)==x, (m,n,'cut image')
     checks+=1
    # idempotence via projection-on-generators only for small cases
    if N<=28:
     for j,xc in enumerate(M):
      yy=[sum(M[k][i]*xc[k] for k in range(N)) for i in range(N)]
      assert yy==xc,(m,n,typ,j)
      checks+=N
    if N<=50:
     if typ=='cut':
      for vertex in range(m*n):
       g=grad(m,n,[F(int(i==vertex)) for i in range(m*n)])
       out=[sum(M[k][i]*g[k] for k in range(N)) for i in range(N)]
       assert out==g,(m,n,vertex)
       checks+=N
     else:
      # Q identity on cycle flows: triangles in each K_m layer and K_n layer,
      # and all elementary rectangles from two coordinates.
      def gcycle(seq):
       out=[F(0) for e in Ec]
       eidx={e:j for j,e in enumerate(Ec)}
       for w,z in zip(seq,seq[1:]+seq[:1]):
        for typ,a,b,c in Ec:
         if typ=='h': a0=(a,c);b0=(b,c)
         else: a0=(c,a);b0=(c,b)
         if (w,z)==(a0,b0):out[eidx[(typ,a,b,c)]]+=1;break
         if (w,z)==(b0,a0):out[eidx[(typ,a,b,c)]]-=1;break
        else: raise ValueError('edge missing')
       return out
      seqs=[]
      if m>=3:
       for y in range(n):seqs += [[(i,y) for i in (0,1,2)]]
      if n>=3:
       for x in range(m):seqs += [[(x,j) for j in (0,1,2)]]
      for x in range(m-1):
       for y in range(n-1): seqs += [[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]]
      for seq in seqs:
       v=gcycle(seq);out=[sum(M[k][i]*v[k] for k in range(N)) for i in range(N)]
       assert out==v
       checks+=N
   if m==n:
    assert tC==tZ==F(1,2)
   if m!=n:
    assert tC!=F(m,m+n)
   cases+=1
 print('CHECK_OK:',cases,'parameter pairs,',checks,'exact rational component checks; cut/circulation images, idempotence and norms')
 for m,n in [(2,2),(2,3),(2,4),(3,4),(3,5),(4,5),(5,5)]:
  print(m,n,'cut',*c_norm(m,n),'cycle',*z_norm(m,n))
if __name__=='__main__':run()
