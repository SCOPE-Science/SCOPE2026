# Exact maximum diversity and min-degree star threshold for intersecting 3-graphs on 9–13 vertices

## Context
For intersecting k-uniform families, diversity γ(F) = |F| − Δ(F) (edges missing the
most popular vertex) refines Erdős–Ko–Rado stability beyond edge counts, and the
minimum-degree threshold at which non-stars disappear refines degree stability.
General-n diversity theory is asymptotic or large-n (Kupavskii n ≥ C·k;
Frankl–Wang n > 36k; Pátkos order-of-magnitude), while the Frankl n ≥ 3k diversity
conjecture is false in general for large k just above 3k (Huang). The exact small
window k = 3, n = 9–13 — just above the Fano plane (n = 7) and the n = 2k
degeneracy — where stars, Hilton–Milner-type, and triangle (two-out-of-three)
families compete, had no exact diversity/min-degree table.

## Definitions
- F: intersecting 3-uniform hypergraph on [n] = {0,…,n−1} (every two edges meet).
- deg(v): edges containing v; Δ(F) = max deg; δ(F) = min deg; miss(v) = |F| − deg(v).
- Diversity γ(F) = |F| − Δ(F) = min_v miss(v).
- D(n) = max γ(F) over intersecting 3-graphs on [n].
- Star: some vertex lies in every edge (equivalently min_v miss(v) = 0).
- d(n) = max δ(F) over non-star intersecting 3-graphs on [n], so δ(F) > d(n)
  forces F to be a star.
- Triangle (two-out-of-three) family T_n with core {a,b,c}:
  T_n = {{a,b,c}} ∪ {{i,j,x} : i<j in {a,b,c}, x ∉ {a,b,c}}.

## Result
For each n ∈ {9,10,11,12,13}:

1. **Diversity:** D(n) = n − 3, attained by T_n with |T_n| = 3n − 8,
   Δ(T_n) = 2n − 5, γ(T_n) = n − 3.
2. **Min-degree star forcing:** d(n) = 3; every non-star intersecting 3-graph
   has δ(F) ≤ 3, and T_n attains δ = 3. Equivalently, δ(F) ≥ 4 forces F
   to be a star.

Uniqueness of the extremal type is NOT claimed: at n = 9 optima outside the
triangle isomorphism type exist; full extremal classification is left open.

## Proof / Evidence
Finite machine-checked exhaustive proof (stdlib-only, replayable in ≤ ~40 s
per leg), not a human-readable induction.

- **Symmetry reduction (WLOG):** for the nonempty case, relabel so {0,1,2} ∈ F
  (isomorphism-invariant properties preserved; empty family has diversity 0).
  Every other edge must meet {0,1,2}, else it is disjoint from it. Hence
  F = {{0,1,2}} plus a pairwise-intersecting subfamily of the pool P_n of
  triples meeting {0,1,2} minus {0,1,2} itself
  (|P_9| = 63, |P_10| = 84, |P_11| = 108, |P_12| = 135, |P_13| = 165).
- **Encodings:** γ(F) ≥ t ⟺ miss(v) ≥ t ∀v; non-star δ(F) ≥ 4 ⟺
  miss(v) ≥ 1 and deg(v) ≥ 4 ∀v. Branch-and-bound prover (`div_solver.py`):
  branch on pool triples with disjoint-pair propagation (including i excludes
  all pool triples disjoint from it) plus miss/degree count forcing
  (`have + open < target` prunes; equality forces) with trail undo.
- **Diversity upper bound:** solver certifies UNSAT for t = n − 2
  (no intersecting family with all miss(v) ≥ n − 2) for n = 9,…,13
  (nodes 9975/19550/35204/59331/95093; seconds-scale). Hence γ(F) ≤ n − 3.
- **Min-degree:** solver certifies UNSAT for non-star δ(F) ≥ 4 for n = 9,…,13
  (nodes 15919/68485/274505/1010124/3410894; slowest n = 13 ~36 s).
  Hence every non-star has δ(F) ≤ 3.
- **Witness arithmetic (hand-verifiable):** |T_n| = 1 + 3(n−3) = 3n − 8;
  core-vertex degree 1 + 2(n−3) = 2n − 5 (max); off-core vertex degree 3
  (edges {a,b,x},{a,c,x},{b,c,x}); so γ = (3n−8) − (2n−5) = n − 3, δ = 3;
  intersecting since any two 2-subsets of a 3-set meet; non-star.
- **Validation:** (i) SAT controls pass (diversity t = n−3 SAT; non-star
  deg ≥ 3 SAT), so solver is not vacuously UNSAT; (ii) independently written
  checker (`verify.py`, different propagation code path) re-proves all five
  diversity UNSATs (nodes 13093/26447/48753/83559/135841) and all witness
  identities; (iii) exhaustive 2^|P| brute force on n = 6 over miss/degree
  targets agrees with solver; (iv) auditor re-ran all solver legs and an
  independent fresh-DFS check of n = 9 min-degree UNSAT.

## Limitations
- Machine-checked finite case analysis for exactly k = 3, n ∈ {9,…,13};
  no analytic induction and no generalization to larger n or k.
- Extremal-type uniqueness not proved (counterexamples to uniqueness at n = 9
  acknowledged); only the values D(n), d(n) and one extremal family are proved.
- Soundness rests on code review plus differential/brute-force testing, not
  formal verification of the solver.
- The fallback full diversity-stratified census with shift logs was not
  produced (superseded by the proved exact values).

## Reproducibility
Stdlib-only Python 3:
```
python3 artifacts/verify.py            # witnesses + independent UNSAT re-proof
python3 artifacts/div_solver.py N T    # single diversity decision (N vertices, target T)
```
Non-star min-degree decision: import Solver from div_solver with
miss_targets = [1]*N, deg_targets = [4]*N; False = UNSAT (star forced).

## References
- Kupavskii, Diversity of uniform intersecting families, arXiv:1709.02829
  (large-n bound n ≥ C·k; 2k<n<3k counterexample discussion).
- Frankl–Wang, Improved bounds on the maximum diversity, arXiv:2304.11089
  (bound for n > 36k).
- Han–Kohayakawa, Maximum size of non-trivial family not in HM,
  arXiv:1509.05464 (third-level edge bound 2n−2 for k = 3).
- Frankl–Wang, Intersecting families with covering number three,
  arXiv:2207.05487 (covering-number-three edge bound).
- Pátkos, Size, diversity, minimum degree, sturdiness, dömdödöm,
  arXiv:2501.02596 (asymptotic/large-n β_{p,q} program).
- Huang, Two extremal problems on intersecting families, arXiv:1804.11269
  (Frankl n ≥ 3k conjecture false for large k; k = 3 construction gives only
  diversity 5, not covering n = 9–13).
