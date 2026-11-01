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

# Reproducible checks and boundaries

Run `python3 verify_b6.py` in the folder containing `verify_b6.py`. It depends only on the Python standard library and prints `TYPE_B_SIXTH_HARMONIC_EXACT_CHECK_OK 304` on success.

The script computes normalized Gegenbauer values as exact fractions; forms squared inner products of one representative from each antipodal pair; checks the three rational scalar eigenvalues, standard-block determinant, invariant-block determinant and explicit invariant weight null relation for each integer dimension \(3\le n\le22\). It reconstructs complete projective Gram matrices and independently row-reduces them with exact fractions for dimensions \(3\) to \(6\), verifying ranks \(6,13,24,35\).

These are finite reproducibility checks. The all-dimensions claim is established in RESULT.md by the explicit incidence decomposition and exact rational determinant identities, plus direct positivity arguments. The normalization is \(G_n(1)=1\), not the raw \(L^2\) surface-measure reproducing constant. Neither historical priority nor independent mathematical verification has been certified.
