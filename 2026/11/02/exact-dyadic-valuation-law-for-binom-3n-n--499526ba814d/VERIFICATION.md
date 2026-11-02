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

# Reproducibility

Execute `python3 verify.py` with Python 3.8 or newer and no third-party dependencies. The executable reconstructs the three-state transfer polynomials for lengths \(0\le r\le16\), enumerates the exact valuations of all \(n<2^r\), checks the three-term polynomial recurrence and the closed mean formula, and independently checks the full binary carry process for lengths through \(r=13\). Successful output ends with `VERIFY_OK`.

The code is a finite cross-check, not a proof for unbounded \(r\). The proof for every length follows from Kummer's theorem, state equivalence, exact matrix inversion, and analytic spectral perturbation as stated in `RESULT.md`. The Gaussian asymptotic has not been independently validated externally.
