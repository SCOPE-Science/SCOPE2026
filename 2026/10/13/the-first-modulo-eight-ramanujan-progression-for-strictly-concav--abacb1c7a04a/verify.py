from math import isqrt
N=500
# method 1 product
P=[0]*(N+1);P[0]=1
s=[0]*(N+1)
for j in range(N,-1,-1):
 for k in range(N-j+1):s[j+k]=(s[j+k]+P[k])%8
 if j:
  for k in range(N,-1,-1):
   P[k]=(P[k]+(2*P[k-j] if k>=j else 0)+(P[k-2*j] if k>=2*j else 0))%8
# method 2 qT_o parity
ss=[0]*(N+1)
for j in range(N+1):
 z=8*j+1;v=isqrt(z)
 if v*v==z:
  r=(v-1)//2
  ss[j]=(-1 if r%2 else 1)%8
 if j==0:continue
 n=j-1;t=0
 for m in range(isqrt((n+1)//2)+3):
  if m*(2*m+1)==n+1:t^=1
 # bounded k by nonnegative k(3k+1)
 for k in range(-isqrt(n+2)-2,isqrt(n+2)+3):
  bk=k*(3*k+1)
  if bk>n+1:continue
  for m in range(isqrt(n+2)+2):
   if bk+6*m*m+m==n+1:t^=1
   if bk+6*m*m+5*m+1==n+1:t^=1
 ss[j]=(ss[j]+4*t)%8
if ss!=s:
 print('DIFFERENCES',[(i,a,b) for i,(a,b) in enumerate(zip(s,ss)) if a!=b][:20]);raise SystemExit(1)
print('INDEPENDENT_OK',N+1)
W=[5,7,12,16,17,94,103,119,128,222,249,251,261,277,284,382,386,422]
for w in W:assert s[w]==4
for mod in range(1,25):
 triangular={k*(k+1)//2%mod for k in range(2*mod)}
 assert all((r in triangular) or any(w%mod==r for w in W) for r in range(mod))
print('COVERAGE_OK',len(W),'all moduli m<=24')
w25={}
for r in range(25):
 w25[r]=next((i for i in range(r,N+1,25) if s[i]!=0),None)
print('MOD25_WITNESSES',w25)
assert {r for r,n in w25.items() if n is None}=={8,13,18,23}

print('VERIFY_OK independent_coefficients=501 obstruction_indices=18 smaller_moduli=24 excluded_mod25=21')
