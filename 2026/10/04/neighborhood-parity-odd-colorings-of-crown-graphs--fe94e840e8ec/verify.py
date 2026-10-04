from itertools import product

def proper_extensions(A, k):
    n=len(A)
    counts=[0]*k
    for c in A:
        counts[c]+=1
    allowed=[]
    for j in range(n):
        opts=[]
        for c in range(k):
            if counts[c]==0 or (counts[c]==1 and A[j]==c):
                opts.append(c)
        allowed.append(opts)
    for B in product(*allowed):
        yield B

def odd_condition(A,B,k):
    n=len(A)
    pa=[0]*k
    pb=[0]*k
    for c in A: pa[c]^=1
    for c in B: pb[c]^=1
    for i in range(n):
        # neighbors of a_i are B except b_i
        if not any(pb[c] ^ (1 if B[i]==c else 0) for c in range(k)):
            return False
        # neighbors of b_i are A except a_i
        if not any(pa[c] ^ (1 if A[i]==c else 0) for c in range(k)):
            return False
    return True

def structural_minimum(n,A,B,k):
    if n%2==0:
        if k!=2: return False
        return (len(set(A))==1 and len(set(B))==1 and A[0]!=B[0])
    if n==3:
        if k!=3: return False
        return all(A[i]==B[i] for i in range(n)) and len(set(A))==3
    if k!=4:
        return False
    # exactly two shared colors, each on one matched pair; one exclusive color fills each remainder
    posA={}
    posB={}
    for c in range(k):
        IA=[i for i,x in enumerate(A) if x==c]
        IB=[i for i,x in enumerate(B) if x==c]
        posA[c]=IA; posB[c]=IB
    shared=[c for c in range(k) if posA[c] and posB[c]]
    if len(shared)!=2:
        return False
    shared_idx=[]
    for c in shared:
        if len(posA[c])!=1 or len(posB[c])!=1 or posA[c][0]!=posB[c][0]:
            return False
        shared_idx.append(posA[c][0])
    if shared_idx[0]==shared_idx[1]:
        return False
    exclA=[c for c in range(k) if posA[c] and not posB[c]]
    exclB=[c for c in range(k) if posB[c] and not posA[c]]
    if len(exclA)!=1 or len(exclB)!=1:
        return False
    return len(posA[exclA[0]])==n-2 and len(posB[exclB[0]])==n-2

def enumerate_odd(n,k):
    cnt=0
    bad_struct=0
    proper=0
    for A in product(range(k), repeat=n):
        for B in proper_extensions(A,k):
            proper += 1
            if odd_condition(A,B,k):
                cnt += 1
                if not structural_minimum(n,A,B,k):
                    bad_struct += 1
    return proper,cnt,bad_struct

def predicted(n):
    if n%2==0:
        return 2,2
    if n==3:
        return 3,6
    return 4,12*n*(n-1)

cases=[]
total_proper=0
total_odd=0
for n in range(3,10):
    km, cm = predicted(n)
    for k in range(1,km):
        proper,cnt,bad=enumerate_odd(n,k)
        total_proper += proper
        assert cnt==0,(n,k,cnt)
        assert bad==0
    proper,cnt,bad=enumerate_odd(n,km)
    total_proper += proper
    total_odd += cnt
    assert cnt==cm,(n,km,cnt,cm)
    assert bad==0,(n,bad)
    cases.append((n,km,cnt,proper))

print("VERIFY_OK")
print("n_values_checked =", len(cases))
print("proper_colorings_checked =", total_proper)
print("minimum_odd_colorings_checked =", total_odd)
print("parameters n = 3..9")
for n,k,cnt,proper in cases:
    print("n =",n,"chi_o =",k,"minimum_labeled_colorings =",cnt,"proper_colorings_at_min_palette =",proper)
print("all smaller palettes had zero odd colorings")
print("all minimum colorings matched the structural classification")
