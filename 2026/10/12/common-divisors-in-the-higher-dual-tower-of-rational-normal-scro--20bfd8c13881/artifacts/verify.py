from math import gcd

def v_p(a,p):
    a=abs(a)
    c=0
    while a and a%p==0:
        a//=p
        c+=1
    return c

checks=0
for n in range(2,31):
    for d1 in range(2,13):
        # Every d >= n*d1 is realizable by (d1,...,d1,d-(n-1)d1).
        for d in range(n*d1, n*d1+151):
            vals=[k*d-n*k*(k-1) for k in range(1,d1+1)]
            assert all(x>0 for x in vals)
            g=0
            for x in vals:
                g=gcd(g,x)
            want=gcd(d,2*n)
            assert g==want,(n,d1,d,vals,g,want)
            for p in (2,3,5,7,11,13,17,19):
                assert v_p(g,p)==min(v_p(d,p),v_p(2*n,p))
            assert (g==1)==(d%2==1 and gcd(d,n)==1)
            assert all(x%2==0 for x in vals)==(d%2==0)
            checks+=1

assert [k*6-3*k*(k-1) for k in range(1,3)] == [6,6]
assert [k*7-3*k*(k-1) for k in range(1,3)] == [7,8]
assert [k*6-2*k*(k-1) for k in range(1,4)] == [6,8,6]
print('VERIFY_OK', checks)
