"""Independent finite sanity checks for mixed quadratic divisibility classification."""
from math import gcd, isqrt


def check(bound=240):
    witnessed = set()
    odd_chamber = set()
    even_chamber = set()
    for x in range(1, bound + 1):
        for y in range(1, bound + 1):
            good = (2*y*y+1) % x == 0 and (x*x+1) % y == 0
            n = x*x + 2*y*y + 1
            assert good == (n % (x*y) == 0), (x,y)
            if not good:
                continue
            assert gcd(x,y)==1 and x%2==1
            k = n//(x*y)
            witnessed.add(k)
            if y%2:
                assert k==4, (x,y,k)
                assert (x-2*y)**2 - 2*y*y == -1
                odd_chamber.add((x,y))
            else:
                t=y//2; s=x-k*t
                assert y%4==2 and k%2==1 and k>=3
                assert s*s-(k*k-8)*t*t == -1
                even_chamber.add((x,y))
    assert (1,1) in odd_chamber
    assert (3,2) in even_chamber
    # Pell -> divisibility converse, including both signs.
    count = 0
    for k in range(3, 90, 2):
        D=k*k-8
        for t in range(1, 700):
            s2=D*t*t-1
            if s2<0: continue
            s=isqrt(s2)
            if s*s !=s2: continue
            for x in {k*t+s,k*t-s}:
                y=2*t
                assert x>0 and x%2==1 and y%4==2
                assert (2*y*y+1)%x==0 and (x*x+1)%y==0,(k,s,t,x,y)
                count+=1
    # For odd chamber, norm-(-1) Pell powers give two branches.
    u,y=1,1
    for n in range(9):
        for x in {2*y+u,2*y-u}:
            assert x>0 and (2*y*y+1)%x==0 and (x*x+1)%y==0,(x,y)
        u,y=3*u+4*y,2*u+3*y
    # Prime obstructions for parameter k.
    primes=[7,23,31,47,71,79]
    for k in witnessed:
        for p in primes:
            if k%2==1 and (k*k-8)%p==0:
                raise AssertionError(('local obstruction missed',k,p))
    print('VERIFY_OK', 'bound',bound,'witnessed_parameters',sorted(witnessed),'odd_pairs',len(odd_chamber),'even_pairs',len(even_chamber),'pell_converse_examples',count)


if __name__=='__main__':
    check()
