---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The marked-box conditional expectation gives the covariance formula exactly: E[O | X1=r]=1_{r odd}+(B-1)(1-b^(N-r))/2 and EO=B(1-a^N)/2; p_Nr>0. For even r the monotone sequence Ba^N-(B-1)b^N falls below 1; for r=1 the relevant h_N starts at -1 then increases before decreasing to 0; odd r>=3 has s_r<0 and s_N→1, with first differences 2(b^(N-r)-a^N) switching sign at most once from + to -, so a unique negative-to-positive transition (possibly one zero) follows. The odd-frequency bracket strictly decreases with odd r at fixed B,N. Fixed-r compact density expansion is uniform O_r(B^-1); the limiting simple root yields lambda_r B+O_r(1). Independently enumerated allocations B=4,5, N=2..6 (40 direct exact covariance comparisons) and rational sign checks. This finite check is not the all-B,N proof.

## originality

PASS

Best-knowledge novelty is the complete parity-dependent finite-size sign classification, discrete single switch, and O_r(1) threshold localization, not the elementary multinomial moment identity. Published occupancy-count covariance mechanisms overlap the method, but the located original texts do not imply the sign theorem without new monotonicity analysis. The Resultary one-switch theorem has richness K rather than odd-load count O; this changes the sign geometry. Priority remains bounded, not universal.

## value

PASS

A natural Hamming-weight observable of the nonlazy hypercube walk is compared with the historical coordinate-r frequency count. The exact checkerboard sign phase diagram, unique density threshold and finite error localization are useful structural dependence information, not merely a moment tabulation; the unexpected contrast with richness-frequency dependence motivates the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
