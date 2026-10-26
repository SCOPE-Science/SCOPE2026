from itertools import product
from math import comb

def orbit_num(n, alphabet, generators):
 pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
 perms=[]
 for op in generators:
  if op=='sw':
   perms += [lambda s, e=e: tuple(0 if a==0 else (-a if (i==e)^(j==e) else a) for (i,j),a in zip(pairs,s)) for e in range(n)]
  elif op=='rev':
   perms += [lambda s: tuple(-a for a in s)]
  elif op=='rev3':
   perms += [lambda s: tuple((-a)%3 for a in s)]
  elif op=='rot':
   perms += [lambda s, e=e: tuple((a+((i==e)-(j==e)))%3 for (i,j),a in zip(pairs,s)) for e in range(n)]
  elif op=='gsw':
   perms += [lambda s, e=e: tuple((a+((i==e)^(j==e)))%2 for (i,j),a in zip(pairs,s)) for e in range(n)]
  elif op=='comp':
   perms += [lambda s: tuple(1-a for a in s)]
 all_s=set(product(alphabet,repeat=len(pairs))); num=0
 while all_s:
  cur=all_s.pop();stack=[cur];num+=1
  while stack:
   u=stack.pop()
   for op in perms:
    v=op(u)
    if v in all_s:all_s.remove(v);stack.append(v)
 return num

def formulas(n):
 m=comb(n,2);q=comb(n-1,2)
 sw=sum(comb(n,k)*3**(comb(k,2)+comb(n-k,2)) for k in range(n+1))//2**n
 rsw=sum(comb(n,k)*3**(k*(n-k)) for k in range(n+1))//2**n
 return {'digraph':3**m,'reverse':(3**m+1)//2,'switch':sw,'switch_reverse':(sw+rsw)//2,'rotate':3**q,'rotate_reverse':(3**q+1)//2,'graph':2**m,'graph_complement':2**(m-1) if m else 1,'graph_switch':2**q,'graph_switch_complement':2**max(0,m-n),'symmetric':1}
ops={'digraph':(range(3),[]),'reverse':(range(-1,2),['rev']),'switch':(range(-1,2),['sw']),'switch_reverse':(range(-1,2),['sw','rev']),'rotate':(range(3),['rot']),'rotate_reverse':(range(3),['rot','rev3']),'graph':(range(2),[]),'graph_complement':(range(2),['comp']),'graph_switch':(range(2),['gsw']),'graph_switch_complement':(range(2),['gsw','comp']),'symmetric':(range(1),[])}
for n in range(1,6):
 f=formulas(n)
 for name,(alphabet,gen) in ops.items():
  # for 0-edge no alphabet problem
  actual=orbit_num(n,alphabet,gen)
  assert actual==f[name],(n,name,actual,f[name])
 print('n',n,'counts',f)
four = formulas(4)
assert len(set(four.values())) == 11
assert len(set(formulas(3).values())) < 11
stirling_four = {name: 1 + 7*formulas(2)[name] + 6*formulas(3)[name] + formulas(4)[name] for name in four}
assert len(set(stirling_four.values())) == 11
print('noninjective_four_counts', stirling_four)
print('ALL_DIRECT_ORBITS_PASS')
