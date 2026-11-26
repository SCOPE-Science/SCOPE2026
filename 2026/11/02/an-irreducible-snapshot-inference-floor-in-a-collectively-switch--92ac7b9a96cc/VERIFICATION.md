---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the corrected claim, the stationary convolution gives X_i=ell U+independent Gaussian noise. The centered residuals are independent of (U,S_0,sample mean), so the scaled mean is the whole inference channel, U+delta Z with delta^2=D/(gamma ell^2 N). Zero total stationary flux in the stationary transport equations gives p_1=u f and p_0=(1-u) f with beta density f; stationarity is unique by contraction for a coupled switching history. Thus the risk is the integral of the smaller joint likelihood, and the posterior mean of U has derivative Var(U|Y=y)/delta^2>0 and tends to 0 and 1 at the extremes, giving a unique threshold. The full-U Bayes risk is the stated beta-integral floor; it is strictly positive, and finite noise gives both threshold-crossing errors positive conditional probabilities. For the correction, the signed difference h=(2u-1)f(u) has h'(1/2)=2f(1/2)>0. Taylor expansion of its Gaussian convolution near 1/2 gives threshold 1/2+O(delta^2). Contributions at fixed distance from 1/2 are exponentially small even for singular beta endpoints, by integrability of f. In the remaining compact neighborhood rescale u-1/2=delta z; bounded f there and Gaussian decay give the limit 4f(1/2) times the integral of z Phi(-z) over z>0, which equals 1/4. At A=B=1 symmetry fixes the threshold and the finite integral with upper limit 1/(2delta) gives (5) by integration by parts. More generally integrating the derivative of [u(1-u)]^q gives the symmetric gamma-function floor, with the stated small- and large-q expansions by the digamma values and the gamma ratio asymptotic. The numerical verifier is corroborative only; the proof establishes the limiting coefficient at fixed positive parameters.

## originality

PASS

The stationary law and standard Bayes decision machinery are prior. The closest distinct record gives a positive single-snapshot floor for a random-variance radial statistic, not the finite beta–Gaussian mean-channel risk, sharp evaluated excess-risk coefficient, or uniform-beta all-N expression. No examined source covers that corrected combination of claims by a direct specialization.

## value

PASS

The common environment limits inference even as independent thermal noise is averaged out. The exact positive floor and explicit rate and coefficient of its approach quantify the difference between learning the environment's past-weighted mean and identifying its instantaneous state. This is a natural observable of the model, useful for evaluating a snapshot-based sensor. The symmetric benchmark calibrates the result without being its primary contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
