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

The repaired result preserves the exact rate-sweep theorem. The stationary position is the contracting active convolution plus independent isotropic Gaussian noise; the cross fourth moments cancel against twice the squared second moment, and the pure Gaussian bracket vanishes. In trap units the mode index m=q−p makes the active generator triangular in polynomial degree; the two-state block has determinant (p+q+m²)(p+q+m²+2r)+m²u²>0. Independent exact replay /workspace/branches/31cc3a24-589f-46c7-af4f-7c267601e938/moment_certificate.py reconstructs both moments and verifies the rational cumulant, the specialization of the broader formula and the witness 55/1446336; the supplied script was inspected but not run. For r≤1/4 the numerator P is strictly positive; for r>1/4 it changes sign across a unique positive root in x=u². That root diverges at both ends of r∈(1/4,∞) (asymptotic 7r² at infinity), so it has an attained minimum x_c. Strict P_rr>0 on r≥0 and positivity at the two r boundaries yield exactly one double root at onset and two simple roots above. The discriminant at x=64 and negative witness at x=81 enclose the onset rigorously; only the printed decimal tangency location is numerical. Rescaling r=1/4+c/u² gives the simple limiting root c=455/64 by the implicit function theorem, and scaling r=yu gives the nonzero simple root of 28y³−4y at y=1/√7. Root signs and the two-root count select the respective branches. No conclusions about density modality follow.

## originality

PASS

Pass on the narrowed claim in /workspace/repairs/1/RESULT.md. The exact radial cumulant and fixed-rate quarter-boundary are covered by a distinct indexed general rotational-diffusivity theorem. The repaired claim expressly credits this and retains the sharp finite onset and complete switching-rate sweep at fixed angular speed, with two moving-boundary asymptotics. Those conclusions require analyzing a quartic in r and two nonuniform asymptotic scales; they are not the other record's quadratic-in-W classification or its pointwise high-speed law at fixed r. Publication order and independent origin are not inferred from the index dates.

## value

PASS

At matched relaxation scales a finite onset separates robust all-negative behavior from a genuine bounded positive interval as switching becomes faster. Classifying both thresholds and their different high-speed regimes gives useful predictions not supplied by a fixed-rate limit or one numerical witness. The exact moment formula alone is not counted as new value, and no density-transition or unmatched-timescale claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
