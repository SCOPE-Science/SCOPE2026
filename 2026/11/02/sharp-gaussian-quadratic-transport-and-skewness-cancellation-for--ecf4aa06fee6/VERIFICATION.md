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

At a fixed strictly positive transition matrix the ordered centered pair/triple moments are pqρ^(j−i) and pq(q−p)ρ^(k−i). Counting repetitions and distinct triples and summing their geometric series gives v_n=nσ∞²+O(1) and κ_3(S_n)=nκ_3,∞+O(1) with the stated constants. To check the uniform inversion step, P diag(1,e^{iu}) has spectral radius <1 for 0<|u|≤π: equality would force an eigenvector of constant modulus and the same aligned phase in both rows, hence a constant eigenvector and e^{iu}=1. The near-zero spectral projection is analytic; after exact centering and variance normalization its cubic normalized term has coefficient γ/(6√n) with γ=κ_3,∞/σ∞³. For |u|≤n^(-2/5), Taylor expansion to increasing fixed order and the Gaussian majorant give arbitrary polynomial absolute errors in Fourier inversion; the intermediate arc is bounded by exp(−c n^(1/5)) and the compact outer arc decays exponentially. Summing the local expansion over at most n+1 physical lattice points preserves arbitrary polynomial accuracy by choosing the order high enough. Euler–Maclaurin adds the +h_n φ(x)/2 CDF term, where h_n=v_n^(-1/2), and remaining terms are Gaussian times polynomials. On |x|≤√(20 log n) the density is at least a constant times n^(-10); Taylor inversion thus gives the uniform displayed quantile error O(n^(-1)polylog n). Integrating each shifted cell gives the width term h_n²/12 and squared shift γ²(1−x²)²/(36n); the endpoint and density replacement errors total o(1/n) (each O(n^(-2)polylog n) over O(√(n log n)) cells). Chernoff bounds and uniform fourth moments for the two monotone-coupled marginals make omitted costs o(1/n) by Cauchy–Schwarz. The resulting limit is 1/(12σ∞²)+γ²/18. The sole interior root of 1+4ρ+ρ² is −2+√3, and positivity of both diagonals then gives the stated open p interval. The saved check at p=.3 and the cancellation root gives 0.687247322 at n=3500 versus 0.687321749; this is recorded evidence only. The supporting program and saved output were inspected, not executed.

## originality

PASS

The exact standardized quadratic transport coefficient for fixed, strictly positive dependent binary chains is distinct on the inspected evidence. Earlier sources cover Markov-binomial cumulant and approximation machinery, a nonlattice version of the skewness cost, optimal-order weak-dependence bounds, and an independent-factor representation in one parameter regime. Those do not by themselves supply the exact lattice transport coefficient with the stated cancellation. No priority claim is made for lattice Edgeworth theory, the general transport rate, the Bernoulli representation or the independent-binomial case.

## value

PASS

An exact W2 coefficient gives a quantitative benchmark unobtainable from an order estimate for the canonical one-dimensional dependent lattice count. It distinguishes a positive lattice floor from the contribution of long-run asymmetry and shows how dependence can remove the latter without symmetrizing the marginal. The worthwhile invariant is the sharp transport cost for the family and its separation of effects, not the geometric-series computation in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
