#!/usr/bin/env python3
"""Independent direct checker for extremal rich ternary additive-cube-free words."""
import itertools,sys
from pathlib import Path

def rich(w):
 p={''}
 for i in range(len(w)):
  for j in range(i+1,len(w)+1):
   s=w[i:j]
   if s==s[::-1]:p.add(s)
 return len(p)==len(w)+1

def acfree(w):
 n=len(w)
 for k in range(1,n//3+1):
  for i in range(n-3*k+1):
   sums=[sum(map(int,w[i+j*k:i+(j+1)*k])) for j in range(3)]
   if sums[0]==sums[1]==sums[2]:return False
 return True

def main():
 lines=Path(sys.argv[1]).read_text().splitlines();counts={int(x.split()[1]):int(x.split()[2]) for x in lines if x.startswith('COUNT ')}
 reps=[x[4:] for x in lines if x.startswith('REP ') and len(x[4:])==104]
 assert lines[-1]=='VERIFY_ENUM_OK'; assert counts[104]==8 and counts[105]==0
 assert len(reps)==8 and len(set(reps))==8
 for n in range(11):
  num=0
  for t in itertools.product('012',repeat=n):
   s=''.join(t)
   if rich(s) and acfree(s):num+=1
  assert num==counts[n],(n,num,counts[n])
 for s in reps:
  assert len(s)==104 and set(s)==set('012') and rich(s) and acfree(s)
  for c in '012':assert not (rich(s+c) and acfree(s+c))
 assert {s[::-1] for s in reps}==set(reps)
 assert {''.join(str(2-int(c)) for c in s) for s in reps}==set(reps)
 group=[]
 unvisited=set(reps)
 while unvisited:
  w=next(iter(unvisited));orbit={w,w[::-1],''.join(str(2-int(c)) for c in w),''.join(str(2-int(c)) for c in w[::-1])}
  assert orbit<=set(reps);group.append(orbit);unvisited-=orbit
 print('VERIFY_OK max_len=104 labeled=8 symmetry_orbits='+str(len(group))+' independently_bruteforced_lengths=0..10')
if __name__=='__main__':main()
