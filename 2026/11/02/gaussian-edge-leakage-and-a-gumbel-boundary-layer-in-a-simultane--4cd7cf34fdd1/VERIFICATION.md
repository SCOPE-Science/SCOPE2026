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

# Reproducible checks and proof boundaries

The standalone `verify.py` requires Python with SciPy and NumPy, and is run as `python verify.py`. It evaluates the **exact conditional-Gaussian mixture integrals**, not a Monte Carlo approximation to a population of size \(N\). For \(\beta=1/2,1,2\) it compares the finite-\(N\) values of \((\log N)^\beta\Pr(Y_N>x)\) at several fixed \(x\) with the beta–Gumbel integral; it separately compares \((\log N)^{\beta+1/2}\Pr(M_N>\sigma\sqrt{2\log N})\) with \(\Gamma(\beta+1)/\sqrt{4\pi}\). Gaussian normal tails use stable numerical evaluation, and values as large as \(N=10^{80}\) are accessed only through a one-dimensional analytic integral. The code also checks limiting moments of the Gumbel excess and an exponential-integral identity.

Execution outcome: **PASS, 94 numerical and exact-identity diagnostics**. The analytic arguments in `RESULT.md` establish every universal limit: the exact age-density transformation, Gaussian extreme-value normalization, a uniform normal-tail exponential envelope, and dominated convergence for both edge limits. A finite run cannot establish convergence for all \(N\), certify priority, or substitute for independent mathematical audit. No external solver or formal proof certificate is implied.
