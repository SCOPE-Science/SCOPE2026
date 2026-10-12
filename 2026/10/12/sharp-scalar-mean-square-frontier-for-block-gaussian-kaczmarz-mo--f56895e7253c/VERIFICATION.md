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

The reproducibility script `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic, evaluating a direct permutation determinant of each 3-by-3 matrix. Run `python3 verify.py` in this directory.

Actual replay completed: `PASS: 1890 exact determinant checks; discriminant and leading-coefficient identities`. The same run printed `PASS: rank-one block-width examples and eight exact rational second moments` and the sequence `1, 3/4, 7/8, 1, 35/32, 77/64, 85/64, 375/256` for source-initialized block width one with \(\alpha=\omega=1/2\).

The script verifies finite rational identities and a worked example, but **does not** enumerate every real parameter or prove the eigenvalue asymptotics. The full, continuum-valid derivation is the covariance-cone Perron argument, one-crossing determinant, and global-optimality discriminant proof in `RESULT.md`. It checks no high-dimensional, non-Gaussian, adaptive, or independently audited claim.
