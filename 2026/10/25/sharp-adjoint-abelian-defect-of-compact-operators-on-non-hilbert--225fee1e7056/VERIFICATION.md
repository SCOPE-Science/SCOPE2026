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

PASS: Compact T on infinite ℓ_p satisfies Te_n→0 and T'e_n'→0 for remote coordinates, while J_p(a u+b e_n)=a^(p−1)J_p(u)+b^(p−1)e_n' on disjoint unit supports. Therefore δ_p(T)≥a||Tu||−a^(p−1)||T||, uniformly after ε→0; maximizing a−a^(p−1) gives c_p=(p−2)/(p−1)*(p−1)^(-1/(p−2)). Rank-one coordinate projection exactly yields t−t^(p−1), sharp over all compact T. Independently checked p=4 coefficient 2/(3√3), optimizer 1/√3, and endpoint limits. Uses infinite-dimensional compactness essentially; finite checks alone cannot prove this.

## originality

PASS

PASS, qualified best-of-knowledge: Qualitative exact-solution classification only proves δ(T)>0 for each nonzero compact T, not the UNIFORM sharp bound δ(T)≥c_p||T|| or the rank-one attainment. The disjoint-coordinate weak-null/compactness argument is the substantive improvement. Residual risks: An older quantitative stability theorem for approximate duality intertwiners under a different name could give the coefficient, though none was identified.; No assertion for 1<p<2 or general Lp; complex scalar homogeneity convention requires care.

## value

PASS

PASS: The prior qualitative absence of nonzero compact adjoint-abelian operators is strengthened to the best possible stable norm gap with an elementary attaining rank-one map. This sharp ideal-wide coefficient is a meaningful perturbative invariant on non-Hilbert Banach sequence spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
