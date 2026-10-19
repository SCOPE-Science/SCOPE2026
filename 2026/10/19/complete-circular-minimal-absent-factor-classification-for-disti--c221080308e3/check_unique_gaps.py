from itertools import permutations,product

def candidates(g):
 r=len(g);M=max(g);S=set(g)
 E=[(g[i],g[(i+1)%r]) for i in range(r)]
 P=lambda u,v:any(x>=u and y>=v for x,y in E)
 nxt={g[i]:g[(i+1)%r] for i in range(r)}
 prv={g[(i+1)%r]:g[i] for i in range(r)}
 A={'1'*(M+1)}
 A.update('1'*u+'0'+'1'*v for u in range(1,M+1) for v in range(1,M+1) if not P(u,v) and P(u-1,v) and P(u,v-1))
 A.add('00')
 A.update('0'+'1'*j+'0' for j in range(1,M) if j not in S)
 for j in S:
  if P(j,nxt[j]+1):A.add('0'+'1'*j+'0'+'1'*(nxt[j]+1))
  if P(prv[j]+1,j):A.add('1'*(prv[j]+1)+'0'+'1'*j+'0')
 for x in S:
  for y in S:
   if y <= nxt[x] and x <=prv[y] and y!=nxt[x]:
    A.add('0'+'1'*x+'0'+'1'*y+'0')
 return A

def direct(g,cap=25):
 w=''.join('0'+'1'*i for i in g)
 # all cyclic factors up to longest candidate+1 length (including oversized cyclic)
 U=min(cap,max(map(len,candidates(g)))+1)
 ww=w*(1+(U+len(w)-1)//len(w))
 F={ww[i:i+k] for k in range(1,U+1) for i in range(len(w))}
 return {s for k in range(2,U+1) for s in map(''.join,product('01',repeat=k)) if s not in F and s[:-1] in F and s[1:] in F}

def checks():
 n=0
 for r in range(2,6):
  for g in permutations(range(1,r+1)):
   A=candidates(g);B=direct(g)
   if A!=B:
    print('FAIL',g,'only A',sorted(A-B),'only B',sorted(B-A));return
   n+=1
 print('PASS full enumeration',n)
 irregular=((1,2,5),(1,4,7),(2,4,7),(1,2,3,7),(1,3,5,6),(1,2,4,6,7))
 for gaps in irregular:
  assert candidates(gaps)==direct(gaps)
 print('PASS irregular profiles',len(irregular))
 assert len(candidates((1,2,3,4)))==10
 assert len(candidates((1,3,2,4)))==11
 for r in (3,4,5):
  D={}
  for g in permutations(range(1,r+1)):
   z=len(candidates(g));D.setdefault(z,[]).append(g)
  print('r',r,'spectra',[(z,len(g)) for z,g in sorted(D.items())]);print('representatives',[(z,g[0]) for z,g in sorted(D.items())])
if __name__=='__main__': checks(); print('ALL_DISTINCT_GAP_CIRCULAR_MAW_CHECKS_PASSED')
