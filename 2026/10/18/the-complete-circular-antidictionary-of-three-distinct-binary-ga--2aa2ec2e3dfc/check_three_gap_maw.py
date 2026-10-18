from itertools import combinations

def expected(a,b,c):
 assert 1<=a<b<c
 return ({'00','1'*(c+1), '1'*(b+1)+'0'+'1'*(a+1),
         '0'+'1'*a+'0'+'1'*(b+1), '1'*(a+1)+'0'+'1'*b+'0',
         '0'+'1'*a+'0'+'1'*a+'0', '0'+'1'*b+'0'+'1'*a+'0'}|
        {'0'+'1'*j+'0' for j in range(1,c) if j not in (a,b)})

def actual(a,b,c):
 w='0'+'1'*a+'0'+'1'*b+'0'+'1'*c
 n=len(w);W=(w+w)
 fact={W[i:i+k] for k in range(1,n+1) for i in range(n)}
 maws=set()
 for v in fact:
  if len(v)>=n:continue
  for ch in '01':
   word=v+ch
   if word not in fact and word[1:] in fact:maws.add(word)
 return maws

def independent(a,b,c):
 w='0'+'1'*a+'0'+'1'*b+'0'+'1'*c
 n=len(w)
 # Generate all factor length k as edges of cyclic suffix index, then test candidate from two extension routes.
 layers=[{''}]
 for k in range(1,n+1):layers.append({''.join(w[(i+j)%n] for j in range(k)) for i in range(n)})
 result=set()
 for k in range(2,n+1):
  U=layers[k-1]
  for u in U:
   for ch in '01':
    v=u+ch
    if v not in layers[k] and v[1:] in U:result.add(v)
 return result

def main():
 count=0;hi=0
 for c in range(3,25):
  for a,b in combinations(range(1,c),2):
   x=expected(a,b,c);y=actual(a,b,c)
   if x!=y:raise AssertionError((a,b,c,'missing',y-x,'extra',x-y))
   if len(x)!=c+4:raise AssertionError(('count',a,b,c,len(x)))
   count+=1;hi=max(hi,3+a+b+c)
 for a,b,c in [(1,2,3),(1,4,9),(2,3,7),(2,6,10),(3,7,12)]:
  assert actual(a,b,c)==independent(a,b,c)==expected(a,b,c)
 # Reversal/cyclic rotation invariance of actual circular MAW sets.
 for a,b,c in [(1,2,3),(2,5,8),(2,7,12)]:
  w='0'+'1'*a+'0'+'1'*b+'0'+'1'*c
  n=len(w)
  for rot in range(n):
   v=w[rot:]+w[:rot]
   # Generate MAWs of rotated representation independently.
   layers=[{''}]
   for k in range(1,n+1):layers.append({''.join(v[(i+j)%n] for j in range(k)) for i in range(n)})
   cur=set()
   for k in range(2,n+1):
    for u in layers[k-1]:
     for ch in '01':
      z=u+ch
      if z not in layers[k] and z[1:] in layers[k-1]:cur.add(z)
   assert cur==expected(a,b,c)
 print('ALL_THREE_GAP_MAW_CHECKS_PASSED', 'parameter_triples',count, 'max_cycle_length',hi,'independent_examples',5,'rotation_tests',sum(3+a+b+c for a,b,c in [(1,2,3),(2,5,8),(2,7,12)]))
if __name__=='__main__':main()
