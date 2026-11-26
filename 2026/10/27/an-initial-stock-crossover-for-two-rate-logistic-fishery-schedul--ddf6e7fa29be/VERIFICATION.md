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

For each r,K>0, h>ell>=0, u,v>0 and X0>0, I recomposed the constant-rate logistic flow and its catch a log(1+x J_a). The HL and LH terminal denominators are 1+mz and 1+nz, with n-m=(H-L)pq>0. Writing s=1-L, the catch difference divided by K is d A-L B, with B>0 and sign A=sign(z-s). For L>0 the derivative ratio A'/B' is (1+mz)(2z+nz^2-s)/(d(1+pz)(1+qz)); both positive factors increase for z>max(0,s), since 2+qs>0. Averaging against dB, including the mass B(s) with zero slope when s>0, gives strict increase of A/B on that domain. Its initial limit is 0 for s>=0 or (L-1)/d for s<0, below L/d; its limit at infinity is infinite. At z=1 the two log arguments 1+m+Hpq and 1+m have weighted mean 1+n, with strictly positive weights d/H and L/H; strict log concavity places the crossing above 1. For L=0 the factorization itself gives equality exactly at 1. Integral J_a covers a=1 without division by zero. Thus the comparison is global in positive initial stock, with no restrictions on rates relative to r. Replay: RESULT.md lines 41–98 supply the analytic identities. Independently integrating x'=x(1-a-x), c'=ax by classical RK4 with 2048 uniform steps per block and bisecting z in [1,2] reproduced the numerical example, z_crit about 1.018264393667 and delta at z=.6 about -0.099326033822. The frozen script was read, not executed; that illustrative check is not the proof.

## originality

PASS

The supported distinct contribution is the all-parameter prescribed finite-horizon catch-order crossover, especially for two strictly positive efforts and its sharp location relative to K, together with the contrasting terminal ordering. Neither the population law nor the elementary zero-low-effort comparison is credited as a new method or model.

## value

PASS

The exact order criterion addresses a natural comparison when the two efforts and durations are fixed. It proves that below carrying capacity the later high-effort block increases catch but leaves less stock, and that two positive efforts postpone the unique reversal beyond carrying capacity. That is actionable mathematical information about two distinct objectives in the model, not a general policy recommendation or a statement about sustainable yield.

The dated certificate retains the supplied scientific assessment, sources and limitations.
