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

# Verification

Run `python3 verify.py` with Python 3 standard library. The script independently generates pairs of involutions through size seven, constructs all alternating colored components, compares counts to the exact coefficient generating function and checks 63 first, second and mixed factorial-moment identities using rational arithmetic. Its expected terminal signal is `TWO_INVOLUTION_COMPONENTS_EXACT_OK 60398 63 last_coefficient 3364/315`.

Mathematical verification also requires checking the proof of the recurrence bound \(\sqrt n\le I_n/I_{n-1}\le1+\sqrt n\), the finite-vector Poisson method of moments, and application of bounded-degree Hanf locality to the two function graphs. These infinite statements cannot be certified by a finite checker alone. The review is self-review only; independent scientific validation has not been performed.
