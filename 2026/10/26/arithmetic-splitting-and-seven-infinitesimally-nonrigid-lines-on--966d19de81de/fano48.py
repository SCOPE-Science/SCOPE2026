import itertools,time
# GF(9) = F3[t]/(t^2+1)
q=9
ADD=[[((a%3+b%3)%3)+3*(((a//3+b//3)%3)) for b in range(9)] for a in range(9)]
NEG=[((-a%3)%3)+3*((-(a//3))%3) for a in range(9)]
MUL=[[( (a%3*b%3 +2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)]
# pairs product of two 5-vector coeffs in homog degree4
# poly (degree≤4) as 5 coefficients by exponent of v, eval at x_i=u*row1[i]+v*row2[i].
def pmul(a,b):
 out=[0]*(min(len(a)+len(b)-1,5))
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):
    if bj and i+j<len(out):out[i+j]=ADD[out[i+j]][MUL[ai][bj]]
 return out

def pplus(*xx):
 out=[0]*max(map(len,xx))
 for a in xx:
  for j,b in enumerate(a):out[j]=ADD[out[j]][b]
 return out

def pminus(a,b):return pplus(a,[NEG[x] for x in b])

def psi(w,x,y,z):
 w2=pmul(w,w);x2=pmul(x,x);y2=pmul(y,y);z2=pmul(z,z)
 t=pplus(w2,pmul(w,x),x2,y2,pmul(y,z),z2)
 return pmul(pmul(w,z),t)

def contained(r0,r1):
 ll=[[r0[i],r1[i]] for i in range(4)]
 a,b,c,d=ll
 aa=psi(a,b,c,d)
 bb=psi([NEG[x] for x in b],a,[NEG[x] for x in d],c)
 return not any(pminus(aa,bb))

def rrefs(q):
 for i in range(4):
  for j in range(i+1,4):
   aa=[c for c in range(i+1,4) if c!=j]
   bb=[c for c in range(j+1,4)]
   for vals in itertools.product(range(q),repeat=len(aa)+len(bb)):
    r0=[0]*4;r1=[0]*4;r0[i]=r1[j]=1
    for k,v in zip(aa,vals):r0[k]=v
    for k,v in zip(bb,vals[len(aa):]):r1[k]=v
    yield (tuple(r0),tuple(r1))

def mat_inv2(A):
 a,b=A[0];c,d=A[1];det=ADD[MUL[a][d]][NEG[MUL[b][c]]]
 if not det:return None
 inv=next(t for t in range(1,q) if MUL[t][det]==1)
 return ((MUL[inv][d],MUL[inv][NEG[b]]),(MUL[inv][NEG[c]],MUL[inv][a]))

def canonical(V):
 a=[list(V[0]),list(V[1])];row=0
 for col in range(4):
  pivot=next((j for j in range(row,2) if a[j][col]!=0),None)
  if pivot is None:continue
  a[row],a[pivot]=a[pivot],a[row]
  inv=next(z for z in range(1,9) if MUL[z][a[row][col]]==1)
  a[row]=[MUL[inv][z] for z in a[row]]
  for i in range(2):
   if i!=row:
    fac=a[i][col];a[i]=[ADD[a[i][k]][NEG[MUL[fac][a[row][k]]]] for k in range(4)]
  row+=1
  if row==2:break
 assert row==2
 return tuple(map(tuple,a))

def frob(V):return canonical([[MUL[x][MUL[x][x]] for x in row] for row in V])

if __name__=='__main__':
 start=time.time();res=[]
 for V in rrefs(9):
  if contained(*V):res.append(V)
 print('q9 count',len(res),'time',time.time()-start)
 classes={};r=set(res)
 for V in res:
  if V not in classes:
   w=frob(V);assert w in r
   if w==V:classes[V]=1
   else:classes[V]=2;classes[w]=2
 print('orbits', {n:sum(1 for k,v in classes.items() if v==n)//n for n in set(classes.values())})
 print('frob rational lines',sum(frob(V)==V for V in r))
 print('F3 lines',sum(contained(*V) for V in rrefs(3)))
 print('total number mats',sum(1 for _ in rrefs(9)))
 for n in range(1,3):
  print('samples length',n,[V for V in res if classes[V]==n][:3])
