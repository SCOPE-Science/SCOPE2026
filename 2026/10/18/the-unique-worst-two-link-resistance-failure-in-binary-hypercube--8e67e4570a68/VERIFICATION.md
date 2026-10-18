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

Run `python3 verify.py` with a Python 3 interpreter; no external packages are needed.

The exact-rational program checks: (i) binomial-integral formulas for the four edge-pair correlations and the two rational exceptional-dimension gaps; (ii) strictly positive orientation inequalities at dimensions 3 through 11; (iii) all \(\binom{d2^{d-1}}2\) distinct edge pairs for \(d=3,4,5\) by independent Walsh sums; (iv) exact maximizing-pair counts; and (v) direct dense inverses of the connected deleted graphs for \(d=3,4\). The check completed with `VERIFY_OK 7503 exact rational Fourier, rank-two, all-pair and direct-inverse identities`.

The all-dimensional conclusion instead relies on the paper's integral comparisons and the rank-two inverse identity. Numerical tests and finite enumeration alone cannot certify that conclusion. Independent mathematical audit has not been performed.
