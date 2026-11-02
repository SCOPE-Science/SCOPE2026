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

# Reproduction of finite pivotalities

Run `python3 check_heterogeneous_proxy.py`. It requires only Python 3 standard libraries and does not access external data. Its `exact_formula` computes Poisson-binomial mass functions by rational convolution. Its `exhaustive_formula` separately enumerates choices to delegate, directly vote NO or directly vote YES for all other agents, using exact rational probabilities and conditioning on a fixed root ballot for leaf counterfactuals.

Observed output: `PASS: 120 arbitrary-heterogeneous exact profiles and 540 pivotality values`. These tests include 1–6 delegators, probabilities zero and one, mixed unequal propensities, parity changes and strict-majority ties. Both sides of each comparison are exact rational numbers.

As an additional, noncertifying numerical check, independent two-binomial convolution simulations used half-zero/half-positive delegation arrays at sizes \(m\in\{1000,4000,16000\}\) and \(\Delta_m\in\{-3,0,3\}\). At \(\Delta_m=0\), the observed normalized powers were approximately \(0.58218,0.56922,0.56277\), approaching the analytic limit \((1+\sqrt{2/\pi})^{-1}\approx0.55621\). These simulations are not part of the mathematical proof.

The proof in `RESULT.md` is analytic and applies to all probability arrays, not merely checked inputs. The local moderate-deviation lemma is justified there using exponential tilting, bounded cumulants and Fourier inversion; its possible asymptotic modeling limits are listed in `RESULT.md`. No independent external validation or audit is asserted.
