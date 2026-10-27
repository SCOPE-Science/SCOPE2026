from math import comb
from itertools import product
T=[[-1 if (k.bit_count()&1)==0 else 1 for k in range(1<<i)] for i in range(12)]
def com(s,i):
 return (-1 if i%2 else 1)*sum(comb(k,i)*x for k,x in enumerate(s) if k>=i)
def comp(s, upto, cap=100000):
 s=list(s)
 for i in range(upto+1):
  c=com(s,i)
  den=1<<(i*(i-1)//2)
  if c%den:return i-1,len(s)
  b=c//den
  if len(s)+abs(b)*(1<<i)>cap:return -5,len(s)
  if b:
   blk=T[i] if b>0 else [-q for q in T[i]]
   s.extend(blk*abs(b))
 return upto,len(s)

if __name__=="__main__":
 sign_word=tuple(-1 if k.bit_count()%2==0 else 1 for k in range(16))+(-1,)
 six=comp(sign_word,6,cap=20000)
 seven=comp(sign_word,7,cap=20000)
 assert six==(6,960),(six,sign_word)
 assert seven==(6,960),(seven,sign_word)
 print("explicit length-17 word:",sign_word)
 print("six-completion and final length:",six)
 print("seven-completion:",seven, "(not attainable)")
