---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For 2x2 SPD A=[a c;c b] with independently sampled Rademacher signs, the leave-one-out projector on Aw yields signed residual vector f_s=-s(ab-c^2)(b+sc,a+sc)/[(a+sc)^2+(b+sc)^2]. Enumerating all held-out sign outcomes gives RX=((ab-c^2)^2(a^2+b^2+c^2))/[(a^2+b^2)^2-8abc^2+4c^4], versus four-probe BKS risk c^2/2. The cubic H_sigma(z) has H_sigma(0)>0, H_sigma(1)<0 for sigma>2 and H_sigma prime strictly negative since H_sigma double-prime>0 and derivative at 1<0; sigma=2 yields positive H=2(1-z)^2(2-z). High-dimensional non-domination: A=I_n makes BKS exact and XDiag can err when probes coincide, whereas A=vv^T+epsilon I with superincreasing coordinates makes leave-one-out projection converge to rank-one exact while BKS variance remains positive. Independent exact rational sign enumerations matched both risks in four SPD examples.

## originality

PASS

XDiag and BKS estimators, projection and variance motivations come from Epperly, Tropp & Webber and earlier Bekas estimators. Inspected XTrace primary paper (sections 2.4, 4.4) defines leave-one-out XDiag and shows empirical performance but does not derive this 2D all-SPD equal-four-matvec crossover or high-dimensional arbitrarily separated risks. Related Resultary AdaHessian result concerns a different optimizer and stochastic Hessian diagonal RMS. The 2025 dissertation Chapter XVI was additionally inspected: Sections 16.1–16.3 derive the estimators and Sections 16.4–16.5 compare errors in synthetic/application tests; its inspected chapter does not state an exact all-SPD 2x2 risk crossing. Unsearched older specializations remain a risk.

## value

PASS

Exact risk reversal gives a decision boundary for a natural established estimator comparison under matched matrix-vector budget and clarifies that general variance superiority cannot be expected. The two-dimensional case is a mathematically exact diagnostic, not a recommendation over direct coordinate probing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
