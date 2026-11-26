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

For x>0 the map is mx-floor((2m-1)x/2), with sign preserved; oddness handles x<0. Above 2 the remainder bound contracts the excess by at least a factor 1/2 as long as the orbit stays above 2, and the first branch above 2 maps sufficiently near points below 2. The two strips inside (0,2) outside the core map by expanding the distance from 0 or 2 until core entry. On the closed core, the endpoints of each cell image are between the core endpoints, including the actual value at each even-indexed jump. Even/odd cells have successor intervals starting at r and r+m. Each cell can reach 2m-2 in at most two steps, and this hub can reach 2 by decreasing even indices. From 2 it reaches 1 through m, then the remainder of the left half via smaller even predecessors. The hub reaches its reflected hub via 2m-3, including m=2, and reflection covers the right half. The hub self-loop makes the graph primitive. Because affine inverse branches have constant Jacobian 1/m, uniform within-cell densities give exactly the Markov conditional laws even after specifying a finite past itinerary. Shrinking cylinders make this partition generating. The positive stationary density is equivalent to core Lebesgue; mixing and Birkhoff give uniqueness among ACIPs and physicality, with nonsingular finite entry extending the a.e. statement to the full sign half-line. Entropy is log(m) and the derivative product is m^n off the null set of boundary preimages. The sole incoming edge to cell 1 forces pi_1=pi_2/m. Independent exact interval pushforward and moment integration checked m=2 (variance 1/9); replay: python3 /workspace/branches/independent_checks.py 3. The original verifier was inspected, not executed; neither finite check establishes the universal or a.e. claims.

## originality

PASS

Credit the published remainder-addition model and general theory of expanding piecewise-linear Markov maps. The supported distinction is the concrete all-integer finite-entry core and primitive transition classification, with the resulting nonuniform physical measures. It is not novelty for the seed construction, positive Lyapunov exponent, or the abstract Markov density method. No compared evidence establishes coverage of this conjunction. Same-model full-text retrieval and the strongest related indexed record remained limited as described below.

## value

PASS

The uniform-in-m trapping and communication result resolves whether the linear remainder construction has a single statistical regime and whether its expanding branches yield a uniform physical density. The answer is two sign-separated mixing regimes with strictly nonuniform density and exact rational cell weights. This is useful structure for the published model, not a conclusion about digital randomness, finite precision or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
