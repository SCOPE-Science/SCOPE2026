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

# Reproduction and scope

Run `python verify.py` with NumPy and SymPy. The program constructs complete two-cube adjacency graphs independently of its direct radial Jacobi construction for dimensions \(1\le n\le6\), checks the full-to-radial intertwining and normalization, and uses exact symbolic recurrences to generate the squared-frequency polynomials through dimension 15. It verifies the even-dimensional mod-two constraint, the predicted smallest-squared-frequency windows, and direct positive-time returns for dimensions one and two. The run returned `PASS: 23 checks`.

The proof in `RESULT.md` handles every positive integer dimension; the verification program does not attempt exhaustive infinite-domain computation. The cited primary paper concerns remote-corner revival plots on the same graph, not a directly published joint-hub periodicity criterion. Independent mathematical audit, independent software validation, and exhaustive priority certification have not been performed.
