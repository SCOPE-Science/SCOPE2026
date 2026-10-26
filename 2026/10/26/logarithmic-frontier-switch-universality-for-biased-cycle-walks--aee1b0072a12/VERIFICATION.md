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

# Verification record

Reproduce the finite computations with `python verify_frontier.py`; the recorded output is `verification_output.txt`. The script uses exact `Fraction` arithmetic to compare the explicit discovery-direction transition formulas against an independent Gaussian-elimination solution of the absorbing gambler's-ruin boundary equations. For \(3\le n\le9\), four rational step probabilities were checked. For \(3\le n\le6\), three rational step probabilities were checked through an independent 400-step propagation of the *original* nearest-neighbor walk on a growing visited interval, with the probability of still being unabsorbed verified smaller than \(10^{-12}\); each final count coefficient differed from the exact answer by at most this remaining probability. Symmetric-case coefficients from an independent Bernoulli-product expansion and the elementary inequalities in the short-range coupling were also checked. The program reports 2435 checks passed.

The computer check covers finite systems and numerical inequalities at enumerated parameters only; it does not certify the asymptotic assertions, the complete continuous parameter range, or historical priority. Those are assessed by the analytic proof and the bibliographic comparisons. Independent validation has not been performed.
