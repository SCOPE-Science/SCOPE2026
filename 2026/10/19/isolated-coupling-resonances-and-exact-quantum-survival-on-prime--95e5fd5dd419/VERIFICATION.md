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

# Verification of the prime-prism survival formula

`python verify.py` (install `requirements.txt`) reconstructs the full real-symmetric hopping matrices in the position basis and evaluates the sink-bright spectral projector from numerical eigenspaces, without inserting the analytically derived survival fraction in the computation. It compares the resulting survival probabilities with the theorem at all predicted exceptional couplings and four off-resonant couplings for each odd prime in \(\{3,5,7,11,13,17\}\), using both signs of nonzero intra-cycle hopping.

Observed replay output: `VERIFY_OK dense_spectral_cases=212 nonhermitian_checks=6 max_dense_error=4.996e-15`.

The script also constructs the actual non-Hermitian sink Hamiltonian and checks six long-time norm values against the independent bright-projector computation. These checks are numerical and finite. Infinite-time decay on the bright space and the uniqueness of all cosine gaps for arbitrary odd primes are proved analytically in `RESULT.md`, not inferred from the grid or simulator. Numerical eigenspace grouping uses a tolerance and can fail near unresolved degeneracies; it is a corroboration only. Independent audit: not yet performed.
