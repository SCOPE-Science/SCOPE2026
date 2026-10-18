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

Install the two dependencies from `requirements.txt` and execute `python verify.py` in the directory holding both files. The checker constructs the full graph Laplacian, all site-projector Lindblad terms and the full vectorized density-matrix superoperator independently of the reduced three-variable proof. The tested graph sizes are \(k\in\{2,3,4,5,6\}\) peripheral vertices, with empty, complete, sparse and alternating induced edge sets and four dephasing rates; time samples are explicitly given in the checker. It directly compares full quantum evolution with the analytic reduced model, compares density matrices among different induced peripheral graphs, verifies trace/positivity, evaluates the reduced zero-frequency resolvent, tests the optimizer at selected degrees and corroborates the large-degree exponential limit. The expected output is `VERIFY_OK 970 direct full-Lindblad / resolvent / optimizer / scaling checks`.

The proof of the exact rational Laplace transform is finite-dimensional symbolic block algebra, the convergence is established with the cubic Routh–Hurwitz test, and optimization is elementary calculus. The large-degree law follows from distinct-root and residue perturbation, not a sample of degree values. Numerical matrix exponentials are approximate; their tolerated discrepancies do not furnish a formal error bound for every size or time. The test does not establish independent auditing, publication priority or conclusions beyond the specified initial condition, Laplacian Hamiltonian and uniform positive site-dephasing rates.
