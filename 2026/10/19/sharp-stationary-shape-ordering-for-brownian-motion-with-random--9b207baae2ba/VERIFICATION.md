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

The analytic argument uses a contractive coupling, a backward Poisson series, Gaussian conditioning, the stop-loss form of convex ordering, Jensen's inequality, the chord inequality on \([0,1]\), and the invariant-generator even-moment recurrence. The general theorem is proved mathematically, not through simulation.

Run the included `verify.py` using Python 3 with NumPy installed. It checks exact fraction arithmetic for independent operational-time and spatial moment recursions through ten nontrivial even orders, five squared-reset-factor laws (deterministic, binary, uniform, asymmetric two-point, and a deterministic/binary mixture), sharp moment inequalities, generator identities and kurtosis bounds. A seeded, 75-step, 60,000-path truncation separately compares each stationary operational-time mean against its known exact value. The checked execution reported `PASS: 172 exact and seeded numerical checks`.

The seeded test is not an infinite-horizon proof and its tolerance accounts for Monte Carlo uncertainty. No formal interval certificate is supplied for probabilistic quantities beyond the exact rational computations. The stationary density at zero and moment-generating bounds follow from the analytic convex-order proof; they are not independently certified numerically. Independent scientific audit remains unperformed.
