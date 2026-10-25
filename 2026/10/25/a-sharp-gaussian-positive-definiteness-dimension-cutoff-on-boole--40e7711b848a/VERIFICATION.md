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

# Reproducibility and verification

The proof is the finite-group Fourier argument in `RESULT.md`; it relies on character orthogonality, an explicit two-term plus tail expansion, and elementary inequalities valid for the stated full parameter range. The recurrence-free computational checker `check.py` can be run with Python 3 and `mpmath` to reconstruct the unnormalized Walsh spectrum.

The checker uses exact rational arithmetic to compare direct vertex character summation against the Krawtchouk coefficient formula in dimensions one through seven for three specified rational damping bases. It also performs exact rational minimum-eigenvalue and cutoff checks near three representative dimension thresholds, and uses 70-digit arithmetic to bracket unique roots for dimensions 17, 19, 24 and 40. The stored run returned `PASS exact/numerical checks: 327`; approximate root values are printed by the checker. The code is not a universal certificate: the proof of the all-dimensional claim is the explicit, auditable inequality argument in the result.

Equality cases are proved analytically: precisely one parity Walsh eigenvalue may vanish, and every other eigenvalue is strictly larger. Outside \(0<q\le1/16\), no classification is asserted. Independent external verification is not yet performed.
