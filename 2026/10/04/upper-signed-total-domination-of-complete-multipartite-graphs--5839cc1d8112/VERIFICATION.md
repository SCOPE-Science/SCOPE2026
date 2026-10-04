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

The proof establishes the infinite statement directly. The bundled `verify.py` is supplementary finite evidence. It enumerates all nondecreasing complete-multipartite profiles through order 10 and every vertex labeling by \({-1,1}\), checks open-neighborhood signed total domination literally, compares minimality with the tight-part criterion, computes the maximum minimal weight, and checks the theorem formula. For profiles through order 7 it also compares against every coordinatewise smaller labeling rather than relying only on single flips.

Replay result:

`VERIFY_OK profiles=128 labelings=64916 minimal_functions=6921 full_lower_checks=511 formula_checks=128 pair_targets=1026 max_order=10`

The finite range does not certify cases above order 10; those cases are covered by the symbolic proof. The literature portion of the originality check has the access limitation recorded in REVIEW.md and AUDIT.json.
