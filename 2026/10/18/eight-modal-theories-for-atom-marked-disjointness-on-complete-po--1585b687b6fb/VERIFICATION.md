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

The Python 3 standard-library program `verify.py` is packaged alongside the proof. Execute `python3 verify.py` in the same directory. It constructs the original disjointness Kripke models for ground-set sizes one through nine, computes the successor-type profile of every nonempty subset, directly evaluates each of the eight characteristic formulas, and independently computes the finite modal-depth refinement signatures through depth four.

Observed run: `ATOM_DISJOINTNESS_VERIFY_OK finite_models=9 worlds=1013 characteristic_semantics=8104 depth_classes=2,6,7,8,8 formula_classes=4,64,128,256,256 all_successor_profiles=true sharp_depth=3`.

These computations test 1,013 pointed worlds and 8,104 formula/world pairs; they are not an exhaustive search over all finite sets, let alone infinite ground sets. Full correctness relies on the explicit type partition, successor-profile proof, back-and-forth bisimulation, characteristic formulas and finite representative construction in RESULT.md. Tests are reproducible without network access or third-party dependencies.

The restricted language includes exactly one fixed propositional observation, true at singleton sets. This verification does not certify claims for arbitrary propositional valuations, induced subframes or additional modal operators. No independent audit has been performed.
