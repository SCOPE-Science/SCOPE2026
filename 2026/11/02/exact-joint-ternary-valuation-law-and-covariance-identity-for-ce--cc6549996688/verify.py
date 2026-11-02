from fractions import Fraction as Q
from math import factorial

def val3(z):
 t=0
 while z and z%3==0:z//=3;t+=1
 return t

def direct(L):
 P=3**L; counts={}
 for n in range(P):
  x=val3(factorial(2*n)//factorial(n)**2)
  y=val3(factorial(3*n)//factorial(n)**3)
  counts[x,y]=counts.get((x,y),0)+1
 return counts

def transfer(L):
 st={(0,0,0):1}
 for i in range(L):
  nxt={}
  for (c,x,y),count in st.items():
   for d in range(3):
    z=int(2*d+c>=3)
    key=(z,x+z,y+d)
    nxt[key]=nxt.get(key,0)+count
  st=nxt
 out={}
 for (c,x,y),num in st.items():out[x,y]=out.get((x,y),0)+num
 return out

def check(L):
 q=transfer(L); tot=3**L
 eX=sum(x*c for (x,y),c in q.items())*Q(1,tot)
 eY=sum(y*c for (x,y),c in q.items())*Q(1,tot)
 vX=sum(x*x*c for (x,y),c in q.items())*Q(1,tot)-eX**2
 vY=sum(y*y*c for (x,y),c in q.items())*Q(1,tot)-eY**2
 cov=sum(x*y*c for (x,y),c in q.items())*Q(1,tot)-eX*eY
 z=Q(1,3)**L
 assert eX==Q(L,2)-Q(1-z,4)
 assert eY==L
 assert vX==Q(L,2)-Q(7,16)+z/2-z*z/16
 assert vY==Q(2*L,3)
 assert cov==eX
 if L<=7:assert q==direct(L)
 return len(q)
if __name__=='__main__':
 sizes=[check(L) for L in range(1,13)]
 print('VERIFY_OK direct_lengths=1..7 transfer_lengths=1..12 joint_cell_counts='+repr(sizes))
