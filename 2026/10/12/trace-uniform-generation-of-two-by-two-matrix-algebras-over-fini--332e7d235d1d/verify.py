"""Reproduce the small-field tests for trace-conditioned generators of M_2(F_q).

Uses elementary finite-field arithmetic and explicit word-space closure, with
no external dependencies or precomputed orbit classifications.
"""
from collections import Counter
from itertools import product


def add(a,b,q):
    return (a ^ b) if q in (2,4) else (a+b)%q


def neg(a,q):
    return a if q in (2,4) else (-a)%q


def mul(a,b,q):
    if q != 4:
        return (a*b)%q
    z=0
    if b&1: z ^= a
    if b&2: z ^= a << 1
    if z&8: z ^= 0b1110 # x^3 = x^2+x, from x^2=x+1
    if z&4: z ^= 0b111  # x^2=x+1
    return z


def inverse(a,q):
    assert a
    return next(v for v in range(1,q) if mul(a,v,q)==1)


def mm(a,b,q):
    return (add(mul(a[0],b[0],q),mul(a[1],b[2],q),q),
            add(mul(a[0],b[1],q),mul(a[1],b[3],q),q),
            add(mul(a[2],b[0],q),mul(a[3],b[2],q),q),
            add(mul(a[2],b[1],q),mul(a[3],b[3],q),q))


def rref_rank(vecs,q):
    basis={}
    for vec in vecs:
        v=list(vec)
        for p in sorted(basis):
            if v[p]:
                k=v[p]
                for j in range(p,4):
                    v[j]=add(v[j],neg(mul(k,basis[p][j],q),q),q)
        nz=next((i for i,x in enumerate(v) if x),None)
        if nz is not None:
            iv=inverse(v[nz],q)
            for j in range(nz,4):v[j]=mul(v[j],iv,q)
            basis[nz]=v
    return len(basis)


def generates(mats,q):
    # For 2x2 matrices the generated associative algebra is spanned by all words.
    # Repeatedly extend by right multiplication with generators until stable.
    one=(1,0,0,1)
    seen=[one]
    rank=1
    while True:
        proposals=[]
        for w in seen:
            for a in mats:
                proposals.append(mm(w,a,q))
        added=False
        for p in proposals:
            if rref_rank(seen+[p],q)>rank:
                seen.append(p)
                rank+=1
                added=True
                if rank==4:return True
        if not added:return False


def test(q,m):
    mats=list(product(range(q),repeat=4))
    traces={a:add(a[0],a[3],q) for a in mats}
    counts=Counter()
    tested=0
    for tpl in product(mats,repeat=m):
        tested+=1
        if generates(tpl,q):
            counts[tuple(traces[a] for a in tpl)]+=1
    expectation=q**m*(q**m-1)*(q**m-q)
    assert tested==q**(4*m)
    assert set(counts)==set(product(range(q),repeat=m)) if m>=2 else not counts
    for tr in product(range(q),repeat=m):
        assert counts[tr]==expectation,(q,m,tr,counts[tr],expectation)
    assert sum(counts.values())==q**(2*m)*(q**m-1)*(q**m-q)
    print('PASS',f'q={q}',f'm={m}',f'checked={tested}',f'per_trace={expectation}',f'generating={sum(counts.values())}')


if __name__=='__main__':
    for q,m in ((2,2),(3,2),(4,2),(2,3)):
        test(q,m)
    print('VERIFY_OK_TRACE_GENERATION')
