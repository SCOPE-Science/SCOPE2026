#!/usr/bin/env python3
"""Affine residue-interval exact certificate for S_{2,4h+2}."""
def blocks(h, K=5):
 g=4*h+2; P=3*g+3
 A=[(2,2),(g,2*g-2),(g+1,2*g-1),(2*g+2,2*g+2),(2*g+3,3*g+1)]
 for k in range(1,K):
  o=k*P
  A += [(o+2,o+g-4),(o+g,o+2*g-2),(o+g+1,o+2*g-1),(o+2*g+3,o+3*g+1)]
 assert all((b-a)%4==0 and b>=a for a,b in A)
 for i,(a,b) in enumerate(A):
  for c,d in A[i+1:]:
   if (a-c)%4==0: assert b<c or d<a,('overlap',h,(a,b),(c,d))
 return A

def residue(h):
 g=4*h+2
 return [(2,g-4),(g,2*g-2),(g+1,2*g-1),(2*g+3,3*g+1)]

def disjoint(U,V):
 for a,b in U:
  for c,d in V:
   if (a-c)%4==0 and max(a,c)<=min(b,d):return False,(a,b,c,d)
 return True,None

def cover(U,lo,hi):
 for p in range(4):
  start=lo+(p-lo)%4; end=hi-(hi-p)%4
  if start>end:continue
  ints=[]
  for a,b in U:
   if a%4==p:
    x=max(a,start); y=min(b,end)
    x+=(p-x)%4; y-=(y-p)%4
    if x<=y:ints.append((x,y))
  ints.sort();pos=start
  for a,b in ints:
   if pos<a:return False,(p,pos,a,b)
   if b+4>pos:pos=b+4
   if pos>end:break
  if pos<=end:return False,(p,pos,end)
 return True,None

def verify(h):
 g=4*h+2; P=3*g+3; A=blocks(h);R=residue(h);E=2*g+2
 RR=[(a+c,b+d) for a,b in R for c,d in R]
 ER=[(a+E,b+E) for a,b in R]
 for su in (RR,ER):
  ok,detail=disjoint(R,[(a-k*P,b-k*P) for a,b in su for k in range(3)])
  assert ok,('modular sumfree',h,detail)
 sums=[]
 for i,(a,b) in enumerate(A):
  for j,(c,d) in enumerate(A[i:],start=i):
   if i==j:
    if b-a>=4:sums.append((2*a+4,2*b-4))
   else:sums.append((a+c,b+d))
 ok,detail=cover(A+sums,g,5*P-1)
 assert ok,('greedy saturation',h,detail)
 return len(A),len(sums)

def raw(h):
 g=4*h+2;P=3*g+3
 cand={x for a,b in blocks(h) for x in range(a,b+1,4) if x<5*P}
 observed=[2,g]; seen={g+2}
 while observed[-1]<5*P-1:
  n=observed[-1]+1
  while n in seen:n+=1
  seen.update(n+a for a in observed);observed.append(n)
 assert cand=={n for n in observed if n<5*P},('raw mismatch',h)
 return len(cand)

def check_affine_endpoint_bound():
    # Every endpoint is u*h+v with u divisible by 4.
    g=(4,2); p=(12,9)
    def add(x,y):return (x[0]+y[0],x[1]+y[1])
    def scale(x,k):return (x[0]*k,x[1]*k)
    def plus(x,c):return (x[0],x[1]+c)
    raw=[((0,2),(0,2)),(g,plus(scale(g,2),-2)),(plus(g,1),plus(scale(g,2),-1)),(plus(scale(g,2),2),plus(scale(g,2),2)),(plus(scale(g,2),3),plus(scale(g,3),1))]
    R=[((0,2),plus(g,-4)),(g,plus(scale(g,2),-2)),(plus(g,1),plus(scale(g,2),-1)),(plus(scale(g,2),3),plus(scale(g,3),1))]
    for k in range(1,5):raw.extend([(add(x,scale(p,k)),add(y,scale(p,k))) for x,y in R])
    endpoints=[x for ab in raw for x in ab]
    for i,(a,b) in enumerate(raw):
        for j,(c,d) in enumerate(raw[i:],start=i):
            if i==j:
                if b[0]>a[0] or b[1]-a[1]>=4:
                    endpoints.extend([plus(scale(a,2),4),plus(scale(b,2),-4)])
            else:endpoints.extend([add(a,c),add(b,d)])
    E=plus(scale(g,2),2)
    for src in (R,[(add(x,E),add(y,E)) for x,y in R], [(add(a,c),add(b,d)) for a,b in R for c,d in R]):
        for a,b in src:
            for k in range(3):endpoints.extend([add(a,scale(p,-k)),add(b,scale(p,-k))])
    endpoints.extend([g,plus(scale(p,5),-1)])
    quotient=[]
    for a,v in endpoints:
        assert a%4==0
        for residue in range(4):
            lower=(v+(residue-v)%4-residue)//4
            upper=(v-(v-residue)%4-residue)//4
            quotient.extend([lower,upper])
    assert min(quotient)>=-50 and max(quotient)<=70,(min(quotient),max(quotient))
    return min(quotient),max(quotient)

def check_unique_circular_gap(h):
    g=4*h+2;P=3*g+3
    R=sorted(n for a,b in residue(h) for n in range(a,b+1,4))
    diffs=[(R[(i+1)%len(R)]-R[i])%P for i in range(len(R))]
    assert len(R)==g+1 and sum(diffs)==P
    assert sum(diffs[i]==1 and diffs[(i+1)%len(diffs)]==4 for i in range(len(diffs)))==1

def main():
 print("Affine intercept certificate:", check_affine_endpoint_bound())
 for h in range(2,133):verify(h);check_unique_circular_gap(h)
 for h in range(2,14):raw(h)
 print('PASS: exact mod-4 residue disjointness and complete greedy exclusion coverage for h=2..132.')
 print('PASS: direct independent sequence replay h=2..13.')
 print('AFFINE LEMMA: all parity-by-four quotient endpoints have integer form alpha*h+beta with -50<=beta<=70, even after allowed modular shifts and distinct-sum endpoints. Adjacency adds at most one to beta, so for h>=123 relative ordering cannot change. Verifying through h=132 proves universal h>=2.')
if __name__=='__main__':main()
