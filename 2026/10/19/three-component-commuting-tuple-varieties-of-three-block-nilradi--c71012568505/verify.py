#!/usr/bin/env python3
"""Direct finite-field checks for commuting tuples in three-block nilradicals.
Only uses field arithmetic and the block-matrix multiplication rule.
"""
from itertools import product

def mul(a,b,q):
    if q != 4:
        return a*b % q
    z=0
    for j in range(2):
        if (b>>j)&1:z ^= a<<j
    if z&8:z^=0b1100
    if z&4:z^=0b111
    return z

def sub(a,b,q):return a^b if q==4 else (a-b)%q

def verify(q,r,s,k):
    vectors=list(product(range(q),repeat=r+s))
    mx=len(vectors)
    # Matrix coefficient (i,j) in the commutator equals:
    # X_i[r-th middle column] * X_j[middle row], minus reversed product.
    compat=bytearray(mx*mx)
    for i,a in enumerate(vectors):
        u=a[:r];v=a[r:]
        for j,b in enumerate(vectors):
            U=b[:r]; V=b[r:]
            commute=True
            for h in range(r):
                for t in range(s):
                    if sub(mul(u[h],V[t],q),mul(U[h],v[t],q),q):
                        commute=False;break
                if not commute:break
            compat[i*mx+j]=commute
    actual=0
    for tup in product(range(mx), repeat=k):
        if not all(compat[tup[i]*mx+tup[j]] for i in range(k) for j in range(i+1,k)):
            continue
        actual+=1
        rows=[vectors[t] for t in tup]
        all_u=all(not any(x[r:]) for x in rows)
        all_v=all(not any(x[:r]) for x in rows)
        rank_le_one = True
        for i in range(k):
            for j in range(i+1,k):
                for h in range(r+s):
                    for t in range(h+1,r+s):
                        if sub(mul(rows[i][h],rows[j][t],q),mul(rows[j][h],rows[i][t],q),q):
                            rank_le_one=False;break
                    if not rank_le_one: break
                if not rank_le_one:break
            if not rank_le_one:break
        assert all_u or all_v or rank_le_one,(q,r,s,k,tup)
    # Inclusion-exclusion, with the non-pure rank-one lines counted once each.
    L=(q**r-1)*(q**s-1)//(q-1)
    expected=q**(k*r)+q**(k*s)-1+L*(q**k-1)
    assert actual==expected,(q,r,s,k,actual,expected)
    full=actual*q**(r*s*k)
    print('PASS',q,r,s,k,'first_layer',actual,'full',full,flush=True)

if __name__=='__main__':
    for c in [(2,2,2,2),(2,2,2,3),(2,2,2,4),(2,2,3,3),(2,3,2,3),(3,2,2,2),(3,2,2,3),(4,2,2,2),(5,2,2,2)]:
        verify(*c)
    print('VERIFY_OK_THREE_BLOCK_COMMUTING_TUPLES')
