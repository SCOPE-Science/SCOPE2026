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

# Reproduction and scope

Run `python verify_pappus.py` with `requirements.txt` installed. The script is standalone and checks all finite graph automorphisms, all 297 two-dimensional cubical boundary columns, all 216 signed Lefschetz traces and the exact thirteen-class multiplication identities.

The certificate uses exact finite arithmetic, including two-component rational elements of the quadratic field with square root of three, and does not infer infinite statements from a finite experiment. The graph configuration-space identification uses the established two-particle cubical subdivision criterion. Integral equivariant structure and generalization to other graphs were not checked or claimed. Independent audit has not been performed.
