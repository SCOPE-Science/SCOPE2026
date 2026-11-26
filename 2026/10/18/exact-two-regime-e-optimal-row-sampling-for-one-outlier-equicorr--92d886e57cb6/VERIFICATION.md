---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Pythagorean identity gives the exact conditional progress eigenvalue; boundary weights give zero while interior weights give positive progress. For the reciprocal objective F=λ_max(Σ_i v_i v_iᵀ/p_i) with v_i the columns of U⁻¹, the top-eigenspace subgradient at an interior minimizer is represented by a PSD trace-one Z. The Lagrange multiplier is F(p*) after summing the stationarity equations against p_i*, so v_iᵀZv_i=F(p*)p_i*²>0. Testing with this Z and using strict Cauchy–Schwarz in Σ_i(v_iᵀZv_i)/p_i proves unrestricted uniqueness, hence exchangeability. For ordinary weights (1−p)/m the transverse mode is t(1−p), t=(1−c)/m, and the core block has diagonal p,a(1−p) and off-diagonal r√(p(1−p)). The discriminant quadratic Q=Ap²+Bp+C satisfies 4AC−B²=16r²(a−r²)>0, giving strict concavity of the lower core root. Substitution at p_s=(a+r)/(1+a+2r) gives λ_s=(a−r²)/(1+a+2r) as the lower root (the two shifted diagonal entries are positive), with zero derivative. There the core minus transverse gap is Θ/[m(1+a+2r)]. If positive, the increasing core crosses the decreasing transverse line first; the determinant at t(1−p) is (1−p)[(c−r²)p−ct(1−p)], yielding the displayed crossing and its value. At Θ=0 both branches coincide. Uniformity follows because p_s>1/(m+1), while p_c equals that value iff r=c, which is in the crossing branch. In the singular family the core branch applies; mΛ_unif tends to the smaller root (2+α−√(α²+4β²))/2, below the transverse limit 1. Rationalizing yields the stated ratio and its divergence across families with β²=α+1/2.

## originality

PASS

The supported distinct contribution at the frozen publication date is the full E-optimal two-regime classification, in particular the transverse/core crossing regime and its boundary. The SDP and the inverse-positive slice (including the singular example after row sign switching) are covered and are not separately credited. A later documented catalogue publication gives an exact matching classification; this overlap is acknowledged without a claim about authorship or historical dependence.

## value

PASS

The complete branch boundary is a meaningful exact benchmark for choosing fixed sampling among correlated equations with one outlier. It tells when a simple core design stops controlling worst-direction progress and when the transverse cluster mode determines the optimum, with global rather than assumed-symmetric uniqueness. This value does not depend on claiming the sign-switch-covered asymptotic example as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
