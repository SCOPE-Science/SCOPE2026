---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The preimage of each consecutive index interval under the physical clock gives the stated half-open stage endpoints: proportional T_(m+1)=bT_m+1, square-root T_(m+1)=4T_m²+1, with T_0=0 and T_1=1. On each such stage the value is y_m. Integral comparison yields W_m∼C q^m with q=b^(1−gamma) under proportional subcritical weights. For the square-root clock u_m=log T_m=c2^m+O(1) with c>0 (iterate u_(m+1)=2u_m+log 4+O(T_m^−2) and bound the remaining rescaled tail), giving q=2^(1−gamma) under the subcritical logarithmic weights. The raw square-root weights instead satisfy W_m/(sum of prior W_j)→∞. In the geometric case the last j-th stage has limiting mass (q−1)q^(−j−1), with the remote tail uniformly small; grouping by phase gives v_r^(q). A partial new stage moves along an affine segment toward its y_m and all fractions up to the normalized stage-end fraction are sampled in the limit because individual jumps vanish. With raw square-root weights the limiting endpoints are the phase point masses. Subsequence extraction of phase and partial mass also excludes extraneous limits. The finite-q vertices are an invertible cyclic linear transform of distinct delta masses, with barycenter mu_*; this gives the p=1, p=2 and p≥3 conclusions. For the critical cases the integral and discrete errors give W_m=log b+O(b^−m) and W_m=log 2+O(2^−m), respectively, absorbing initial omitted stages into the summable errors. Against c_0 times the undelayed sum on completed stages, the signed mass imbalance on every measurable set is bounded by the total absolute stage errors plus the uniformly bounded partial mass; the total mass is c_0k+O(1). Dividing, including the normalization difference, proves O(1/k) TV uniformly over arbitrary orbits. Since k(N) tends to infinity and hits every sufficiently large stage, both limit-set inclusions follow. The bounded replay `python3 /workspace/review-evidence/independent_finite_checks.py 3` independently checks direct scalar index iteration through 40805 and sample critical weights, not the infinite-time estimates.

## originality

PASS

The supportable distinct contribution is the explicit subcritical occupation-limit geometry across both clocks and the quantitative orbit-independent critical comparison. Stage recurrences and a qualitative discrepancy of averages are prior, and the critical proof is an application of summable reweighting, not a new general summability method. A related record mentions an unidentified homogeneous occupation result, so priority for isolated cases, particularly raw proportional-delay sampling, is not established; no available matched statement gives the weighted spectra and critical TV comparison.

## value

PASS

The identified clocks assign long and very unequal physical durations to known base-orbit states, so an endpoint average does not answer the physical-time occupation question. Exact limit polygons, including the effect of incomplete stages, show how strongly the clock changes the allowed statistical laws and why the undelayed barycenter can be excluded. A fixed critical weight provably removes this distortion with a uniform rate and preserves every subsequential occupation limit without assuming periodicity or a unique limiting law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
