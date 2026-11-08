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

PASS. For fixed λ≥0 and c_n=λn^{-4/5}, the exact lens radial boundary is √(1-c_n²sin²θ)−c_n|cosθ| and its area is π+O(n^-4/5). When pair distance exceeds 2−tn^-4/5, both radial deficits are O(n^-4/5) and angular antipodality defect is O(n^-2/5). In scaled coordinates the deficiency is 2λ|cosθ|+u1+u2+z²/4+o(1). Independent integration of the 3-dimensional constraint verified inner volume 16a^{5/2}/15, giving unordered-pair Poisson mean Λ=8/(15π²)∫(t−2λ|cosθ|)_+^{5/2}dθ. For factorial moments, connected v≥3 overlap component probability O(s^{(3v−1)/2}) times n^v = O(n^{(2−v)/5})→0. Thus maximum-distance CDF 1−exp(−Λ) for fixed t≥0. λ=0 coefficient 16/(15π) and λ>0 small t exponent 7/2 follow by exact angular integration. No claim when λ depends on n or about finite-n rates.

## originality

PASS

PASS best of knowledge. Mayer–Molchanov proves the unit-ball extremal diameter law, furnishing the λ=0 endpoint and Poisson method. Appel–Najim–Russo 2002 concerns a fixed sampling region with geometric regularity, while Jammalamadaka–Janson studies fixed spherical sampling distributions. A triangular array of vanishing lenses has critical angular cutoff and non-Weibull crossover not stated or implied by those fixed-body theorems without new uniform analysis. A potentially general U-max-statistics theorem may streamline the Poisson step, which is acknowledged as standard.

## value

PASS

PASS. Maximum interpoint distance is a natural stochastic-geometric observable. This exact n^{-4/5} boundary perturbation interpolates the rotationally degenerate disk Weibull law and fixed-axis lens extremes, yields a new explicit non-Weibull angular mixture, a sharp onset at t=2λ, and changes the lower-tail exponent 5/2 to 7/2. The crossover answers a meaningful double-scaling question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
