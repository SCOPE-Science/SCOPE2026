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
The proof is symbolic and does not depend on finite enumeration.

The key graph-theoretic reconstruction is
\[
U\le W\iff N(U)\subseteq N(W).
\]
The reverse implication is witnessed by a hyperplane containing \(W\) but excluding a chosen vector of \(U\setminus W\).

For rank three, the spectral computation uses the exact projective-plane identities
\[
MM^{\mathsf T}=pI+J
\]
and
\[
BB^{\mathsf T}=pI+p(p-1)J,
\qquad
B=J-M.
\]
These split the adjacency action into the all-ones two-space and its orthogonal complement.

The packaged checker `artifacts/verify.py` reconstructs the rank-three join graph for
\[
p=2,3,5.
\]
It verifies the subgroup counts, adjacency rule, degree classes, both matrix identities, neighborhood-order reconstruction for every proper-subspace pair, the spectral annihilating polynomial, and the spectral multiplicity moment checks.

The checker returns `VERIFY_OK`.

Finite checks are not used to prove the universal automorphism theorem.
