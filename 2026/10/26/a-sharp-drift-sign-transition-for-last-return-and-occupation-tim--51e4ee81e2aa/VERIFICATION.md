---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: For 2n iid biased +/-1 steps, K_n is half last zero time and U_n is half the count of positive midpoint steps. Prefix conditional on last return at 2k is a uniform bridge; Chung–Feller makes positive semiduration J_k uniform 0..k. Remaining 2m-step nonreturn meander has ballot count b_mr=(r/m) binom(2m,m-r) and positive sign probability w_m=A_m+/(A_m++A_m-). The ratio b_(m+1),r/b_mr increases strictly in r and added maximum-support value gives strict MLR order for the signed terminal height; for p>1/2, w_m strictly increases above 1/2. Conditional mean n/2+m(w_m-1/2) strictly decreases in k and covariance via independent-copy identity is negative, with reflection for p<1/2, and zero at p=1/2. Independently enumerated all sign paths for n<=5 at five rational biases and verified exact sign. No finite test replaces general ballot/MLR proof.

## originality

PASS

Chung–Feller bridge occupation uniformity and Lachal biased sojourn laws are clearly prior; Hartmann–Majumdar 2025 treats driftless Brownian joint last-zero/occupation. Target strict drift-dependent conditional-mean order and finite-n covariance sign are not stated as consequences of the inspected prior theorems. Extensive classical walk literature leaves an older equivalent joint-law risk.

## value

PASS

Strict finite-horizon covariance sign reversal and the stronger conditional mean monotonicity are qualitative new structure for two natural path functionals; they go beyond marginals and classical zero-drift symmetry. Ballot MLR supplies a reusable explanation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
