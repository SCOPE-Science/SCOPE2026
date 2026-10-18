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

# Verification of the weighted Hamming interaction projection theorem

The proof is in `RESULT.md`. Its nonstandard steps are checked directly: the double-centering operator is idempotent with zero marginals; averaging any projection over the finite coordinate-permutation group cannot increase its norm; and equivariance forces the averaged projection to annihilate the two one-coordinate subspaces. No irreducibility theorem is assumed. Sharpness uses explicit 1-Lipschitz functions that attain each candidate edge difference. The contractive classification includes equal weights and the boundary ratios.

`CHECK.py` performs an independent finite-dimensional primal-molecule/dual-Lipschitz linear-program check. For each of 144 combinations with coordinate counts from 2 to 5 and weights in {1,2,3}, it constructs the centering matrix, checks idempotence and marginal annihilation, and optimizes the Lipschitz dual objective over all coordinate edges. The maximum is compared to the formula with absolute tolerance 2e-8. Reproduce with `python CHECK.py` after installing `requirements.txt`.

All tested cases passed. Linear programs approximate finite optima numerically; they do not establish the theorem for every size or every positive real weight. The universal assertion relies on the elementary analytic proof. An independently performed audit or external certification is not asserted.
