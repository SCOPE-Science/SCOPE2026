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

The standalone Python 3 standard-library checker `verify.py` was executed from its actual packaged source and completed with:

```text
VERIFY_OK exact_commutant_profiles= 86 exact_matrix_positions= 7868 spectral_profiles= 245 spectral_matrix_entries= 37240
```

The 86 exact rational profiles use a commutator linear-system construction independent of the proof's four-dimensional bright-sector spectral argument. The 245 numerical profiles reconstruct the full average-mixing matrix from directly diagonalized Hamiltonians and test predicted nullity and stochastic row sums. Profiles include equal and unequal onsite energies, balanced and unbalanced aggregate leaf coupling, left/right size-two contrasts, and asymmetric leaf-group sizes. The finite profile count does not prove the theorem for all sizes or real parameters. The analytical proof, including the structural cospectrality equivalence, is in `RESULT.md`. No independent audit has been performed.
