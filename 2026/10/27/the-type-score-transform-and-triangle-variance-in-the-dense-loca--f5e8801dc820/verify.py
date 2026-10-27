"""Finite checks for the one-point extension score spectrum of locally transitive tournaments.
Run with Python 3: python local_order_type_verifier.py
No external libraries are used.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def is_locally_transitive(A):
    n=len(A)
    for v in range(n):
        for sign in (0,1):
            N=[w for w in range(n) if w!=v and A[v][w]==sign]
            for a,b,c in combinations(N,3):
                if (A[a][b] and A[b][c] and A[c][a]) or (A[b][a] and A[c][b] and A[a][c]):
                    return False
    return True


def adjacency_from_mask(n,mask):
    A=[[0]*n for _ in range(n)]
    for t,(i,j) in enumerate(combinations(range(n),2)):
        A[i][j]=(mask>>t)&1
        A[j][i]=1-A[i][j]
    return A


def extension_scores_direct(A):
    n=len(A); result=Counter()
    for bits in product((0,1),repeat=n):
        B=[row+[1-bits[i]] for i,row in enumerate(A)]
        B.append(list(bits)+[0])
        if is_locally_transitive(B):
            result[sum(bits)]+=1
    return result


def expected_scores(A):
    n=len(A); result=Counter()
    for row in A:
        s=sum(row)
        result[s]+=1
        result[s+1]+=1
    return result


def triangle_count(A):
    ans=0
    for a,b,c in combinations(range(len(A)),3):
        if (A[a][b] and A[b][c] and A[c][a]) or (A[b][a] and A[c][b] and A[a][c]):
            ans+=1
    return ans


def verify_claim(A):
    n=len(A)
    expected=expected_scores(A)
    actual=extension_scores_direct(A)
    assert expected==actual,(n,expected,actual)
    scores=Counter(sum(row) for row in A)
    assert all(scores[s]==scores[n-1-s] for s in range(n))
    assert sum(actual.values())==2*n
    # The moment identity is checked with integer arithmetic throughout.
    lhs=sum(c*(2*d-n)**2 for d,c in actual.items())
    assert 3*lhs == 2*n*(n*n+2)-48*triangle_count(A)

bases=0
for n in range(1,7):
    count=0
    for mask in range(1<<comb(n,2)):
        A=adjacency_from_mask(n,mask)
        if is_locally_transitive(A):
            verify_claim(A)
            count+=1
    bases+=count
    print(f"ALL_LABELED_TOURNAMENTS_ORDER_{n}: {count} locally transitive bases checked")

# Independent geometric construction from all antipodal-complement binary words.
# Every binary word w of length n yields w+complement(w) on the 2n boundary slots.
words=0
for n in range(1,13):
    for half in product((0,1),repeat=n):
        word=half+tuple(1-x for x in half)
        places=[i for i,b in enumerate(word) if b==0]
        A=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    A[i][j]=int(0<(places[j]-places[i])%(2*n)<n)
        assert is_locally_transitive(A)
        scores=[sum(row) for row in A]
        assert Counter(scores)==Counter(n-1-s for s in scores)
        # The 2n distinct gap patterns are computed independently from scores.
        # Every boundary slot starts a gap in the geometric model.
        profiles=[]
        for boundary in range(2*n):
            bits=[]
            for p in places:
                d=(p-boundary)%(2*n)
                bits.append(int(1<=d<=n))
            profiles.append(tuple(bits))
        assert len(set(profiles))==2*n
        actual=Counter(sum(a) for a in profiles)
        expected=Counter()
        for s in scores:expected[s]+=1;expected[s+1]+=1
        assert actual==expected,(n,half,actual,expected)
        words+=1
print(f"ALL_GEOMETRIC_WORDS_1_TO_12: {words} antipodal words checked")
print(f"ALL_DIRECT_BASES: {bases}")
print("ALL_TESTS_PASS")
