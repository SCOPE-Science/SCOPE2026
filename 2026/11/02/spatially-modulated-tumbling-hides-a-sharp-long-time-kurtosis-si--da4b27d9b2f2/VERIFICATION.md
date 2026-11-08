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

For periodic λ(x)=a±b on equal half-cells (a>|b|≥0), constant speed ±v and unwrapped coordinate, the tilted generator is sv(∂+k)+λ(f_{−s}−f_s). Monodromy across the two half-periods uses traceless B_λ(θ)=[[θ+λ,−λ],[λ,−θ−λ]]/v, B²=θ(θ+2λ)I/v². Periodicity gives half-trace F(θ)=cosh(kL), with the exact cosh/sinhc product, and Taylor coefficients F'(0)=L²a/v² and F''(0)/2=L²(4L²a²−L²b²+12v²)/(24v⁴). Analytic implicit inversion yields ψ(k)=v² k²/(2a)+[−v⁴/(8a³)+L²b²v²/(96a³)]k⁴+O(k⁶), so ψ''(0)=v²/a, ψ''''(0)=−3v⁴/a³+L²b²v²/(4a³). Therefore sign switches exactly at L|b|=2√3v, under admissibility a>|b|. The excess-kurtosis leading t^{-1} coefficient follows after normalization and only unwrapped cumulants are claimed. Independently expanded transfer matrix with SymPy for all symbolic parameters and matched both cumulants. Markov phase compactness/positive switches supplies local analytic eigenbranch; no finite-time sign claim.

## originality

PASS

Best-of-knowledge originality PASS for the precise stated claim, not a priority certificate. Equivalent formulations include the tilted-Floquet principal eigenvalue, periodic telegraph-equation monodromy and fourth derivative of the scaled cumulant generating function. Generic deformed generators can in principle compute all cumulants but do not state the equal-zone two-rate sign threshold. Monthus 2021 studies generic space-dependent velocities/switching rates and deformed generators on the infinite line *with a localized steady state*, then perturbation to low cumulants. Our periodic symmetric reversal rates have no localized steady state on the infinite line and the specific fourth derivative, unchanged diffusivity and sign boundary are not in the inspected paper. Singh–Sabhapandit–Kundu 2020 study inhomogeneous nonperiodic asymmetric reversal with survival/exit observables. Angelani–Garra 2019 concerns space-dependent speed; its inaccessible full text remains a residual comparison risk. Principal residual risk: An unindexed periodic telegraph equation/Floquet higher-cumulant theorem might explicitly contain this sign transition.

## value

PASS

Holding the diffusive variance growth fixed while reversing the sign of the leading non-Gaussian fourth-cumulant correction by changing spatial reversal contrast is a sharp physically meaningful transport distinction. The precise L|b| threshold and feasible parameter region characterize an observable stochastic-phase transition, not a routine diffusion coefficient calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
