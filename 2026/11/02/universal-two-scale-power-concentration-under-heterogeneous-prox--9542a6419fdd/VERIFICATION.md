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

When the root is NO only direct leaf YES ballots count; when it is YES only direct NO ballots oppose it. Root monotonicity makes the two failure events disjoint. A counterfactually direct leaf needs exactly h_m−1 other YES ballots; conditioning on the root's two possible votes gives the two point probabilities, including when p_j=1 and at both threshold parities. B_m>0: a direct ballot replaced by a delegation can only enlarge the root's switching interval, compared with the no-delegation case which has positive pivotality. The sum's variance is (m−∑p_j²)/4 with ∑p_j²≤S_m, so the bounded triangular-array CLT gives 2Φ(s)−1 for S_m/√m bounded and convergent. Both tails vanish by Hoeffding for S_m/√m→∞. For the leaf masses, both targets lie S_m/2+O(1) above the omit-j means, uniformly in j. If S_m≤m^{3/5}, all but O(S_m+1) Bernoulli parameters stay bounded away from the lattice-degenerate endpoints. The tilt making the target the exact mean is O((S_m+1)/m), its tilted variance is m/4+O(S_m+1), and the exponent is −S_m²/(2m) with error O((S_m+1)/m+(S_m+1)³/m²)=o(1) uniformly. Fourier inversion on |θ|≤m^{−2/5} gives the Gaussian local prefactor √(2/(πm)), since the cumulant remainder is O(m|θ|³); on the complementary part of [−π,π] the many nondegenerate Bernoulli factors give exp(−c m sin²(θ/2)). Summing the relative-error estimate gives √(2/π) exp(−Δ_m/2)(1+o(1)). For S_m>m^{3/5}, a uniform Hoeffding bound controls the whole leaf sum by m exp(−c m^{1/5}). These estimates give all three regimes, including a diverging leaf sum for Δ_m→−∞ when the root power might not approach one.

## originality

PASS

The distinct result is the two-scale asymptotic theorem under arbitrary leaf-by-leaf delegation propensities, particularly the universal normalization window and constant. The frozen text correctly credits pivotality definitions, finite computation and the homogeneous-star special case rather than asserting those as new. The strongest inspected matches cover different asymptotic observables or a narrower finite model.

## value

PASS

The random-star model isolates the difference between a proxy being almost surely pivotal and holding almost all of the normalized power. The aggregate of many individually small leaf pivotalities produces a second scale with a nontrivial sharp profile. Uniformity under arbitrary heterogeneity (including deterministic delegation on some leaves) identifies when only total propensity matters asymptotically, a useful result beyond a finite index evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
