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

The factorization T_Re_n=n^-R v_n with v_n=(sqrt(w_j)n^-s_j) gives H_R=T_R*T_R and m-dimensional zeta Gram G_R=Σn^-2R v_nv_n*, with finite trace since s_j>0,R>=1. Strictly increasing distinct s_j imply independence of v_1,..,v_k by the Chebyshev/exponential-polynomial zero lemma, so Δ_k>0 and rank=m. Exterior-power compound expansion into positive u_Iu_I* terms has unique minimum index product k! for I={1,..,k}, with squared leading wedge norm Δ_k; all other tuple products >=(k-1)!(k+1). The tail is summable using Σn^-2 and bounded v_n, giving norm asymptotic Δ_k/(k!)^(2R)[1+O((k/(k+1))^(2R))]. Divide consecutive top k eigenvalue products to get λ_k=(Δ_k/Δ_{k-1})k^-2R[1+O((k/(k+1))^(2R))]. Thus eigenvalue hierarchy, simplicity and optimal compact rank-r norm error follow. Independently checked exact rational Δ1=14, Δ2=133/64, Δ3=1/324 for the provided three-vector diagnostic; finite identities are corroboration only.

## originality

PASS

Best-of-knowledge PASS for translated-atomic fixed-k eigenvalue asymptotics with exact universal bases. General Helson moment representation/finite-rank theory supplies the operator model but no inspected theorem gives the k^-2R asymptotic and Gram-minor ratios. Generic separated rank-one perturbation principles remain a named residual risk.

## value

PASS

The complete fixed-rank eigenvalue separation hierarchy for a natural translated positive Helson moment family, including determinant prefactors and universal integer decay bases, provides exact best finite-rank approximation errors not contained in mere trace/finite-rank criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
