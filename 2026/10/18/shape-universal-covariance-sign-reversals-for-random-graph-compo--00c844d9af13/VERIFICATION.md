---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For disjoint vertex sets of sizes h and k, two specified connected-component events share exactly hk required absent cross-edges, so P(A_S and B_T)=P(A_S)P(B_T)(1-p)^(-hk). Intersecting vertex sets cannot both be distinct components. Summing over disjoint sets gives E(C_H*C_K)=mu_H*mu_K[(n-h)_k/(n)_k](1-p)^(-hk), hence exact covariance and rank-one cross-size block, with a unique positive sign-switch p*. The negative log of 1-p* is the rectangular average of log((n-a-b)/(n-a-b-1)); strictly increasing summands establish threshold ordering whenever both size pairs feasible. Taylor expansion yields p*=1/n+(h+k-2)/(2*n*n)+O(n^-3). At p=1/n+lambda/n^2, tree-leading means E[X_j]=n*tau_j(1)+O(1) and bracket=hk(lambda-(h+k-2)/2)/n^2+O(n^-3), giving the finite critical-window covariance. Domain h!=k, h+k<=n, 0<p<1, fixed h,k for asymptotics. Independent exact-Fraction enumeration of labeled G(n,p), n=4,5,6 and 3 rational p values checked mixed factorial moments; enumeration is not the universal proof.

## originality

PASS

Best-of-knowledge statement-and-implication originality check after current primary reading and published-Resultary search. Equivalent forms, broader theorems, exact tables, and prior implication are assessed separately; residual risks are not hidden. A known tree-census asymptotic leading covariance (Pittel 1990) covers the order-n regime away from criticality. Since the critical p=1/n+lambda/n^2 cancellation requires one further expansion, the finite p sign hierarchy and O(1) critical constants are not shown to be a direct corollary of the accessible abstract; full-text uncertainty recorded.

## value

PASS

Different connected-component types in random graphs interact even though edge indicators are independent. The complete finite-p shape-universal rank-one covariance block and strictly size-ordered sign changes give an exact dependence classification; nonzero n^-2 crossover offsets at criticality are informative for sharp finite-size fluctuation calculations. Exact factorial moments alone are familiar, but the assembled transition/eigenstructure of the cross-size block is a motivated, nontrivial mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
