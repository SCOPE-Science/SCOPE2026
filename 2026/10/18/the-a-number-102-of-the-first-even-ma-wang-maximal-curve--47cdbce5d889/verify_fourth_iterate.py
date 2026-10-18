import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 import verify_cartier_polynomial as T
p=3;m=82
matrices={}
for j in range(1,m):
 d=T.D[j]
 jn=(55*j)%82
 e=(3*jn-j)//82
 target=T.D[jn]
 E=j*13//82+13*e
 den=T.powb(jn*13//82)
 cols=[]
 for k in range(d):
  P=T.mul((0,)*k+(1,),T.mul(T.powa(e),T.powb(E)))
  Q=tuple(P[i] for i in range(2,len(P),3)) or (0,)
  Z=T.divexact(Q,den)
  cols.append([Z[x] if x<len(Z) else 0 for x in range(target)])
 matrices[j]=(jn,cols)
# semilinearity scalar powers nonzero, all coeff in F3, straightforward products
max4=0; counts=[]
for j in range(1,m):
 n=T.D[j]
 if not n:continue
 vectors=[[int(a==b) for a in range(n)] for b in range(n)]
 jj=j
 for i in range(4):
  jnext,cols=matrices[jj]
  vectors=[[sum(v[c]*cols[c][h] for c in range(len(v)))%3 for h in range(T.D[jnext])] for v in vectors]
  jj=jnext
  if i==3:
   nonzero=sum(bool(any(v)) for v in vectors)
   counts.append((j,nonzero))
   max4=max(max4,nonzero)
print('Cartier fourth iterate maximum number of nonzero basis vectors',max4)
print('nonzero fourth iterate blocks',[(j,n) for j,n in counts if n])
assert max4==0
