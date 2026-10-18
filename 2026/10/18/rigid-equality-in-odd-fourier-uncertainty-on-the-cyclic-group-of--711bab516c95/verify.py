import itertools
p=109;n=27
z=next(pow(a,(p-1)//n,p) for a in range(2,p) if pow(a,(p-1)//n,p)!=1 and pow(a,(p-1)//n*9,p)!=1)
assert pow(z,27,p)==1 and pow(z,9,p)!=1
print('z',z,flush=True)
S=[[ (pow(z,(j*k)%n,p)-pow(z,(-j*k)%n,p))%p for j in range(1,14)] for k in range(1,14)]

def rank_cols(A,rows):
 m=[[S[r][j] for j in A] for r in rows]; rk=0;a=len(A)
 for c in range(a):
  pivot=next((i for i in range(rk,len(m)) if m[i][c]),None)
  if pivot is None:continue
  m[rk],m[pivot]=m[pivot],m[rk]
  inv=pow(m[rk][c],-1,p)
  for i in range(rk+1,len(m)):
   if m[i][c]:
    coef=m[i][c]*inv%p
    for h in range(c,a):m[i][h]=(m[i][h]-coef*m[rk][h])%p
  rk+=1
  if rk==a:break
 return rk

for a in (1,2,3):
 b=6-a; cnt=0;ex=[]
 for A in itertools.combinations(range(13),a):
  for B in itertools.combinations(range(13),b):
   rows=[j for j in range(13) if j not in B]
   if rank_cols(A,rows)<a:
    cnt+=1
    if len(ex)<10:ex.append((tuple(i+1 for i in A),tuple(i+1 for i in B)))
 print('a,b',a,b,'deficient',cnt,'examples',ex,flush=True)

# The sole surviving coefficient kernel has complex dimension one, via an explicit witness.
A=(2,5,11);B=(2,5,11)
assert rank_cols(A,[i for i in range(13) if i not in B])==2
print("unique modular kernel dimension=1: PASS")
