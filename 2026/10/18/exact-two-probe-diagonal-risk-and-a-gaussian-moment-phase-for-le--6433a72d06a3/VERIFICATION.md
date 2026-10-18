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

# Reproduction and independent-assessment limits

With Python 3 and NumPy installed, run `python verification/check_xdiag.py` from the directory containing `RESULT.md`. No network calls, private datasets, or other companion programs are required. The saved output is `verification/output.txt`.

The verifier directly evaluates leave-one-out projectors using NumPy pseudoinverses, exhaustively enumerates a range of Rademacher sign patterns with exact rational covariance calculations, compares finite diagonal-input calculations with the projected XDiag expression, verifies Gaussian exact endpoints, and checks a local \(1/s\) pole and the two-dimensional signed-tail coefficient by simulation. A successful run is reported by the program itself; the checks are a reproducibility aid, not an infinite-dimensional or exact-law proof. The stated moment thresholds and sharp constants are established analytically in `RESULT.md`.

The probe-distribution warning is material: Gaussian substitution pertains only to the literal coordinate-quotient formula; the source's supported efficient XDiag algorithm is specialized to signs. This record carries no independent audit or external certification.
