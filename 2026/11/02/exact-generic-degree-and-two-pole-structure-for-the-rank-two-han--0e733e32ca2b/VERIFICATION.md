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

# Verification

The mathematical proof uses a dense-open recurrence parametrization, an exact rational elimination of \(P\), and complete determination of the pole divisor of the last moment \(a_{n-1}\). The two poles have the orders \(n-4\) and \(\lfloor(n-1)/2\rfloor\). These are algebraic identities valid for all integers \(n\ge5\) over the stated field.

The reproducibility artifact `verification/check_degree.py` constructs exact rational recurrences, cancels numerators and denominators, and verifies the pole orders and map degrees for each \(5\le n\le18\) at two admissible rational triples. Run `python verification/check_degree.py` with Python 3 and SymPy. Passing these finite checks does not prove the infinite claim; the separate induction and leading-coefficient analysis do.

No independent external mathematical audit or certificate is asserted.
