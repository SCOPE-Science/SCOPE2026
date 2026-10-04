from itertools import product
from math import comb
from fractions import Fraction

edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def h2_dimension(d,k):
    m=d-3
    if m<0:
        return 0
    # For four general points and m<=2, simple point conditions are independent.
    return max(comb(m+2,2)-k,0)

def pg_closed(n):
    num=7*n**5-30*n**4+35*n**3+30*n**2-90*n+48
    assert num%12==0
    return num//12

for n in range(2,9):
    total_q=0
    nonzero={}
    char_count=0
    for a in product(range(n), repeat=6):
        S=sum(a)
        if S%n:
            continue
        char_count+=1
        d=S//n
        if d==0:
            assert all(x==0 for x in a)
            continue
        sums=[0,0,0,0]
        for w,(u,v) in zip(a,edges):
            sums[u]+=w
            sums[v]+=w
        b=[s//n for s in sums]
        assert all(x in (0,1,2) for x in b)
        k=sum(x==2 for x in b)
        chi=Fraction(1)+Fraction(d*(d-3),2)-k
        h2=h2_dimension(d,k)
        h1=-chi+h2
        assert h1.denominator==1 and h1>=0
        h1=int(h1)
        if h1:
            nonzero[(d,k,h1)]=nonzero.get((d,k,h1),0)+1
        total_q+=h1
    assert char_count==n**5
    assert set(nonzero).issubset({(2,1,1),(4,4,1)})
    assert nonzero.get((2,1,1),0)==4*comb(n-1,2)
    assert nonzero.get((4,4,1),0)==comb(n-1,2)
    expected=5*comb(n-1,2)
    assert total_q==expected
    chi_num=(7*n*n-30*n+35)*n**3
    assert chi_num%12==0
    chi=chi_num//12
    pg=chi+total_q-1
    assert pg==pg_closed(n)
    print(f"n={n} characters={char_count} d2k1={nonzero.get((2,1,1),0)} d4k4={nonzero.get((4,4,1),0)} q={total_q} pg={pg}")

assert 5*comb(5,2)==50
assert pg_closed(6)==1975
print("n6_degree_zero_H2_dimension=50")
print("VERIFY_OK")
