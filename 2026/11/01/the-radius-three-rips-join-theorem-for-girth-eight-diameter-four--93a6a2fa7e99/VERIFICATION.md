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

# Reproducible verification

Run `python3 verify.py` and `python3 crosscheck.py` using Python 3.8 or newer, without external dependencies. The exact observed output of both programs, in that order, is bundled as `verification_output.txt`. Successful checks end with `GENERALIZED_QUADRANGLE_RIPS_STRUCTURAL_CHECKS_OK` and `GQ_W2_FULL_CHAIN_CROSSCHECK_OK` respectively.

`verify.py` generates the cycle, the grid incidence graph, and both symplectic generalized quadrangles from first principles, verifies graph distances and exclusions of short cycles, reconstructs all within-side distance-two cliques from neighborhood blocks, and computes exact mod-two cellular ranks. `crosscheck.py` instead generates the small duad–syntheme quadrangle and enumerates every clique and mod-two boundary matrix of its full Vietoris–Rips complex for scales zero through three. The complete scale-three face vector and homology are printed.

These are finite cross-checks. They do not certify the infinite-family theorem independently. The uniform proof uses the absence of four- and six-cycles to obtain a join decomposition, a common simplicial expansion collapsing to the graph, a standard topological join identity, and Adamaszek's published girth-collapse theorem. Integral torsion-freeness follows from the actual homotopy equivalences, not merely the mod-two computations. The programs assume the exact finite-field arithmetic and graph models as implemented; their scope is deliberately limited to the stated finite examples.
