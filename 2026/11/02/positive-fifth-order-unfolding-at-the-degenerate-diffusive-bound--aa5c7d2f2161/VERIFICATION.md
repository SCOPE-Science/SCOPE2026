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

# Reproducibility and limits

Run `python3 verify_quintic.py` (Python 3 standard library, no external dependencies). This constructs the boundary Fourier series through fourth order and the resonant fifth-order coefficient via integer-only outward intervals, verifies exact enclosures for \(\sqrt2\) and \(\sqrt6\), recovers the published critical second-order coefficient, and certifies
\[
 0.70584603791928416421<K<0.70584603791928416422.
\]
The expected output is in `verification_output.txt`; the final line is `EXACT_OUTWARD_INTERVAL_QUINTIC_SIGN_PASS`.

The source's smooth local Hopf branch is a separate analytical theorem, not a computational claim. The checker establishes the algebraic coefficient and its strict sign conditional on the rigorously established branch. It does not establish orbital stability at the cubic degeneracy or an exhaustive historical-priority result.
