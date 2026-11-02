from collections import Counter
from math import comb

def trees(n):
    rows=[((),(),1,1)] # (recursive tree shape, canonical signature, automorphism size, bottom bitmask)
    for h in range(1,n+1):
        nxt=[]
        subs=[None]+rows
        for left in subs:
            for right in subs:
                left_mask = left[3] if left else 0
                right_mask = right[3] if right else 0
                mask = left_mask | (right_mask << (2**(h-1)))
                child_sigs=[a[1] for a in (left,right) if a is not None]
                sig = tuple(sorted(child_sigs, key=str))
                aut=(left[2] if left else 1)*(right[2] if right else 1)*(2 if len(sig)==2 and sig[0]==sig[1] else 1)
                nxt.append(((left[0] if left else None,right[0] if right else None),sig,aut,mask))
        rows=nxt
    return rows
for n in range(4):
    rows=trees(n)
    signatures=Counter(r[1] for r in rows)
    leafcount=Counter()
    for _,sig,aut,mask in rows:
        leafcount[mask]+=aut*signatures[sig]
    B=2**n
    c=2**(B-1)
    exp=(2**(2*B-1)-1)
    assert len(leafcount)==2**B if n>0 else len(leafcount)==1
    assert leafcount[0]==c-1,(n,leafcount[0],c-1)
    assert all(leafcount[m]==c for m in range(1,2**B)),(n,leafcount)
    assert sum(leafcount.values())==exp
    byrank=[sum(v for m,v in leafcount.items() if m.bit_count()==k) for k in range(B+1)]
    print(f'n={n} root_subtrees={len(rows)} map_count={exp} fixed_nonempty={c} zero={c-1} by_rank={byrank}')
print('VERIFY_OK')
