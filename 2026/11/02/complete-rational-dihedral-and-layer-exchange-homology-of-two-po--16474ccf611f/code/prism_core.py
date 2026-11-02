from itertools import combinations
from collections import defaultdict

def graph(n):
 V=list(range(2*n)); E=sorted({tuple(sorted((a,b))) for i in range(n) for layer in range(2) for a,b in [((layer*n+i),(layer*n+(i+1)%n)),(i,n+i)]}); return V,E

def act(n,r=0,s=0,t=0):
 return {layer*n+i:(layer^t)*n+ (( (-i if s else i)+r)%n) for layer in range(2) for i in range(n)}

def char(n,r=0,s=0,t=0):
 V,E=graph(n); m=len(E); g=act(n,r,s,t); eix={e:i for i,e in enumerate(E)}
 gg=lambda e:tuple(sorted((g[e[0]],g[e[1]])))
 gm=[eix[gg(e)] for e in E]; ss=[1 if g[e[0]]<g[e[1]] else -1 for e in E]
 vfix=sum(g[v]==v for v in V)
 c0=sum({g[v],g[w]}=={v,w} for v,w in combinations(V,2))
 c1=sum(ss[i]*(vfix - sum(g[v]==v for v in e)) for i,e in enumerate(E) if gm[i]==i)
 c2=0
 for i,j in combinations(range(m),2):
  if set(E[i])&set(E[j]):continue
  if gm[i]==i and gm[j]==j:c2+=ss[i]*ss[j]
  elif gm[i]==j and gm[j]==i:c2-=ss[i]*ss[j]
 # face char via 2 caps plus lateral faces
 # cap fixed if t=0 (regardless rotation/reflection), lateral fixed count if i maps to i as edge of n-cycle
 fcap=2 if not t else 0
 flat=sum({(r+(-i if s else i))%n,(r+(-(i+1) if s else i+1))%n}=={i,(i+1)%n} for i in range(n))
 eps=(-1)**(s+t)
 h1=eps*(fcap+flat)
 h2=c0-c1+c2-1+h1
 return (c0,c1,c2,fcap,flat,eps,h1,h2)

if __name__=='__main__':
 for n in (5,6,7,8,9,10):
  print('N',n,'Euler',char(n)[0]-char(n)[1]+char(n)[2],'h1',char(n)[-2], 'h2',char(n)[-1]);
  for typ, args in [('rot1',(1,0,0)),('rot2',(2,0,0)),('half',(n//2,0,0)),('ref0',(0,1,0)),('ref1',(1,1,0)),('swap',(0,0,1)),('rot-swap',(1,0,1)),('ref-swap0',(0,1,1)),('ref-swap1',(1,1,1))]:
   print(typ,args,char(n,*args)[-4:])
