from itertools import permutations,product
from math import factorial,comb

def _count_fixed(n,pi,sig):
    edges=[(0,1),(0,2),(1,2)]
    idx={p:i*(2*n-1) for i,p in enumerate(edges)}
    dim=3*(2*n-1)
    def e(i,j,x,y):
        off=idx[(i,j)]
        if y==0:return 1<<(off+x)
        return (1<<(off+x)) ^ (1<<(off+n+y-1))
    pivots={}
    for i,j in edges:
      for x,y in product(range(n),repeat=2):
        ii,jj=pi[i],pi[j]
        xx,yy=sig[i][x],sig[j][y]
        t=0
        if ii>jj:
            ii,jj=jj,ii;xx,yy=yy,xx;t=1
        m=e(i,j,x,y)^e(ii,jj,xx,yy)
        z=m|(t<<dim)
        while m:
            bit=m.bit_length()-1
            if bit not in pivots:
                pivots[bit]=z
                break
            z^=pivots[bit];m=z&((1<<dim)-1)
        else:
            if z>>dim:return 0
    return 2**(dim-len(pivots))

def theoretical(n):
 P=comb(n+3,3)
 Q=n//2+1 if n%2==0 else 0
 C=(n//2+1)*((n+1)//2+1)
 numerator=P**3+3*P*Q*Q+4*Q**3+12*Q*(C+int(n%4==0))+8*(P+Q)
 assert numerator%48==0
 V=numerator//48
 assert (P**3+3*P*Q*Q+4*Q**3)%8==0
 U=(P**3+3*P*Q*Q+4*Q**3)//8
 assert Q*(C+int(n%4==0))%2==0
 trans=Q*(C+int(n%4==0))//2
 assert (P+Q)%2==0
 cyc=(P+Q)//2
 return U,trans,cyc,V

def run(n):
 perms=list(permutations(range(n)))
 ps=[(0,1,2),(1,0,2),(1,2,0)]
 av=[]
 for pi in ps:
    s=0
    for sig in product(perms,repeat=3):s+=_count_fixed(n,pi,sig)
    assert s % (factorial(n)**3)==0
    av.append(s//(factorial(n)**3))
 print('n=',n,'fixed coset averages=',tuple(av),'orbits=',(av[0]+3*av[1]+2*av[2])//6)
 assert av==list(theoretical(n)[:3]),(av,theoretical(n))
 assert (av[0]+3*av[1]+2*av[2])//6==theoretical(n)[3]
for n in range(1,5):run(n)
for n in range(1,50):
 u,t,c,v=theoretical(n)
 assert (u+3*t+2*c)%6==0
 assert v==(u+3*t+2*c)//6
print('ALL_TESTS_PASS')
