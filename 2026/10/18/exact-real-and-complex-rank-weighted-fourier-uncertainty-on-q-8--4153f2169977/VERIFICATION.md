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

# Exact algebraic verification

The standalone `checker.py` script evaluates each of the 16 displayed witness functions with symbolic arithmetic in SymPy; checks their precise nonzero support counts, all four one-dimensional Fourier coefficients, the rank of the two-dimensional Fourier matrix, and its determinant; and verifies the quaternion group relations and the character-ratio lemma.

Invocation: `python checker.py` (Python 3, SymPy). The observed successful run reported both exact profiles and concluded with `All sixteen witness computations and structural character identities passed.`

No floating-point tolerance is used. The general lower bounds and the impossibility of real rank-one Fourier blocks are mathematical deductions explained in `RESULT.md`; finite checks supplement but do not replace these proofs. No independent external validation was conducted.
