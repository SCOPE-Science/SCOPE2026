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

# Reproduction and limits

Execute `python verify.py` with Python 3 and no third-party packages. The program constructs exact rational polynomials, recovers each strictly positive transmission coefficient, compares both forms of the full mean-field vector field coefficient-by-coefficient and tests every prescribed root and its exact local derivative. It checks 20 successive interaction orders and 52 further admissible nonuniform constructions (72 total). The \(M=5\) witness is printed with all rates.

The infinite-dimensional parameter quantifiers in the paper are proved analytically by a decreasing-elementary-symmetric-coefficient lemma and a scalar root-count argument; finite tests alone cannot establish them. Verification establishes no finite-population stochastic limit theorem and does not exhaust the scientific literature. No independent scientific audit has been performed.
