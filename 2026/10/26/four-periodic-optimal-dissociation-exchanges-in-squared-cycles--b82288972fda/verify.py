"""Reproduce the dissociation-set counts and exchange structures for squared cycles.

Run: python verify.py
This finite verifier checks explicit graphs; the unrestricted theorem uses the
block argument given in RESULT.md.
"""
from collections import Counter, deque
from itertools import combinations, product
from math import comb


def ok(mask, m):
    for i in range(m):
        if mask >> i & 1:
            if sum((mask >> ((i + k) % m)) & 1 for k in (-2, -1, 1, 2)) > 1:
                return False
    return True


def exhaustive(m):
    valid = []
    best = 0
    for mask in range(1 << m):
        if not ok(mask, m):
            continue
        t = mask.bit_count()
        if t > best:
            best = t
            valid = [mask]
        elif t == best:
            valid.append(mask)
    return best, set(valid)


def partitions_of_sum(total, slots):
    if slots == 0:
        if total == 0:
            yield ()
        return
    for value in range(total + 1):
        for tail in partitions_of_sum(total - value, slots - 1):
            yield (value,) + tail


def from_blocks(m):
    # Block patterns: singleton S=100, short pair P=1100,
    # long pair L=10100. Additional zeroes follow any block.
    ans = set()
    t = (m // 2) - (m % 4 == 2)
    for s in range(t % 2, 3, 2):
        p = (t - s) // 2
        k = p + s
        if k <= 0:
            continue
        for shortlong in product((False, True), repeat=p):
            ell = sum(shortlong)
            excess = m - (4*p + 3*s + ell)
            if excess < 0 or excess > 2:
                continue
            for singles in combinations(range(k), s):
                flags = []
                c = 0
                for j in range(k):
                    if j in singles:
                        flags.append('S')
                    else:
                        flags.append('L' if shortlong[c] else 'P')
                        c += 1
                for gaps in partitions_of_sum(excess, k):
                    word = ''.join({'S':'100', 'P':'1100', 'L':'10100'}[typ] + '0'*z
                                   for typ,z in zip(flags,gaps))
                    if len(word) != m:
                        continue
                    pattern = sum(1 << i for i,bit in enumerate(word) if bit == '1')
                    for shift in range(m):
                        rot = ((pattern << shift) | (pattern >> (m-shift))) & ((1 << m)-1) if shift else pattern
                        ans.add(rot)
    return t, ans


def classify(mask, m):
    chosen = [i for i in range(m) if mask >> i & 1]
    gaps = [(chosen[(j+1)%len(chosen)]-chosen[j]) % m for j in range(len(chosen))]
    cuts = [j for j,v in enumerate(gaps) if v > 2]
    assert cuts
    groups = []
    for x in range(len(cuts)):
        a = (cuts[x] + 1) % len(chosen)
        b = cuts[(x+1) % len(cuts)]
        group = []
        while True:
            group.append(chosen[a])
            if a == b: break
            a = (a + 1) % len(chosen)
        typ = 'S' if len(group)==1 else ('P' if (group[1]-group[0])%m == 1 else 'L')
        groups.append((group[0], typ))
    groups.sort()
    labels=[]
    for j,(start,typ) in enumerate(groups):
        step=(groups[(j+1)%len(groups)][0]-start)%m
        labels.append((typ,step-{'P':4,'S':3,'L':5}[typ]))
    return labels


def statistics(m, vertices):
    d={mask:i for i,mask in enumerate(sorted(vertices))}
    arr=list(d)
    adj=[set() for _ in arr]
    for i,mask in enumerate(arr):
        for a in range(m):
            if not (mask >> a) & 1: continue
            for b in range(m):
                if (mask >> b) & 1: continue
                target=mask ^ (1 << a) ^ (1 << b)
                j=d.get(target)
                if j is not None and j>i:
                    adj[i].add(j);adj[j].add(i)
    remaining=set(range(len(arr)))
    sizes=[]
    while remaining:
        seed=remaining.pop(); queue=[seed]; size=1
        while queue:
            for v in adj[queue.pop()] & remaining:
                remaining.remove(v);queue.append(v);size+=1
        sizes.append(size)
    degrees=Counter(len(x) for x in adj)
    return arr,adj,degrees,sorted(sizes)


def expected(m):
    if m%4==0:
        return m//2,4,0,{0:4},[1]*4
    if m%4==1:
        return m//2,2*m,3*m,{2:m,4:m},[2*m]
    if m%4==2:
        return m//2-1,5*m*(m-2)//8,m*(7*m-6)//4,{
            4:m*(m-8)//4,6:m*(m+2)//4,8:m*(m+2)//8},[5*m*(m-2)//8]
    return m//2,m,m,{2:m},[m]


def verify():
    # Independent, complete subset enumeration rather than using the block formula.
    for m in range(7,17):
        max_size,brute=exhaustive(m)
        proposed,structured=from_blocks(m)
        assert max_size==proposed and brute==structured,(m,'exhaustive comparison')
        print('EXHAUSTIVE_OK',m,max_size,len(brute))
    for m in range(7,33):
        val,ans=from_blocks(m)
        theory=expected(m)
        arr,adj,degrees,components=statistics(m,ans)
        assert val==theory[0] and len(ans)==theory[1],(m,'count')
        assert sum(len(x) for x in adj)//2==theory[2],(m,'edges')
        assert degrees==Counter(theory[3]) if False else dict(degrees)==dict(theory[3]),(m,'degree')
        assert components==theory[4],(m,'components')
        assert all(ok(x,m) for x in ans)
        # Verify the precise defect-degree table, independent of the closed counts.
        for mask,neighbors in zip(arr,adj):
            b=classify(mask,m)
            if m%4==2:
                singles=[j for j,(tag,extra) in enumerate(b) if tag=='S']
                longs=sum(tag=='L' for tag,extra in b)
                if singles:
                    k=len(b)
                    near=(singles[0]-singles[1])%k in (1,k-1)
                    assert len(neighbors)==(6 if near else 4)
                else:
                    assert len(neighbors)==(8 if longs==0 else 6 if longs==1 else 4)
            elif m%4==1:
                assert len(neighbors)==(2 if any(tag=='L' for tag,extra in b) else 4)
        print('EXCHANGE_OK',m,'states',len(ans),'edges',theory[2],
              'degree_counts',dict(sorted(degrees.items())),
              'components',len(components))
    print('VERIFY_OK')

if __name__=='__main__': verify()
