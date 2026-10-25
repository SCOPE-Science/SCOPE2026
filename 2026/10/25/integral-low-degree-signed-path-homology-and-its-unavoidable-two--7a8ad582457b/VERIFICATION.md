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

# Reproducibility of bounded checks

Run `python verify.py` using Python 3 and SymPy. The bundled `verification.log` is the exact output for the recorded run and concludes with `VERIFY_OK`. There are 362 graph/signing cases across cycles, a cycle cactus, the Petersen graph and the Heawood graph, 16,644 eligible two-path generator checks, and 6,764 primitive backtrack relation checks. The checker compares the rank and integer Smith invariants of signed incidence maps with independent spanning-tree balance tests, and checks connectedness of the signed cover in unbalanced examples. These computations are finite evidence; the universal assertions rely on the mathematical proof in RESULT.md. No independent audit is asserted.
