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

The proof integrates exact planar rational polygons and uses a root-of-unity criterion for the cyclic reduction of the strip law. It also proves pairwise independence through torus coverings and arbitrary-time binary triple independence through sign inversion.

The standalone `check.py` (run directly with Python 3) returned `VERIFY_OK: rational polygon integration, arithmetic threshold, entropy, and pairwise ranks`. Exact polygon tests cover \(3\le t\le30\); modular tests cover \(2\le q\le40\); determinant tests cover the first nine indices for \(3\le t\le20\). The information formula's logarithms are checked numerically only; it is established for all parameters by a separate closed entropy calculation. None of the infinite claims relies on the finite testing range.

There is no independent audit or external formal certification. The earliest dated supporting primary text is the 22 July 2010 preprint of Siemaszko and Wojtkowski, arXiv:1007.3984. The source is used for background in toral partition dynamics, not as an assertion of the new cylinder formula.
