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

Analytical verification: the rearrangement argument determines both support functions; sign parity gives the finite angular cases; \(\min_i |G_i|\) follows a half-normal extreme-value limit, while \(\|G\|_2/\sqrt n\) converges to one. Moment convergence follows from exponential minimum tails and bounded inverse-chi moments.

Reproduction: run `python verify.py` using the Python standard library. The script independently enumerates signed-permutation extrema in ranks two through five, including the applicable ranks four and five, and prints stochastic scale diagnostics. Such diagnostics are not proof of an asymptotic law. No external or independent audit is represented.
