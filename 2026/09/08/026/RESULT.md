# Simple rank-3 matroids on 8 elements: census, maximal T(2,0), and Fano window certificate

## Context and motivation

Simple rank-3 matroids on 8 points form the standard small-order catalogue
window (Blackburn-Crapo-Higgs; Mayhew-Royle catalogue to 9 elements).
The Tutte polynomial $T_M(x,y)$ is the universal deletion-contraction
invariant; its evaluation $T_M(2,0)$ is a classical specialization in the
acyclic-orientation / region-counting family. Recognized background questions
are Tutte-polynomial distinguishing power, the Rota / Geelen-Gerards-Whittle
excluded-minor program, and small-field representability (Fano vs non-Fano
phenomena). No published source gives a window-complete $T(2,0)$ table or
maximality gap over this window.

## Definitions

- Ground set $E=[8]=\\{0,\\dots,7\\}$.
- A simple rank-3 matroid on $E$ is encoded by its family $F$ of nontrivial
  lines (subsets of size $\\ge 3$, pairwise meeting in at most one point),
  excluding $F=\\{[8]\\}$ (rank 2). Triples inside a line are dependent;
  all other triples are bases. Rank: $r(S)=|S|$ for $|S|\\le 2$,
  $r(S)=2$ if $S$ lies in a line, else $\\min(|S|,3)$.
- Tutte polynomial by deletion-contraction; evaluation at $(2,0)$.
- $U(3,8)$: uniform matroid (empty line family, all $\\binom{8}{3}=56$
  triples are bases).
- Fano matroid $F_7$: 7-point rank-3 matroid whose 7 triple-lines cover each
  of the $\\binom{7}{2}=21$ pairs exactly once (projective plane of order 2).

## Result

(a) Census: there are exactly **68** isomorphism types of simple rank-3
matroids on 8 elements, accounting for **433,038** labeled line families
(433,039 families including the single rank-2 family $F=\\{[8]\\}$).

(b) Maximality with gap: over all 68 types, $T_M(2,0)$ is uniquely maximized
by the uniform matroid $U(3,8)$ with $T_{U(3,8)}(2,0)=\\mathbf{58}$.
The runner-up (single 3-point line) has $T=\\mathbf{56}$. Hence with
$G:=58-56=2\\ge 1$,
$T_W(2,0)-T_M(2,0)\\ge 2>0$ for every non-uniform simple rank-3 $M$ on 8
points. Distinct values:
$\\{58,56,54,52,50,48,46,44,42,40,38,36,28\\}$.
Maximizer Tutte polynomial:
$T_{U(3,8)}(x,y)=x^3+5x^2+15x+(y^5+3y^4+6y^3+10y^2+15y)$,
so $T(2,0)=8+20+30=58$.

(c) Window representability separation: census type 66 with lines
$\\{1,2,5\\},\\{0,3,5\\},\\{0,2,6\\},\\{1,3,6\\},\\{0,1,7\\},\\{2,3,7\\},\\{5,6,7\\}$
(point 4 on no line) deletes to $M\\setminus 4 \\cong F_7$ on
$\\{0,1,2,3,5,6,7\\}$ (7 triple-lines covering 21 distinct pairs; explicit
isomorphism certified). $F_7$ is representable over GF(2) (e.g.
0:001, 1:010, 2:100, 3:111, 5:110, 6:101, 7:011, under which exactly the
7 lines are dependent) and is an excluded minor for characteristic $\\ne 2$
representability, so type 66 is not GF(3)-representable (indeed not
representable over any field of characteristic $\\ne 2$).

## Proof / evidence

Computer-assisted exhaustion with two independent paths (stdlib Python only):

1. Enumeration: pair-branching DFS over the 219 candidate lines
(subsets of size $\\ge 3$); branch on first uncovered pair (leave uncovered
or choose a covering line; conflicts exclude pair-sharing lines). Leaves are
exactly valid families: 433,039 including $F=\\{[8]\\}$; 433,038 simple
rank-3. Isomorphism reduction under $S_8$ by invariant bucketing (sorted
line sizes, point degrees, per-line degree profiles, per-point incidence
multisets: 68 buckets) plus collinearity-preserving backtracking within
buckets: 68 buckets = 68 types, labeled counts summing to 433,038 with every
count dividing $8!=40320$. Log: `enum_log.txt`
(`leaves=433039 rank2skip=1 labeled=433038 buckets=68 types=68 time=34.5s`).
Reran independently: identical counters.
2. Tutte: per-type memoized deletion-contraction on
(remaining-set, contracted-set) states ($\\le 209$ states/type), full
polynomials in `tutte_table.json`; sorted $T(2,0)$ table in
`tutte_t20_table.csv`; replay traces `replay_W.json`/`replay_runnerup.json`.
3. Cross-checks: independent subset-sum $T(2,0)=\\sum_{A\\subseteq E}(-1)^{|A|-r(A)}$
agrees on all 68 types; independent rank-generating subset expansion of full
polys agrees on all 68 types; identities $T(1,1)=\\#\\text{bases}$ and
$T(2,2)=2^8=256$ hold per type; rank axioms (R1 + full $A,B$ submodularity
over $2^8$ subsets) verified for all 68 types; 68 invariant keys distinct and
exhaustive $S_8$ collinearity check confirms pairwise non-isomorphic within
each group. Fresh-path `verifier.py` reports `ALL CHECKS PASSED`.

No general monotonicity theorem is claimed (only the verified inequality).

## Limitations

- Maximality proof is computer-assisted exhaustion, not a human closed form.
- Isomorphism reduction uses bespoke invariant+backtracking, not an external
  canonical-labeling library; validated by labeled-sum, orbit-stabilizer, and
  exhaustive $S_8$ cross-check.
- The Fano certificate is window-level (type 66), not on the uniform
  maximizer $U(3,8)$ (representable over every field, so it admits no such
  minor). The admitted target's ``W (or a co-maximizer)'' phrasing is thus
  only partially met literally (unique maximizer, no co-maximizers); the
  separation delivered is: maximal-$T(2,0)$ forces representability while the
  window contains certified nonrepresentable members.
- Fano characteristic-$\\ne 2$ nonrepresentability invokes the classical
  $F_7$ excluded-minor theorem (Oxley), not reproved here.
- Originality rests on pre-registered admission triage plus failed-search
  evidence, not on a proof of nonexistence of obscure tables.

## Reproducibility

Stdlib only. From the lane root (artifacts in `output/artifacts/`):
`python3 enumerate_types.py && python3 tutte_compute.py && python3 crosscheck.py && python3 theorem_checks.py && python3 verifier.py`
(enumeration ~35 s, rest seconds). Do not name the enumerator `enum.py`
(shadows stdlib `enum`).

## References

- D. Mayhew, G. F. Royle, Matroids with nine elements, arXiv:math/0702316.
  Catalogue to 9 elements (counts/database); no $T(2,0)$ extremal.
- C. Merino, M. Ramirez-Ibanez, G. Rodriguez-Sanchez, The Tutte polynomial
  of some matroids, arXiv:1203.0090. Family formulas survey; no
  window-complete extremal census.
- M. Bamiloshin, O. Farras, C. Padro, A Note on Extension Properties and
  Representations of Matroids, arXiv:2306.15085. Extension-property checks
  on 8-9 element matroids; no $T(2,0)$ census or gap.
- G. Brettell, The excluded minors for GF(5)-representable matroids on ten
  elements, arXiv:2307.14614. Excluded-minor method baseline; no Tutte
  extremal in this window.
- J. Oxley, Matroid Theory (Fano excluded-minor / characteristic-2
  representability facts).
