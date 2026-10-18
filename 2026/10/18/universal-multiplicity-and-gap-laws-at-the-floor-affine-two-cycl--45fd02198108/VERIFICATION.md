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

# Reproducibility

Run `python3 verify.py` with Python 3.10 or newer. It requires only the standard library. The script independently evaluates the floor-affine map and its second iterate using `fractions.Fraction`, and counts primitive two-cycles as unordered integer pairs. It compares this direct count to the asserted tower-membership and uniform triangular phase-error rules at ordinary phases and at exact half-open endpoints. It then partitions the entire fundamental parameter interval into rational atoms, exactly integrates the direct cycle census, and compares each tail mass with the claimed formula. Output: `PASS 3208 exact-rational independent cycle and survival checks`, plus `PASS 16 exact-rational near-critical orbit-gap moment comparisons`.

The derivation from interval intersections, nesting, and the Lipschitz estimate for the distribution functions supplies the all-real proof. The program checks rational examples only and cannot by itself prove an identity for every real parameter. No external or independent audit has been performed.
