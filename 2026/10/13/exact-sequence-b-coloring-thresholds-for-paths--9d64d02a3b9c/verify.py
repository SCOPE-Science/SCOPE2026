from itertools import product


def cdv_counts(word):
    k=max(word)+1 if word else 0
    counts=[0]*k
    for i in range(1,len(word)-1):
        if word[i-1]!=word[i+1]:
            counts[word[i]]+=1
    return counts


def min_order_formula(r,s,t):
    assert r>=s>=t>=1
    if r==s==t:
        return 3*r+2
    return 2*r+s+1


def construct_three(r,s,t):
    assert r>=s>=t>=1
    if r==s==t:
        return tuple(([0,1,2]*r)+[0,1])
    if r==s:
        return tuple(([0,1,2]*r)+[0])
    w=[0,1,2]*(s+1)
    endpoint=2
    for _ in range(r-s-1):
        nxt=0 if endpoint==2 else 2
        w.extend([1,nxt])
        endpoint=nxt
    return tuple(w)


def sorted3(word):
    c=cdv_counts(word)
    if len(c)<3: c += [0]*(3-len(c))
    return tuple(sorted(c[:3], reverse=True))


def all_proper_words(n,k):
    if n==0: return
    w=[0]*n
    def rec(i):
        if i==n:
            yield tuple(w); return
        for c in range(k):
            if i and w[i-1]==c: continue
            w[i]=c
            yield from rec(i+1)
    yield from rec(0)


def realizes_three(word,req):
    if set(word)!={0,1,2}: return False
    c=sorted3(word)
    return all(c[i]>=req[i] for i in range(3))

# Explicit construction checks on a wide grid.
construction_cases=0
for r in range(1,81):
    for s in range(1,r+1):
        for t in range(1,s+1):
            w=construct_three(r,s,t)
            N=min_order_formula(r,s,t)
            assert len(w)==N
            assert all(w[i]!=w[i+1] for i in range(N-1))
            c=sorted3(w)
            assert c[0]>=r and c[1]>=s and c[2]>=t, (r,s,t,c,w)
            construction_cases += 1

# Exhaustive exact minimality for all requests whose formula is at most 12.
# Color 0 can be fixed at the first vertex by color symmetry.
achievable_by_n={}
word_checks=0
for n in range(2,13):
    vecs=set()
    for tail in product(range(3), repeat=n-1):
        word=(0,)+tail
        if any(word[i]==word[i+1] for i in range(n-1)):
            continue
        word_checks += 1
        if set(word)=={0,1,2}:
            c=sorted3(word)
            if c[2]>=1:
                vecs.add(c)
    achievable_by_n[n]=vecs

minimality_cases=0
for r in range(1,6):
    for s in range(1,r+1):
        for t in range(1,s+1):
            N=min_order_formula(r,s,t)
            if N>12: continue
            assert any(all(c[i]>=x for i,x in enumerate((r,s,t))) for c in achievable_by_n[N]), (r,s,t,N)
            for n in range(2,N):
                assert not any(all(c[i]>=x for i,x in enumerate((r,s,t))) for c in achievable_by_n[n]), (r,s,t,n,c)
            minimality_cases += 1

# Verify the sign-run lower-bound lemma exhaustively through n=14.
lemma_words=0
for n in range(3,15):
    for tail in product(range(3), repeat=n-1):
        word=(0,)+tail
        if any(word[i]==word[i+1] for i in range(n-1)):
            continue
        lemma_words += 1
        cnt=cdv_counts(word)
        if len(cnt)<3: cnt += [0]*(3-len(cnt))
        a,b,c=sorted(cnt[:3], reverse=True)
        q=sum(1 for i in range(1,n-1) if word[i-1]==word[i+1])
        assert a-c <= q+1, (word,cnt,q)
        assert n-2 == a+b+c+q
        assert 2*a+b <= n-1

# Two-color branch: alternating coloring gives all vertices CDV and exact bipartition sizes.
two_color_cases=0
for n in range(2,201):
    w=tuple(i%2 for i in range(n))
    cnt=cdv_counts(w)
    # endpoints are also CDVs for a two-coloring; cdv_counts above only implements 3-color interior test,
    # so check directly here.
    direct=[0,0]
    for i,c in enumerate(w):
        seen={c}
        if i: seen.add(w[i-1])
        if i+1<n: seen.add(w[i+1])
        if seen=={0,1}: direct[c]+=1
    assert sorted(direct, reverse=True)==[ (n+1)//2, n//2 ]
    two_color_cases += 1

print('ALL CHECKS PASSED; construction_cases=%d; minimality_cases=%d; proper_word_checks=%d; lower_bound_words=%d; two_color_cases=%d; exhaustive_order_max=12; lower_bound_order_max=14; construction_r_max=80' % (construction_cases,minimality_cases,word_checks,lemma_words,two_color_cases))
