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
# Reproducibility checks

The included `verify_spider.py` uses standard Python only. In the directory containing this file, run `python3 verify_spider.py`. Its expected output is:

`VERIFY_OK 15 full mod-2 Betti vectors; 142 oriented Lefschetz characters; 142 orbit-fixed quotient predictions; 20915 independent face instances`

It enumerates independent sets directly from graph edges, computes simplicial mod-two ranks by boundary reduction, and computes signed Lefschetz traces for every arm permutation of the selected finite spiders. The actual output above was obtained from the included source file. This finite experiment is not an infinite proof, nor does it establish integral torsion absence or an equivariant homotopy equivalence. Those conclusions use the mathematical center-cofiber proof, full-subgroup fixed analysis and representation-sphere homotopy constructions in RESULT.md.

Independent mathematical audit: not performed.
