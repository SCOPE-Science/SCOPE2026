# Complete census of shifted C5^(3)-free 3-graphs on 7 vertices

## Context
The 3-uniform tight 5-cycle C5^(3) is the flagship open case on the tight-cycle Turán frontier. The Mubayi–Rödl iterated blow-up gives pi >= 2√3−3 ≈ 0.4641, conjectured tight; Kamčev–Letzter–Pokrovskiy proved equality only for large cycle lengths not divisible by 3, leaving C5 open. Shifted (left-compressed) families are the canonical compression reduction and 7 vertices is the flag-SDP order named in the attack, so the shifted 7-vertex landscape is the natural small-order/flag-basis reference. This record is the exact preset-fallback census; it does not claim any upper bound on pi(C5^(3)).

## Definitions
- Vertex set {0,…,6} (alias {1,…,7}); all 35 triples C(7,3).
- Shifted (left-compressed): H such that for every edge t, every shift-down (replace j in t by i<j, i not in t) is also an edge; equivalently the edge set is predecessor-closed (order ideal) in the shift poset. Closure under immediate downs implies full shiftedness.
- Tight C5^(3): five distinct vertices v_0…v_4 with edges v_0v_1v_2, v_1v_2v_3, v_2v_3v_4, v_3v_4v_0, v_4v_0v_1. There are 12 distinct edge-sets per 5-set; 21 five-sets on 7 vertices; 252 forbidden masks total.
- Isomorphism: S7 action on vertex labels; canonical form = minimum over all 5040 images.

## Result (headline claim)
On {0,…,6}:
- Exactly 352 labeled shifted 3-graphs (order ideals).
- Exactly 68 of them are tight-C5^(3)-free.
- Up to permutation (S7) these form 68 isomorphism classes; every class is a singleton (labeled orbit size within shifted-free = 1 for all 68; 68 distinct full-S7 canonical forms, so no two distinct labeled shifted C5-free ideals are isomorphic).
- Maximum edge count in this class is 16, attained by the unique labeled extremal {012,013,014,015,016,023,024,025,026,034,035,036,045,046,056,123} (all triples containing 0 plus 123).
- Edge-count distribution of the 68 classes: 0:1, 1:1, 2:1, 3:2, 4:3, 5:4, 6:5, 7:7, 8:7, 9:8, 10:8, 11:7, 12:5, 13:4, 14:2, 15:2, 16:1.
- Full list of 68 representatives with edge counts is in artifacts/census.json.

## Proof / evidence (machine-checkable)
1. Generator exhaustiveness: DFS over triples in nondecreasing (sum,lex) order; every triple's predecessors (strict sum decrease on shift-down) are decided before it. EXCLUDE k forces all dependents out; INCLUDE k allowed iff all immediate predecessors are in. Each order ideal generated exactly once → 352. Cross-checked by independent BFS growth (start from empty, add any triple whose predecessors are present) → 352, and by the independent verifier regenerating 352 via its own code path.
2. Per-entry C5-freeness: each ideal tested against all 252 tight-C5 masks → 68 contain none. Every census.json representative re-tested (shifted + C5-free + edge count) by the independent verifier. Auditor independently regenerated 252 masks (12 per 5-set) and confirmed 68 free with the stated distribution.
3. Isomorphism classification: S7 orbits (all 5040 permutations) restricted to the shifted-free set give 68 classes; full-S7 canonical forms pairwise distinct (auditor recomputed 68 distinct canons); every labeled free ideal matches exactly one representative.
4. Maximum: max over the 68 labeled free ideals is 16 edges (unique extremal above, verified shifted and C5-free by brute force).
5. Replay: `python3 output/artifacts/verify_census.py` → VERIFY_OK (stdlib only, minutes). `python3 output/artifacts/shifted_census_n7.py` regenerates census.json.

## Limitations
- Census is over shifted families only (exact fallback scope), not all C5-free 3-graphs on 7 vertices (2^35 infeasible to brute force directly).
- No upper bound on pi(C5^(3)) is claimed; the 0.46-type SDP target remains open.
- Isomorphism grouping verified computationally (S7 orbits + canonical forms), not by a structural human-readable classification.
- Proof is exhaustive machine case analysis with replayable certificates, not a formal proof-assistant certificate.

## Reproducibility
- `python3 output/artifacts/verify_census.py` → VERIFY_OK (stdlib only).
- `python3 output/artifacts/shifted_census_n7.py` → regenerates census.json (352/68/68/16).
- Context-only auxiliaries: `python3 output/artifacts/mr_lower_bound.py` → VERIFY_OK (benchmark 2√3−3); `python3 output/artifacts/verify_shift_violation.py` → VERIFY_OK (naive shifting need not preserve C5-freeness).

## References
- N. Kamčev, S. Letzter, A. Pokrovskiy, The Turán density of tight cycles in three-uniform hypergraphs, arXiv:2209.08134 (pi(C_l)=2√3−3 for large l not divisible by 3; C5 left open).
- J. Balogh, H. Luo, Turán density of long tight cycle minus one hyperedge, arXiv:2303.10530 (distinct C_l^- family, pi=1/4).
- V. Falgas-Ravry, E. Vaughan, On applications of Razborov's flag algebra calculus to extremal 3-graph theory, arXiv:1110.1623 (joint-family flag SDP densities, no single-forbidden tight-C5 ceiling).
