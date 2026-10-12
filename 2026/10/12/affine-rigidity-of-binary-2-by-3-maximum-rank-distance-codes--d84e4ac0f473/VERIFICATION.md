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

Run `python3 artifacts/verify.py`. The script uses only the Python standard library. It reconstructs all \(64\) binary \(2\times3\) matrices, computes rank by exact binary Gaussian elimination, builds the rank-distance compatibility graph, and exhaustively enumerates its maximum cliques.

It then independently enumerates all \(1395\) three-dimensional subspaces of \(\mathbb F_2^6\), filters those whose nonzero matrices all have rank \(2\), checks equality with the zero-containing maximum-code census, generates every affine coset, and enumerates the full stated \(\operatorname{GL}_2(\mathbb F_2)\times\operatorname{GL}_3(\mathbb F_2)\) action.

The expected output includes `VERIFY_OK`, `maximum=8`, `labeled_maxima=384`, `linear_mrd_3spaces=48`, `affine_cosets=384`, and `linear_orbits=1 orbit_size=48 stabilizer=21`.

The computation is exhaustive only for the finite domain stated in the finding. No higher-dimensional or other-field classification is inferred.
