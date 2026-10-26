# Scientific review

## Correctness — PASS

The 27-vertex seed is specified by 81 explicit colours in `certificate.json`; a standalone exhaustive enumerator in `verify.py` checks distinctness at every one of its 27 vertices and all 81 simple four-cycles. A proper six-colouring of any six-regular graph with an odd number of vertices is impossible by a matching-count argument. Reduction modulo three on each length-\(3a\) cycle is a locally bijective graph covering; squares of the larger product descend to rainbow squares of the seed, proving the unrestricted bound without computational extrapolation. The verifier also checks six larger lifted graphs, but the generality rests on this proof.

## Originality — PASS, subject to further bibliographic review

Gyárfás–Sárközy (2023), Theorem 1.8, leave the ternary three-cube at bounds seven through eight; their Theorem 1.7 covers a seven-divisibility family instead. Jiang–Li (2026), Section 7, explicitly conjecture degree-plus-one for all odd discrete tori. Their Lemma 2.4 already gives the repetition mechanism, so only the newly supplied seven-colour seed and its resulting exact triple-family resolution are claimed here. A direct reading of both complete relevant primary texts revealed no seven-colour seed for this graph or theorem for the positive odd triples of three-multiples. Independent novelty confirmation remains outstanding.

## Value — PASS

The object is the smallest previously unresolved three-dimensional odd torus under the established bounds for a natural, recently studied invariant related to rainbow edge-colouring. Its exact value closes a genuine one-colour uncertainty, and a finite explicit certificate instantly settles an infinite congruence family of the 2026 conjecture. Neither a renaming of a known formula nor an arbitrary slice is involved: the residue class is forced by the nontrivial period-three construction and graph coverings.

## Sources and boundaries

The closest primary papers are Gyárfás–Sárközy (2023), DOI `10.1007/s00373-023-02697-x`, and Jiang–Li (2026), arXiv:`2608.21774v1`. Stronger coverage by an unindexed or later result remains possible; other triples of odd cycles and higher dimensions remain open here. The covering principle itself is prior art, not an original lemma.

Self-review: passed. Independent audit: not yet performed.
