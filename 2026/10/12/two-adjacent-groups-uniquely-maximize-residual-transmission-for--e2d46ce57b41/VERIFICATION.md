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

# Reproducibility and scope of checks

Run `python verify_cycle.py` with Python 3 and the version-compatible SymPy dependency in `requirements.txt`. An independent run against the packaged `verify_cycle.py` printed:

```
VERIFY_OK: exact resolvent, quadratic expansion, maximizer derivatives, and both characteristic factors
```

The code uses exact integers and rational symbolic algebra, not floating-point tolerances. It recomputes the undirected five-cycle adjacency matrix; the reduced-resolvent identities; the complete second-order coefficient matrix; the identity relating it to edge and nonedge pair sums; the gradient and face restriction at the representative adjacent split; and the full characteristic polynomials for the equal-adjacent and single-node strategies. Substituting a Taylor root near \(2\) checks the exact quadratic coefficients \(1/25\) and \(0\), respectively.

The infinite family of admissible allocations is covered by the **analytic** argument in `RESULT.md`: elementary support shifting proves the edge bound for every nonnegative probability vector, and uniform analytic perturbation plus strict face curvature and symmetry promotes the five isolated quadratic maximizers to the only exact spectral maximizers for sufficiently small positive budgets. Symbolic checks support the algebraic premises but do not independently certify the infinite-dimensional quantifiers, a numerical value of the budget threshold, or originality. No external independent audit or validation has been conducted.
