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

# Verification of the new claim

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The same source was run successfully and returned `VERIFY_OK`; the expected exact checks are 475 scale-three faces, forty scale-two free-face pairs, 219 scale-three Morse pairs, one critical zero-face and 36 critical three-faces, 1,770 Hasse cover relations, and mod-two boundary ranks `(9,36,84,75,15)`. The graph has ten vertices, fifteen edges and diameter two.

The acyclicity test is complete on the full face poset: every cover relation is oriented and checked by topological sorting. This is a finite exhaustive certificate for a single graph; a finite test cannot establish an infinite-family theorem, and no such extension is claimed. The relative scale-two collapse proves the inclusion persistence map is an isomorphism in degree one. The critical-cell configuration proves the integral homotopy type, while the mod-two computation is a separate cross-check. Independent external audit is not part of this verification.
