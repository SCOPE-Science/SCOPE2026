from collections import Counter

def morph(w):return ''.join('001' if c=='0' else '110' for c in w)

def mus_brute(w):
 c=Counter(w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1))
 return [(i,j) for i in range(len(w)) for j in range(i+1,len(w)+1) if c[w[i:j]]==1 and (j-i==1 or (c[w[i+1:j]]>=2 and c[w[i:j-1]]>=2))]

def mus_sa(w):
 n=len(w)
 sa=sorted(range(n),key=lambda i:w[i:]); lcp=[0]*(n+1)
 for r in range(1,n):
  i,j=sa[r-1],sa[r];k=0
  while i+k<n and j+k<n and w[i+k]==w[j+k]:k+=1
  lcp[r]=k
 mx=[0]*n
 for r,i in enumerate(sa):mx[i]=max(lcp[r],lcp[r+1])
 return [(i,i+mx[i]+1) for i in range(n) if i+mx[i]+1<=n and (mx[i]==0 or (i+1<n and mx[i+1]>=mx[i]))]

w='0';checks=0
for n in range(1,9):
 w=morph(w)
 r=mus_sa(w); m=3**(n-2) if n>=2 else None
 expected= [(j*m-1,(j+1)*m+1) for j in (2,3,5,6,7)] if n>=2 else [(0,2),(2,3)]
 assert r==expected,(n,r,expected)
 if n<=5:assert r==mus_brute(w)
 print('n=',n,'length=',len(w),'MUSs=',len(r),'first=',r[0],'last=',r[-1])
 if n<=4 and n>=2:
  p=morph('0')
  prior='0'
  for _ in range(n-1):prior=morph(prior)
  c=Counter(w[i:j] for i in range(len(w)) for j in range(i+4,len(w)+1))
  cprior=Counter(prior[i:j] for i in range(len(prior)) for j in range(i+1,len(prior)+1))
  for i in range(len(w)):
   for j in range(i+4,len(w)+1):
    a,b=i//3,(j-1)//3
    assert c[w[i:j]] == cprior[prior[a:b+1]],(n,i,j)
    checks+=1
print('total factor-parent multiplicity comparisons',checks)
