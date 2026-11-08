---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed clique dichotomy: intervals of k successive edges versus exactly k exceptional triangles [a,a+k,a+2k]. Independently exhaustive clique enumeration for k=2,3,4 yields respectively 26,75,196 faces, precisely interval-core faces plus 2,3,4 exceptional triangles. The interval core is a good circular-arc nerve homotopy S1 and its radial map sends the embedded C_{3k} once around; each exceptional triangular boundary has degree +1, giving primitive relative differential (1,...,1):Z^k->Z. Relative long exact sequence gives free H2 kernel, H1=0 and wedge after first disk kills pi1. Rotation cyclically permutes triangle orientations, reflections reverse sign; the quotient target is sign, so integral representation follows, rather than only rational character. Finite tests not used for all k.

## originality

PASS

Adamaszek Corollary 6.7 and the later Nerve Complexes Theorem 8.2 cover nonequivariant wedge of k-1 S2. Nerve Complexes Proposition 7.2 provides a dihedral module for N(n,k) on n arcs, but Theorem 8.5 maps clique N(n+k,k) to a nerve on n vertices and is not equivariant under the original full 3k-vertex dihedral action. The coincidence of some rational trace formulas must not be confused with an isomorphism of the exact integral D_{3k} module; no prior theorem with this original group action was found in inspected statements.

## value

PASS

At the first winding 1/3 singularity, a circle-like Rips complex gains precisely k two-cells. An exact integral module and reflection-sign control distinguish equivariant behavior invisible in known nonequivariant wedge ranks; natural unbounded k family and fixed-submodule ranks have independent use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
