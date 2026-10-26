"""Independent finite checks for square-zero endomorphisms of unequal cyclic p-groups."""
from itertools import product


def expected(p,a,b):
    assert a in (1,2) and b>a
    if a==1:
        return (2*p-1)*p**(b//2) if b%2==0 else p**((b+3)//2)
    return (2*p*p-1)*p**((b+2)//2) if b%2==0 else (3*p-2)*p**((b+3)//2)


def direct_count(p,a,b):
    pa,pb=p**a,p**b
    h=b-a
    # Tabulate directly all possible lower-right entries by product t.
    roots=[[z for z in range(pb) if (z*z+p**h*t)%pb==0] for t in range(pa)]
    count=0
    for u,v,w in product(range(pa), repeat=3):
        t=(v*w)%pa
        if (u*u+p**h*t)%pa:continue
        for z in roots[t]:
            # Directly compute the two off-diagonal entries of T^2.
            if (v*(u+z))%pa==0 and (w*(u+z))%pa==0:
                count+=1
    return count


def main():
    tests=[]
    for p in (2,3,5,7):
        for a in (1,2):
            for b in range(a+1, a+8):
                if p**(3*a+b)>6000000:continue
                found=direct_count(p,a,b)
                target=expected(p,a,b)
                assert found==target,(p,a,b,found,target)
                tests.append((p,a,b,found))
    for p in (2,3,5,7):
        mod=p*p
        fib=[0]*mod
        for v,w in product(range(mod),repeat=2):fib[v*w%mod]+=1
        assert fib[0]==p*(3*p-2),(p,'zero-fiber',fib[0])
        for t in range(1,mod):
            if t%p:
                assert fib[t]==p*(p-1),(p,t,fib[t])
            else:
                assert fib[t]==2*p*(p-1),(p,t,fib[t])
    print('SQUARE_ZERO_MIXED_P_GROUP_OK',len(tests),'exhaustive_cases')
    print('LOW_EXPONENT_EXAMPLES',[t for t in tests if t[0]==2 and t[1]==2])

if __name__=='__main__':main()
