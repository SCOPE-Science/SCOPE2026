"""Exact finite checks for biased-majority modal reductions; Python 3 stdlib."""
from itertools import product
from fractions import Fraction

def var(i): return ('v',i)
def neg(f): return ('not',f)
def conj(f,g): return ('and',f,g)
def cmp_(f,g): return ('cmp',f,g)
def bval(f,t):
 if f[0]=='v': return t[f[1]]
 if f[0]=='not': return not bval(f[1],t)
 if f[0]=='and': return bval(f[1],t) and bval(f[2],t)
 assert f[0]=='const'
 return f[1]
def reduction(f,k,weights):
 if f[0]=='v': return f
 if f[0]=='not':return neg(reduction(f[1],k,weights))
 if f[0]=='and':return conj(reduction(f[1],k,weights),reduction(f[2],k,weights))
 assert f[0]=='cmp'
 a=reduction(f[1],k,weights);b=reduction(f[2],k,weights)
 av=sum(w for t,w in weights if bval(a,t));bv=sum(w for t,w in weights if bval(b,t))
 assert av!=bv or all(bval(a,t)==bval(b,t) for t,w in weights)
 return ('const',av>=bv)
def evalf(f,labels,edge,v):
 if f[0]=='v':return labels[v][f[1]]
 if f[0]=='not':return not evalf(f[1],labels,edge,v)
 if f[0]=='and':return evalf(f[1],labels,edge,v) and evalf(f[2],labels,edge,v)
 assert f[0]=='cmp'
 n=len(labels)
 left=sum(evalf(f[1],labels,edge,j) for j in range(n) if edge[v*n+j]);right=sum(evalf(f[2],labels,edge,j) for j in range(n) if edge[v*n+j]);return left>=right

def run():
 k=2; ps=(Fraction(1,3),Fraction(1,5))
 ts=list(product((False,True),repeat=k))
 ws=[(t,ps[0] if t[0] else 1-ps[0]) for t in ts]
 ws=[(t, w*(ps[1] if t[1] else 1-ps[1])) for t,w in ws]
 assert sorted(w for t,w in ws)==[Fraction(1,15),Fraction(2,15),Fraction(4,15),Fraction(8,15)]
 assert len({sum(w for i,(t,w) in enumerate(ws) if (mask>>i)&1) for mask in range(1<<4)})==16
 p,q=var(0),var(1)
 f1=cmp_(p,q)
 f2=cmp_(p,p)
 f3=cmp_(cmp_(p,q),p)
 f4=conj(p,cmp_(q,p))
 fs=[f1,f2,f3,f4]
 for f in fs:
  r=reduction(f,k,ws)
  print('reduct:',f,'->',r)
 for n in range(1,4):
  for f in fs:
   total=Fraction(0);uniform=Fraction(0)
   r=reduction(f,k,ws)
   for lab_ix in product(range(4),repeat=n):
    labs=[ws[i][0] for i in lab_ix];lp=__import__('math').prod(ws[i][1] for i in lab_ix)
    for bits in range(1<<(n*n)):
     edges=[bool(bits>>j&1) for j in range(n*n)]
     ep=lp/Fraction(1<<(n*n))
     total+=ep*evalf(f,labs,edges,0)
     uniform+=ep*all(evalf(f,labs,edges,v)==bval(r,labs[v]) for v in range(n))
   assert Fraction(0)<=total<=1 and Fraction(0)<=uniform<=1
   if n==3 and f==f2:assert uniform==1
   print('n',n,'f',fs.index(f)+1,'prob',str(total),'uniform',str(uniform))
 print('ALL_CHECKS_OK')
if __name__=='__main__':run()
