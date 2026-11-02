"""Exact finite cross-checks for two-marker ordered contiguous k-mer profiles."""
from collections import defaultdict, Counter
from hashlib import sha256

def word(a,b,c):
    return '0'*a+'1'+'0'*b+'1'+'0'*c

def profile(a,b,c,k):
    w=word(a,b,c)
    return tuple(sorted(Counter(w[i:i+k] for i in range(len(w)-k+1)).items()))

def label(a,b,c,k):
    t=k-1
    A,B,C=min(a,t),min(b,t),min(c,t)
    if B==t and A<t and C<t and A+C==k-2:
        return ('exception',)
    return (A,B,C)

def all_triplets(n):
    N=n-2
    for a in range(N+1):
        for b in range(N-a+1):
            yield a,b,N-a-b

def run():
    cases=0
    marker_words=0
    for k in range(2,12):
        for n in range(max(k,3*k-2),3*k+9):
            from_label=defaultdict(set); from_profile=defaultdict(set)
            for a,b,c in all_triplets(n):
                p=profile(a,b,c,k)
                L=label(a,b,c,k)
                from_label[L].add(p)
                from_profile[p].add(L)
                marker_words+=1
            assert all(len(s)==1 for s in from_label.values()), ('label_not_sufficient',k,n)
            assert all(len(s)==1 for s in from_profile.values()), ('label_not_necessary',k,n)
            expected=3*k*k-4*k+3-(n==3*k-2)
            assert len(from_profile)==expected, (k,n,len(from_profile),expected)
            cases+=1
    # Check exceptional class itself for all parameters, incl no other profile collision
    for k in range(2,11):
        n=3*k+1
        e=[(a,b,c) for a,b,c in all_triplets(n) if label(a,b,c,k)==('exception',)]
        assert len(e)==k-1
        assert len({profile(*v,k) for v in e})==1
    print('VERIFY_OK k_range=2..11 n_range=3k-2..3k+8 parameter_cases=',cases,'source_words=',marker_words,'boundary_sharp=True','full_profile_partition=True')
    return cases,marker_words
if __name__=='__main__':
    run()
