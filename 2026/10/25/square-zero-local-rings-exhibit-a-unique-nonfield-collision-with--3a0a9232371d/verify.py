"""Direct finite-ring and Gaussian-subspace checks for a zero-ideal-product count."""
from itertools import product
from math import prod


def ideals_of_eight_element_ring(elements, add, mul, zero):
    """Enumerate every subset and test the defining ideal conditions."""
    ideals=[]
    for mask in range(1 << len(elements)):
        subset=frozenset(elements[i] for i in range(len(elements)) if (mask >> i)&1)
        if zero not in subset:
            continue
        if not all(add(a,b) in subset for a in subset for b in subset):
            continue
        if not all(mul(a,r) in subset for a in subset for r in elements):
            continue
        ideals.append(subset)
    return ideals


def check_ring(elements, add, mul, zero, name):
    ideals=ideals_of_eight_element_ring(elements,add,mul,zero)
    assert len(ideals)==6, (name,len(ideals))
    top=frozenset(elements)
    proper_nonzero=[I for I in ideals if I != top and I != frozenset([zero])]
    assert len(proper_nonzero)==4
    def zero_product(I,J):
        return all(mul(a,b)==zero for a in I for b in J)
    for k in range(2,6):
        count=0
        for tup in product(ideals,repeat=k):
            # For square-zero maximal ideal, the nonzero products are exactly
            # all-top tuples or tuples with a single nonzero proper ideal.
            predicts_nonzero=(all(I==top for I in tup) or
                              (sum(I!=top for I in tup)==1 and all(len(I)>1 for I in tup)))
            really_zero=True
            partial=ideals[0]  # replaced immediately with the first factor
            for idx, I in enumerate(tup):
                if idx==0: partial=I
                else: partial=frozenset(mul(a,b) for a in partial for b in I)
            really_zero=(partial==frozenset([zero]))
            assert predicts_nonzero == (not really_zero), (name,k,tup)
            count+=really_zero
        assert count==6**k-(1+4*k), (name,k,count)
    print(name,'ideals',len(ideals),'zeta_2=27/36','checks_passed')

F2=list(product(range(2),repeat=3))
def add_f2(a,b): return tuple((x+y)%2 for x,y in zip(a,b))
def mul_f2(a,b):
    s,x,y=a; t,u,v=b
    return (s*t % 2,(s*u+t*x)%2,(s*v+t*y)%2)
check_ring(F2,add_f2,mul_f2,(0,0,0),'F2[x,y]/(x,y)^2')

Z4xF2=list(product(range(4),range(2)))
def add_z4(a,b): return ((a[0]+b[0])%4,(a[1]+b[1])%2)
def mul_z4(a,b): return ((a[0]*b[0])%4,((a[0]%2)*b[1]+(b[0]%2)*a[1])%2)
check_ring(Z4xF2,add_z4,mul_z4,(0,0),'Z4[t]/(2t,t^2)')


def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def subspace_count(q,r):
    return sum(gaussian(r,j,q) for j in range(r+1))
for q in (2,3,4,5):
    for r in range(4):
        L=subspace_count(q,r)+1
        assert (L==2 if r==0 else L>=3)
        for k in range(2,13):
            numerator=L**k-1-k*(L-2)
            assert numerator>=0
            eq_field=numerator*2**k==(2**k-1)*L**k
            assert eq_field == (r==0 or (q,r,k)==(2,2,2)),(q,r,k)
        print('q',q,'r',r,'ideals',L,'zero_pairs',L*L-(2*L-3))
print('VERIFY_OK')
