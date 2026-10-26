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

## Checks performed

- Reconstructed the birth–death scale-product formula and the hitting-probability solution \(h(n)=S_n/S_0\).
- Verified the asymptotic expansions through the \(o(1/(n\log n))\) conditioned-drift term using the stated \(o(1/(n(\log n)^2))\) hypothesis.
- Derived the conditioned-chain weight asymptotic \(\pi_n=n^{-1}\exp(o(\log\log n))\) and the divergent lower bound \(\pi_n\ge c/[n(\log n)^{1/2}]\) for sufficiently large \(n\).
- Used the first-step recurrence and nonnegative increments of the expected hitting-time profile to prove that the conditional mean cannot be finite.
- Ran `verification/check_birth_death_boundary.py`. It checks exact rational identities for the stated example over indices \(2\) through \(1000\); it does not certify the infinite argument.
- The result is limited to \(\beta=1\), nearest-neighbour transitions, the stated boundary behavior, and the log-squared drift error. The weaker error condition and general bounded-jump case remain open here.

Independent audit and independent validation have not been performed.
