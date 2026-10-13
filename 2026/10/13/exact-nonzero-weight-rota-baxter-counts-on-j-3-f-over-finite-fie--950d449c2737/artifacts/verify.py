from itertools import product

def inv(a,p): return pow(a%p,-1,p)
def mm(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)] for i in range(3)]
def mv(A,v,p): return tuple(sum(A[i][j]*v[j] for j in range(3))%p for i in range(3))
def det3(A,p):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%p
def inv3(A,p):
    d=det3(A,p); assert d
    c=[[0]*3 for _ in range(3)]
    for i in range(3):
      for j in range(3):
        rows=[r for r in range(3) if r!=j]; cols=[s for s in range(3) if s!=i]
        minor=(A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]])%p
        c[i][j]=((-1)**(i+j)*minor*inv(d,p))%p
    return c

def prodJ(x,y,d1,d2,p):
    a,u,v=x; b,s,t=y
    return ((a*b+d1*u*s+d2*v*t)%p,(a*s+b*u)%p,(a*t+b*v)%p)
def add(*vs,p): return tuple(sum(v[i] for v in vs)%p for i in range(3))
def scal(c,v,p): return tuple(c*x%p for x in v)
def rb_ok(A,d1,d2,Delta,p):
    bas=[(1,0,0),(0,1,0),(0,0,1)]
    for x in bas:
      for y in bas:
        Rx,Ry=mv(A,x,p),mv(A,y,p)
        lhs=prodJ(Rx,Ry,d1,d2,p)
        inside=add(prodJ(Rx,y,d1,d2,p),prodJ(x,Ry,d1,d2,p),scal(Delta,prodJ(x,y,d1,d2,p),p),p=p)
        rhs=mv(A,inside,p)
        if lhs!=rhs:return False
    return True

def rank3(A,p):
    # row reduction
    M=[row[:] for row in A]; r=0
    for c in range(3):
      piv=next((i for i in range(r,3) if M[i][c]%p),None)
      if piv is None: continue
      M[r],M[piv]=M[piv],M[r]; z=inv(M[r][c],p); M[r]=[(z*x)%p for x in M[r]]
      for i in range(3):
        if i!=r and M[i][c]%p:
          z=M[i][c]%p; M[i]=[(M[i][j]-z*M[r][j])%p for j in range(3)]
      r+=1
    return r

def proj_lines_2(p):
    return [(1,t) for t in range(p)]+[(0,1)]
def proj_points_3(p):
    out=[]
    for v in product(range(p),repeat=3):
      if v==(0,0,0):continue
      k=next(i for i,x in enumerate(v) if x)
      if v[k]!=1:continue
      # normalized iff first nonzero coordinate is 1
      if any(v[i] for i in range(k)):continue
      out.append(v)
    return out

def predicted_ops(p,d1,d2,Delta=1):
    conic=[z for z in proj_points_3(p) if (z[0]*z[0]-d1*z[1]*z[1]-d2*z[2]*z[2])%p==0]
    rank1=set()
    for z in conic:
      v=(z[1],z[2])
      for w in proj_lines_2(p):
        if (w[0]*v[1]-w[1]*v[0])%p==0: continue
        B=[[1,0,z[0]],[0,w[0],z[1]],[0,w[1],z[2]]]
        assert det3(B,p)
        D=[[0,0,0],[0,0,0],[0,0,(-Delta)%p]]
        A=mm(mm(B,D,p),inv3(B,p),p)
        assert rank3(A,p)==1 and rb_ok(A,d1,d2,Delta,p)
        rank1.add(tuple(sum(A,[])))
    assert len(conic)==p+1
    assert len(rank1)==p*(p+1)
    rank2=set()
    for flat in rank1:
      A=[list(flat[0:3]),list(flat[3:6]),list(flat[6:9])]
      P=[[(-A[i][j]-(Delta if i==j else 0))%p for j in range(3)] for i in range(3)]
      assert rank3(P,p)==2 and rb_ok(P,d1,d2,Delta,p)
      rank2.add(tuple(sum(P,[])))
    return conic,rank1,rank2

for p in (3,5,7,11):
  nonsq=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
  for d2 in (1,nonsq):
    conic,r1,r2=predicted_ops(p,1,d2)
    total=2+len(r1)+len(r2)
    assert total==2*p*p+2*p+2
    print({'q':p,'d':(1,d2),'conic_points':len(conic),'rank_distribution':(1,len(r1),len(r2),1),'total':total})

# exhaustive ambient check for both isometry types over F3
p=3
for d2 in (1,2):
  counts=[0,0,0,0]
  sols=set()
  for flat in product(range(p),repeat=9):
    A=[list(flat[0:3]),list(flat[3:6]),list(flat[6:9])]
    if rb_ok(A,1,d2,1,p):
      counts[rank3(A,p)]+=1; sols.add(flat)
  _,r1,r2=predicted_ops(p,1,d2)
  zero=(0,)*9
  minusI=(2,0,0,0,2,0,0,0,2)
  pred={zero,minusI}|r1|r2
  assert sols==pred
  assert counts==[1,12,12,1]
  print({'EXHAUSTIVE_q':3,'d':(1,d2),'rank_distribution':counts,'total':sum(counts)})
print('VERIFY_OK')
