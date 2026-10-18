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

The package supplies `verify_integral.py` (exact Smith normal forms over \(\mathbb Z\), using SymPy) and `verify_dual.py` (independent recursive face generation, mod-two linear algebra, a connected dual-facet graph, a seven-step nonorientability sign obstruction, and a cycle-overlap module check). The programs neither load nor trust the stored results. Run them using `python verify_integral.py` and `python verify_dual.py` from a directory containing the two scripts. Captured outputs are `verify_integral.txt` and `verify_dual.txt`.

The integral checker verifies all adjacent chain maps compose to zero and recomputes every Smith factor from the full signed boundary matrices. This is an exact finite calculation, not an inference from sampling. No assertion of a general classification, smallest-order counterexample, or independent audit is made. The original conjecture is cited specifically as it appeared in the 2022 preprint.
