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

`VERIFY_KERNEL.py` uses the Python 3 standard library only. Run `python3 VERIFY_KERNEL.py` from the directory containing this file. It constructs the exact Kneser pair graphs for \(5\le n\le11\) and verifies the incidence and adjacency identities, first-harmonic eigenvectors, and generators of the second-harmonic sector. It independently checks the full exponential Gram matrices against the derived spectral eigenvalues at five values of \(2^p\) and four positive bandwidths per graph.

It also bisects the unique positive transition for the \(c=2\) critical window at \(5\le n\le16\), checks strict monotonicity on those cases, checks the exact special cases against \(\log((1+\sqrt5)/2)\) and \(\log2\), and tests the stated first finite-size correction numerically for four additional sizes. Actual successful terminal output ends with `ALL_PAIR_KERNEL_CHECKS_OK 7 graph_cases; 12 finite-size roots`.

The incidence calculations are exact integer/rational checks. Exponential evaluations and root comparisons are standard floating-point diagnostics, not certified interval computations. The theorem for all integers, powers and bandwidths is justified instead by the elementary three-sector proof and scalar monotonicity analysis in `RESULT.md`. No independent audit or external correctness certification has been performed.
