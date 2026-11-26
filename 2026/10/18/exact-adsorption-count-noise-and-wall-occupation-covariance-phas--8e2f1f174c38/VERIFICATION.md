---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At fixed positive rates and v,x₀>0, the decaying solution of the two-velocity backward equations with the incoming boundary condition gives φ₀(z)=exp[−(x₀/v)√(z(z+2α))]. Conditioning on the first Poisson reset gives (1−φᵣ(z))/z=(1−p)/(z+rp), p=φ₀(r+z); evaluation and differentiation at zero reproduce the stated mean m and variance s². Both bulk resets and independent exponential wall desorption return to (x₀,−1); bulk clocks are stopped while bound. With centered excursion and residence times U,V, the centered cycle rewards are (−(U+V),mV−bU)/(m+b), giving the stated covariance per unit time by independence. The actual covariance limit, not just a distributional CLT, is justified: a reset followed by direct leftward traversal gives a uniform positive chance of hitting in a fixed time block, so the first delay and ordinary cycles have exponential tails. Ordinary cycles also have duration at least x₀/v. Stopping the centered-reward martingale at the first cycle end after t gives its covariance as the expected number of sampled cycles times the one-cycle covariance. The overshoot reward and centering error are bounded in L² by the initial delay and the maximum of O(t) exponentially-tailed cycles, hence are o(√t) in L². Dividing by t yields the displayed covariance and the mean-rate/Fano normalization. The cross term has its unique zero at m/s²; the Fano sign is that of s²−m²−2mb. The ratio rβ′/(1−e⁻ᵝ) is a product of two strictly increasing positive factors and goes from 1/2 to infinity, giving precisely one resetting crossover. The weak-reset asymptotics m∼K r⁻¹ᐟ² and s²∼K r⁻³ᐟ², K=(x₀/v)√(2α), give the two claimed constants after t→∞ at fixed r. The frozen simulation script was inspected, not executed; finite simulations are corroborative only.

## originality

PASS

The supported distinct result is the combined model-specific sign diagram, with a unique r crossover and two ordered desorption thresholds with different weak-reset constants. Count/occupation fluctuation methods and first-passage inputs are prior; in particular Akimoto's accessible full text already encodes mixed count/occupation moments. No priority is assigned to that general fluctuation framework.

## value

PASS

The sign diagram answers when increased wall occupation is positively correlated with counts even though the count process is quieter than Poisson. The unique reset crossover specifies exactly when the Fano transition disappears, and the different weak-reset constants quantify a robust separation of the two boundaries. Those distinctions add information beyond a stationary mean or a generic fluctuation identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
