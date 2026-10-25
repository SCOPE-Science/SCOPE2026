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

Execute `python3 check_clique_path.py` with Python 3 and no external dependencies. The script constructs each grounded graph Laplacian for the full Cartesian-product graph, inverts it with exact `fractions.Fraction` arithmetic, computes every original cut and cycle projector column, and compares each with independently formed one-dimensional resolvent formulas.

Eight cases were checked: `(m,n)=(3,4),(3,5),(3,6),(3,7),(4,4),(4,5),(5,4),(5,5)`. The check found 327 exact edge columns, and 654 cut/cycle absolute column sums. It verifies maximal-column direction and odd/even norm ordering for these finite cases. All assertions passed.

The infinite-parameter statement instead uses the analytical product-resolvent, tridiagonal positivity and explicit inequalities reproduced in `RESULT.md`. The finite checker is not a formal proof and does not verify untested parameters by enumeration. No independent mathematical audit has been performed.
