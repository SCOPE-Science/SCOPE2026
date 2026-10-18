---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Checked Sun Proposition3.2 double-integral ground-state identity with C_{n,alpha}/2 and h=||x||^{-(n-alpha)/2}; for unequal ultrametric shells k,l the kernel integral factors exactly as (1-p^-n)^2 p^{-(n+alpha)|k-l|/2}. Summing orientations cancels 1/2 and same-shell differences vanish for radial v; Hardy mass per shell equals (1-p^-n)|a_k|². With r=p^{-(n+alpha)/2}, D_m(a)=sum_k |a_{k+m}-a_k|², r D1<=sum_m r^m D_m, while D_m<=m² D1 by telescoping. The Dirichlet path first eigenvalue with 2N+1 interior sites is lambda_N=4sin²(pi/(4N+4)), attained by displayed sine shell profile, and sum m²r^m=r(1+r)/(1-r)^3; gives both constant factors and sharp asymptotic N^-2. No nonradial or exact multiplicative constant claimed.

## originality

PASS

Sun’s sharp p-adic Hardy theorem gives the whole-space ground-state representation and hard-cutoff approximating sequence with O(1/N) normalized gap, but no optimal spectral-scale lower bound for arbitrary radial profiles on finite annuli. Reduction to an all-pairs shell Dirichlet form plus sharp path Poincaré and matching sine test adds the missing N^-2 spectral order; no stronger published radial annular estimate was located.

## value

PASS

The sharp Hardy weight has no attained ground state, and quantitative annular coercivity is a natural model for concentration/minimizing sequences. Showing smooth radial profiles achieve the optimal quadratic width decay as opposed to the known hard truncation O(1/N) supplies meaningful new spectral stability information; exact coefficient is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
