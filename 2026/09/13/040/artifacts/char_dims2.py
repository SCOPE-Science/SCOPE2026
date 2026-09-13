from math import factorial
from collections import Counter
import itertools

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

def stats_of_part(part,n):
    c=Counter(part)
    # fix = m1
    f=c.get(1,0)
    m2=c.get(2,0)
    return f,m2,c

def chi_V(part,n):
    f,_,_=stats_of_part(part,n)
    return f-1

def chi_V2(part,n):
    # chi_V(g^2): fix(g^2)= f + 2*m2 (1-cycles stay, 2-cycles become 2 fixed points each)
    from collections import Counter
    c=Counter(part)
    f=c.get(1,0); m2=c.get(2,0)
    return (f+2*m2)-1

def chi_W(part,n):
    a=chi_V(part,n); b=chi_V2(part,n)
    return (a*a-b)//2

def chi_G(part,n):
    # perm on 2-subsets: C(f,2)+m2
    f,m2,_=stats_of_part(part,n)
    return f*(f-1)//2+m2

def chi_H2(part,n):
    f,_,_=stats_of_part(part,n)
    return 2*f

def chi_H4(part,n):
    # H^4(M^k): pt_i (perm, char f) + a_ia_j (perm2), b_ib_j (perm2), a_ib_j (ordered i!=j: f^2 - f? number fixed: ordered pairs i!=j fixed: f^2 - f? plus? g(i)=i,g(j)=j gives f(f-1); 2-cycles give? a_i b_j with {i,j} 2-cycle: g swaps i,j: a_i b_j -> a_j b_i != itself (since a vs b differ). So no contribution from 2-cycles. Similarly? So char = f(f-1).
    f,m2,_=stats_of_part(part,n)
    perm2 = f*(f-1)//2  # for A and B each? chi for A pairs = C(f,2)+m2? Wait a_ia_j with i<j: fixed if {i,j} fixed as set (including 2-cycles, since a_ia_j symmetric). So same as G: C(f,2)+m2. Similarly B. C (a_ib_j ordered, i!=j): fixed iff i,j both fixed (since a/b labels distinguish, swap changes type? g swapping i,j sends a_ib_j to a_jb_i, different basis element unless...? Actually a_j b_i is also a basis element, distinct. So swapped pair not fixed). So char_C = f(f-1).
    return f + 2*(f*(f-1)//2+m2) + f*(f-1)

def inner(chi1, chi2, n):
    tot=0
    for part in partitions_of_n(n):
        tot+= class_size(n,part)*chi1(part,n)*chi2(part,n)
    return tot//factorial(n)

for n in range(2,13):
    print(f"n={n} inv(G,W)={inner(chi_G,chi_W,n)} inv(H4,W)={inner(chi_H4,chi_W,n)} inv(H2,W)={inner(chi_H2,chi_W,n)}")

# Also compute inv of image span Delta? But H4 inv is 0 as before? Let's verify chi_H4 vs chi_W inner should be 0.
# Compute chi of A6 = H^6(M^k): pt_i a_j, pt_i b_j (ordered i!=j: char 2*f*(f-1)? plus? 2-cycles? pt_i a_j under swap i<->j: pt_j a_i distinct, not fixed. So char=2f(f-1)) + triple a/b choices: each triple positions i<j<l with 8 labelings. Character: fixed triples: all three fixed: C(f,3)*8; triples containing a 2-cycle + fixed? e.g., positions {i,j} swapped, l fixed: monomial a_ia_jb_l? Under swap, a_ia_j symmetric? Depends. Let's brute force character for A6 via enumeration for small n and class rep.
