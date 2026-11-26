---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification

The standalone `verify_cubocta_pm.py` requires Python 3.10 or newer (it uses `int.bit_count`) and no external libraries. Run it in the source package to reproduce the exact JSON in `VERIFIER_OUTPUT.txt`. The checker constructs \(L(Q_3)\) and its 32 perfect matchings, builds their full simplicial downset with 1,428 nonempty faces, and evaluates the signed augmented simplicial trace of all 48 automorphisms. The traces are consistent within each of the ten signed coordinate-cycle classes and give a weighted sum of 96. In particular, the invariant dimension is two.

To obtain the degree-two character from these traces, one uses concentration of the reduced homology in degree two. This is already known from the integral wedge result cited in `RESULT.md`. The checker also confirms that prerequisite: its augmented face-poset acyclic matching leaves 43 critical two-faces and pairs the empty face. Removing the empty-face pair leaves one critical vertex and 43 critical two-faces in the ordinary face poset. The separate mod-two computation is a consistency check, not the source of the integral result or of the rational character.
