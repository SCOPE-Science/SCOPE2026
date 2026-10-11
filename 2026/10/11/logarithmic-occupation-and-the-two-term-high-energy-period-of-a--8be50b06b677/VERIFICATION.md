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
# Verification and limits

The Hamiltonian identity is checked algebraically at rational sample points with exact `Fraction` arithmetic in `checker.py`. The checker then solves for the negative turning point by bisection, evaluates the physical-time quadrature after a cosine endpoint substitution, and tests the additive high-energy constant at four admissible parameter pairs. The standalone command is `python3 checker.py` and prints `CHECK_OK` on passing those finite checks.

The mathematical proof, not these finite tests, establishes the limit over all real \(E\to\infty\): exact integration of \(1/\sqrt{q(x)}\), an integrable endpoint estimate for the remaining quadrature, and a signed mass-ratio argument. The computed checks do not certify publication priority, parameter-uniformity near \(k=a^2\), global period monotonicity, or the entire infinite-energy range.
