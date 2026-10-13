from math import gcd,isqrt,pi

def kth_power_free(n,k):
    d=2
    while d**k<=n:
        if n%(d**k)==0:return False
        d+=1
    return True

def via_euclid(X,k):
    ans=[]
    for m in range(2,isqrt(X)+2):
        for n in range(1,m):
            if m*m+n*n>X:continue
            if gcd(m,n)!=1 or (m+n)%2==0:continue
            if kth_power_free(m*m-n*n,k):ans.append((m*m-n*n,2*m*n,m*m+n*n))
    return sorted(ans)

def via_uv(X,k):
    ans=[]
    for v in range(3,isqrt(2*X)+2,2):
        for u in range(1,v,2):
            if (u*u+v*v)>2*X:continue
            if gcd(u,v)!=1 or not kth_power_free(u*v,k):continue
            m=(u+v)//2;n=(v-u)//2
            ans.append((u*v,2*m*n,(u*u+v*v)//2))
    return sorted(ans)

for X in [50,500,10000,100000,1000000]:
 for k in [2,3,4]:
  a=via_euclid(X,k);b=via_uv(X,k)
  assert a==b,(X,k, set(a)^set(b))
  print('MATCH',X,k,len(a))
