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

Run `python checker.py` using Python 3 with SciPy's `linprog` available. The checker uses exact fractions for the symbolic formulas and equality criterion and linear programming independently for projection-norm minimization over real parameters. Its deterministic execution reported 1,001 successful instances. The proof is given in `RESULT.md`, Steps 1--4. The finite numerical test is not an infinite-dimensional or all-parameter proof and does not establish historical novelty. The field-independent argument treats complex coefficients through modulus inequalities and realizes the optimal phases explicitly. The cited 1974 historical source could not be inspected in full; no claim of priority certification or independent validation is made.
