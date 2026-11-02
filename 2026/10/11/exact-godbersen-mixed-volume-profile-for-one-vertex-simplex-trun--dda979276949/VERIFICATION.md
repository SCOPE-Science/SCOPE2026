---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The full statement is independently reconstructed. For z=x-r y, coordinate slack w_i>=0 gives P<=1, N<=r and t-r<=sum z_i<=1-rt exactly; choosing total slack u in the intersection proves sufficiency. On 0<r<t, negative orthant has zero volume, positive orthant contributes [(1-rt)^n-(t-r)^n]/n!, and each mixed-sign j-positive orthant has simplex-slice densities and a one-dimensional beta integral. Its degree-m coefficient is, for j>=n-m, (-1)^s*C(n,j)/((j-s)!(m)!)*(t^m-t^(n-m)) with s=j-(n-m), and the s=0 orthant term C(n,n-m)/(m!(n-m)!)*(1-t^(n-m)). The alternating binomial partial sum equals -C(n-1,m-1); c_m=C(n,m)^2/n!*[1-(m/n)t^m-((n-m)/n)t^(n-m)]. Minkowski polynomial uniqueness gives the all-r mixed volume coefficient. c_0=c_n=(1-t^n)/n!, consistent with Vol(K_t). Dividing by C(n,m)Vol(K_t) gives G>0 as t^m,t^(n-m)>t^n; central simplification and small-t order follow directly. Independent ConvexHull computations of 64 full K_t-rK_t volumes in n=2..5 and 4 truncations by 4 scale values agree to max relative error 3.88e-15. These finite tests are corroboration only, not an all-n proof.

## originality

PASS

Best-of-knowledge originality for the exact coefficient-by-coefficient truncation profile, not for the universal Godbersen bound or the simplex equality case. The full parameter family K_t, with all n,m and t, is not a formal consequence of a qualitative sharp bound and uniqueness of extremizers: inequalities do not recover a polynomial. Relevant primary statements and their geometrical scope were compared; a potentially unindexed older frustum mixed-volume formula remains a material residual risk.

## value

PASS

A complete exact family of natural mixed-volume coefficients is a mathematically motivated quantitative benchmark at the sharp simplex extremizer of Godbersen. The family is canonical one-vertex parallel truncation, with all n and all interior indices covered; the central even-dimensional t^h/(1+t^h) exhibits arbitrarily high directional flattening, not a chosen unmotivated scalar. A researcher studying quantitative rigidity near simplices could use the precise order and coefficients. The theorem neither claims a universal stability exponent nor large generalization; its value is the full exact profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
