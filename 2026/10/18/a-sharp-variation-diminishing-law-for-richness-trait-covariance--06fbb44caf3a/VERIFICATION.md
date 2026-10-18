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

The exact mathematical checks are replayable with `python3 verify.py`. The program does not require nonstandard Python packages or network access. Its JSON output, including the final newline, must match `certificate.json` exactly.

Checks reproduce the closed covariance formula by a separate direct enumeration of labeled-individual subsets, for 65 abundance partitions totaling between 2 and 8 individuals under three trait assignments each: 1,245 direct comparisons. They also check the sharpened sign-variation inequality in all 195 enumerated profiles, 1,370 monotone-trait signs, and exact sharpness interpolation witnesses for 2 through 8 abundance classes. The four-class population has two consecutive strict changes, independently verified by direct enumeration of all its sample subsets.

Finite checks substantiate the implementation; the general bound and arbitrary-level sharpness rest on the explicit analytic proof in `RESULT.md`. This package has not been independently audited or certified by an external reviewer.
