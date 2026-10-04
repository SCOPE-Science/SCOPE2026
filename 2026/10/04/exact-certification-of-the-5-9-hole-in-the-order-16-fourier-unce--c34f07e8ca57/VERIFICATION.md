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

The claim is finite and is checked exhaustively with exact arithmetic by `verify_z16_5_9_hole.py`.

For each five-point time support \(A\) and seven-point Fourier zero set \(B\), the verifier applies the exact kernel-rank criterion for a vector with all five time coefficients nonzero and no Fourier zeros outside \(B\). Independent time translation and modulation reduce the search to \(273\cdot715=195{,}195\) orbit representatives; the reduction is exact because five- and seven-subsets have trivial translation stabilizer in \(\mathbb Z_{16}\).

Every rank calculation uses exact determinants in \(\mathbb Q(\zeta_{16})\). Since \(\Phi_{16}(X)=X^8+1\), a determinant is represented as eight integer coefficients; zero testing is therefore exact and tolerance-free.

Packaged replay output:

`support_representatives=273`

`zero_set_representatives=715`

`orbit_pairs=195195`

`full_rank=193416`

`rank_deficient=1779`

`rank_histogram={3:27,4:1752}`

`deletion_conditions_pass=136`

`extension_conditions_fail=136`

`admissible_exact_support_pairs=0`

`VERIFY_OK`

The computation proves only the stated fixed order-\(16\) claim. It does not infer a pattern for larger orders. Independent audit has not been performed.
