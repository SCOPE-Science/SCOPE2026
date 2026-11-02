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

# Reproducibility and scientific limits

The analytical proof in `RESULT.md` is the primary evidence. `verification.py` independently evaluates the two families of semiaxes and their containment inequalities for representative dimensions and parameters, numerically optimizes the two reduced constrained strictly concave problems, checks normalized contact-orbit covariance identities, and locates the unique zero of the stated cubic equation. It also probes the predicted high-dimensional constant.

Run `python verification.py` with Python 3, NumPy and SciPy. In one completed execution, 88 finite configurations passed; the maximum numerical independent-optimum-or-certificate deviation was approximately \(5.16\times10^{-6}\), and the exact rational benchmark \(\mathcal R_3(2/5)=125/42\) agreed to floating-point tolerance. The high-dimensional scaled values approached \((2e)^{-1/4}\).

The numerical optimizer's tolerance and finite-dimensional samples do not certify an infinite theorem or a historical-priority claim. Proof Parts 1–5 establish the required all-dimensional statements, and no independent external mathematical audit has been performed.
