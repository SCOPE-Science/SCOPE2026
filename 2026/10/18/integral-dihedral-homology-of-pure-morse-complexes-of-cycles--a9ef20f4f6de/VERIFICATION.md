---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For all n>=5, published Chari–Joswig Thm4.1 gives underlying wedge S²∨2S^{n-2}. The proof itself constructs boundaries of alternating incidence n-vertex sets E/O; all facets in their supports are disjoint with coefficients ±1, so these two cycles form a primitive integer top homology basis, and rotation shifts E/O as n-cycle with sign (-1)^(n-1). Reflection exchanges these two cycles up to adjustable sign. On nontrivial generator rotation there are no fixed nonempty simplices, giving reduced Lefschetz -1; top trace -2(-1)^(n-2)=-2 in alternating Euler sum, so H2 trace +1. For reflection, the invariant edge-pairs Q_j allow pure-face fixed strata of precisely two contractible simplices, each of positive size for n>=5, yielding reduced Lefschetz +1. Top trace0 forces H2 reflection sign +1. Since r,s generate D_n, H2 is trivially acted on. Independently enumerated all pure facets and fixed traces for n=5..9, with n² facets; these finite tests corroborate but do not prove all-n lemma.

## originality

PASS

Best-of-knowledge original only for the precise additional integral/equivariant/multiplicative result; explicit known portions carved out. Two targeted indexed semantic searches plus specified primary comparisons do not show a stronger implying theorem; absence of hits is not a proof of novelty. See each named mathematical implication check and named residual risks.

## value

PASS

The pure discrete-Morse complex of a cycle has a classical nonequivariant wedge decomposition; the exact integral dihedral action on the free homology lattices is a natural finer invariant. Reflection and parity-dependent rotation signs alter rational quotient Betti degrees, information invisible in ordinary homology ranks. This is a motivated structural symmetry refinement rather than a rebranding of the wedge theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
