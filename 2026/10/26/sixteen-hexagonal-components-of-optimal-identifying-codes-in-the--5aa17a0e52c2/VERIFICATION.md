---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification instructions

The graph is defined directly from six offsets in \(\mathbb Z_4^2\), with vertex index \(4a+b\). No external Python modules are required. Execute `python3 verify_exhaustive.py` and `python3 verify_structural.py` from this package directory. They must terminate without assertion errors and print `CHECK_EXHAUSTIVE_OK` and `CHECK_STRUCTURAL_OK`, respectively; recorded outputs are included only as replay references, not as a replacement for the source code.

The first program computes closed-neighborhood signatures for all \(4368\) five-subsets, checks all sixteen parameter families and constructs every exchange edge by symmetric difference; it independently checks the cospectral rook-graph minimum-cardinality contrast. The second program instead uses sixteen closed-neighborhood and 120 pairwise-difference hitting constraints, checks all \(1820\) four-subsets and \(4368\) five-subsets, and verifies all \(16\) six-code components and their edges. In particular, the assertion that the union of templates equals every valid five-subset is an exhaustive equality check, not a small-case sample.

The result is confined to this explicitly defined sixteen-vertex graph. No computational evidence purports to establish novelty or independently validate mathematics outside this finite domain.
