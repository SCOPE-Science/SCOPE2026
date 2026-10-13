"""Independent brute-force total domination test and exact labeled-species comparison."""
import itertools,math,sys
from collections import Counter
from fractions import Fraction

def exact_coeffs(n):
    C={}
    for p in range(n+1):
      for q in range(n+1):
        if p+q<2:continue
        v=1+p+2*q
        if v>n:continue
        k=p+2*q
        C[(v,k)]=C.get((v,k),Fraction(0))+Fraction(1,math.factorial(p)*math.factorial(q))
    if n>=4:C[(4,3)]-=Fraction(1,2)
    E={(0,0):Fraction(1)}
    power={(0,0):Fraction(1)}
    for j in range(1,n+1):
      nxt={}
      for (v,k),a in power.items():
        for (w,l),b in C.items():
          if v+w<=n:
            key=(v+w,k+l)
            nxt[key]=nxt.get(key,Fraction(0))+a*b
      power=nxt
      for key,c in power.items(): E[key]=E.get(key,Fraction(0))+c/math.factorial(j)
    result=Counter()
    for (v,k),c in E.items():
      if v==n-1:
        cc=c*math.factorial(n)
        assert cc.denominator==1
        result[k]+=int(cc)
    if n%3==0:
      result[2*(n//3)]+=math.factorial(n)//(2**(n//3)*math.factorial(n//3))
    return +result

def actual(n):
    es=list(itertools.combinations(range(n),2))
    neighborhoods=[]
    for i,e in enumerate(es):
        bitset=sum(1<<j for j,f in enumerate(es) if j!=i and len(set(e)&set(f)))
        neighborhoods.append(bitset)
    status=bytearray(1<<len(es))
    for mask in range(1,len(status)):
      if all(mask&nb for nb in neighborhoods): status[mask]=1
    cc=Counter()
    for mask in range(1,len(status)):
        if not status[mask]:continue
        v=mask
        while v:
            bit=v&(-v)
            if status[mask-bit]:break
            v-=bit
        else:
            cc[mask.bit_count()]+=1
    return cc
if __name__=='__main__':
    for n in range(3,8):
        a=actual(n);p=exact_coeffs(n)
        print('n=',n,'actual=',dict(sorted(a.items())),'predicted=',dict(sorted(p.items())),flush=True)
        assert a==p,(n,a,p)
    print('VERIFY_OK n=3..7 all_subset_checks='+str(sum(2**(n*(n-1)//2) for n in range(3,8)))+' minimal_set_coefficients_agree',flush=True)
