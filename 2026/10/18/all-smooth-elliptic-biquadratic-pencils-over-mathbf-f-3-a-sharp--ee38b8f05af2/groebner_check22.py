import sympy as s,time
U,V,S,T=s.symbols('U V S T');x=(U,V,S,T)
q=(lambda a,b:(a*a,a*b,b*b))
mon=[a*b for a in q(U,V) for b in q(S,T)]
parts=[[s.diff(m,z) for m in mon] for z in x]
valid=[];start=time.monotonic();count=0
for m in range(1,19683):
 cc=[];n=m
 for k in range(9):cc.append(n%3);n//=3
 if next(v for v in cc if v)!=1: continue
 good=True
 for aa,bb in [(U,V),(V,U)]:
  for ss,tt in [(S,T),(T,S)]:
   repl={aa:1,ss:1};pcoords=(bb,tt)
   pp=[]
   for d in parts:
    poly=sum(c*z for c,z in zip(cc,d) if c).subs(repl)
    if poly:pp.append(poly)
   g=s.groebner(pp,*pcoords,modulus=3)
   if list(g)!=[s.Integer(1)]:good=False;break
  if not good:break
 if good:valid.append(m)
 count+=1
 if count%2000==0:print('processed',count,'smooth',len(valid),'elapsed',round(time.monotonic()-start,1),flush=True)
open('groebner_smooth_codes.txt','w').write('\n'.join(map(str,valid))+'\n')
print('FINAL',count,len(valid),'elapsed',time.monotonic()-start)
