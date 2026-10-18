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
# Reproducibility and verification

Run `python3 check.py` from the directory containing that file. The script uses only the Python standard library, enumerates all \(k\)-assignments for \(2\le p\le5\), \(p\le q\le6\), \(1\le k\le p\), and checks exact rational pair counts, covariance spectra, affine ranks and contact equalities. The observed output is `PASS: 44 profiles; 7925 individual matchings; exact pair moments and spectral-contact identities`.

The general theorem follows instead from the proof in `RESULT.md`: one/two-edge inclusion probabilities, tensor eigenspace decomposition, universal constant Mahalanobis vertex norm, and the averaged-constraint determinant inequality. The tests do not certify unbounded parameters. The complete-bipartite restriction, intrinsic metric and potential earlier equivalent formulation are scientific limits. Independent mathematical audit has not been performed.
