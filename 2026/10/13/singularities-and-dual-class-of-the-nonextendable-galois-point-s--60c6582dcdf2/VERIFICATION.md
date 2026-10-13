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

# Verification information

The companion `septic_check.py` runs with Python 3 standard-library `fractions` and `itertools` only. It uses exact arithmetic in \(\mathbb Q[\zeta_5]/(\zeta_5^4+\zeta_5^3+\zeta_5^2+\zeta_5+1)\), with no floating-point approximation. The finite checks reconstruct the four coincidence cubics, check each leading coefficient nonzero, confirm each discriminant norm is \(674041\), and confirm each of the six distinct pairs has resultant norm \(2000\). Denominator exceptions, the implicit equation and its degree-two tangent cone at the Galois point, tangent cross-products, genus and dual-class computations are also checked.

Command: `python3 septic_check.py`

Observed result:

`VERIFY_OK degree=7 nodes=13 cusp=A4 dual_degree=11 discriminant_norms=4x674041 pair_resultant_norms=6x2000`

The analytic classification at the parameter \(t=0\), at \(t=\pm i\), and at \(t=\infty\) is proved in `RESULT.md`; the checker alone is not an external or infinite certification. This calculation does not establish any general classification beyond the explicit curve. No independent audit was performed.
