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

The proof in `RESULT.md` establishes an exact probability mass formula from [1, Theorem 1.4], proves that the associated survival law telescopes, and factors the cross-parameter increment of each survival-ratio factor. Monotonicity of its finite bracket gives the claimed stochastic-order trichotomy and one-crossing assertion for all admissible integer parameters. The support endpoint and the equal-support exception are handled explicitly. The sharp order-eleven comparison and the macroscopic phase boundary follow from exact polynomial inequalities, not numerical extrapolation.

`check_exact.py` is a standalone standard-library verification file. Running `python3 check_exact.py` passed 89,613 exact assertions: full normalization and telescoping checks for \(2\leq a\leq18\), \(1\leq b\leq18\); independently enumerated spanning trees for \(2\leq a,b\leq5\) with \(a+b\leq8\); factor identities and complete comparison signs for \(4\leq N\leq60\); and exact order-eleven fractions. It does not search all infinitely many cases. Full proof validity depends on the explicitly written argument and the known prescribed-tree inclusion theorem, not on the finite checker.

Known sources establish the path inclusion and more general forest counts. Their direct consequences are not claimed as new. The claimed finite stochastic-order comparison is subject to residual historical-priority uncertainty. Independent audit has not been performed.
