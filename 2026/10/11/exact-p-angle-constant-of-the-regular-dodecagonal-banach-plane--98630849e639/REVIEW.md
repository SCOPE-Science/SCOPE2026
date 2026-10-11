# Same-model review

## Correctness
PASS. For unit \(x,y\), the P-angle expression is exactly
\[
\frac{A^2+B^2-4}{2AB},
\qquad
A=N_{12}(x+y),\ B=N_{12}(x-y).
\]
The signed-facet dual representation proves the sharp weighted inequalities
\[
A+\sqrt3B\le4,
\qquad
\sqrt3A+B\le4,
\]
and triangle inequality gives \(A,B\le2\). These constraints define a six-vertex feasible polygon. The positive-definite quadratic \(A^2+B^2-(2-\sqrt3)AB\) is convex and is at most \(4\) at every vertex of that polygon, which proves the global upper bound. The explicit unit pair \(x=(1,2-\sqrt3)\), \(y=(-1,2-\sqrt3)\) attains equality. The bundled exact-arithmetic checker independently reproduces every finite facet and polygon-vertex calculation.

## Originality
PASS. Searches covered the P-angle and \(S_P\) names, regular-dodecagon and regular-polygon aliases, and exact same-invariant results. The defining Yang--Li full text was inspected around the definition, two-dimensional remark, universal bound, classical \(\ell_p\) example, and Hilbert characterization; no dodecagonal computation was found. The closest exact same-invariant public result covers real \(\ell_p\) sequence spaces only. Exact octagonal and hexagonal P-angle values concern different norms, and same-dodecagon results checked in the research corpus concern different invariants rather than this P-angle supremum.

## Value
PASS. The regular dodecagon is a canonical non-Hilbert polyhedral plane, and \(S_P\) is a Hilbert-detecting angular constant. Its exact value is therefore a natural benchmark. The proof also supplies two sharp weighted dual inequalities that expose the dodecagonal geometry and can be reused in related two-point extremal problems.

## Closest literature and limitations
Yang and Li introduced \(S_P\) in arXiv:2208.11239v1, first public on 24 August 2022, with MSC 46B20. A later exact result computes the same invariant on real \(\ell_p\) sequence spaces, but that family does not contain the regular dodecagonal norm. The theorem here does not classify all regular polygonal norms, and the literature search cannot prove absolute uniqueness. The source's earlier standing dimension convention is recorded as a notation-scope limitation; the calculation directly evaluates the displayed definition that the source itself immediately discusses in the two-dimensional Euclidean case.

Same-model review: passed. Independent audit: not yet performed.
