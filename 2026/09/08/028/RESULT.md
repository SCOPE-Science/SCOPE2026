# Transversal packing spectrum over the complete 22-type isotopy classification of Latin squares of order 6

## Context

The maximum number of pairwise disjoint transversals in a Latin square is a
recognized open problem (Kazemi–Pahlavsay: "most famous open problem involving
Combinatorics"). Order 6 is its classical closed boundary: Euler conjectured
and Tarry proved that no pair of orthogonal Latin squares of order 6 exists,
so every order-6 packing number satisfies p < 6, with unknown distribution.
The complete isotopy classification of order-6 Latin squares has exactly 22
types (McKay; OEIS A040082: 1,1,1,2,2,22,564,...). Hall–Paige theory predicts
that group-based (Cayley-table) types have no transversals, leaving the
nongroup spectrum open. No prior source publishes per-type transversal counts
or disjoint-packing numbers over all 22 types.

## Definitions

- Fix the 22 McKay isotopy representatives in file order of
  `latin_is6.txt` (https://users.cecs.anu.edu.au/~bdm/data/latin.html),
  each a 36-character row-major string over symbols {0,...,5}, numbered
  Type 1–22 in file order. Matrices are embedded in the verifier.
- A **transversal** is a set of 6 cells meeting every row, every column, and
  every symbol exactly once (equivalently a column-permutation
  c(0..5) with distinct symbols L[i][c(i)]).
- **T_i** = number of transversals of Type i.
- **p_i** = transversal packing number of Type i: maximum cardinality of a
  family of pairwise cell-disjoint transversals (cells disjoint).
- **p_max** = max_i p_i; **extremal types** = {i : p_i = p_max}.
- **Group-based** means isotopic (row/column/symbol permutations) to a group
  Cayley table. Up to isomorphism the only groups of order 6 are Z_6 and S_3.

## Result

For the 22 types in McKay file order:

| Type | T | p | Type | T | p |
|---|---|---|---|---|---|
| 1 | 32 | 4 | 12 | 24 | 4 |
| 2 | 0 | 0 | 13 | 8 | 2 |
| 3 | 8 | 4 | 14 | 8 | 4 |
| 4 | 0 | 0 | 15 | 8 | 4 |
| 5 | 0 | 0 | 16 | 8 | 2 |
| 6 | 24 | 4 | 17 | 0 | 0 |
| 7 | 24 | 4 | 18 | 0 | 0 |
| 8 | 8 | 2 | 19 | 0 | 0 |
| 9 | 0 | 0 | 20 | 0 | 0 |
| 10 | 8 | 2 | 21 | 8 | 4 |
| 11 | 0 | 0 | 22 | 0 | 0 |

Hence **p_max = 4**, attained exactly on the eight extremal types
**{1, 3, 6, 7, 12, 14, 15, 21}**; all p < 6 (consistent with Euler/Tarry).
Distributions: T in {0: 10 types, 8: 8 types, 24: 3 types, 32: 1 type};
p in {0: 10 types, 2: 4 types, 4: 8 types}.

Hall–Paige stratification: exactly Types 2 (isotopic to Z_6) and 4
(isotopic to S_3) are group-based, both with T = p = 0; the other 20 types
are nongroup.

Representative attaining families (row i → column; full pairs for p=2 types
in witnesses.json):

- Type 1: [0,2,3,4,5,1], [1,3,2,5,4,0], [2,0,4,3,1,5], [3,1,5,2,0,4]
- Type 3: [2,4,1,5,0,3], [3,2,0,1,5,4], [4,5,3,2,1,0], [5,3,4,0,2,1]
- Type 6: [0,2,1,4,5,3], [1,3,5,0,4,2], [2,0,4,3,1,5], [5,4,0,2,3,1]
- Type 7: [0,2,3,1,4,5], [1,4,2,5,3,0], [2,1,4,0,5,3], [4,0,5,3,2,1]
- Type 12: [0,2,3,1,5,4], [1,4,5,0,2,3], [4,1,0,2,3,5], [5,0,1,3,4,2]
- Type 14: [0,2,3,1,4,5], [1,5,4,0,2,3], [4,0,1,3,5,2], [5,1,0,2,3,4]
- Type 15: [1,2,0,5,3,4], [2,5,1,0,4,3], [3,1,5,4,2,0], [5,3,4,1,0,2]
- Type 21: [0,5,1,4,2,3], [1,4,0,3,5,2], [4,1,2,0,3,5], [5,0,3,2,1,4]

Isotopy witnesses: Type 2 ≅ Z_6 via r = c = [0,3,5,1,2,4],
s = [0,3,4,1,5,2]; Type 4 ≅ S_3 via r = c = s = [0,3,4,1,2,5].

## Proof / evidence

Finite exhaustive computation with deterministic replay (stdlib Python,
seconds-scale), i.e. proof by enumeration:

1. Scope fixed first: the 22 matrices above; no seeding. Live
   `latin_is6.txt` re-fetched 2026-09-08 matches the embedded strings
   line-for-line; all 22 are valid Latin squares.
2. Transversal enumeration: scan of all 720 column-permutations per square
   with symbol-distinctness check (triple-checked during research by
   backtracking and vectorized paths; verifier uses a fresh loop order).
   Reproduces the T-vector exactly.
3. Packing optimality: branch-and-bound max set-packing over found
   transversals plus independent exhaustive C(T,p+1) scan proving no
   (p+1) pairwise-disjoint family exists. Worst cases: C(32,5)=201376
   (Type 1), C(24,5)=42504 (Types 6,7,12), 56 elsewhere, trivial at T=0.
   Every stored witness family is verified to consist of p transversals
   from the enumerated list that are pairwise cell-disjoint.
4. Stratification: exhaustive isotopy search (720 row-perms × 720
   column-perms, symbol map forced by first row) against Z_6 and S_3
   Cayley tables. Only hits: Type 2 ≅ Z_6, Type 4 ≅ S_3 (witnesses above,
   checked cell-by-cell). Both have T = p = 0, as Hall–Paige predicts
   (Sylow 2-subgroups cyclic/nontrivial). Independent auditor re-ran the
   full scan: 20 nongroup types confirmed.
5. Independent verifier `artifacts/verify.py` (stdlib only) replays all of
   the above from matrices alone and prints `ALL VERIFY PASS`.

## Limitations

- Type numbering is McKay `latin_is6.txt` file order, not a canonical
  invariant ordering; replay must use the same file (embedded in scripts)
  or re-index.
- Group-based labels are computational isotopy readings with stored
  witnesses, not structural derivations.
- Optimality certificates are exhaustive brute-force scans; there is no
  closed-form theorem for the spectrum.
- No claim beyond order 6 or beyond these representatives. Orthogonal-mate
  existence (all-negative by Tarry) and near-transversal certificates
  (Best et al. to order 11) are conceded, not claimed.
- Timings are machine-local and not part of the claim.

## Reproducibility

- `artifacts/table.json`: (T_i, p_i) vectors, pmax, extremal set, labels.
- `artifacts/witnesses.json`: per-type T, p, witness column-perms,
  combos_checked.
- `artifacts/verify.py`: stdlib-only replay; run `python3 verify.py`.
  Expected: per-type `T=.. p=.. witness+optimality OK` lines 1–22 plus
  `group-label spot checks OK; pmax=4; ALL VERIFY PASS`.

## References

- McKay combinatorial data + latin_is6.txt:
  https://users.cecs.anu.edu.au/~bdm/data/latin.html ;
  https://users.cecs.anu.edu.au/~bdm/data/latin_is6.txt
- OEIS A040082 (isotopy classes): https://oeis.org/A040082
- Best–Pula–Wanless, Small Latin arrays have a near transversal:
  https://arxiv.org/abs/1911.05936
- Montgomery, Transversals in Latin Squares (survey):
  https://arxiv.org/abs/2406.19873
- Wanless, Transversals in Latin Squares: https://arxiv.org/abs/0903.5142
- Kazemi–Pahlavsay, Quasi-transversal in Latin Squares:
  https://arxiv.org/abs/1808.05213
- Cavenagh–Wanless, Latin squares with no transversals:
  https://arxiv.org/abs/1609.03001
- Potapov, On the number of transversals: https://arxiv.org/abs/1506.01577
