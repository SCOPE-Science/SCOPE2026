# Transversal packing numbers and orthogonal-mate status of the two K3,3-free order-8 Latin squares

## Context
K3,3-free Latin squares are the value tables of universally noncommutative loops (Brouwer–Wanless 2011). Krotov–Krotov (arXiv:2304.07157 v3, accepted Discrete Math. 350 (2027), 115402) report the exhaustive-search classification: no K3,3-free Latin squares of orders 3–7, 9–11, and exactly two such squares of order 8 up to equivalence (main classes), shown in their Figure 1, plus rectangle counts and an order-16 switched construction. That paper states no transversal counts, disjoint-packing numbers, or orthogonal-mate verdicts for the two order-8 representatives. The generic transversal-free literature and surveys record no such data for this pair. This record supplies that table from the two committed arrays.

## Definitions
- Latin square of order 8: 8x8 array over symbols {0,…,7} with each symbol once per row and column.
- Transversal: set of 8 cells, one per row, one per column, with all 8 symbols distinct. Equivalently a permutation p of {0,…,7} with symbols L[r][p[r]] all distinct. T(L) = number of transversals.
- Packing number p(L): maximum number of pairwise disjoint transversals. Since each uses 8 cells of 64, p(L) <= 8; p(L)=8 iff the cells partition into 8 disjoint transversals.
- Orthogonal mate: Latin square M with all 64 ordered pairs (L[r][c],M[r][c]) distinct. Standard theorem: M exists iff L partitions into 8 disjoint transversals (mate symbol classes are the transversals).
- K3,3-free: the Latin-square graph has no induced K3,3; tested here by Proposition 1 of Krotov–Krotov: for all ordered distinct row triples and column triples, the equalities L[r1][c2]==L[r2][c1], L[r2][c3]==L[r3][c2], L[r3][c1]==L[r1][c3] never jointly hold.

## Committed representatives
Symbols {0,…,7}, rows/columns 0..7. K1 = Figure-1 left square, K2 = Figure-1 right square (differ only in the 2x4 blocks at rows 1–2):

K1:
```
1 0 7 2 4 3 6 5
0 1 2 7 3 4 5 6
2 3 0 5 1 6 7 4
3 2 5 0 6 1 4 7
4 5 3 6 0 7 1 2
5 4 6 3 7 0 2 1
7 6 4 1 5 2 0 3
6 7 1 4 2 5 3 0
```
K2:
```
1 0 2 7 4 3 6 5
0 1 7 2 3 4 5 6
2 3 0 5 6 1 7 4
3 2 5 0 1 6 4 7
4 5 3 6 0 7 2 1
5 4 6 3 7 0 1 2
6 7 4 1 5 2 0 3
7 6 1 4 2 5 3 0
```

## Result
For the committed arrays:
- K1 has exactly T1 = 64 transversals; packing number p1 = 8; it has an orthogonal mate.
- K2 has exactly T2 = 192 transversals; packing number p2 = 8; it has an orthogonal mate.

Hence K3,3-freeness (universal noncommutativity) does NOT force orthogonality failure at order 8: both class members admit orthogonal mates, while their transversal counts separate them (64 vs 192).

Explicit 8-way disjoint-transversal partitions (cell index v = 8r+c):
- K1: [0,10,22,28,33,45,55,59], [1,11,23,29,34,46,52,56], [2,8,20,30,39,43,49,61], [3,9,21,31,36,40,50,62], [4,14,18,24,35,47,53,57], [5,15,19,25,32,44,54,58], [6,12,16,26,37,41,51,63], [7,13,17,27,38,42,48,60].
- K2: [0,10,20,27,38,41,55,61], [1,11,21,31,32,42,52,62], [2,13,22,28,33,43,48,63], [3,9,23,29,34,40,54,60], [4,14,18,24,37,47,51,57], [5,15,16,26,36,46,49,59], [6,12,19,25,39,45,50,56], [7,8,17,30,35,44,53,58].

Explicit mates (symbol = partition-class index):
Mate of K1:
```
0 1 2 3 4 5 6 7
2 3 0 1 6 7 4 5
6 7 4 5 2 3 0 1
4 5 6 7 0 1 2 3
5 0 1 4 3 6 7 2
3 6 7 2 5 0 1 4
7 2 3 6 1 4 5 0
1 4 5 0 7 2 3 6
```
Mate of K2:
```
0 1 2 3 4 5 6 7
7 3 0 1 6 2 4 5
5 7 4 6 0 1 2 3
4 6 5 0 2 3 7 1
1 2 3 7 5 4 0 6
3 0 1 2 7 6 5 4
2 5 6 4 1 7 3 0
6 4 7 5 3 0 1 2
```

## Proof / evidence
Deterministic exhaustive computation, stdlib only, replayed by the auditor:
1. Latin check: every row/column is a permutation of 0..7 — passes for both.
2. K3,3-freeness: ordered-pattern test gives 0 hits for both; re-check with distinct-letter (induced-subgraph) filter also gives 0 hits.
3. Transversal counts: brute force over all 8! = 40320 column permutations; permutation p is a transversal iff the 8 symbols L[r][p[r]] are distinct. Yields 64 (K1), 192 (K2); reproduced by independent recount.
4. Packing/mates: each listed 8-set verified to contain all rows, columns, symbols (hence a transversal); the eight sets partition all 64 cells; hence p = 8 (attains the absolute upper bound, so no UNSAT log needed). Mate square M[r][c] = class index verified Latin with all 64 ordered pairs distinct, hence orthogonal; each mate-symbol class verified a transversal, closing the mate-iff-partition equivalence.

## Limitations
- Arrays reconstructed from Krotov–Krotov Figure 1, not the authors' machine files; all array-conditional claims computationally verified on the committed arrays.
- Class-completeness statement (exactly two members; unique nonempty case in orders 3–11) is relied upon from Brouwer–Wanless / Krotov–Krotov, not re-proved.
- Isotopy-canonicity of the K1/K2 labels not re-derived.
- No claims beyond order 8; order-16 generalization untouched.

## Reproducibility
Artifacts: `artifacts/squares.json` (committed K1, K2 arrays), `artifacts/verify_all.py` (stdlib-only checker). Run `python3 verify_all.py` inside `artifacts/`; expected output: latin OK, K3,3 hits 0, counts 64/192, both 8-way partitions verified, both mates verified, ALL CHECKS PASSED.

## References
- A. D. Krotov, D. S. Krotov, Do K3,3-free Latin squares exist? arXiv:2304.07157 v3 (Discrete Math. 350 (2027) 115402).
- N. J. Cavenagh, I. M. Wanless, Latin squares with no transversals, arXiv:1609.03001.
- B. A. Kazemi, B. Pahlavsay, Quasi-transversal in Latin Squares, arXiv:1808.05213 (mate iff partition; Brualdi–Stein–Ryser direction).
- I. M. Wanless, Transversals in Latin Squares, arXiv:0903.5142; R. Montgomery, Transversals in Latin Squares, arXiv:2406.19873 (survey gap).
