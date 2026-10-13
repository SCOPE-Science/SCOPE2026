"""Independent finite checks for cyclic adjacent-merge reset thresholds.
Python >=3.9, standard library only. Run: python3 verify.py
"""
from collections import deque
from itertools import combinations
from random import Random


def rt_formula(n, marked):
    assert n >= 2 and marked and all(0 <= p < n for p in marked)
    best = None
    best_start = None
    for start in range(n):
        hits = 0
        length = 0
        while hits < n-1:
            pos = (start-length) % n
            if pos in marked:
                hits += 1
            length += 1
        if best is None or length < best:
            best, best_start = length, start
    return best, best_start


def forward_image(mask, n, marked, letter):
    full = (1 << n)-1
    if letter == -1:
        return ((mask << 1) & full) | (mask >> (n-1))
    j = letter
    source = (j-1) % n
    if mask & (1 << source):
        return (mask & ~(1 << source)) | (1 << j)
    return mask


def independent_forward_bfs(n, marked):
    full = (1 << n)-1
    q = deque([(full, 0)])
    seen = {full}
    while q:
        mask, d = q.popleft()
        if mask.bit_count() == 1:
            return d
        for a in [-1, *sorted(marked)]:
            nxt = forward_image(mask,n,marked,a)
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt,d+1))
    raise AssertionError('unsynchronizing')


def backwards_witness(n, marked):
    length, s = rt_formula(n,marked)
    singleton = s
    interval = {s}
    reverse_letters=[]
    for _ in range(length):
        if s in marked:
            # Full inverse image under the idempotent j-1 -> j.
            j=s
            old=interval
            interval={x for x in range(n) if (j if x == (j-1)%n else x) in old}
            reverse_letters.append(j)
        else:
            interval={(x-1)%n for x in interval}
            reverse_letters.append(-1)
        s=(s-1)%n
        assert interval=={(s+i)%n for i in range(len(interval))}
    assert len(interval)==n
    mask=(1<<n)-1
    for letter in reversed(reverse_letters):
        mask=forward_image(mask,n,marked,letter)
    assert mask==(1<<singleton)
    return length


def check_interval_preimages(max_n):
    count=0
    for n in range(2,max_n+1):
        for s in range(n):
            for size in range(1,n+1):
                interval={(s+i)%n for i in range(size)}
                for j in range(n):
                    pre={x for x in range(n) if (j if x==(j-1)%n else x) in interval}
                    if pre:
                        assert pre=={(s+i)%n for i in range(len(pre))} or (s==j and pre=={((s-1)+i)%n for i in range(len(pre))})
                        if len(pre)>len(interval):
                            assert s==j and len(pre)==len(interval)+1
                        if len(pre)<len(interval):
                            assert len(pre)==len(interval)-1
                    count+=1
    return count


def test():
    rng=Random(20261008)
    examples=0
    for n in range(2,12):
        if n<=8:
            family=[frozenset(i for i in range(n) if b>>i&1) for b in range(1,1<<n)]
        else:
            family=[frozenset({0,k}) for k in range(1,n)]
            family.extend(frozenset(rng.sample(range(n),rng.randrange(1,n+1))) for _ in range({9:150,10:80,11:35}[n]))
        for marked in family:
            predicted,start=rt_formula(n,marked)
            measured=independent_forward_bfs(n,marked)
            assert predicted==measured, (n,marked,predicted,measured)
            assert backwards_witness(n,marked)==measured
            if len(marked)==2:
                i,j=sorted(marked)
                gap=min(j-i,n-(j-i))
                if n%2==0:
                    closed=n*(n-2)//2 + 1
                else:
                    closed=n*(n-3)//2 + 1 + gap
                assert measured==closed
            if len(marked)==1:
                assert measured==(n-1)**2
            examples+=1
    intervals=check_interval_preimages(12)
    print('VERIFY_OK', f'automata={examples}',f'interval_cases={intervals}',
          'complete_subfamilies=n2..8', 'random_and_two_pin=n9..11',
          'one_pin=(n-1)^2','two_pin_parity_gap=checked',
          'forward_BFS=independent','backward_witness=replayed')


if __name__=='__main__':
    test()
