---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The dual Lipschitz polytope has dimension n-1; a feasible f is extreme exactly when its saturated-edge incidence vectors span rank n-1, equivalent to a connected tight graph. Every such graph has edge height differences 1 or 2, hence integer heights after normalization, and range 1 or 2 by diameter. Range-one words require all n-1 adjacent pairs to alternate, giving exactly two. Range-two words contain both 0 and 2, never adjacent; all 0-to-2 pairs give a connected tight complete bipartite core. Each height-one vertex must attach via an adjacent extremal symbol, equivalently interior 1-runs of length <=2 and endpoint runs <=1; this is both necessary and sufficient. Unique maximal colored 0/2 blocks, internal 1-runs marked z+z^2 and optional endpoint 1s give the all-color GF (1+z)^2 2R/(1-2RS) with R=z/(1-z); subtract two monochrome classes (1+z)^2 2R/(1-RS). The difference simplifies to the stated rational H and adds 2z^2/(1-z). A(z)=1-z-2z²-2z³ has a unique smallest-modulus simple zero rho>0 by positivity and aperiodicity, with B(rho)=rho²+rho³>0. Therefore F_n~C rho^-n with lambda=1/rho and C=-2rho^3(1+rho)^3/(rho A’(rho)B(rho)). Boundary n=2,3 and polarity are explicitly accounted for.

## originality

PASS

Best-of-knowledge originality for the all-length cap-two path facet generating function and exponential growth base, not for the general tight-edge criterion. Direct full-text comparisons locate no dominating result: generic, tree-like, complete bipartite/multipartite and disjoint-short-pair theorems have rigorously different hypotheses. Unindexed exact formulas and fuller inspection of broad sources remain explicit priority risks.

## value

PASS

The exact number of facets of a Lipschitz-free unit ball is a natural Banach/polyhedral invariant, and the integer-cap-two path is the first simple nontree truncation of the ordinary path metric (already n=4 fails the four-point test). The word-classification proof exposes a structural mechanism for the new extremal patterns, yields a complete exact all-length invariant rather than a tiny numerical sample, and proves the growth base changes from 2 (ordinary path) to 2.269530842...; the result is motivated and potentially reusable for weighted/truncated metric-polytope calculations. Its value does not depend on novelty searches or code reproducibility alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
