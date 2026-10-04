from math import gcd, isqrt

def prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def sigma_bb_pp(p,e):
    s=sum(p**j for j in range(e+1))
    if e%2==0:
        s-=p**(e//2)
    return s

def d_bb_pp(e):
    return e+1 if e%2 else e

def buh_p2aq(p,a,q):
    den=sigma_bb_pp(p,2*a)*(q+1)
    num=(p**(2*a))*q*(2*a)*2
    return num%den==0

# Prime-power formula check by explicit exponent exclusion.
for p in (2,3,5,7):
    for a in range(1,7):
        lhs=sigma_bb_pp(p,2*a)
        rhs=((p**a-1)*(p**(a+1)+1))//(p-1)
        assert lhs==rhs

assert buh_p2aq(3,1,5)

# Branch 1: q<p. The proof forces a=1, q+1|4, and p^2+1|4q.
branch_q_lt_p=[]
for q in (2,3):
    if prime(q) and 4%(q+1)==0:
        for p in range(q+1, 10):
            if prime(p) and (4*q)%(p*p+1)==0:
                branch_q_lt_p.append((p,1,q))
assert branch_q_lt_p==[]

# Branch 2: p<q<=4a. The proof forces a<=3 and p^(2a)<16a^2.
branch_small_q=[]
for a in (1,2,3):
    for p in range(2,4*a+1):
        if not prime(p) or p**(2*a)>=16*a*a: continue
        B=sigma_bb_pp(p,2*a)
        for q in range(p+1,4*a+1):
            if prime(q) and (4*a*q)%B==0:
                branch_small_q.append((p,a,q))
assert branch_small_q==[]

# Branch 3: p<q and q>4a. The proof forces A|4a and hence a<=4.
# For a>=2 this bounds p directly. For a=1, C/q=t|4 and the three t cases are exact.
branch_large_q=[]
# a=1, t in divisors of 4
for t in (1,2,4):
    if t==1:
        ps=(2,)  # p odd would make p^2+1 an even integer >2
    elif t==2:
        ps=(3,)  # for p!=3, gcd((p^2+3)/2,p)=1 forces (p^2+3)/2|4
    else:
        ps=()    # p^2+1 is never divisible by 4 for prime p
    for p in ps:
        C=p*p+1
        if C%t: continue
        q=C//t
        if q>4 and q>p and prime(q) and (4*p*p)%(q+1)==0 and buh_p2aq(p,1,q):
            branch_large_q.append((p,1,q))
# a=2..4, enumerate exactly from A<=4a
for a in (2,3,4):
    for p in range(2,4*a+1):
        if not prime(p): continue
        A=(p**a-1)//(p-1)
        if A>4*a: continue
        C=p**(a+1)+1
        # q must be a prime divisor of C exceeding 4a, and A*(C/q)|4a
        for q in range(4*a+1,C+1):
            if prime(q) and C%q==0 and (4*a)%(A*(C//q))==0 and buh_p2aq(p,a,q):
                branch_large_q.append((p,a,q))
assert branch_large_q==[(3,1,5)]

# Corroborative bounded scan only; not part of the infinite proof.
scan=[]
plist=[n for n in range(2,200) if prime(n)]
for p in plist:
    for q in plist:
        if p==q: continue
        for a in range(1,13):
            if buh_p2aq(p,a,q): scan.append((p,a,q))
assert sorted(set(scan))==[(3,1,5)]
print('VERIFY_OK theorem_candidates=%s scan_bound_pq=199 scan_a=12' % branch_large_q)
