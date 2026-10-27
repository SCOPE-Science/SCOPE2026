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

# Verification

The analytical proof reconstructs the exact three-state occupation-count generator and its reversible stationary distribution, differentiates the all-jumps tilted generator twice, and solves the centered Poisson equation. Exact substitution shows the Fano excess equals two manifest nonnegative Dirichlet contributions divided by the mean rate. For stars the excess simplifies to \((N-4)^2/N^2\); for arbitrary bipartitions the sign of \(N^2-6N+4\) determines the strict fixed-order extremizers. In \(K_{1,3}\), all configurations have total rate two, yielding a complete Poisson counting process, not merely a second-moment match.

Run `python verify.py` with the dependencies in `requirements.txt`. The script independently enumerates full particle configurations and computes the generator and Poisson equation without relying on lumped transition rates; it compares 35 parameter pairs up to part size six, verifies two symbolic identities, and tests all fixed-order extremizers from three through thirty vertices. These tests corroborate but do not establish statements for infinitely many graph sizes. No external expert or independent audit has been performed.
