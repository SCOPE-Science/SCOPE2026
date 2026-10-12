from collections import defaultdict

def p(n):
 assert n>=1
 odd=n//(n&-n)
 return 0 if odd%4==1 else 1

def h(n):
 return (n^(n>>1)).bit_count()

def predicted_for_M(M):
 N=1<<M
 d={}
 for K in range(2,M+1):
  for r in range(1,K):
   L=(1<<K)-(1<<r)
   P=1<<(K+1)
   starts=[]
   for a in range(N-L):
    if a%P in ((1<<r)-1,1<<K):starts.append(a)
   d[L]=set(starts)
 return d

def actual_for_M(M):
 N=1<<M
 H=[h(n) for n in range(N)]
 d=defaultdict(set)
 for a in range(N-1):
  floor=H[a]
  for b in range(a+1,N):
   floor=min(floor,H[b])
   if floor<H[a]:break
   if H[b]==H[a]:d[b-a].add(a)
 return dict(d)

total=0
for M in range(2,13):
 pred=predicted_for_M(M)
 act=actual_for_M(M)
 assert act==pred,(M,[(L,len(v),len(act.get(L,set()))) for L,v in pred.items() if v!=act.get(L,set())], set(act)-set(pred))
 total+=sum(len(v) for v in act.values())

N=1<<18
s=0
for n in range(1,N+1):
 s+=1 if p(n)==0 else -1
 assert s==h(n),(n,s,h(n))

for K in range(2,13):
 for r in range(1,K):
  L=(1<<K)-(1<<r)
  P=1<<(K+1)
  a=(1<<r)-1
  b=1<<K
  x=''.join(str(p(i)) for i in range(a+1,a+L+1))
  y=''.join(str(p(i)) for i in range(b+1,b+L+1))
  assert (x==y)==((K,r) in {(2,1),(3,2)}),(K,r)
  for q in range(8):
   c=q*P+a;d=q*P+b
   assert ''.join(str(p(i)) for i in range(c+1,c+L+1))==x
   assert ''.join(str(p(i)) for i in range(d+1,d+L+1))==y
  M=K+3
  pred=predicted_for_M(M)
  assert len(pred[L])==1<<(M-K)
print('VERIFY_OK','gray_prefix=2^18','finite_exhaustion_M=2..12','occurrences',total,'two_factor_classification_K=2..12','modular_shift_checks=8','count_formula_verified')
