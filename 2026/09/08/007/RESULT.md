# Isotopy census of order-8 Latin squares admitting a diagonal autotopism of order 7

## Context

Order-8 Latin squares are enumerated in aggregate (1,676,267 isotopy classes;
283,657 main classes; 31,833 classes with nontrivial isotopy, per McKay's census
files), but per-symmetry censuses are not published: which autotopism cycle
structures occur is known (Stones–Vojtěchovský–Wanless determine Atp(n) for
n ≤ 17 as 1-bit existence per structure; Falcón classifies cycle structures to
order 11), while how many isotopy types realize each structure is not. This
record closes the diagonal order-7 class: the sharpest prime-order window with
one fixed point plus a 7-cycle in each coordinate.

## Definitions

- Let `[8] = {0,1,2,3,4,5,6,7}` with `7 = ∞` and `σ = (0 1 2 3 4 5 6)` fixing `7`.
- Let `Θ = (σ,σ,σ)`, a diagonal autotopism of order 7 acting on `[8]^3` by `σ`
  in each coordinate.
- An isotopy is a triple `(a,b,g) ∈ S_8^3` acting by
  `L'(a(i),b(j)) = g(L(i,j))`. The autotopism group `Atp(L)` is the stabilizer
  of `L` under this action.
- Define `N_7` = number of isotopy classes `[L]` of Latin squares `L` of order 8
  such that `Atp(L)` contains an element conjugate (under the full isotopy
  group `G = S_8^3`) to `Θ`. Equivalently, the number of isotopy classes
  containing at least one Θ-invariant labelled square.
- Let `M` = number of Θ-invariant labelled Latin squares of order 8.
- Let `C_G(Θ)` be the centralizer of `Θ` in `G`.

## Result

**Theorem (computed, replayable).** `N_7 = 8`.

Supporting computed facts:

- `M = 931` Θ-invariant labelled squares: each of the 49 `(r,c)` pairs admits
  exactly 19 completions (`49 × 19 = 931`); each symbol-7 position in the
  diagonal parameter accounts for exactly 133 completions.
- The centralizer `C_G(Θ) = C_{S_8}(σ)^3` has order 343 with `K = 19` orbits on
  the invariant set, all of size exactly 49. Hence `N_7 ≤ M/49 = 19`.
- The 8 classes have sizes in `M` of `49, 294, 294, 98, 49, 49, 49, 49`
  (sum 931), intercalate numbers `28, 21, 21, 112, 7, 28, 7, 28`, and
  autotopism orders `42, 7, 7, 10752, 42, 42, 42, 42` (ordered as R0, R1, R2,
  R5, R6, R8, R12, R18 below). Each representative carries an explicit,
  substitution-verified autotopism of order 7. R5 with `|Atp| = 10752 = 64·168`
  is the `(Z_2)^3` group table; R1, R2 attain the minimum `|Atp| = 7`.
- One reduced (first row and column = identity) representative per class:

