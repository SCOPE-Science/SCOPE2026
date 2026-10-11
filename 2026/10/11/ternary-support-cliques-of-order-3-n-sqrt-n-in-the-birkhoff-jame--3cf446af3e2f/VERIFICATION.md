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

# Verification record

The proof supplies coordinate witnesses for each direction of mutual Birkhoff–James orthogonality for arbitrary real or complex perturbation scalars. It counts canonical representatives and identifies the maximal support layer by an exact adjacent-term ratio. The asymptotic prefactor follows analytically from Stirling at the binomial mode.

`verify.py` is an optional reproducible Python standard-library check of selected small dimensions. Run `python3 verify.py` from the folder containing the script. It verifies the signed representative counts, all unordered mutual-orthogonality tests in support layers through dimension six, and best layers through dimension eight, concluding:

`VERIFY_OK layer_count_checks=36 mutually_orthogonal_pairs=475172 all_pairs_exact=True`

Computations do not certify the formula for all dimensions, nor optimize over all projective normed-space vectors. The complete analytic proof supports the constructive bound; exact clique maxima and a full-text comparison with the 2022 survey remain open. This is not an independent audit.
