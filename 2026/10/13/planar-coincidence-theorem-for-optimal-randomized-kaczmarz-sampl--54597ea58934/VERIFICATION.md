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

# Reproduction and verification

Execute `python3 verify_planar_rk.py` using only the Python standard library. The expected final output is exactly:

`VERIFY_OK 789 exact/geometry checks`

The checker was run using its bundled source file, and its recorded output matched. It implements exact rational orthogonal projections and covariance propagation, compares the resulting finite-time mean-square errors against the theorem's two-endpoint formula, tests the isotropic three-direction all-horizon formula at finitely many horizons, verifies the exact doubled-angle moment identity, and compares selected circular-arc and segment distances. A rational three-row instance also tests the optimal angular support lower bound.

The 789 checks comprise 588 exact pair/horizon/error identities, 36 exact isotropic identities, 50 exact moment identities, 49 deterministic arc-geometry checks, and 66 rational candidate comparisons. All numerical geometry checks use a specified absolute tolerance for floating-point trigonometry; rational equalities use `fractions.Fraction` and exact equality.

The analytic proof in `RESULT.md` supplies the arbitrary-real-angle, arbitrary-row-count, all-initialization and infinite-time quantifiers. The checker does **not** establish originality, replace the proof, certify mathematical statements independently, or cover noisy systems and quenched error rates. The source-document comparisons and their residual risk are documented in `REVIEW.md` and `AUDIT.json`.
