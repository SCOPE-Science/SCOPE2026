#!/usr/bin/env python3
"""Finite verification of a balanced ternary single-deletion code theorem.
Standard-library-only; no external files or network access.
"""
from itertools import product, combinations
from collections import Counter

ALPHABET = "012"
WORDS = tuple("".join(t) for t in product(ALPHABET, repeat=6)
              if all(t.count(s) == 2 for s in ALPHABET))
assert len(WORDS) == 90 and len(set(WORDS)) == 90
SHADOW = tuple(frozenset(w[:i] + w[i+1:] for i in range(6)) for w in WORDS)
OUTS = frozenset().union(*SHADOW)
assert len(OUTS) == 90

# Exact 18-output upper-bound witness.
TRANSVERSAL = ("00112", "00221", "01012", "01120", "02021", "02210",
               "10012", "10120", "11022", "11200", "12102", "12201",
               "20021", "20210", "21102", "21201", "22011", "22100")
assert len(set(TRANSVERSAL)) == 18
assert set(TRANSVERSAL) <= OUTS
# Each input has exactly one output in the displayed transversal.
for s in SHADOW:
    assert len(s.intersection(TRANSVERSAL)) == 1
GROUPS = tuple(tuple(j for j, s in enumerate(SHADOW) if out in s)
               for out in TRANSVERSAL)
assert all(len(g) == 5 for g in GROUPS)
assert sorted(j for g in GROUPS for j in g) == list(range(90))

# By the preceding identity, each single-deletion code has at most 18 words.
# The complete equality enumeration chooses one word from each of the 18
# five-word groups. Its recursion visits every feasible partial choice.
ALL90 = (1 << len(WORDS)) - 1
COMPAT = tuple(sum(1 << j for j in range(len(WORDS))
                   if j != i and not (SHADOW[i] & SHADOW[j]))
               for i in range(len(WORDS)))
GROUPMASKS = tuple(sum(1 << j for j in g) for g in GROUPS)
SOLUTIONS = set()
NODES = 0

def enumerator(rem: tuple[int, ...], allowed: int, selected: tuple[int, ...]):
    global NODES
    NODES += 1
    if not rem:
        SOLUTIONS.add(tuple(sorted(selected)))
        return
    # MRV is only an ordering heuristic; no branch is pruned except when
    # some as-yet-unfilled group has no available candidate.
    opts = [((GROUPMASKS[g] & allowed).bit_count(), g) for g in rem]
    num, g = min(opts)
    if not num:
        return
    candidates = GROUPMASKS[g] & allowed
    rest = tuple(h for h in rem if h != g)
    while candidates:
        bit = candidates & -candidates
        v = bit.bit_length()-1
        candidates ^= bit
        enumerator(rest, allowed & COMPAT[v], selected+(v,))

enumerator(tuple(range(18)), ALL90, ())
assert len(SOLUTIONS) == 8, (len(SOLUTIONS), NODES)
CODESETS = {frozenset(WORDS[i] for i in code) for code in SOLUTIONS}
assert len(CODESETS) == 8 and all(len(s) == 18 for s in CODESETS)
assert all(not (SHADOW[i] & SHADOW[j]) for code in SOLUTIONS
           for i, j in combinations(code, 2))
CORE = frozenset.intersection(*CODESETS)
assert len(CORE) == 12
CORE_EXPECTED = set("001122 002211 010212 020121 101202 110022 112200 121020 202101 212010 220011 221100".split())
assert CORE == CORE_EXPECTED
BLOCKS = ((('012210','102201'),('012201','102210')),
          (('021120','201102'),('021102','201120')),
          (('120012','210021'),('120021','210012')))
GENERATED = {frozenset(CORE.union(*[set(BLOCKS[i][b]) for i,b in enumerate(bits)]))
             for bits in product((0,1),repeat=3)}
assert GENERATED == CODESETS

# Direct self-contained chromatic and clique verification.
# These are maximal-clique calculations on the *confusability* graph.
CONFLICT = tuple(sum(1 << j for j in range(len(WORDS))
                     if j != i and (SHADOW[i] & SHADOW[j]))
                 for i in range(len(WORDS)))
MAXIMAL = Counter()

def bron_kerbosch(r: int, p: int, x: int):
    if not p and not x:
        MAXIMAL[r.bit_count()] += 1
        return
    union = p | x
    if union:
        best = max((v for v in range(len(WORDS)) if (union >> v) & 1),
                   key=lambda v: (p & CONFLICT[v]).bit_count())
        candidates = p & ~CONFLICT[best]
    else:
        candidates = p
    while candidates:
        bit = candidates & -candidates
        v = bit.bit_length()-1
        candidates ^= bit
        bron_kerbosch(r | bit, p & CONFLICT[v], x & CONFLICT[v])
        p ^= bit
        x |= bit

bron_kerbosch(0, ALL90, 0)
assert max(MAXIMAL) == 5, MAXIMAL
assert MAXIMAL[5] == 96 and sum(MAXIMAL.values()) == 272, MAXIMAL

# Explicit six-coloring by descent syndrome modulo 6.
def color(word: str) -> int:
    return sum(i+1 for i in range(5) if word[i] > word[i+1]) % 6
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        if SHADOW[i] & SHADOW[j]:
            assert color(WORDS[i]) != color(WORDS[j])
assert Counter(map(color,WORDS)) == Counter({0:16, 1:14, 2:16, 3:14, 4:16, 5:14})
# The eighteen five-parent cliques force every color class in any hypothetical
# proper five-coloring to have 18 elements. Every 18-code contains CORE.
# Thus two such color classes cannot be disjoint: impossible.
assert CORE and all(len(g)==5 for g in GROUPS)
print("VERIFY_OK inputs=90 outputs=90 transversal=18 max_code=18 "+
      f"max_code_sets={len(CODESETS)} common_core={len(CORE)} "+
      f"search_nodes={NODES} clique_max=5 clique5=96 maximal_cliques=272 "+
      "chromatic=6")
