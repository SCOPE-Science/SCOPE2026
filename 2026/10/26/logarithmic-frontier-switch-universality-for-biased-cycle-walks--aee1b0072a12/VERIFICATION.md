---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

From the actual RESULT.md proof: at a discovery with m visited arc sites and current frontier at right, gambler ruin gives a_m=r^m/S_m for switching right→left; for current left it gives b_m=1/S_m to switch left→right, with S_m=∑_{j=0}^m r^j and r=(1−p)/p after reflection p≥1/2. At r=1 both equal 1/(m+1), so uniform U_m realizes independent Bernoulli switch indicators exactly, including m=n−1 interpreted by entry side. For mθ≤1, S_m≥(m+1)e^(−mθ) and 1−r^j≤jθ give b_m−1/(m+1)≤eθ/2 and 1/(m+1)−a_m≤eθ; summing stagewise mismatches through M=min(n−1,floor θ^(−1)) gives ≤e. For m>M, a_m=(1−r)r^m/(1−r^(m+1))≤(1−r)r^m/(1−e^(−1)); its sum is ≤1/(1−e^(−1)), while binary switches alternate so total tail switches ≤1+2N_(R→L). Hence E|K−∑B_m|≤e+1+2/(1−e^(−1))<7 for all n≥3 and 0<p<1. Independent B_m have harmonic mean and variance log ℓ+O(1), and Lindeberg plus L1 approximation gives triangular-array CLT for ℓ=min(n,θ^(−1))→∞. For fixed θ>0, summable right→left transitions yield finitely many switches almost surely under common-chain coupling. Independent raw-step propagation for n=3..7, p=1/3,1/2,3/4 (700 steps each) matched exact two-state probabilities with maximal coefficient difference ≤6.7×10^(−16), residual non-absorption ≤1.1×10^(−31); separate early-mismatch calculations at θ=10^(−6),.001,.01,.03,.1,.4 satisfied the analytic e bound. These bounded checks are corroborative only. All quantifiers, centering, first/final discovery conventions, cutoff θ=0 and fixed-drift boundary are accounted for.

## originality

PASS

The predecessor Idnani–Salem (2026), Theorems 3.4 and 4.1, gives the exact interval-expansion process and two-state gambler-ruin transition law, and so implicitly determines all finite laws, but its analyzed target is the last-covered vertex. It neither states a law for the number of changes between expansion sides nor an all-bias absolute-L1 independent-Bernoulli comparison and effective drift-scale Gaussian limit. A fresh statement-level comparison of primary full text, relevant classical record literature, independent two-walk lead-change literature and published Resultary search hits did not find a result implying this uniform coupling/critical crossover. Familiar permutation-cycle Bernoulli factors are an algebraic law analogy, not a theorem about frontier switches. Originality is a narrow best-of-knowledge assessment, with prior transition machinery fully credited.

## value

PASS

A walk’s alternation between opposite exploration frontiers indexed by newly discovered sites is a natural coverage statistic not characterized by its last vertex alone or by ordinary time-indexed record counts. The nonasymptotic drift-uniform L1 transfer to a harmonic Bernoulli array yields the effective exploration scale min(n,1/|log odds|), an exact symmetric generating function, a Gaussian crossover across all bias-decay triangular arrays, and a fixed-bias finite-switch regime. This reveals a meaningful stochastic phase boundary and gives a reusable quantitative approximation, not an arbitrary special case or mere finite computation. Its contribution is bounded by the known underlying Markov chain and does not claim optimal constant or cover-time law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
