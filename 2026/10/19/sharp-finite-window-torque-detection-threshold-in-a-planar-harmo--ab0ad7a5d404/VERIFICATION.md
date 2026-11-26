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

In a positively oriented drift eigenbasis the torque is (λ1−λ2) Z1 Z2. Stationarity gives Sii=Dii/λi and S12=2D12/k in that basis. Independently, the centered product Z1 Z2−S12 is an eigenfunction of the OU generator with eigenvalue −k, so its full stationary covariance is its variance times exp(−k|t|). Gaussian fourth moments give the instantaneous squared mean/variance ratio r/(1+r), where r=S12²/(S11 S22)=α² D12²/(D11 D22). Time averaging multiplies the variance by F(kT); strict positive definiteness bounds r strictly below α², and correlations approaching ±1 realize the supremum in the limit. The integral F(z)=2∫₀¹(1−s)e^(−zs)ds decreases strictly from 1 to 0 and is asymptotic to 2/z, proving the exact strict threshold, nonattainment at equality, and the soft-mode limit. In the Cartesian two-bath example the eigenbasis correlation has absolute value |Tx−Ty|/(Tx+Ty), so the same supremum is approached with one cold bath. The threshold time is an infimum, not an attained least time. The recorded 455 tests and verify.py were inspected, not independently executed; they are finite cross-checks, not the proof. The distinct-eigenvalue assumption excludes zero torque and an undefined ratio.

## originality

PASS

The supported distinction is the exact sharp diffusion-optimized finite-window SNR and its necessary-and-sufficient observation-time boundary for drift torque. The OU and Gaussian moment ingredients, and the ability to calculate a finite-window variance, are not independently claimed as novel. No earlier coverage of the optimized boundary was found in the focused catalogue and source comparison.

## value

PASS

The result gives an exact feasibility limit for resolving a natural stationary mechanical observable even with optimally chosen baths, rather than an asymptotic variance or a calculation at one diffusion matrix. The strict boundary and soft-mode divergence despite unchanged normalized correlation time distinguish a limitation of the signal amplitude from a limitation of temporal averaging. This is a moment-based ratio, not a confidence level, a claim about stochastic angular-velocity noise, or a guarantee for experimentally constrained baths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
