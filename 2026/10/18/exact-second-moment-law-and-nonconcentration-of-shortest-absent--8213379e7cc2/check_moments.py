"""Independent finite checks for two rational moment laws of binary missing subsequences.

Only Python's standard library is required. Exhaustive checks validate finite cases;
the accompanying mathematical argument proves the unrestricted assertions.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb

D1 = {(0,0):1, (1,0):-1, (0,1):-1, (1,1):-2,
      (2,1):2, (1,2):2, (2,2):-1}
N1 = {(0,0):2, (1,0):-1, (0,1):-1}
D2 = {(0,0):1, (1,0):-1, (0,1):-1, (1,1):-4,
      (2,1):4, (1,2):4, (2,2):-1, (3,2):-2,
      (2,3):-2, (3,3):2}
N2 = {(0,0):4, (1,0):-3, (0,1):-3,
      (2,1):2, (1,2):2, (2,2):-2}

def rational_coeffs(num, den, max_n):
    a = defaultdict(int)
    for n in range(max_n+1):
        for i in range(n+1):
            j=n-i
            val=num.get((i,j),0)
            for (u,v),c in den.items():
                if u==v==0: continue
                if i>=u and j>=v: val -= c*a[(i-u,j-v)]
            a[(i,j)]=val
    return a

def missing_count(word):
    seen=set(); arches=0
    for x in word:
        seen.add(x)
        if len(seen)==2:
            arches+=1;seen.clear()
    m=arches+1
    absent=0
    for target in product((0,1),repeat=m):
        j=0
        for ch in word:
            if j<m and ch==target[j]: j+=1
        absent+=(j<m)
    return absent

def poly_add(a,b,cap):
    c=dict(a)
    for k,v in b.items():
        if sum(k)<=cap:
            c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def poly_mul(a,b,cap):
    c=defaultdict(int)
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=cap:
                c[(i+k,j+l)]+=v*w
    return {k:v for k,v in c.items() if v}

def transfer_coeffs(power,cap):
    # Enumerate arch choices independently for a single target (power=1)
    # or for an ordered pair of targets (power=2).
    states=list(product((0,1),repeat=power));dim=len(states)
    matrix=[[{} for _ in states] for _ in states]
    for i,now in enumerate(states):
        for j,nxt in enumerate(states):
            arcs=defaultdict(int)
            for base in (0,1):
                for run in range(1,cap):
                    # For this arch, every target greedily matches just once.
                    if all(now[h]!=base or (run==1 and nxt[h]==base)
                           for h in range(power)):
                        aa,bb=(run,1) if base==0 else (1,run)
                        if aa+bb<=cap:arcs[(aa,bb)]+=1
            matrix[i][j]=dict(arcs)
    tail=[]
    for now in states:
        v={(0,0):1}
        if all(b==1 for b in now):
            v.update({(r,0):1 for r in range(1,cap+1)})
        if all(b==0 for b in now):
            v.update({(0,r):1 for r in range(1,cap+1)})
        tail.append(v)
    row=[{(0,0):1} for _ in states]
    result={}
    for m in range(cap//2+1):
        for j in range(dim):
            result=poly_add(result,poly_mul(row[j],tail[j],cap),cap)
        new=[]
        for j in range(dim):
            col={}
            for i in range(dim):
                col=poly_add(col,poly_mul(row[i],matrix[i][j],cap),cap)
            new.append(col)
        row=new
    return result

def poly_val(coeffs,z):
    return sum(Fraction(c)*z**i for i,c in enumerate(coeffs))

def run_checks():
    limit=14
    first=rational_coeffs(N1,D1,40)
    second=rational_coeffs(N2,D2,40)
    for n in range(limit+1):
        totals=defaultdict(lambda:[0,0])
        for word in product((0,1),repeat=n):
            v=missing_count(word)
            key=(n-sum(word),sum(word))
            totals[key][0]+=v
            totals[key][1]+=v*v
        for a in range(n+1):
            b=n-a
            assert totals[(a,b)]==[first[(a,b)],second[(a,b)]],(n,a,b)
            assert first[(a,b)]==first[(b,a)]
            assert second[(a,b)]==second[(b,a)]
    # A separate expansion lists the possible arch words and both target
    # patterns directly; it does not use either rational denominator.
    for p,expected in [(1,first),(2,second)]:
        got=transfer_coeffs(p,12)
        for n in range(13):
            for a in range(n+1):
                b=n-a
                assert got.get((a,b),0)==expected[(a,b)],(p,n,a,b)
    assert first[(5,5)]==1110 and second[(5,5)]==10174
    assert Fraction(second[(5,5)],comb(10,5))-Fraction(first[(5,5)],comb(10,5))**2==Fraction(12331,588)
    # Polynomial isolating intervals for the positive dominant roots.
    one_million=10**6
    a1=Fraction(460811,one_million);b1=Fraction(460812,one_million)
    a2=Fraction(406865,one_million);b2=Fraction(406866,one_million)
    q1=[1,-1,-3,1]
    q2=[1,-1,-5,3,2,-2]
    assert poly_val(q1,a1)>0>poly_val(q1,b1)
    assert poly_val(q2,a2)>0>poly_val(q2,b2)
    assert b2<2*a1*a1
    print('PASS first_and_second_moments all_binary_words_length_0_through_14')
    print('PASS independent_arch_pair_transfer all_coefficients_total_degree_at_most_12')
    print('PASS exact_fixed_weight_variance_and_root_brackets')

if __name__=='__main__':
    run_checks()
