---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The normal form and the algebraic group classification use inverse spanning-tree monomial maps and the primitive relation in the quotient torus character lattice. The recovery of this lattice relation follows from the action on the Lie algebra of the unipotent radical, over an arbitrary field. These are exact proof steps, not consequences of numerical tests.

The unchanged `verify.py` tests the edge-weight isomorphism between the two nonisomorphic six-vertex examples on finite-field points, and checks the previously covered class-count formula on four graph configurations over fields of sizes 2, 3, 4 and 5. It requires Python 3.8 or later and no third-party packages; the expected termination marker is `VERIFY_OK`. The finite test of the coordinate map is ancillary and does not establish necessity for algebraic group isomorphism.
