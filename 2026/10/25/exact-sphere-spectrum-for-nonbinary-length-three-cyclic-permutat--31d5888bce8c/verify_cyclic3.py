from collections import Counter,defaultdict
from itertools import product
from fractions import Fraction

def outputs(x):
    n=len(x)
    yy={x}
    for j in range(n-2):
        a,b,c=x[j:j+3]
        for y in ((b,c,a),(c,a,b)):
            yy.add(x[:j]+y+x[j+3:])
    return yy

def direct_defect(x):
    n=len(x)
    h=sum(x[i]==x[i+1]==x[i+2] for i in range(n-2))
    c=sum(x[i+1]!=x[i+2] and x[i] in (x[i+1],x[i+2]) and x[i+3] in (x[i+1],x[i+2]) for i in range(n-3))
    return 2*h+c

def transfer_distribution(q,n):
    dd={('T',2):q,('T',0):q*(q-1),('S',0):2*q*(q-1),('D',0):q*(q-1)*(q-2)}
    v=defaultdict(int)
    for (s,d),v0 in dd.items():v[s,d]+=v0
    trans={'T':[('T',2,1),('S',0,q-1)],'S':[('T',1,1),('S',1,1),('D',0,q-2)],'D':[('T',0,1),('S',0,1),('D',0,q-2)]}
    for _ in range(n-3):
        nxt=defaultdict(int)
        for (s,d),num in v.items():
            for ns,add,mult in trans[s]:nxt[ns,d+add]+=num*mult
        v=nxt
    pol=Counter()
    for (s,d),num in v.items():pol[2*n-3-d]+=num
    return +pol

checks=0
configs=[(2,range(3,12)),(3,range(3,10)),(4,range(3,9)),(5,range(3,8))]
for q,lens in configs:
  for n in lens:
    measured=Counter()
    for x in product(range(q),repeat=n):
        ylen=len(outputs(x));assert ylen==2*n-3-direct_defect(x),(q,n,x,ylen,direct_defect(x))
        measured[ylen]+=1;checks+=1
    transfer=transfer_distribution(q,n)
    assert measured==transfer,(q,n,measured,transfer)
    assert sum(measured.values())==q**n
    exp=Fraction(sum(k*v for k,v in measured.items()),q**n)
    theoretical=Fraction(2*n-3,1)-Fraction(2*(n-2),q*q)-Fraction(4*(n-3)*(q-1),q**3)
    assert exp==theoretical,(q,n,exp,theoretical)
    maxcount=measured[2*n-3]
    if q>=3:
        fm=0
        if n==3:fm=q*(q-1)*(q+1)
        elif n==4:fm=q*(q-1)*(q*q+q-5)
        else:
            # direct recurrence initial F3 F4 F5
            aa=q*(q-1)*(q+1);bb=q*(q-1)*(q*q+q-5);cc=q*(q-2)*(q-1)**2*(q+4)
            if n==5:fm=cc
            else:
                for l in range(6,n+1):aa,bb,cc=bb,cc,(q-2)*(cc+bb)+(q-1)*(q-2)*aa
                fm=cc
        assert maxcount==fm,(q,n,maxcount,fm)
    print('q=%d n=%d all=%d max=%d max_count=%d'%(q,n,q**n,max(measured),maxcount))
print('q4 n6 distribution',sorted(transfer_distribution(4,6).items()))
print('TOTAL_WORDS',checks)
print('VERIFY_OK')
