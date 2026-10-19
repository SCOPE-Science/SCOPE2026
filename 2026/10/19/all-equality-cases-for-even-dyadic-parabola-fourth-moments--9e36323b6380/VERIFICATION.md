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

The Fourier-to-incidence normalization, exact valuation formula for all differences, parent/daughter mass equality conditions, and subgroup-generator Cauchy equality are proved in RESULT.md. The equality-condition proof applies to all positive integers \(k\), not only the tested examples.

Run `python3 checker.py` to enumerate all differences and verify exact collision counts in rings of sizes 4, 16, 64, and 256, then independently compute the two-sum-fiber fourth moment of representative complex character-phase packets and a strict nonextremal case at every size. `checker_output.txt` records the actual execution. The numerical packet moments are checked to tolerance \(10^{-9}\); no numerical sample is offered as an infinite proof.

The candidate's scientific scope, literature implications and residual novelty risk are described in REVIEW.md and AUDIT.json. Independent audit has not been performed.