**R0** (param `r=0,c=0,s=(7,2,4,6,1,3,5)`; 28 intercalates; class size 49; |Atp|=42):
```
0 1 2 3 4 5 6 7 | 1 2 3 4 5 0 7 6 | 2 3 4 0 6 7 1 5 | 3 0 5 6 7 1 2 4
4 5 6 7 1 2 0 3 | 5 6 7 1 0 3 4 2 | 6 7 0 2 3 4 5 1 | 7 4 1 5 2 6 3 0
```
**R1** (param `(0,0,(7,2,5,1,6,4,3))`; 21 intercalates; size 294; |Atp|=7):
```
0 1 2 3 4 5 6 7 | 1 7 4 0 2 3 5 6 | 2 6 3 7 0 4 1 5 | 3 5 7 2 6 1 0 4
4 2 0 5 7 6 3 1 | 5 0 6 4 1 7 2 3 | 6 4 5 1 3 0 7 2 | 7 3 1 6 5 2 4 0
```
**R2** (param `(0,0,(7,2,6,5,3,1,4))`; 21 intercalates; size 294; |Atp|=7):
```
0 1 2 3 4 5 6 7 | 1 7 3 5 0 2 4 6 | 2 6 7 0 3 1 5 4 | 3 0 4 7 2 6 1 5
4 2 0 6 5 7 3 1 | 5 3 6 1 7 4 0 2 | 6 4 5 2 1 0 7 3 | 7 5 1 4 6 3 2 0
```
**R5** (param `(0,0,(7,3,6,1,5,4,2))`; 112 intercalates; size 98; |Atp|=10752):
```
0 1 2 3 4 5 6 7 | 1 0 5 7 6 2 4 3 | 2 5 0 4 3 1 7 6 | 3 7 4 0 2 6 5 1
4 6 3 2 0 7 1 5 | 5 2 1 6 7 0 3 4 | 6 4 7 5 1 3 0 2 | 7 3 6 1 5 4 2 0
```
**R6** (param `(0,0,(7,3,6,2,5,1,4))`; 7 intercalates; size 49; |Atp|=42):
```
0 1 2 3 4 5 6 7 | 1 2 0 4 5 6 7 3 | 2 3 4 5 0 7 1 6 | 3 4 5 6 7 1 0 2
4 0 6 7 1 2 3 5 | 5 6 7 0 2 3 4 1 | 6 7 1 2 3 0 5 4 | 7 5 3 1 6 4 2 0
```
**R8** (param `(0,0,(7,4,1,5,2,6,3))`; 28 intercalates; size 49; |Atp|=42):
```
0 1 2 3 4 5 6 7 | 1 0 3 4 5 6 7 2 | 2 3 0 5 6 7 1 4 | 3 4 5 0 7 1 2 6
4 5 6 7 0 2 3 1 | 5 6 7 1 2 0 4 3 | 6 7 1 2 3 4 0 5 | 7 2 4 6 1 3 5 0
```
**R12** (param `(0,0,(7,5,3,1,6,4,2))`; 7 intercalates; size 49; |Atp|=42):
```
0 1 2 3 4 5 6 7 | 1 2 3 4 0 6 7 5 | 2 0 4 5 6 7 1 3 | 3 4 5 6 7 0 2 1
4 5 0 7 1 2 3 6 | 5 6 7 1 2 3 0 4 | 6 7 1 0 3 4 5 2 | 7 3 6 2 5 1 4 0
```
**R18** (param `(0,0,(7,6,5,4,3,2,1))`; 28 intercalates; size 49; |Atp|=42):
```
0 1 2 3 4 5 6 7 | 1 2 3 0 5 6 7 4 | 2 3 4 5 6 7 0 1 | 3 4 0 6 7 1 2 5
4 5 6 7 1 0 3 2 | 5 0 7 1 2 3 4 6 | 6 7 1 2 0 4 5 3 | 7 6 5 4 3 2 1 0
```

Remark: since every Θ-invariant square satisfies `L(7,7) = 7`, the
"Θ fixing a prescribed symbol pointwise" subcase coincides with the whole
census (931 labelled squares, same 8 classes).

## Proof / Evidence

Proved by hand:

1. **Orbit lemma.** `⟨Θ⟩ ≅ C_7`. Since `σ` has cycle type 7+1, a triple is
   fixed iff each coordinate is 7: the unique fixed cell is `(7,7,7)`. Every
   other orbit has size 7 (7 prime). Hence `512 = 1 + 73·7`.
2. **Fixed-point forcing.** `σ(L(7,7)) = L(σ(7),σ(7)) = L(7,7)`, so `L(7,7)`
   is a fixed point of `σ`, i.e. 7. Writing `r = L(7,0)`, `c = L(0,7)` gives
   `L(7,j) = σ^j(r)`, `L(i,7) = σ^i(c)`; Latinness of row 7 and column 7
   forces `r,c ≠ 7`.
3. **Parametrization.** For `i,j ∈ {0,…,6}` put `d = (j−i) mod 7`. The 7 cells
   `{(k,k+d)}` form one Θ-orbit, so a Θ-invariant square is fixed by
   `(r,c,s)` with `s[d] = L(0,d)` via `L(k,k+d) = σ^k(s[d])`, plus the forced
   last row/column and `L(7,7) = 7`.
