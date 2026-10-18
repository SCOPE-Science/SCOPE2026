---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For every finite simple graph (including isolates), prime-power q and integer t>=1, derive the common-centralizer linear equations u_v*b_w-u_w*b_v=0 independently for every edge. For support S of nonzero F_q^t vertex vectors, each vertex outside N[S] is unconstrained; inside G[S] a connected component contributes exactly one centralizer-kernel dimension if its nonzero vectors are projectively constant, and zero otherwise (a nonproportional edge forces zero propagating through the component). The number of projective directions is P=(q^t-1)/(q-1). Thus for each S the component factor P+(P^|C|-P)T yields q^{tm}(q-1)^|S| T^{|N[S]|-c(S)} times the product. At T=1 total q^{t(n+m)}, also including empty graph, t=1, q=2. The maximum codimension t=1 is n-c(G); for t>=2 it is n-i(G), attained by two nonproportional vectors within each edge-containing component, and this gives center-cutting. Independently reconstructed 4-vertex path/star over F2,t=2 by direct finite-field row elimination: path coefficients 64,384,3648,3840,8448 at ranks 0..4; star 64,4032,0,1536,10752, each summing to 2^14. The unrestricted proof is componentwise linear algebra, not finite extrapolation. Graphical-group orbit sizes rely specifically on the standard integral graphical group commutator equations, not arbitrary groups.

## originality

PASS

Best-of-knowledge originality after independent statement/implication comparison, published-record semantic search and relevant primary material inspection. The known premises and residual risks below are credited, not silently treated as novel.

## value

PASS

The complete common-centralizer codimension distribution of ordered t-tuples is a natural refinement of Rossmann's one-element conjugacy-class polynomial. It distinguishes graph shape even at fixed n,m (binary four-vertex path versus star), measures the first tuple length that cuts to the center, and gives every simultaneous conjugacy-orbit-size multiplicity in a canonical graph-derived nilpotent family. These are structural finite-field enumerations, neither a renamed one-element count nor an isolated tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
