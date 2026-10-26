import itertools,time,collections
from tri_probe import mul,powpoly
GL=[]
for m in itertools.product((0,1),repeat=4):
 a,b,c,d=m
 if a*d^b*c:GL.append(m)
assert len(GL)==6

def cubicmap(mat):
 a,b,c,d=mat;out=[]
 for i in range(4):
  p=mul(powpoly([a,b],3-i),powpoly([c,d],i))
  out.append(sum(x<<k for k,x in enumerate(p)))
 return out
GLc=[cubicmap(m) for m in GL]
trans=[]
for a in GLc:
 for b in GLc:
  for swap in (False,True):
   bs=[]
   for i in range(4):
    for j in range(4):
     val=0
     for s in range(4):
      if a[i]>>s&1:
       for t in range(4):
        if b[j]>>t&1:val^=1<<((t*4+s) if swap else (s*4+t))
     bs.append(val)
   trans.append(bs)
assert len(trans)==72

def xform(f,basis):
 out=0
 while f:
  bit=f&-f;out^=basis[bit.bit_length()-1];f-=bit
 return out

def get_orbits():
 seen=bytearray(65536); result=[]
 for f in range(1,65536):
  if seen[f]:continue
  orb={xform(f,b) for b in trans}
  for v in orb:seen[v]=1
  result.append((f,len(orb)))
 assert sum(z for _,z in result)==65535
 return result
if __name__=='__main__':
 t=time.monotonic();o=get_orbits(); print('orbits',len(o),'sum',sum(x[1] for x in o),'sizes',collections.Counter(z for _,z in o),'time',time.monotonic()-t)
