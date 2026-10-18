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

The proof is self-contained in RESULT.md: structural induction establishes rooted truth invariance, negated Boolean minterms distinguish exactly the leaf-color sets, and a finite disjunction over \(k\)-element color sets witnesses every strict transition.

Run `python verify_fork_types.py` using Python 3.9 or later. The completed run reported 43,291 valuation/type checks, 1,013 direct separating-formula checks, and 999 full formula-validity checks, all passing. These enumerations cover only the explicitly stated finite parameter ranges; they are not the proof for unbounded \(n\) or \(k\).

The published source date is supported by the dated arXiv v1 submission. Related general finite-model and type-color arguments are cited in RESULT.md. The result has received only self-review, not independent validation or certification.
