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

The primary proof is analytic and covers every positive weighted finite metric star. The standalone Python file `check_fm_star.py` uses only the standard library. Run `python check_fm_star.py` from the directory containing the file.

The program independently enumerates extreme points as feasible intersections of linearly independent active inequalities and compares them to the claimed complete fiber-anchor classification. It also checks the facet witnesses and count formula. Signed measures are evaluated by three independent exact-rational methods: exhaustive extreme-point support, the proposed finite-breakpoint formula, and the sorted slope-sweep formula.

The observed run printed `PASSED 897 exact-rational assertions`, with exhaustive active-set enumeration in dimensions three through five and supplemental count tests through nine leaves. All displayed numeric checks use exact fractions; the analytic proof, not the finite checks, establishes the infinite family statement. Independent audit has not been performed.
