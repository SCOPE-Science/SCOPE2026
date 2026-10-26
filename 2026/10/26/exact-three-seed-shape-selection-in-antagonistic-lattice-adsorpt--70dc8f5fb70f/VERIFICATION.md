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

# Verification and limitations

The mathematical result follows from an exact arrival-order equivalence: every exterior type-\(A\) site must be reached after its earliest adjacent designated type-\(B\) arrival. Integrating independent exponential clocks yields a finite rational sum over seed arrival orders; a separate subset dynamic program counts the same events by uniform permutations of relevant initial arrivals.

Execute `python3 verify_triads.py` in a directory containing the script. In the completed package, that command passed 171 exact assertions. It checks the rational values \(1/48\), \(2/63\), their ratio \(32/21\), the conditional shape law \(64/85\), counts of toroidal placements for several circumferences, symmetries, and unrelated three-site patterns. The code relies only on Python's standard library.

Both the correctness proof and exact computations concern the one-arrival-per-site, three-designated-type-\(B\) setting. They do not verify third-order coefficients for unrestricted repeated A/B adsorption attempts, nor any equilibrium or thermodynamic-limit assertion. Independent scholarly audit has not been performed.
