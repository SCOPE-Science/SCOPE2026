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

# Reproducibility and scope

Run `python verify.py` in a standard Python 3 interpreter. The checker constructs finite fields of cardinalities \(2\), \(3\), \(4\), \(8\), \(9\), \(16\), and \(27\), using explicit irreducible polynomials where needed. It evaluates the exact associated polynomial seeds and recursively applies the operators \(L\) and \(E\), enumerates all candidate tuples when the finite enumeration bound permits, and checks the resulting counts against the theorem.

Recorded execution:

`VERIFY_OK direct_extension_field_cases=124 associated_tuples_checked=172556`

The test includes prime-power bases \(q=4\) and \(q=9\), nontrivial extensions, four seeds, and the parent-chain indices. Its code does not invoke the theoretical lifting recurrence to produce the enumerated totals. It verifies that the base-field cases equal the respective even polygonal numbers and that every directly tested extension count satisfies the formula.

**Limits:** These are 124 finite examples, not a proof of any universal statement. Infinite-field-size and all-index assertions depend on the exact seed computations, the extension-field lifting lemma, and the telescoping proof in `RESULT.md`. The optional polynomial extensions away from \(X=0\) do not change counts because of the triangular open-fiber argument. There is no independent audit.
