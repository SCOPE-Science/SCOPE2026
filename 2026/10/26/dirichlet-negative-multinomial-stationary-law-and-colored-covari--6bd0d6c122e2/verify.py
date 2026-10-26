from fractions import Fraction as F
from itertools import product


def moment_builder(N,M,t,left,right):
    L=N+1; delta=[left[a]-right[a] for a in range(M)]
    def mu(i,a): return (F(L-i,L)*left[a]+F(i,L)*right[a])
    def covw(i,j): return F(min(i,j)*(L-max(i,j)),L*L*(L*t+1))
    def first(i,a): return t*mu(i,a)
    def second(i,a,j,b):
        ma,mb=mu(i,a),mu(j,b)
        G=covw(i,j)
        if i!=j: return t*t*(ma*mb+delta[a]*delta[b]*G)
        return t*t*ma*mb + t*(ma if a==b else 0) + t*ma*mb + t*(t+1)*delta[a]*delta[b]*G
    def rate1(source,a): return first(source,a)/t
    def rate2(source,a,b): return (second(source,a,source,b)+ (t*first(source,a) if a==b else 0))/(t*(t+1))
    def local_events(i,a):
        # event position site i to neighbor or reservoir; j=-1 means off-system
        return [(i-1 if i>1 else 0),(i+1 if i<N else N+1)]
    def generator_second(i,a,j,b):
        accum=F(0)
        # bulk directed source→dest and reservoir removals
        for source in range(1,N+1):
            for target in local_events(source,a):
                x=(int(target==i)-int(source==i))
                y=(int(target==j)-int(source==j))
                if x!=0: accum+=x*second(source,a,j,b)/t
                if y!=0: accum+=y*second(source,b,i,a)/t
                if x*y!=0: accum+=x*y*rate2(source,a,b)
        # boundary injections
        for site,rv in [(1,left),(N,right)]:
            if i==site: accum+=rv[a]*first(j,b)
            if j==site: accum+=rv[b]*first(i,a)
            if i==site and j==site: accum+=rv[a]*rv[b]+(rv[a] if a==b else 0)
        return accum
    def generator_first(i,a):
        accum=F(0)
        for source in range(1,N+1):
            for target in local_events(source,a):
                accum+=(int(target==i)-int(source==i))*rate1(source,a)
        if i==1: accum+=left[a]
        if i==N: accum+=right[a]
        return accum
    tot=0
    for i in range(1,N+1):
      for a in range(M):
        y=generator_first(i,a)
        assert y==0,(N,M,'first',i,a,y)
        for j in range(1,N+1):
          for b in range(M):
            v=generator_second(i,a,j,b)
            assert v==0,(N,M,t,'second',i,a,j,b,v)
            tot+=1
    return tot
if __name__=='__main__':
    ntest=0
    for N in range(1,9):
      for M in range(1,5):
        for t in [F(1,2),F(1),F(3,2),F(3)]:
          left=[F((3*a+2)%11+2,4+a+M) for a in range(M)]
          right=[F((5*a+4)%13+1,8+a+M) for a in range(M)]
          ntest+=moment_builder(N,M,t,left,right)
    print('PASS',ntest,'exact rational stationary second-moment identities')

# Exact finite-chain illustration from the theorem: two colors with opposing gradients.
if __name__ == '__main__':
    t=F(2); L=4
    delta=(F(3,5),F(-3,5))
    G13=F(1,16*(L*t+1))
    G22=F(4,16*(L*t+1))
    assert t*t*delta[0]*delta[1]*G13==F(-1,100)
    assert t*F(1,2)*F(1,2)+t*(t+1)*delta[0]*delta[1]*G22==F(11,25)
    print('PASS exact cross-color correlation-sign example')
