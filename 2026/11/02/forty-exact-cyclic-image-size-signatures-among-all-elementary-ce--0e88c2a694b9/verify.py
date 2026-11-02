#!/usr/bin/env python3
"""Exact classification of one-step cyclic image-count signatures of binary radius-one cellular automata.

No external packages are required. Run: python3 verify.py
"""
from collections import defaultdict, Counter
import hashlib
import json

IDENTITY = sum(1 << (5*i) for i in range(4))


def reflected(rule):
    return sum(((rule >> (((j & 1) << 2) | (j & 2) | (j >> 2))) & 1) << j for j in range(8))


def color_conjugated(rule):
    return sum((1-((rule >> (7-j)) & 1)) << j for j in range(8))


def symmetry_classes():
    unseen = set(range(256))
    classes = []
    while unseen:
        orbit = {min(unseen)}
        while True:
            expanded = orbit | {reflected(r) for r in orbit} | {color_conjugated(r) for r in orbit}
            if expanded == orbit:
                break
            orbit = expanded
        assert orbit <= unseen
        unseen -= orbit
        classes.append(tuple(sorted(orbit)))
    assert len(classes) == 88 and sum(map(len, classes)) == 256
    return classes


def boolean_product(left, right):
    result = 0
    for i in range(4):
        row = (left >> (4*i)) & 15
        newrow = 0
        for j in range(4):
            if row & (1 << j):
                newrow |= (right >> (4*j)) & 15
        result |= newrow << (4*i)
    return result


def rule_relations(rule):
    matrices = [0,0]
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                source = (a << 1) | b
                target = (b << 1) | c
                symbol = (rule >> ((a << 2) | (b << 1) | c)) & 1
                matrices[symbol] |= 1 << (4*source+target)
    return matrices


def transition_graph(rule):
    m0,m1 = rule_relations(rule)
    states = [IDENTITY]
    number = {IDENTITY:0}
    arrows = []
    for relation in states:
        successors = []
        for matrix in (m0,m1):
            target = boolean_product(relation,matrix)
            if target not in number:
                number[target] = len(states)
                states.append(target)
            successors.append(number[target])
        arrows.append(tuple(successors))
    return states, arrows


def initial_vector(states):
    return [int(bool(x & IDENTITY)) for x in states]


def advance(v, arrows):
    return [v[i]+v[j] for i,j in arrows]


def first_terms(states, arrows, count):
    v = initial_vector(states)
    out = []
    for n in range(count):
        out.append(v[0])
        v = advance(v, arrows)
    return tuple(out)


def check_equal_all_lengths(x, y, cached):
    states_x, arrows_x = cached[x]
    states_y, arrows_y = cached[y]
    bound = len(states_x) + len(states_y)
    vx = initial_vector(states_x)
    vy = initial_vector(states_y)
    for n in range(bound):
        assert vx[0] == vy[0], (x,y,n,vx[0],vy[0])
        vx = advance(vx, arrows_x)
        vy = advance(vy, arrows_y)
    return bound


def forward_image_count(rule,n):
    # Independently evaluate the local lookup table on each indexed ring.
    seen = set()
    for word in range(1 << n):
        output = 0
        for pos in range(n):
            left = (word >> ((pos-1) % n)) & 1
            center = (word >> pos) & 1
            right = (word >> ((pos+1) % n)) & 1
            output |= ((rule >> (4*left+2*center+right)) & 1) << pos
        seen.add(output)
    return len(seen)


def main():
    classes = symmetry_classes()
    representatives = [c[0] for c in classes]
    cache = {r: transition_graph(r) for r in representatives}
    fingerprints = {r:first_terms(*cache[r], 7) for r in representatives}
    grouped = defaultdict(list)
    for r in representatives:
        grouped[fingerprints[r]].append(r)
    grouped = list(grouped.values())
    assert len(grouped) == 40
    assert Counter(map(len, grouped)) == {1:8,2:26,4:4,6:2}
    assert len(set(fingerprints[g[0]] for g in grouped)) == len(grouped)

    checks = []
    for group in grouped:
        base = group[0]
        for r in group[1:]:
            checks.append((base,r,check_equal_all_lengths(base,r,cache)))
    assert len(checks) == 48

    # Every nongroup pair is already separated by one of n=1,...,6.
    for i, g in enumerate(grouped):
        for h in grouped[i+1:]:
            assert fingerprints[g[0]] != fingerprints[h[0]]

    # The cyclic-image algebra is also verified independently by direct forward enumeration.
    for n in range(1, 12):
        predicted = {r:first_terms(*cache[r],n+1)[n] for r in representatives}
        for c in classes:
            for rule in c:
                assert forward_image_count(rule,n) == predicted[c[0]],(rule,n)

    result = {
        "definition":"A_r(n)=|{F_r(x):x in {0,1}^n}| with cyclic indices and synchronous updates",
        "rule_count":256,
        "ordinary_symmetry_classes":len(classes),
        "all_length_image_count_classes":len(grouped),
        "class_size_histogram":{str(k):v for k,v in sorted(Counter(map(len,grouped)).items())},
        "groups_of_symmetry_class_representatives":grouped,
        "maximum_first_distinguishing_length":max(next(n for n in range(7) if fingerprints[g[0]][n]!=fingerprints[h[0]][n]) for i,g in enumerate(grouped) for h in grouped[i+1:]),
        "all_length_pair_equalities_checked":len(checks),
        "largest_pair_bound":max(n for _,_,n in checks),
        "largest_single_automaton_state_count":max(len(cache[r][0]) for r in representatives),
        "small_direct_checks_all_rules":"n=1,...,11",
        "pair_checks": [{"representatives":[r,s],"number_of_initial_coefficients_proved_equal":bound} for r,s,bound in checks]
    }
    canonical = json.dumps(result,sort_keys=True,separators=(',',':')).encode('utf-8')
    print('RESULT',json.dumps({k:v for k,v in result.items() if k not in ('groups_of_symmetry_class_representatives','pair_checks')},sort_keys=True))
    print('CERTIFICATE_SHA256',hashlib.sha256(canonical).hexdigest())
    print('VERIFY_OK')
    return result

if __name__ == '__main__':
    main()
