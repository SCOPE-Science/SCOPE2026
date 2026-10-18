---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Inspected frozen RESULT.md SHA c1ab9d6f70439b7dda1eda2f37dc44065fa38039 and code verify.py SHA cdb127e9b209bc1713cfa87e849091648f7d739f. Unit-edge tetrahedron with face normals n_i·n_j=−1/3 has projected area A(u)=√3/8 Σ|u·n_i|, perimeter P(u)=Σ_{i<j}1_{(u·n_i)(u·n_j)<0}√(1−(u·e_ij)^2) over six silhouette edges. Splitting the sphere into sign sectors and integrating polar angle yields E[AP]=4√3/(3π)+(2/π)∫₀^atan√2(1+sin²t)/√(2+sin²t)dt. Algebraic decomposition gives the stated 2E−F incomplete elliptic combination; E A=√3/4, E P=3 atan√2. The source certificate uses exact Fraction interval arithmetic, enclosing sqrt2,sqrt3,π,θ and the n≤14 binomial expansion with bounded alternating remainder ≤5/3^16, so -0.0004<cov<-0.0003 independent of float rounding. Separately recomputed high-precision quadrature and mpmath elliptic functions: E[AP]=1.24063482223759045867… and cov=-0.00035786769230333175…, consistent with the rational certificate. Numerical calculation alone does not prove the exact sign; the inspected exact interval construction does.

## originality

PASS

Finch’s 2012 primary full article directly covers the SAME numeric mixed moment and qualitative negative correlation, but states that its closed form was unknown. The added closed incomplete-elliptic identity and rational strict sign proof are nontrivial exact results beyond the earlier numerical benchmark. Resultary failure is not novelty evidence; an equivalent older stochastic-geometric integral remains possible.

## value

PASS

The joint area×perimeter moment of a natural regular solid shadow is a central two-intrinsic-volume covariance; Finch explicitly identified the exact form as an unsolved calculation. A closed special-function evaluation and rigorous anticorrelation interval are precise, reusable geometric constants rather than arbitrary tiny measurements. No whole joint law is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
