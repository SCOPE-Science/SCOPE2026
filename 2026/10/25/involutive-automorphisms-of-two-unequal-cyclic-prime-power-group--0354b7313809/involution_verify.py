"""Finite direct checks for order-dividing-two automorphisms of unequal cyclic p-groups.

Run: python3 involution_verify.py

Every tuple (u,v,w,z) defines the homomorphism
(x,y) -> (u*x+v*y mod p**a, p**(b-a)*w*x+z*y mod p**b).
Only unit u,z are enumerated, so these are precisely all automorphisms.
The checker applies the map twice to each group generator, rather than using
any of the square-root counting steps in the mathematical proof.
"""
from itertools import product


def expected(p, a, b):
    assert a>=1 and b>a
    if p!=2:
        return 2+2*p**(2*a)
    gap=b-a
    if a==1:
        return (6,12,16)[min(gap,3)-1]
    if a==2:
        return (3,4,5)[min(gap,3)-1]*4**a
    return (3,4,5)[min(gap,3)-1]*4**a+32


def count_all(p, a, b):
    small=p**a; large=p**b; factor=p**(b-a)
    total=0
    for u in range(small):
        if u%p==0:continue
        for z in range(large):
            if z%p==0:continue
            for v in range(small):
                for w in range(small):
                    # Square the images of (1,0), (0,1).
                    e1x=(u*u+factor*v*w)%small
                    e1y=(factor*w*(u+z))%large
                    e2x=(v*(u+z))%small
                    e2y=(factor*v*w+z*z)%large
                    if e1x==1 and e1y==0 and e2x==0 and e2y==1:
                        total+=1
    return total


def main():
    cases=(
        [(2,1,b) for b in range(2,8)]
       +[(2,2,b) for b in range(3,7)]
       +[(2,3,b) for b in range(4,8)]
       +[(2,4,b) for b in range(5,9)]
       +[(2,5,b) for b in (6,7,8)]
       +[(3,1,b) for b in (2,3,4)]
       +[(3,2,3),(5,1,2),(7,1,2)]
    )
    for p,a,b in cases:
        actual=count_all(p,a,b)
        predicted=expected(p,a,b)
        assert actual==predicted,(p,a,b,actual,predicted)
        print('p=%d a=%d b=%d count=%d OK'%(p,a,b,actual))
    print('RANK_TWO_INVOLUTION_CENSUS_OK %d_cases'%len(cases))

if __name__=='__main__':main()
