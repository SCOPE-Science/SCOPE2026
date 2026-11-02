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

The critical proof is the analytic derivation in `RESULT.md`, not the numerical sample. Specifically, it checks the strictly positive second derivative of entropy production in the single cycle-current variable, the three-factor tangent identity that characterizes conservative minima, the odd-power Taylor coefficient, and the monotone scalar limiting equation for strong driving.

The self-contained `check_triangle.py` uses the Python standard library, a fixed pseudorandom seed, and bisection for the exact scalar stationarity equation. Replayed in the same directory as this document, it printed `PASS: 5007 deterministic numerical assertions`. Checked examples include: preservation of the probability continuity equations; vanishing affinity on each of the three exceptional lines; the global sign formula across randomly chosen positive kinetic weights and velocities; the small-driving cubic coefficient; the generic strong-driving limit; and a closed-form example with equal reduced traffic rates.

The finite numerical tests do not certify the all-parameter theorem, nor establish publication priority or independent validation. The strong-driving formula requires pairwise distinct linear offsets; the sign and conservative-locus statements do not.
