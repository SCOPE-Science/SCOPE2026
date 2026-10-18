---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: For n>=2 iid uniform points and fixed clockwise arc length s in (0,1), cyclic normalized spacings D form Dirichlet(1,...,1), uncovered gap count K=sum 1{D>s}, covered fraction C=1-sum(D-s)_+. Independent integration of marginal and pair Dirichlet tails gives Cov(K,C)=n(1-s)^(2n-1)-(1-s)^n-(n-1)(1-2s)_+^n. For 0<s<1/2, factor (1-s)^n Bn(s), whose derivative is governed by R=(1-2s)^(n-1)/(1-s)^(2n-1) with log derivative (1-2ns)/((1-2s)(1-s)); R crosses 1 only once, so Bn has one positive zero for n>=3, and n=2 simplifies to s²(1-2s) on first half. Independently verified rational Dirichlet identities for n=2,...,24 and numerical roots s3=0.40333046641386133, s4=0.33214428, n40 root≈0.04341838. Expansion s=c/n gives e^-2c(1+c+c²-e^c), unique positive c*=1.7932821329 by convexity, and unique finite thresholds imply ns_n->c*. Finite checks do not replace all-n proof.

## originality

PASS

PASS with bounded risk: Circular uniform-spacing Dirichlet theory, marginal moments and Huillet's much broader joint coverage transform are existing science, and the covariance is in principle derivable from a full joint law. The assessed specific new content is the global one-zero sign classification for each n, including the sharp sparse-scale c* limit. Resultary and primary-source searches did not find this exact sign-classification statement. Holst–Hüsler (1984) and Huillet (2003) could not be inspected in full under institutional access; their potential equivalent derived covariance or sign discussion is a nontrivial residual risk. No novelty for the joint law or covariance as a formal transform derivative is claimed.

## value

PASS

PASS: Gap count and covered fraction are canonical geometric coverage observables; their covariance switches sign exactly once rather than obeying a simple monotone relationship. The exact finite-sample phase boundary and sparse scaling constant give a motivated, reusable description of dependence that cannot be read directly as the sign of standard marginal coverage formulas. Not about nonuniform arc lengths or full-coverage threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
