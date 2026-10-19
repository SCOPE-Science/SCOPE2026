"""Independent finite-state transfer check for C5-by-Cn two-domination.

Enumerates all independent column configurations and checks a local triple,
without the structural classification or direct vertex recursion.
Run: python verify_transfer.py
"""
from collections import defaultdict

M=5
columns=[x for x in range(1<<M) if all(not (x>>i & 1 and x>>((i+1)%M) & 1) for i in range(M))]
assert len(columns)==11
states=[(a,b) for a in columns for b in columns if not (a&b)]
transition={s:[] for s in states}
for a,b in states:
    for c in columns:
        if b&c:continue
        if any(not ((b>>i)&1) and (((b>>((i-1)%M))&1)+((b>>((i+1)%M))&1)+((a>>i)&1)+((c>>i)&1)<2) for i in range(M)):
            continue
        transition[(a,b)].append((b,c))
        assert (b,c) in transition

def count(n):
    # trace(A^n) on ordered adjacent column pairs.
    total=0
    for start in states:
        dp={start:1}
        for _ in range(n):
            nxt=defaultdict(int)
            for st,w in dp.items():
                for v in transition[st]:nxt[v]+=w
            dp=nxt
        total+=dp.get(start,0)
    return total

# A closed n-walk encodes exactly one cyclic sequence of n labelled columns.
for n in range(3,41):
    actual=count(n)
    expected=10 if n%5==0 else 0
    assert actual==expected, (n,actual,expected)
    print(f'length={n} cyclic_transfer_count={actual}')

# Identify states lying on directed cycles by transitive closure.  The
# recurrent subgraph consists of exactly two directed five-cycles.
reach={v:set(transition[v]) for v in states}
for _ in range(len(states)):
    before=sum(len(x) for x in reach.values())
    for v in states:
        for w in list(reach[v]):reach[v]|=reach[w]
    if sum(len(x) for x in reach.values())==before:break
cyclic={v for v in states if v in reach[v]}
assert len(cyclic)==10
assert all(len([w for w in transition[v] if w in cyclic])==1 for v in cyclic)
assert all(sum(v in transition[w] for w in cyclic)==1 for v in cyclic)
remaining=set(cyclic)
cycle_lengths=[]
while remaining:
    start=next(iter(remaining))
    here=start
    trail=set()
    while here not in trail:
        assert here in remaining
        trail.add(here)
        here=next(w for w in transition[here] if w in cyclic)
    assert here==start
    remaining-=trail
    cycle_lengths.append(len(trail))
assert sorted(cycle_lengths)==[5,5]
print('independent_columns',len(columns),'adjacent_pair_states',len(states))
print('directed_transitions',sum(len(v) for v in transition.values()))
print('cyclic_states',len(cyclic),'cyclic_components',2,'cycle_length',5)
print('TRANSFER_VERIFICATION_OK')
