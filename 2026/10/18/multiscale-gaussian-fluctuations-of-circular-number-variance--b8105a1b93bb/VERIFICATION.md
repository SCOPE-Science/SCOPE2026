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

# Verification details

Run `python verify.py` with a standard Python interpreter from the directory containing the verification file. On the reviewed package this printed `PASS: 770 finite identities and consistency checks`. The checks cover 450 pair-sum versus direct-count integrations for point configurations of sizes 1–10, 120 comparisons between the finite Fourier spectral series and the exact covariance polynomial, 100 evaluations of the mesoscopic covariance identity, and 100 of the limiting increment identity. The Fourier series is truncated at 4,000 terms; the checked numerical comparison threshold is \(10^{-9}\). A fixed pseudorandom seed makes the examples reproducible.

These finite checks do not prove the equalities for all configurations or the central limit theorem. The complete proof is in RESULT.md: canonical U-statistic decomposition; Parseval and Bernoulli polynomial; common Brownian-bridge spectral representation and Lyapunov theorem; fourth-moment tightness; and a KMT coupling error that is uniform in the window-length parameter.

Scientific limits: the coupling condition \(\delta_N\sqrt N/\log N\to\infty\) is sufficient; no optimality for that lower scale or claim beyond fixed compact index intervals is established. No independent audit or validation has been performed.
