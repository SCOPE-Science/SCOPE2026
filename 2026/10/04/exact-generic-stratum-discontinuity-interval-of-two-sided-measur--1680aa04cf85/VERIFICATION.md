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

The proof is analytic. `verify_werner_cluster.py` supplies an independent finite-dimensional replay of the matrix identities used in the proof.

For dimensions \(2\) through \(6\), the script constructs the flip operator and product-basis dephasing directly. It verifies
\[
\|F-\Pi_U(F)\|_2^2
=
m^2-\sum_{i,j}|U_{ij}|^4
\]
for aligned, Fourier, and intermediate unitary bases.

It also constructs explicit product-state perturbations with nondegenerate marginals and checks the exact finite-\(\varepsilon\) law
\[
N_{AB}(\tau_\varepsilon)
=
\frac{b^2[m^2-S(U)]}{(1+\varepsilon)^2}.
\]

The script does not certify all dimensions by enumeration. Infinite-dimensional or exhaustive numerical certification is unnecessary because the range \([1,m]\) follows analytically from rowwise probability bounds, endpoint constructions, and connectedness of \(U(m)\).

The classification excludes paths that remain on degenerate marginal strata. No independent audit has been performed.
