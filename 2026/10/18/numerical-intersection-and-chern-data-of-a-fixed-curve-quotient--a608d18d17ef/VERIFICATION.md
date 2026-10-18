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

# Reproducibility and checked limits

The standalone script `verify_fixed_fermats.py` uses Python's standard library only. Running `python verify_fixed_fermats.py` checks Vandermonde maximal-minor products and projected-rank formulas for sample full-spark matrices for dimensions \(3\le t\le8\), Chern-coefficient computations and involution quotient Euler characteristics, and the specific \(t=4\) fixed genus-17 curve, cubics, Chern pairings, and Hodge arithmetic. Its final message includes:

`VERIFY_OK CY3 Hodge=(2,58) cubic=(8,0,-32,-128) c2=(56,64) pi1=needs_proof`

The message notes that no finite test proves the fundamental-group assertion, which is established by the fixed-point quotient argument in RESULT.md. Similarly, Vandermonde tests provide examples, not a proof for all full-spark coefficient matrices; the latter is proved symbolically from rank and the geometrically forced local normal action.

The exact cubic identities use the degree-two finite map \(q:\widehat Y\to Z\), \(q^*D=\beta^*H\), and \(q^*E=2\widehat E\); they are not inferred from numerical enumeration. The Euler characteristic is derived from Chern classes and the finite quotient's fixed-point formula. The divisor \(D\) is nef and big but is not asserted to be ample on the resolution. The rational divisor-space spanning statement does not certify an integral lattice basis. Historical originality has no computational proof; literature comparisons and residual uncertainty are documented in AUDIT.json.
