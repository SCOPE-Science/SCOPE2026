from itertools import product
from math import comb

def valid_pair(n, op0, opa):
    N=1<<n; full=N-1
    subset=lambda a,b: a&~b==0
    for c in (op0,opa):
        if c[0] != 0: return (False,False,False)
    for x in range(N):
        if not subset(op0[x],opa[x]) or not subset(opa[x],op0[full]): return (False,False,False)
        for y in range(N):
            if not subset(op0[(full^x)|y]&op0[x],op0[y]): return (False,False,False)
            if not subset(op0[(full^x)|y]&opa[x],opa[y]): return (False,False,False)
    serial = op0[full]==full and opa[full]==full
    det=True
    for x in range(N):
        for y in range(N):
            if not subset(op0[x|y],op0[x]|opa[y]) or not subset(opa[x|y],opa[x]|opa[y]): det=False
    return (True,serial,det)

def check(n):
  N=1<<n
  opts=[]
  for vals in product(range(N),repeat=N-1): opts.append((0,)+vals)
  counts=[0,0,0,0]
  for op0 in opts:
    for opa in opts:
      ok,s,d=valid_pair(n,op0,opa)
      if ok:
        counts[0]+=1
        counts[1]+=s
        counts[2]+=d
        counts[3]+=s and d
  return counts

for n in (1,2):
 c=check(n)
 expected={1:[2,1,2,1],2:[49,36,16,9]}[n]
 print(n,c,expected)
 assert c==expected
print('ALL_CHECKS_OK')
