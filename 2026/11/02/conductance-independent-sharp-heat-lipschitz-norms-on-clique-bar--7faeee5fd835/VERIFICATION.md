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

Execute `python3 verify_weighted_barbell.py` using Python 3 with no additional libraries. The verifier constructs fifteen independently heterogeneous positive rational conductance graphs, including both cliques, and checks the gradient intertwining identity on every standard basis vector by **exact fractions**. It then independently evaluates the full heat kernel by positive uniformization at three times per graph with high-precision decimal arithmetic, checks the explicit bridge-norm formula and the strict bridge-vs-other-edge inequalities, and compares five peak values.

Observed output:

`CHECK_OK exact_gradient_intertwining_basis=120 weighted_graphs=15 independent_heat_edge_comparisons=45 root_asymptotic_cases=5`

The computation does **not** enumerate every real conductance choice or every time. The universal result relies on the explicit differential identities, positivity/oscillation arguments, two-dimensional spectral solution, and rigorous large-order expansion in RESULT.md. The uniformization truncation has a checked tail next term less than \(10^{-52}\) in the implemented tested regimes; the finite numerical tolerance is stated in the source code. The self-review is not independent validation.
