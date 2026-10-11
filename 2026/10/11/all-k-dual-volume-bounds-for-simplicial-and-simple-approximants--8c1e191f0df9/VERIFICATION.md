---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The all-dimensional proof has two inputs.

First, the classical Lower Bound Theorem for a simplicial \(d\)-polytope with \(v\) vertices states that its \(j\)-face count is at least that of a stacked polytope with \(v\) vertices. The explicit formulas are
\[
\phi_{d,j}(v)
=
\binom d j v-j\binom{d+1}{j+1}
\]
for \(1\le j\le d-2\), and
\[
\phi_{d,d-1}(v)
=
(d-1)v-(d+1)(d-2).
\]
Solving \(\phi_{d,j}(v)\le M\) for \(v\) gives exactly \(v\le\Lambda_{d,j}(M)\).

Second, the full lead-source text was checked at Theorem 3.7 in the vertex case and Theorem 3.8 in the facet case. Those inequalities have the complexity dependence
\[
N^{-2/(d-1)},
\]
inside an increasing minimum, so their right-hand sides decrease as the allowed endpoint count \(N\) increases.

For an inscribed simplicial polytope, substitute
\[
f_0(P)\le\Lambda_{d,k}(M).
\]
For a circumscribed simple polytope, polarity gives
\[
f_{d-1}(Q)=f_0(Q^\circ),
\qquad
f_k(Q)=f_{d-1-k}(Q^\circ),
\]
so the same combinatorial inversion gives
\[
f_{d-1}(Q)\le\Lambda_{d,d-1-k}(M).
\]
The endpoint source theorems then give the claimed bounds.

The bundled checker verifies the stacked face formulas and their exact inverses for all \(2\le d\le40\), all face dimensions, and multiple vertex counts, and verifies the polarity index map. These finite checks are supplementary and do not certify the classical Lower Bound Theorem itself.

No claim is made for arbitrary nonsimplicial or nonsimple polytopes in the missing face-dimension ranges.
