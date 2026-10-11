from fractions import Fraction
from itertools import combinations

def maxcut(n, edges):
    best=-1
    sizes=[]
    for mask in range(1<<n):
        c=sum(((mask>>u)&1) != ((mask>>v)&1) for u,v in edges)
        sizes.append(c)
        best=max(best,c)
    return best,sizes

def complete(n):
    return list(combinations(range(n),2))

def cycle(n):
    return [(i,(i+1)%n) for i in range(n)]

def petersen():
    e=[]
    e += [(i,(i+1)%5) for i in range(5)]
    e += [(5+i,5+((i+2)%5)) for i in range(5)]
    e += [(i,5+i) for i in range(5)]
    return e

def check_graph(name,n,edges):
    m=len(edges)
    M,sizes=maxcut(n,edges)
    assert 2*M-m>0
    c=Fraction(1,2*M-m)
    vals=[Fraction(1)+c*(m-2*s) for s in sizes]
    assert min(vals)==0
    assert all(v>=0 for v in vals)
    obj=Fraction(1)+m*c
    assert obj==Fraction(2*M,2*M-m)
    return len(sizes)

cuts=0
graphs=0
for n in range(2,9):
    cuts += check_graph('K',n,complete(n)); graphs+=1
for n in range(3,12):
    cuts += check_graph('C',n,cycle(n)); graphs+=1
    if n%2==1:
        k=(n-1)//2
        m=n; M=n-1
        W=Fraction(m,m-2)
        rhs=(1+W)/2
        a=W-rhs
        assert a==Fraction(1,2*k-1)
        assert W==m*a
        assert Fraction(2*M,2*M-m)==Fraction(4*k,2*k-1)
cuts += check_graph('Petersen',10,petersen()); graphs+=1
print(f'VERIFY_OK graphs={graphs} cuts={cuts} odd_cycle_rigidity=5 exact_fraction_arithmetic')
