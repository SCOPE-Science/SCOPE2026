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

# Reproducibility and verification scope

Execute `python VERIFY_CYCLE.py` using Python 3 with SymPy available. The checker terminates with `VERIFY_OK` and reports complete vertex enumeration at \(n=4,6,8,10\). The observed pairs (vertices, singular fixed points) are \((7,6)\), \((18,17)\), \((47,46)\), and \((123,122)\), respectively.

The checks construct active primitive facet normals, test their integer Smith invariants and unimodular determinants, verify the four-ray conifold circuits and the full-cycle dependence, exhaust the component intersection conditions, and test parity-dependent contact with the distinguished diagonal line. The all-parameter theorem depends on the explicit active-graph circuit proof in `RESULT.md`; enumerating four parameters cannot prove infinitely many cases. The transverse semigroup description and intersection-dimension assertions are additionally established symbolically in that proof. This is self-review, not independent audit or external certification.
