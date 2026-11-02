#!/usr/bin/env python3
"""Exact finite quotient and independent microscopic checks for 4-color CCA on K_{a,b,c}."""
from collections import Counter, defaultdict
from itertools import product
from math import comb
from pathlib import Path

Q = 4
STATES = list(product(range(1, 16), repeat=3))


def support_step(state):
    next_masks = []
    for shore in range(3):
        neighbors = state[(shore + 1) % 3] | state[(shore + 2) % 3]
        image = 0
        for color in range(4):
            if state[shore] & (1 << color):
                nxt = (color + 1) % 4
                new_color = nxt if (neighbors & (1 << nxt)) else color
                image |= (1 << new_color)
        next_masks.append(image)
    return tuple(next_masks)


def decorated_trajectory(s, length=7):
    """One distinguishable vertex of every initially occupied shore-color."""
    labels = [tuple(c for c in range(4) if m >> c & 1) for m in s]
    out = [tuple(labels)]
    for _ in range(length):
        sets = [set(sh) for sh in labels]
        labels = [tuple((c + 1) % 4 if ((c + 1) % 4) in (sets[(i + 1) % 3] | sets[(i + 2) % 3]) else c
                        for c in sh) for i, sh in enumerate(labels)]
        out.append(tuple(labels))
    return out


def periodic_class(track):
    for t in range(4):
        for p in (1, 2, 4):
            if t + p <= 7 and track[t] == track[t + p]:
                return (t, p)
    raise AssertionError('no short eventual period')


def surj(k, n):
    return sum((-1) ** j * comb(k, j) * (k - j) ** n for j in range(k + 1))


# Expected (support-cardinality multiset : per-ordered-assignment multiplicity).
EXPECTED = {
    1: {(1,1,1):16,(1,1,2):8,(1,2,2):4,(2,2,2):2},
    4: {(1,1,2):4,(1,2,2):16,(1,2,3):8,(1,3,3):12,
        (1,3,4):4,(1,4,4):4,(2,2,2):42,(2,2,3):32,
        (2,2,4):6,(2,3,3):36,(2,3,4):12,(2,4,4):6,
        (3,3,3):36,(3,3,4):12,(3,4,4):4,(4,4,4):1},
}


def count_from_tensor(size, coeff):
    a, b, c = size
    return sum(v * surj(i,a) * surj(j,b) * surj(k,c)
               for (i,j,k),v in coeff.items())


def direct_step(config, sizes):
    a,b,c=sizes
    sh = [config[:a], config[a:a+b], config[a+b:a+b+c]]
    new = []
    for i, part in enumerate(sh):
        opposite = set(sh[(i+1)%3]) | set(sh[(i+2)%3])
        new.extend(((x+1)%4 if (x+1)%4 in opposite else x) for x in part)
    return tuple(new)


def direct_count(size):
    counts=Counter()
    support_counts=Counter()
    N=sum(size)
    for state in product(range(Q), repeat=N):
        path=[state]
        for i in range(7):
            path.append(direct_step(path[-1],size))
        assert path[3] == path[7]
        cp=periodic_class(path)
        counts[cp]+=1
        a,b,c=size
        tri=state[:a],state[a:a+b],state[a+b:a+b+c]
        masks=tuple(sum(1 << j for j in set(sh)) for sh in tri)
        support_counts[(masks,cp)]+=1
    return counts, support_counts


def main():
    assert len(STATES) == 3375
    classes={}
    cycle_hist=Counter()
    seen_global=set()
    max_pre=0
    for s in STATES:
        track=decorated_trajectory(s)
        assert track[3]==track[7], ('F7 != F3',s)
        sup=s
        for t in range(8):
            assert tuple(sum(1<<c for c in set(sh)) for sh in track[t])==sup
            if t<7:sup=support_step(sup)
        cl=periodic_class(track)
        classes[s]=cl
        max_pre=max(max_pre,cl[0])
    assert max_pre==3
    header="support_mask_a\tsupport_mask_b\tsupport_mask_c\tfirst_periodic_time\tleast_temporal_period\n"
    table=header+"".join(f"{s[0]}\t{s[1]}\t{s[2]}\t{classes[s][0]}\t{classes[s][1]}\n" for s in STATES)
    data=Path(__file__).resolve().parent / "support_classes.tsv"
    if data.is_file(): assert data.read_text(encoding="utf-8")==table
    assert classes[(1,1,6)]==(3,1)

    expected_tensors={p:Counter() for p in (1,4)}
    for s, (t,p) in classes.items():
        if t==0:
            expected_tensors[p][tuple(m.bit_count() for m in s)]+=1
    for p,tab in expected_tensors.items():
        observed = defaultdict(set)
        for k,v in tab.items(): observed[tuple(sorted(k))].add(v)
        assert all(len(vals)==1 for vals in observed.values())
        scalar={k:next(iter(vals)) for k,vals in observed.items()}
        assert scalar==EXPECTED[p], (p,scalar,EXPECTED[p])
        print('period',p,'recurrent support nodes',sum(tab.values()),'multiset coefficient terms',len(scalar))
    assert sum(len(x) for x in EXPECTED.values())==20
    # Enumerate primitive support cycles independently via forward orbits.
    for s in STATES:
        if s in seen_global:continue
        orbit=[];pos={}; v=s
        while v not in pos and v not in seen_global:
            pos[v]=len(orbit);orbit.append(v);v=support_step(v)
        if v in pos:cycle_hist[len(orbit)-pos[v]]+=1
        seen_global.update(orbit)
    assert cycle_hist=={1:55,2:9,4:150},cycle_hist
    assert Counter(classes.values())=={
        (0,1):54,(0,4):619,
        (1,1):112,(1,4):702,
        (2,1):856,(2,4):384,
        (3,1):552,(3,4):96,
    },Counter(classes.values())
    print('support quotient 3375 verified; recurrent support cycles',dict(cycle_hist))
    print('complete preperiod-period support histogram:',sorted(Counter(classes.values()).items()))

    samples=[(1,1,1),(1,1,2),(1,2,2),(2,2,2),
             (1,2,3),(1,3,3),(2,2,3),(2,3,3),(1,3,4)]
    total=0
    for sizes in samples:
        counts,sup_counts=direct_count(sizes)
        n=4**sum(sizes);total+=n
        predicted=Counter()
        for state,c in classes.items():
            weight=1
            for shore,s in enumerate(state):weight*=surj(s.bit_count(),sizes[shore])
            predicted[c]+=weight
        assert counts==predicted, (sizes,counts,predicted)
        for p in (1,4):
            formula=count_from_tensor(sizes,expected_tensors[p])
            assert formula==counts[(0,p)]==(count_from_tensor(sizes,{k:v for k,v in expected_tensors[p].items()}))
            assert formula%p==0
        assert sum(counts.values())==n
        for (s,cp),m in sup_counts.items():
            assert classes[s]==cp
        print('micro',sizes,'states',n,'fixed',counts[(0,1)],'period2',counts[(0,2)],'period4',counts[(0,4)])
    print('total independently simulated microscopic configurations',total)
    print('CCA4_TRIPARTITE_VERIFY_OK')

if __name__=='__main__':main()
