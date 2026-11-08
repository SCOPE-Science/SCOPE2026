---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Reconstructed plane-partition facet criterion: extreme matchings (0,0),(n,n) and diagonal (j,j) exhibit every proper face of chosen n+1 vertices while no matching contains all; this is an induced simplex boundary. Original published sequential x/y toggle matching has exactly one unmatched face tau={y,z_1,...,z_(n-1)}, and matched pairs cannot cross the specified induced core; hence the complete relative acyclic matching gives ordinary simplicial collapse K searrow L. Though this collapse order is not equivariant, the inclusion is equivariant and an integral homology isomorphism. Rotation swaps x,y and reverses z sequence, inducing permutation sign (-1)^(1+floor((n-1)/2))=(-1)^(n(n+1)/2); rational transfer yields mod-four invariant homology. Independently reconstructed facets, face counts and toggle matching for n=2,3,4: 1347,17487,206127 faces; explicit relative acyclicity topological sorting for n=2,3, with n=4 only complete pairing verified. Infinite acyclicity uses published general toggle lemma.

## originality

PASS

Published Bayer–Jelić Milutinović–Vega theorem establishes only the nonequivariant sphere homotopy type and supplies the exact matching tools. The new result is not claiming the sphere alone: it specifies a geometrically half-turn invariant induced spine, actual collapse onto it, the integral homology action and rational quotient mod-four dichotomy. Full closest primary text inspected; no explicit equivariant character found. A subtle risk is that a later paper or an implicit corollary of the original proof already records the character.

## value

PASS

A canonical invariant minimal sphere core and a parity-dependent rotation representation answer a natural equivariant refinement that the known nonequivariant sphere result cannot determine; quotient rational homology alternates in mod-four classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
