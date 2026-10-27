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

# Computational and mathematical verification

Run `python verify.py` after installing the two packages named in `requirements.txt`. The checker independently builds adjacency and combinatorial Laplacian matrices for all cycle-length pairs from 3 to 12; checks normalized dark eigenvectors and hub zeros; computes projected site probabilities; and verifies the expected dimension by **exact integer Krylov observability rank** for all 36 pairs from 3 to 8 on both generators. It also checks the exact two-triangle example using rational arithmetic.

The rigorous all-parameter steps are the Dirichlet sine eigenbasis, the odd-index hub boundary cancellation rule, the coprime overlap classification, and the dissipative block-decay argument. Finite verification cannot establish completeness for arbitrary cycle lengths, correctness of all analytic limits, or historical novelty. No independent audit has been performed.
