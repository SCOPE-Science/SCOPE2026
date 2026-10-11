---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The proof is correct. Pairwise disjoint test segments have distinct endpoints, giving the global upper bound \(\sqrt2\) times the Hilbert norm, and a sign-changing vector on one edge attains it. A proper three-edge coloring partitions all tree edges into matchings, so the norm squared dominates one third of the full edge energy. The weighted two-variable inequality with weight \(1/\sqrt2\) gives the energy lower coefficient \(3-2\sqrt2\) at every nonroot vertex, with a larger root coefficient. For a finite path segment, every nonzero variation consumes a distinct support endpoint, while branch-off edges give one disjoint unit variation at every support node, proving the exact square-root segment norm.

## originality

PASS

Best-of-knowledge originality passes with an explicit same-paper access limitation. The source comparison recorded in the package is to a coarser Hilbert estimate and a one-sided segment bound; the current Resultary search returned no prior finding with the three-edge improvement, sharp upper constant, or exact segment identity. The nearby Resultary record concerns the final Argyros--Motakis norm rather than the preliminary \(N_1\) norm.

## value

PASS

The preliminary norm is explicitly motivated as the natural first dyadic-tree James-variation attempt. The theorem materially sharpens its Hilbert comparison, determines the optimal upper constant, and makes the source's branching failure exact on segment indicators. That combination is a useful quantitative diagnosis of why the construction is discarded, not an arbitrary constant tweak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
