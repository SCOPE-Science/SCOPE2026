---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For p>0 the independent geometric block renewal/reward law gives v(p)=p²Σ_{n≥1}a_n(1-p)^{n-1}, a_n=E(Z_n), |a_n|≤n. In a nearest-neighbor walk of length ≤4r, each site is departed at most 2r times; mean-balanced laws with vanishing odd centered moments up to 2r−1 agree with their reflected laws on all such path weights. Reflection reverses displacement, giving a_1=...=a_{4r}=0. At time 4r+1 the sole possible degree-(2r+1) dependence on the site law requires exactly 2r returns to the starting site, each a two-step excursion to ±1. The terminal drift factor yields T=E[2Y_0(C+Y_0D)^{2r}], with C=(1-ω_1+ω_{−1})/2 and D=1-ω_1−ω_{−1}. Antisymmetric odd D powers cancel because the two outer-site laws have equal moments through order 2r; lower odd moments of Y_0 vanish. The sole surviving term is 2 m_{2r+1} E[(Y_1+Y_2)^{2r}], strictly nonzero. Uniform ellipticity and Jensen plus Solomon speed criterion give v(0)=0, while Eω=1/2 gives v(1)=0. Moment determinacy on a compact interval shows that non-reflection-invariance entails a first nonzero odd moment; monotonicity with equal endpoints forces v identically zero and hence reflection symmetry. Independently re-enumerated all ±1 paths through steps five and nine using exact rationals; confirmed zero lower a_n and coefficients 9/2048 and 306144/30517578125 for skewness and fifth-moment cases. Finite tests supplement the all-rank proof.

## originality

PASS

Martin and Nagel, arXiv:2610.11919 (Oct 8 2026), introduce the identical complete geometric-refresh model; their Theorem 2.1 proves speed continuity, smoothness and first low-order derivative consequences, plus nonmonotone examples with nonzero one-step mean. Their proof §3.1 supplies exactly the renewal power series, a necessary antecedent. But the inspected published main theorems and proof do not identify the first nonzero odd site moment at order 4r, do not show the exact universal positive even-moment factor, or classify every mean-balanced law by reflection symmetry. Classical Solomon and cooling results provide different inputs. The all-order triangular identity and iff classification survive as new best-of-knowledge structure; an implicit all-derivatives consequence of the regeneration series remains a residual priority risk.

## value

PASS

The theorem completely characterizes a striking stochastic phenomenon: directional ballistic motion emerges under partial refresh despite zero mean local bias and zero velocities at both extreme refresh rates. It supplies an exact nonmonotonicity classification and a sharp hierarchy tying the first observable speed term to the first odd central moment of the site law. This is useful for models of temporal environmental disorder and is not a routine moment expansion at one chosen law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
