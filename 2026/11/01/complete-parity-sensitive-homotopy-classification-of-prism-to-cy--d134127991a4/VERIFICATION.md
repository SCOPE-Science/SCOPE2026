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

For q!=4 every oriented edge has a unique ±1 increment. Every prism square has zero signed circulation (absolute <=4 and even; no nonzero multiple of q>=5 or q3), so both rim windings coincide, integral w with qw≡n mod2 and |qw|<=n. For strict winding, a directed cycle would have length |qwm|<n|m|<=length (or zero horizontal winding), contradiction; thus induced orientation is acyclic. Differences of two equal-winding signed cocycles are an integral exact 1-cochain; a height lattice with pointwise minima and legal source-vertex ±2 recoloring is connected. Even-target parity at a vertex splits components; odd targets do not. The inspected primary Fujii et al. Theorem 5.1 maps acyclic orientation components to S1; extreme all-horizontal-sign cases yield precisely 4q isolated vertices. For q=4 twin-vertex folding reduces target to K2 and gives two components for even n. Independently enumerated Hom vertex colorings and 1-skeleton recoloring components for n=3..7, q=3..8, matching all counts and isolated cases, not the circle homotopy (which relies on primary theorem).

## originality

PASS

Best-of-knowledge novelty based on actual same-object / different-object implication comparisons and targeted Resultary and primary literature searches. No decisive prior coverage found; named missing-text and unindexed-source risks remain.

## value

PASS

The family of prism-to-cycle Hom complexes is a natural two-parameter graph-topological testing ground. A complete parity- and winding-sensitive circle/isolated-point classification for all targets (including triangle and folded square exceptions) refines the known universal component criterion and a prior pentagon-only special case in a nonroutine way.

The dated certificate retains the supplied scientific assessment, sources and limitations.
