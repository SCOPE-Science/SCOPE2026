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
# Verification notes

The supplied standalone `verify.py` enumerates all inputs and target fibers in \(\mathbb F_{p^2}\), represented explicitly by pairs \((a,b)\) with \(i^2=-1\). It computes polynomial evaluations through field multiplication, checks both signs of the parameter for \(p\in\{11,19,43,59\}\), verifies the zero singleton, the full multiplicity histogram, and the special singleton target lines. The full computation is reproducible with `python3 verify.py` and has no external dependencies.

The proof checks required for general prime powers are in `RESULT.md`: norm-one reduction, the two quadratic exceptions, the cubic discriminant with \(t^2=-2\), square-discriminant Frobenius parity, and the repeated-root factorization. Finite enumeration does not certify the infinite theorem, and there has been no independent audit.
