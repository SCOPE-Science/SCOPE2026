---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the real unweighted relative l1 projection problem on Z=ker incidence for K_r join independent_s, r>=2,s>=1. Signed edge permutations make symmetry averaging norm-nonincreasing even for unrestricted projections; the cut/cycle real representation overlap is a single W_r, giving precisely one free equivariant correction parameter. The explicit pseudoinverse L^+ acts by 1/(r+s) on clique contrasts and 1/r on independent contrasts; its two absolute column-sum functions F_A and F_X are convex. The crossing on [-s/r,1] for s<=3 and the cross-column cusp at -s/r for s>=4 yield respectively 3-6/(r+s)+6s(r-4)(s-1)/[r(r+s)(6s+(r-1)(4-s))] and 3(r-1)/r. Independently built the oriented incidence matrices and grounded Laplacian inverses, then the full P_t in SymPy rationals; verified P_t^2=P_t and exact optimal column norm for r,s=(2,1),(2,4),(3,2),(4,3),(5,4),(6,5), covering small symmetric-group boundaries. Infinite-family minimality follows from the symmetry/representation and convexity proof, not this finite grid.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical claim, not novelty of standard premises or algorithms: Graph-cycle spaces and transportation spaces are related by finite-dimensional duality; the present minimization is over all projections onto the cycle kernel in the full l1 edge space, unlike coordinate-basis projection constants. Checked relevant primary statements and Resultary semantic results. Failed searches alone are not novelty proof; risks explicitly retained.

## value

PASS

The actual minimum relative projection constant is a natural Banach-space invariant of graph cycle subspaces, and a four-independent-vertex saturation threshold is a structurally unexpected exact result. Explicit formulas show canonical Euclidean-orthogonal projection generally fails to minimize l1 norm. This determines all r,s for a prominent symmetric graph family, not an arbitrary sampled graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
