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

The analytic proof reduces the finite core to a symmetric normalized Laplacian and uses continuity of its generalized inverse square root across a fixed-rank limit. The nonzero limiting eigenvalues are \(2\), \(1-\sqrt3/2\), and \(1+\sqrt3/2\), so no finite experiment is being used to exclude an unobserved small eigenvalue.

`verify_graph_riesz_lower_bound.py` is a standard-library sanity checker. It numerically rebuilds the four-vertex matrices for four decreasing values of \(arepsilon\), verifies convergence to the six exact edge limits, checks the weak ratio against \(2/\sqrt3\), and checks the lift identity \(\sum_k a_k=6\). Its successful output is recorded in `verification_output.txt`.

The checker does not prove the limiting theorem, exhaust all weighted graphs, or establish optimality of \(2/\sqrt3\). The theorem's upper endpoint \(2\) is taken from Wang's Theorem 2.1; the new proof establishes only the lower endpoint.
