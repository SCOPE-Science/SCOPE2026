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

# Reproduction and boundary checks

Run `python verify.py` with Python 3, SymPy and NumPy available. It prints `PASS 3849 exact and numerical checks` when all assertions pass. The code builds the full adjacency-constrained stochastic matrix from the graph definition instead of reading any previously generated proof matrices. It verifies exact characteristic-polynomial factorization and prescribed optimizers for small graph sizes; exact interval endpoints and out-of-interval failures are also checked for finite sizes. A numerical matrix eigensolver checks a separate finite feasible grid.

The proof in RESULT.md, not the finite checks, establishes the exact conclusions for every integer \(m\ge2\). Nonuniform-stationary and nonreversible chains are outside scope. Independent scientific validation is not performed.
