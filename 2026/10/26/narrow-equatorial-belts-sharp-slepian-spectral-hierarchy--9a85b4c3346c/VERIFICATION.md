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

# Verification and reproducibility

Run `python verification.py` with Python 3.9 or later; no external packages, datasets or network are needed. The file is included in this package. Actual execution returned:

`PASS 832 exact rational consistency checks`

The script independently inverts exact moment matrices for all \(0\le m\le8\), \(1\le k\le9\), \(0\le j<k\), verifies the Jacobi endpoint expression and monic Legendre squared norm, and checks the global least-mode coefficient and dimension count for \(0\le L\le10\). A separate high-precision numerical Gram diagonalization through \(L=6\), performed during derivation, checked 175 finite-width coefficients with maximum relative deviation 0.021199467238421 at positive widths 0.06 and 0.03. Those comparisons are not an exhaustive validation of the infinite degree range. The analytical proof in RESULT.md supplies universal correctness.

The operator and normalization are defined completely in RESULT.md. No independent scholarly validation is claimed.
