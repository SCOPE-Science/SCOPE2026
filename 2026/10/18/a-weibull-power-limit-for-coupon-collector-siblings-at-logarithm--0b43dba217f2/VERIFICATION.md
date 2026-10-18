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

Run the standalone `verify.py` file using a standard Python 3 installation. It checks the finite exact rational identities for \(\mathbb E U_j^{(N)}\), the exponential-maximum moment coefficient recurrence, conditional Poisson-tail series, and the limiting power-of-exponential distribution's mean for selected \(\alpha\). Successful finite calculations support, but cannot replace, the pathwise and dominated-convergence proof in `RESULT.md`.

The critical mathematical checks in the proof are the independence of post-first-arrival Poisson processes under conditional first-arrival times, almost-sure convergence of centered exponential top spacings, the uniform Poisson lower-tail estimate when \(k/s\le\rho<1\), and the strict exponent gap allowing early ranks to be neglected. Finite testing does not certify these infinite claims. No independent external audit has been performed. The theorem does not treat boundary or supercritical index growth.