4. **Centralizer bound.** `σ` (7-cycle plus fixed point) has
   `C_{S_8}(σ) = ⟨σ⟩` of order 7, so `|C_G(Θ)| = 343`. It preserves the
   Θ-invariant set. Each stabilizer contains `⟨Θ⟩` (order 7), so orbit sizes
   lie in `{1,7,49}`. Each qualifying isotopy class contains a Θ-invariant
   isotope (if `φΘφ^{−1} ∈ Atp(L)` then `φ^{−1}(L)` is Θ-invariant), hence the
   whole centralizer orbit; with `m` the minimum orbit size, `N_7 ≤ M/m`.
   Computation gives all orbits size 49, so `N_7 ≤ 931/49 = 19` (hand lemma
   alone gives `N_7 ≤ 931`).

Computed (deterministic, replayable in ~16 s):

- Depth-first search over `(r,c,s)` (49 pairs, digits `s[0..6]` with row-0 and
  column-block permutation pruning plus full 14-line leaf check): 91,532 nodes,
  `M = 931`, each square rechecked Latin and Θ-invariant by substitution.
- Intercalate bucketing `{28:147, 21:588, 112:98, 7:98}`, then exhaustive
  `(a,b,g)` isotopy search with symbol-consistency pruning within buckets:
  8 classes; all 28 rep-pairs decided pairwise non-isotopic (521–3839 nodes
  each); all 923 member→rep isotopies stored as explicit `(a,b,g)` witnesses
  and re-verified by substitution.
- Autotopism re-scan per representative with explicit order-7 witnesses,
  re-verified by substitution; centralizer-orbit decomposition `K = 19 × 49`.
- Auditor replay: verbatim rerun reproduced `M=931, N_7=8, K=19, nodes=91532`;
  independent substitution audit confirmed 931/931 Latin+invariant squares,
  931/931 witnesses, 8/8 order-7 autotopisms, 8/8 reduced squares, and
  intercalate numbers; an independently written decider re-confirmed
  non-isotopy on all 5 same-intercalate hard pairs (0–8, 0–18, 1–2, 6–12,
  8–18); uniformities `49×19=931` and `7×133=931` re-derived.
- Consistency envelope: `8 ≤ 31833` (McKay nontrivial-isotopy pool).

## Limitations

- No SAT CNF/DRAT replay exists (no solver in the compute environment); the
  plan's Step 5 was replaced by stored-witness substitution checks plus a full
  autotopism re-scan. The count does not depend on SAT.
- Isotopy/non-isotopy was decided by a bespoke exhaustive `(a,b,g)`
  backtracker, not nauty canonical hashes; negative certificates are search
  node counts plus replay. Mitigated by sound forward-consistency pruning,
  runtime witness assertions, and independent re-decision of hard pairs, but no
  nauty cross-match was performed.
- McKay cross-check is the inequality `8 ≤ 31833` only; published
  representative files were not downloaded or matched.
- The number `N_7 = 8` rests on the computation above; prior literature settles
  only existence of the cycle structure, not the count.

## Reproducibility

Single stdlib-only deterministic script `output/artifacts/census.py`
(no RNG): `python3 census.py` reproduces `M=931, N_7=8, K=19` in ~16 s and
writes `census.json` containing all 931 params, per-rep data (param, class
size, intercalates, `|Atp|`, order-7 witness, reduced and Θ-invariant
squares), all 923 member→rep witnesses, all 28 rep-pair non-isotopy node
counts, and the centralizer-orbit decomposition. Every witness is asserted by
direct substitution during the run.

## References

- D. S. Stones, P. Vojtěchovský, I. M. Wanless, Cycle structure of autotopisms
  of quasigroups and Latin squares. arXiv:1509.05655 (J. Combin. Des. 20(5),
  227–263). Determines Atp(n) for n≤17 (existence per structure).
- R. M. Falcón, Cycle structures of autotopisms of the Latin squares of order
  up to 11. arXiv:0709.2973 (Ars Combin. 103, 239–256).
- B. D. McKay, Combinatorial data: Latin squares.
  https://users.cecs.anu.edu.au/~bdm/data/latin.html (order-8 totals
  1676267 isotopy / 283657 main / 31833 with nontrivial isotopy).
- R. J. Stones et al., Computing autotopism groups of partial Latin
  rectangles: a pilot study. arXiv:1910.10103 (method baseline).
