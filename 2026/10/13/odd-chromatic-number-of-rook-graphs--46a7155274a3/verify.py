from itertools import permutations

def is_odd_rook(mat):
    m=len(mat); n=len(mat[0])
    # proper
    for row in mat:
        if len(set(row)) != n:
            return False
    for j in range(n):
        if len({mat[i][j] for i in range(m)}) != m:
            return False
    # direct neighborhood parity
    for i in range(m):
        for j in range(n):
            counts={}
            for jj in range(n):
                if jj!=j:
                    c=mat[i][jj]; counts[c]=counts.get(c,0)+1
            for ii in range(m):
                if ii!=i:
                    c=mat[ii][j]; counts[c]=counts.get(c,0)+1
            if not any(v%2==1 for v in counts.values()):
                return False
    return True

def lemma_criterion(mat):
    m=len(mat); n=len(mat[0])
    for i in range(m):
        R=set(mat[i])
        for j in range(n):
            C={mat[ii][j] for ii in range(m)}
            if R==C:
                return False
    return True

def enumerate_normalized(m,n,q,stop_on_odd=False):
    # normalize first row to 0,1,...,n-1; q>=n
    first=tuple(range(n))
    rows=[first]
    colsets=[{j} for j in range(n)]
    choices=list(permutations(range(q),n))
    complete=0; odd=0
    def rec(i):
        nonlocal complete,odd
        if i==m:
            complete += 1
            mat=[list(r) for r in rows]
            a=is_odd_rook(mat); b=lemma_criterion(mat)
            assert a==b
            if a: odd += 1
            return bool(stop_on_odd and a)
        for row in choices:
            if any(row[j] in colsets[j] for j in range(n)):
                continue
            rows.append(row)
            for j,c in enumerate(row): colsets[j].add(c)
            if rec(i+1): return True
            for j,c in enumerate(row): colsets[j].remove(c)
            rows.pop()
        return False
    rec(1)
    return complete,odd

def construction(n):
    q=n+2
    A=[x for x in range(q) if x not in (0,1)]
    B=[x for x in range(q) if x not in (0,2)]
    assert len(A)==len(B)==n
    return [[(a+b)%q for b in B] for a in A]

print("VERIFY_OK")
total=0
for m,n in [(2,3),(2,4),(3,4)]:
    complete,odd=enumerate_normalized(m,n,n)
    total += complete
    assert complete==odd
    print(f"rectangular m={m}, n={n}, normalized proper n-colorings={complete}, all_odd={odd}")

for n in (2,3,4):
    c_n,o_n=enumerate_normalized(n,n,n)
    c_np1,o_np1=enumerate_normalized(n,n,n+1)
    total += c_n+c_np1
    assert o_n==0 and o_np1==0
    mat=construction(n)
    assert is_odd_rook(mat)
    assert lemma_criterion(mat)
    print(f"square n={n}: normalized proper n-colorings={c_n}, odd={o_n}; "
          f"normalized proper n+1-colorings={c_np1}, odd={o_np1}; n+2 construction OK")

for n in range(2,51):
    mat=construction(n)
    assert is_odd_rook(mat)
    assert lemma_criterion(mat)

print("normalized_proper_colorings_checked =", total)
print("construction_checked_n = 2..50")
print("direct neighborhood parity agrees with row/column-set criterion in all enumerated cases")
