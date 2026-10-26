"""Finite reproducibility checks for the rational FO spectrum of layered permutations.
Uses elementary exhaustive enumeration; the mathematical statement for all lengths
is proved separately by an overlap-free switching argument.
"""
from itertools import product
from fractions import Fraction


def codes(q):
    r=1
    while True:
        us=[''.join(v) for v in product('01',repeat=r) if '00' not in ''.join(v)]
        if len(us)>=q:
            return ['001'+u+'1' for u in us[:q]]
        r+=1


def overlap_free(ws):
    return all(a[-j:]!=b[:j] for a in ws for b in ws for j in range(1,len(a)))


def first_hit(s,ws):
    hits=[(s.find(w),j) for j,w in enumerate(ws) if s.find(w)>=0]
    if not hits: return None
    return min(hits)[1]


def permutation(bits):
    n=len(bits)+1
    cuts=[i+1 for i,v in enumerate(bits) if v=='1']+[n]
    result=[];prev=0
    for x in cuts:
        result.extend(range(x,prev,-1));prev=x
    return result


def recovered_bits(perm):
    return ''.join('1' if perm[i]<perm[i+1] else '0' for i in range(len(perm)-1))


def main():
    count_cases=0
    for q in range(1,19):
        ws=codes(q)
        assert overlap_free(ws),(q,ws)
        assert len(set(ws))==q and len(set(map(len,ws)))==1
        count_cases+=q*q*(len(ws[0])-1)
    for n in range(1,13):
        for bt in product('01',repeat=n-1):
            s=''.join(bt)
            p=permutation(s)
            assert sorted(p)==list(range(1,n+1))
            assert recovered_bits(p)==s
            count_cases+=1
    for q in (2,3,4,5):
        ws=codes(q); L=len(ws[0]);
        for n in range(L,min(L+12,19)):
            counts=[0]*q
            for tup in product('01',repeat=n):
                j=first_hit(''.join(tup),ws)
                if j is not None: counts[j]+=1
            assert len(set(counts))==1, (q,n,ws,counts)
            for m in range(q+1):
                lhs=sum(counts[:m])
                rhs=Fraction(m,q)*sum(counts)
                assert lhs==rhs
            count_cases+=q
    print('LAYERED_RATIONAL_EXACT_OK', count_cases, 'code_families',18, 'q_tested', [2,3,4,5])
if __name__=='__main__':main()
