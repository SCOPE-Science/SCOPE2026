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
# Reproducibility

The included standalone `verify.py` constructs multiplication in the basis \(1,y,\ldots,y^{n-1},x,xy,\ldots,xy^{n-1}\) and evaluates \(ab-ba\) by independent finite-field row reduction, without using the theorem to build the rank matrix. It then checks every element against the rank formula, recomputes the complete histogram via independent weight sums, and verifies its total cardinality. Run with `python verify.py` using Python 3, with no third-party packages.

The tested configurations are \((q,n,\lambda)=(2,5,1),(3,4,2),(4,3,2),(4,3,3),(5,3,2),(5,3,4),(7,3,2),(7,3,3),(7,3,6),(4,4,2)\), where the extension \(\mathbb F_4\) is represented by the irreducible polynomial \(z^2+z+1\). The expected terminating line is `VERIFY_OK_QCI_ADJOINT`. This finite enumeration is a check, not an infinite certificate. Generality follows from the algebraic proof in RESULT.md.
