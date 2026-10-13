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
# Reproduction

Run `python3 verify.py` with Python 3.9 or later and no third-party dependencies. The checker enumerates exactly the 18 balanced four-uniform image pairs with the first image beginning in 0, tests all 15 unequal-image cases, and checks every 1-step through 3-step pair base condition inside the third substitution iterate. It verifies that each of the four lifting residue unions is the full binary ordered-pair set. The finite certificate, combined with the induction in RESULT.md, establishes pair saturation at all positive distances. The program then checks 1,152 direct length-by-length factor complexities against the symbolic boundary formula or coincident-image periodic formula. Expected terminal line: `VERIFY_OK morphisms=18 theorem_pair_base_checks=45 theorem_pair_lift_checks=60 factor_length_checks= 1152`.

The finite factor window is only a consistency test. No separate independent evaluation has been performed; no claim is made about other uniform lengths or nonbalanced images.
