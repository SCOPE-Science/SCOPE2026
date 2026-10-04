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
The proof is self-contained modulo three standard published inputs: the toric convex-body formula for the greatest lower Ricci invariant, its extension to singular toric log Fano varieties, and the weighted-projective fan relation. The derivation specializes these inputs explicitly rather than assuming a precomputed weighted-projective formula.

The bundled `verify.py` performs exact integer-residue Reid--Tai tests for \(2\le r\le40\) over a box containing and extending beyond the proposed canonical region. For every tested pair it compares the direct age test with \(d\le r\) and \(a\le r+d\). It then verifies the closed count \(3r(r+1)/2\), the unique extrema of \(R=(r+2)/(r+a+b)\), and the survival-function breakpoint identities. A separate finite Riemann-sum check confirms convergence of empirical means toward \(\log(3)/3\).

The finite computation is not an exhaustive proof for all \(r\). The infinite claims rest on the explicit age inequalities, the simplex barycentric calculation, and standard Riemann-sum convergence given in `RESULT.md`.