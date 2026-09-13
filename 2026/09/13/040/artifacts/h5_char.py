from math import factorial, comb
from collections import Counter

def partitions_of_n(n, max_part=None):
    if n==0:
        yield []
        return
    if max_part is None: max_part=n
    for f in range(min(max_part,n),0,-1):
        for rest in partitions_of_n(n-f, f):
            yield [f]+rest

def class_size(n, part):
    c=Counter(part)
    denom=1
    for l,m in c.items():
        denom*= (l**m)*factorial(m)
    return factorial(n)//denom

def stat(part,n):
    c=Counter(part)
    return c.get(1,0),c.get(2,0),c.get(3,0),c

def chi_W(part,n):
    f,m2,_,_=stat(part,n)
    a=f-1; b=(f+2*m2)-1
    return (a*a-b)//2

def chi_H5(part,n):
    # H^5(M^k) = span{e_j tensor s_lm}: e has 2 per position (a_j,b_j): char 2f; s has char C(f,2)+m2
    f,m2,_,_=stat(part,n)
    return 2*f*(f*(f-1)//2+m2)

def chi_H6(part,n):
    # A6: pt_i a_j, pt_i b_j ordered i!=j: 2*f*(f-1); triple 2s: positions i<j<l, 8 labelings.
    # For character: fix triples: need count of fixed basis monomials.
    # Enumerate: for class rep with given (f,m2,m3,...), count fixed triples by brute force over small n? Instead formula:
    # A triple monomial T=(S=(i,j,l), labels c). g fixes T iff g(S)=S as set and labels constant on g-orbits within S.
    # Count: sum over 3-subsets S fixed as set of number of labelings fixed by g|_S.
    # Classify S by orbit type: (a) 3 fixed points: # = C(f,3), labelings fixed: 8.
    # (b) one 2-cycle + one fixed: # = m2*f, labelings fixed: those constant on the 2-cycle: 2 (cycle pair) * 2 (fixed pt) = 4.
    # (c) one 3-cycle: # = m3, labelings fixed: constant on the 3-cycle: 2.
    # (d) others (e.g., part of longer cycle) cannot fix a 3-set unless the 3-set is a union of cycles; lengths >=4 can't fit in 3-set except singletons... 4+-cycles contain no 3-subset fixed as set (since orbit length >3). So total triple char = 8*C(f,3)+4*m2*f+2*m3.
    f,m2,m3,_=stat(part,n)
    return 2*f*(f-1) + 8*(f*(f-1)*(f-2)//6) + 4*m2*f + 2*m3

def inner(c1,c2,n):
    tot=0
    for part in partitions_of_n(n):
        tot+= class_size(n,part)*c1(part,n)*c2(part,n)
    return tot//factorial(n)

for n in range(2,13):
    print(f"n={n} invH5W={inner(chi_H5,chi_W,n)} invH6W={inner(chi_H6,chi_W,n)}")
