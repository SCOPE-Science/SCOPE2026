from collections import Counter
p=3
pts=[(x,y,1) for x in range(9) for y in range(9)]+[(x,1,0) for x in range(9)]+[(1,0,0)]
def add(x,y):return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def mul(x,y):return ((x%3*(y%3)+2*(x//3)*(y//3))%3)+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
def smul(*args):
 v=1
 for a in args:v=mul(v,a)
 return v
def sm(*args):
 v=0
 for a in args:v=add(v,a)
 return v
C=[];lines=[]
for x,y,z in pts:
 F=sm(smul(x,x,y),smul(y,y,z),smul(z,z,z))
 if F==0:
  C.append((x,y,z)); lines.append((smul(2,x,y),sm(smul(x,x),smul(2,y,z)),smul(y,y)))
print('rational_pts',len(C));print('pts',C)
cover=Counter()
for pt in pts:
 cover[pt]=sum(1 for l in lines if sm(smul(pt[0],l[0]),smul(pt[1],l[1]),smul(pt[2],l[2]))==0)
print('hist',sorted(Counter(cover.values()).items()))
print('uncovered',[p for p in pts if cover[p]==0]);print('lines',lines)
# hermitian
H=[];LH=[]
for x,y,z in pts:
 if sm(smul(x,x,x,x),smul(y,y,y,y),smul(z,z,z,z))==0:
  H.append((x,y,z));LH.append((smul(x,x,x),smul(y,y,y),smul(z,z,z)))
C2=Counter(sum(1 for l in LH if sm(smul(pt[0],l[0]),smul(pt[1],l[1]),smul(pt[2],l[2]))==0) for pt in pts)
print('hermitian',len(H),'hist',sorted(C2.items()))

def canon_line(v):
 pivot=next(t for t in v if t)
 inv=next(i for i in range(1,9) if mul(pivot,i)==1)
 return tuple(mul(inv,t) for t in v)
assert len(C)==16 and len({canon_line(v) for v in lines})==16
assert dict(Counter(cover.values()))=={0:6,1:41,2:24,3:12,4:5,5:3}
assert len([z for z in pts if cover[z]==0])==6
assert len(H)==28 and dict(C2)=={1:28,4:63}
print('EXAMPLES_VERIFIED')
