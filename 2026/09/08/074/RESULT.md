# Wilf-Number and Type Census of Numerical Semigroups of Genus 6–12

## Context
Let S ⊆ N₀ be a numerical semigroup (0 ∈ S, closed under addition, N₀∖S finite).
Genus g(S) = |N₀∖S|; multiplicity m(S) = min(S∖{0}); Frobenius number F(S) =
max(N₀∖S); conductor c(S) = F+1; embedding dimension e(S) = number of minimal
generators; left set L(S) = S ∩ [0,c), |L| = c−g; pseudo-Frobenius set
PF(S) = {x ∉ S : x + (S∖{0}) ⊆ S}, type t(S) = |PF(S)|; Wilf number
W(S) = e·|L| − c. Wilf's conjecture (1978) asserts W(S) ≥ 0 for all S.
The genus 6–12 window is where multiplicity/type diversification first appears
beyond trivial cases while remaining exhaustively certifiable, and is demanded
as replayable base cases / pruning anchors by the Wilf and Eliahou-number
programs (Bras-Amorós enumeration; Delgado–García-Sánchez type work;
Froberg–Gottlieb–Haggkvist t ≤ e−1 sufficient condition).

## Definitions
- Ap(S,m): Apéry set {w_0=0, w_1,…,w_{m−1}}, w_i = least element of S ≡ i (mod m).
- Kunz vector: ((w_1−1)/m, …, (w_{m−1}−(m−1))/m); its coordinate sum equals g.
- Ordinary semigroup of genus g: ⟨g+1,…,2g+1⟩ = {0} ∪ [g+1,∞).
- Stratum (g,m): all semigroups of genus g and multiplicity m (63 strata in range).

## Result
Complete enumeration of all 1386 numerical semigroups with 6 ≤ g ≤ 12,
per-genus counts 23, 39, 67, 118, 204, 343, 592 (agreeing with OEIS A007323).
For every semigroup the tuple (minimal generators, m, F, c, g, e, Ap(S,m),
Kunz vector, |L|, t, W) is committed in `artifacts/census.json`, each entry
recomputed from the generators by Apéry-set replay with Kunz cross-check.
Verified exact facts:
1. W ≥ 0 for all 1386 semigroups; min W = 0 in every genus g = 6,…,12
   (W=0 counts: 6, 3, 4, 5, 6, 2, 9 respectively).
2. Per genus, max type = g, uniquely attained by the ordinary semigroup
   ⟨g+1,…,2g+1⟩ (multiplicity g+1, Kunz all-ones, W=0).
3. Per (g,m) stratum (all 63): exact max-type value and exact min-Wilf value
   with named witnesses in `artifacts/extremals.json`, each optimal within its
   stratum (machine-checked). Example interior values: (10,5) min W=0 at
   [5,6]; (11,6) min W=3 at [6,7,16]; (12,12) max t=11, min W=10 at
   [12,14,…,23,25]; ordinary witnesses only on the m=g+1 diagonal.

## Proof / evidence
Computational certificate (finite case check, not a general theorem):
1. Enumeration: semigroup tree (children = parent minus one right minimal
   generator > F), BFS from N₀ to genus 12.
2. Replay: from committed minimal generators only, bounded-sieve membership +
   Apéry minima give F, c, g, Kunz, |L|=c−g; generator minimality by subset
   reachability; PF = {gaps x : x+gens ⊆ S}, t=|PF|, W=e|L|−c.
3. Independent verification (`artifacts/verify.py`, separate code path: gcd
   test, bounded-sieve membership, full recomputation): `VERIFY_OK` — all
   1386 rows replay from generators only; extremal optimality confirmed in all
   63 strata. The auditor additionally re-enumerated the tree from scratch
   (counts 0:1,1:1,2:2,3:4,4:7,5:12,6:23,…,12:592) and confirmed the census
   generator-sets equal the tree-sets per genus (0 missing/extra), and
   independently replayed all rows, global extrema, and stratum optima.

## Worked example
S = ⟨13,…,25⟩ (genus-12 global max-type witness): m=13,
Ap = [0,14,…,25], Kunz = (1,…,1) (sum 12 = g ✓), F=12, c=13, e=13, |L|=1,
PF = {1,…,12} so t=12, W = 13·1−13 = 0.

## Limitations
- Scope is genus 6–12 only; no general theorem about Wilf's conjecture proved.
- Boolean W ≥ 0 at these genera is also implied by prior verification to
  genus 100; the new contribution is the per-semigroup (F,e,t,W,Apéry,Kunz)
  table with multiplicity-stratified extremal witnesses.
- Correctness is a machine certificate conditional on exact integer/sieve
  arithmetic (mitigated by two independent code paths, full tree
  re-enumeration, and OEIS count agreement); no external CAS used or needed.

## Reproducibility
`python3 output/artifacts/verify.py` (reads `output/artifacts/census.json`
and `output/artifacts/extremals.json`, recomputes everything from generators
only) prints `VERIFY_OK: 1386 rows, all invariants replayed from generators;
W>=0 everywhere; extremals optimal in all 63 strata`.

## References
- M. Delgado, S. Eliahou, J. Fromentin, A verification of Wilf's conjecture
  up to genus 100, arXiv:2310.07742.
- M. Bras-Amorós, On the seeds and the great-grandchildren of a numerical
  semigroup, arXiv:2306.14034 (Wilf to genus 66).
- M. F. Marashdeh, An upper bound for the type of a numerical semigroup, and
  a reduction of Wilf's conjecture, arXiv:2608.12531.
- OEIS A007323, Number of numerical semigroups of genus n.
