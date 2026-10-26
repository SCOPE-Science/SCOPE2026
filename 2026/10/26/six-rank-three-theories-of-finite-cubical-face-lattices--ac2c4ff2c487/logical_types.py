from functools import lru_cache
from collections import defaultdict
import sys,time
symbols=(0,1,2) # 2 means *
def le(a,b): return a==b or (a in (0,1) and b==2)
# Four relations in bit order: z<=x, x<=z, z<=y, y<=z
local={}
for a in symbols:
 for b in symbols:
  local[(a,b)]=tuple(sorted(set(sum((int(v)<<i) for i,v in enumerate((le(z,a),le(a,z),le(z,b),le(b,z)))) for z in symbols)))
@lru_cache(None)
def masktriple(a,b,c,h,g):
 state=1<<15
 for ab,m in (((0,0),a),((0,1),b),((0,2),c),((2,0),h),((2,2),g)):
  for _ in range(m):
   state2=0
   for v in range(16):
    if state>>v &1:
     for u in local[ab]: state2|=1<<(v&u)
   state=state2
 # add z=bottom, x,y ordinary
 return state|(1<<5)  # mask 1+4=5

def q1nn(a,b,c,h,g):
 pair=(int(b==0 and h==0))| (int(b==0 and c==0)<<1) # x<=y and y<=x
 return (pair,masktriple(a,b,c,h,g))
# x normal y bottom: z=bottom mask bits z<=x true, x<=z false, z<=y true,y<=z true => 13;
# z normal: z<=x,x<=z, z<=bottom false, bottom<=z true
@lru_cache(None)
def mask_nbottom(f,u):
 # local x: f fixed (0), u free (2). mask 2bits: z<=x,x<=z
 st=1<<3
 for x,num in ((0,f),(2,u)):
  vals=set((int(le(z,x)) + (int(le(x,z))<<1)) for z in symbols)
  for _ in range(num):
   st2=0
   for v in range(4):
    if st>>v &1:
     for w in vals:st2|=1<<(v&w)
   st=st2
 out=1<<13
 for v in range(4):
  if st>>v&1:out|=1<<(v|8)
 return out
# bottom y normal: z=bottom mask 1+2+4=7 (z<=x true, x<=z true, z<=y true, y<=z false)
# z normal: 0+2+4*(z<=y)+8*(y<=z)
@lru_cache(None)
def mask_bottom_n(f,u):
 st=1<<3
 for y,num in ((0,f),(2,u)):
  vals=set((int(le(z,y))+(int(le(y,z))<<1)) for z in symbols)
  for _ in range(num):
   st2=0
   for v in range(4):
    if st>>v&1:
     for w in vals:st2|=1<<(v&w)
   st=st2
 out=1<<7
 for v in range(4):
  if st>>v&1:out|=1<<(2|(v<<2))
 return out
# both bottom: z bottom all 4 true, z normal 2+8 true
QBOTH=(3,(1<<15)|(1<<10))

def theory(n):
 ptype=[]; pdetails=[]
 for f in range(n+1):
  types=set()
  types.add((2,mask_nbottom(f,n-f)))
  for a in range(f+1):
   for b in range(f-a+1):
    c=f-a-b
    for h in range(n-f+1):
     types.add(q1nn(a,b,c,h,n-f-h))
  ptype.append(frozenset(types));pdetails.append((f,len(types)))
 bot_types={(1,mask_bottom_n(f,n-f)) for f in range(n+1)}
 bot_types.add(QBOTH)
 ptype.append(frozenset(bot_types)); pdetails.append(('bottom',len(bot_types)))
 return frozenset(ptype),pdetails

if __name__=='__main__':
 start=time.perf_counter();seen={};sig=None
 for n in range(0,int(sys.argv[1]) if len(sys.argv)>1 else 28):
  sig,d=theory(n);k=seen.setdefault(sig,len(seen))
  print(n,'class',k,'1types',len(sig),'q1max',max(s for _,s in d),'time',round(time.perf_counter()-start,2),flush=True)
