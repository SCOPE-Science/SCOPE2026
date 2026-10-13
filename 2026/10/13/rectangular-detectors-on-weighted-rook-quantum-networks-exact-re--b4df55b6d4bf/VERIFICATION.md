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

# Reproduction of mathematical checks

The analytic derivation is in `RESULT.md`, not inferred from numerical tests. To replay the finite checks, install dependencies in `requirements.txt` and run `python3 verify.py`. The executable independently constructs real symmetric weighted Cartesian adjacency matrices and their numerical eigenspaces (rather than reusing the four analytic tensor projectors), projects all detector coordinate vectors into grouped eigenspaces, computes orthonormal bases of their spans, and checks bright-space ranks and sitewise projector diagonals against the theorem. It exhausts all nonempty rectangular detector cardinalities for \(2\le m,n\le6\) at one positive nonresonant hopping pair and one exactly resonant positive pair (800 comparisons). A second check exponentiates the actual non-Hermitian Hamiltonian with differing positive detector rates and compares 12 late-time losses with predicted absorption. Run output:

```text
VERIFY_OK spectral_rank_and_sitewise_cases=800 direct_loss_cases=12
```

Numerical thresholds are \(10^{-8}\) for spectral grouping and numerical rank, \(2\cdot10^{-10}\) for individual spectral-diagonal errors, and \(4\cdot10^{-5}\) for late-time survival discrepancies. Long-time tests use \(t=1000\), so they are checks, not claims of uniform finite-time convergence. The proof handles every size, all positive rates and exact resonances analytically. No independent audit or infinite-size machine certification was performed.
