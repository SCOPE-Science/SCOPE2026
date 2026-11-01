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

# Verification record

The companion `verify.py` is a standalone Python 3 program using only the standard library. It independently builds unordered deleted-product cells and both signed boundary maps for six explicitly named complete bipartite graphs. It checks the composition of the differentials, determines ranks over the prime field \(\mathbb F_{1000003}\), compares the resulting Betti values with the rationally proved predictions, and tests signed cellular traces for every part-preserving symmetry of \(K_{3,3}\), \(K_{3,4}\), \(K_{4,4}\) and every bipartition-exchanging symmetry of the balanced examples. The recorded stdout is in `verification_output.txt`.

Run: `python verify.py`. A completed successful run ends with `VERIFY_OK`.

This finite program is a consistency check for the symbolic proof, not an all-parameter computation or an independent mathematical certification. In particular it does not reconstruct Ko and Park's general first-homology proof. The classification and its domain are proved in `RESULT.md`; no torsion conclusions are asserted.
