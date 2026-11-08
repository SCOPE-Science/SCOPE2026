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

Poissonize coupon draws into independent rate r_(n,i)=1+θ_(n,i)/logn clocks summing exactly n. Their initial first-arrival rare points shifted by logn have intensity κe^(−s), while interarrival gaps exceeding L_n=logn+c form independent asymptotic Poisson births at s≥c of intensity κe^(−c), with unit-exponential residual lifetimes. Bounded θ, convergent κ and rare per-type marks make triangular rare-event limits work on compact intervals; the superposition arrival clock and a vanishing near-threshold gap bound transfer J1 limits to fixed M_n draws. The limit at c is Pois λ and afterwards stationary immigration–death. Its first zero is continuous at almost every limiting integer-valued jump path; before c the CDF is exp(−κe^(−s)), after c it is the stationary-start chain hitting CDF. The standard zero resolvent yields Laplace e^(−λ)/(q∫₀¹ y^(q−1)e^(−λ(1−y))dy) and E H_c=c−E1(λ)+Ei(λ)−γ−logλ. Independent generator calculations verified hitting-time recurrences for λ=0.2,1,2.4; no finite simulation can certify functional convergence.

## originality

PASS

Earlier exact uniform sliding-window missing-count/hitting dynamics and critical one-time flux are explicit antecedents. Long 2026 treats uniform critical one-time mass and stationary flux, Attrill–Garoni treat a different clumsy-update queue. Current new component is the complete functional and hitting law for bounded near-uniform triangular probabilities with relative perturbations 1/logn and universal κ=avg e^(−θ), showing strict Jensen heterogeneity penalty. General marked Poisson extreme process theorems could subsume the proof machinery, and unlocated scan-statistics results pose priority risk, but no inspected direct dominance.

## value

PASS

The perturbation order 1/logn is a natural sensitivity threshold at which vanishing sampling distortions create order-one changes to rare missing-coupon intensities. Universal profile compression to κ and complete critical-window first-completion laws supply substantive finite-lifetime coverage information beyond a single mean or a trivial asymptotic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
