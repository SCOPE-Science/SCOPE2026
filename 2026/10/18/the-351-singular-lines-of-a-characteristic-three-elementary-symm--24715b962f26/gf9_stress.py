"""Optional finite-extension stress-test, using F9=F3[z]/(z*z+1)."""
from itertools import permutations
from collections import Counter
F=range(9)
add=[[((a%3+b%3)%3)+3*((a//3+b//3)%3) for b in F] for a in F]
mul=[[((a%3*b%3+2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in F] for a in F]

def e3(items):
    c=[1,0,0,0]
    for v in items:
        for d in range(3,0,-1):c[d]=add[c[d]][mul[v][c[d-1]]]
    return c[3]

counts=Counter()
for r in range(1,8):
 for s in range(1,9-r):
  t=9-r-s
  for a,b,c in permutations(F,3):
   va=[a]*r+[b]*s+[c]*t
   sing=(e3(va[1:])==0 and e3(va[:r]+va[r+1:])==0 and e3(va[:r+s]+va[r+s+1:])==0)
   expected=False
   if sorted((r,s,t))==[1,1,7]:
    expected=next(v for count,v in ((r,a),(s,b),(t,c)) if count==7)==0
   if sorted((r,s,t))==[1,4,4]:
    four=[v for count,v in ((r,a),(s,b),(t,c)) if count==4]
    expected=add[four[0]][four[1]]==0
   assert sing==expected,(r,s,t,a,b,c,sing,expected)
   counts['tested']+=1
   counts['singular']+=int(sing)
print('GF9_OK',dict(counts))
