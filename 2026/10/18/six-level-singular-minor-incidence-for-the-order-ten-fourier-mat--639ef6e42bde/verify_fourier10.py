"""Exact exhaustive incidence certificate for order-ten DFT four-minors.
Run: python3 verify_fourier10.py (Python 3 standard library only).
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations,permutations
from math import factorial

def cyclotomic_powers():
    # Q[z]/Phi_10(z), Phi_10=z**4-z**3+z**2-z+1.
    powers=[(1,0,0,0)]
    for _ in range(9):
        a,b,c,d=powers[-1]
        powers.append((-d,a+d,b-d,c+d))
    assert powers[5]==(-1,0,0,0)
    assert powers[9]==(1,-1,1,-1)
    return powers

def exact_minor(rows,cols,powers,terms):
    d=[0,0,0,0]
    for perm,sign in terms:
        exp=sum(rows[i]*cols[perm[i]] for i in range(4))%10
        w=powers[exp]
        for j in range(4):d[j]+=sign*w[j]
    return all(v==0 for v in d)

def certify():
    subsets=list(combinations(range(10),4))
    signs=[(p,(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))) for p in permutations(range(4))]
    assert len(signs)==factorial(4)
    powers=cyclotomic_powers()
    distribution=Counter(); incidence=bytearray(); by_row=[]
    for rows in subsets:
        row_count=0
        for cols in subsets:
            singular=exact_minor(rows,cols,powers,signs)
            incidence.append(int(singular));row_count+=singular
        distribution[row_count]+=1
        by_row.append(row_count)
    expected={0:20,10:100,20:50,30:20,110:10,130:10}
    assert dict(distribution)==expected,(distribution,expected)
    assert len(incidence)==44100 and sum(incidence)==5000
    digest=sha256(incidence).hexdigest()
    assert digest=='4a51a0450edaf31bc19e2a0701b5f01e600fa279602fdaae736fda59d8a9df2e'
    print('exact_cyclotomic_minor_incidence:',digest)
    print('row_degree_multiplicities:',sorted(distribution.items()))
    print('singular_4x4_minors:',sum(incidence),'of',len(incidence))
    return digest

if __name__=='__main__':
    certify()
