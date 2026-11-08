---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For count chain on Δ_{k,m}, fixed k>=2,a,b>0,a+b<=1, coordinate reflecting one-agent birth-death generator Q has stationary geometric π_j∝(a/b)^{j-1} and simple first nonzero rate gamma=a+b-2sqrt(ab)cos(pi/k), first normalized eigenvector ψ_j∝(b/a)^((j-1)/2)[sin(jπ/k)-sqrt(b/a)sin((j-1)π/k)] with nonzero endpoints. Independent-coordinate Poissonized chain at s=log m/(2gamma)+c has one-agent density 1+m^-1/2 e^-gamma c ψ(i)ψ(j)+o(m^-1/2), and homogeneous endpoint product log-likelihood has LAN Gaussian shift amplitude |ψ(i)|e^-gamma c, yielding exact 2Φ(amplitude/2)-1 TV. The product likelihood is count-measurable so passing to occupancy states does not diminish this homogeneous TV. Universal chi-square product bound controls arbitrary initial configuration late, endpoints give early lower. Exact spectral tensor comparison of discrete (1-L/m)^t versus continuous e^-Lt/m, splitting fixed H modes, high H≤m and L>m, establishes equality of limits and O(m) cutoff window at t=m log m/(2gamma). Substituting a=(1-α-β)(1-β),b=(1-α-β)β,m=(1-α-β)n cancels α in leading n log m center. Independently computed tridiagonal eigenvalues for k=2,3,5 under symmetric/asymmetric rates, errors <1e-14; finite simulations do not replace the all-m limit.

## originality

PASS

Alistarh–Chatterjee–Karrabi–Lazarsfeld 2023/2024 introduce exact IGT count model, multinomial equilibrium, O(m log m) bound and discuss cutoff constants as future problem, not Gaussian endpoint profile. Chen–Kumagai (2017/2018) establish general product-chain cutoff criteria and continuous/discrete comparison, so generic cutoff principle is covered; the exact reflecting k-level gap, fixed-window Gaussian law for endpoint counts, and α cancellation are model-specific. Relevant Ehrenfest 2012 full text unavailable via open routes and authorized VPN.

## value

PASS

Provides the sharp mixing horizon and profile for a population-protocol strategy-learning model, replacing only coarse order bounds; the leading cancellation of unconditional cooperators and endpoint profile have quantitative value. Does not claim novelty of general product-chain cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
