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

# Reproducibility and limits
The full proof in `RESULT.md` gives an unbounded integer-parameter theorem and explains the integral arm-permutation action. `verify_spider5.py` independently enumerates forbidden connected triples and reconstructs finite chain boundaries for two and three arms. It also checks every arm permutation using signed fixed-face traces, and verifies exact elementary collapses of the two smaller path complexes. The checker requires Python 3 and no external libraries; its observed output is included in `verify_spider5_output.txt`.

The finite checks do not establish the theorem for arbitrary numbers of arms; the unbounded argument is the vertex-link mapping-cone proof. The checker computes mod-two Betti ranks, while the integral group structure follows from an exact integral long exact sequence in the proof, not from mod-two testing. The listed traces are independent consistency tests and do not alone identify an integral module. No independent audit has been performed.
