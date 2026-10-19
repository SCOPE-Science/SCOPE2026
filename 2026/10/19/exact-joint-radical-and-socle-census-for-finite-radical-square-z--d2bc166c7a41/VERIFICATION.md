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

# Verification and reproducibility
The included `verify.py` is Python standard-library code. Run `python3 verify.py` after extracting it. It enumerates all endomorphisms over prime fields, checks **every ordered matrix product** including squares, and computes the two joint rank invariants via independent finite-field row reduction. It compares the complete histograms, not just totals, with the Möbius/Gaussian formula.

Direct exhaustive cases: \((n,k,q)=(2,2,2),(2,3,2),(3,2,2),(2,2,3)\), totals \(10,22,148,33\), all passing. Arithmetic checks for \(n\le6\), \(k=2,3,4\) and \(q=2,3,4,5\) verify coefficient nonnegativity and transpose symmetry; these arithmetic computations of the formula do not independently enumerate matrices over extension fields.

The complete proof is in `RESULT.md`. Independence, publication review, and an externally administered audit have not been performed.
