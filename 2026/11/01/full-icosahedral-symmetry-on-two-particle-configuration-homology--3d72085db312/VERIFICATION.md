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

# Reproducible finite checks

Execute `python3 verify_icosahedron.py` with Python 3; no third-party packages, external data or network access are required. The program reconstructs the combinatorial icosahedral graph, cellular chains, full automorphism group, exact integral cycles, binary ranks and rational character decompositions. Its recorded standard output is `verify_icosahedron_output.txt`. The computation checks 120 complete automorphisms against all 100 independent facial product cycles. The proof of the rational rank uses both the certified mod-two boundary rank and 100 independent integer zero-boundary vectors, not a numerical extrapolation. The application of stable equivalence rests on the graph's nontrivial cycles having length at least three.

The calculation does not establish an integral first-homology torsion classification, a Smith-normal-form description of the integral first-homology quotient, or an integral decomposition of the group representations. No independent validation has yet been performed.
