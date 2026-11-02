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

The exact claim, proof and counterexample scope are in `RESULT.md`. With the two attached standalone artifacts in one directory, execute `python3 verify_kneser.py DEPTH4_TREE.json` using Python 3 standard libraries only. The checker enumerates all finite query supports and concept partitions for \(n=2,\ldots,10\) and all online version spaces for \(n=2,\ldots,14\); it tests all 15 internal nodes and all 16 root-to-leaf paths of the \(n=7\) adaptive tree. A successful run ends with `ALL_RANK_TWO_KNESER_CHECKS_PASS`. The universal VC and Littlestone upper bounds are proved mathematically and are not inferred from those finite checks. The sharp adaptive lower bound uses a complete finite tree witness whose entire path set is verified. No independent audit has been performed.
