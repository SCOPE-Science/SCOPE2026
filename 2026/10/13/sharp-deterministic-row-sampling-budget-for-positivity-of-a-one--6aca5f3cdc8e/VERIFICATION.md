---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Let w=P_Jv/a and write A=cI+δT with T symmetric and ||T||≤1. The scalar is c+(δ/a)wᵀTv, so the radius is at most δ/a. For a<1 a Householder reflection with normal v−w sends v to w; using it or its negative attains both endpoints and gives both eigenvalues μ and L in the corresponding A. If a=1, w=v and a reflection fixing v while negating an orthogonal unit vector gives the same conclusion for n≥2. Convexity gives all intermediate values. The top-s squared mass is at least s/n by averaging the ordered squares and is pointwise optimal; the flat unit vector makes every s-subset attain s/n and the adversary can then choose the required endpoint matrix for the selected subset. Hence the minimax radius is δ√(n/s), and strict uniform positivity is exactly c−δ√(n/s)>0. Equality gives a zero witness; beyond it a negative endpoint persists under small perturbations making the top subset unique. At s=n the interval is [μ,L]. In the printed four-dimensional witness zᵀv=−1/2 and (Av)₁=−1/4, so the quotient is −1/2.

## originality

PASS

Sketched Ritz extraction, the possibility of out-of-range or negative values, and the top-one Q-DEIM convention are prior. The strongest analogous catalog intervals control either an embedding on the two-vector image space or a full-rank sketch of a restricted rank-one SPD family with access to both Krylov vectors. Neither provides the exact minimax sampled-mass law or uniform strict positivity budget for the frozen v-only model, whose extremum includes rank-deficient sketches on the two-vector space. The supported distinction is the fully sharp uniform row-budget result, not the underlying quotient or generic bilinear norm inequality.

## value

PASS

A positive very small projected problem can fail solely because of row truncation even when the chosen rows maximize trial-vector energy. The result turns this known qualitative symptom into an exact design boundary: it distinguishes strictly guaranteed positivity, attainable zero, and actual negative values, and shows that no other v-only deterministic selector can buy uniform positivity with fewer rows. At fixed condition number the bound specifies the requisite fraction of coordinates, information not provided by a demonstration of one spurious value or by empirical oversampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
