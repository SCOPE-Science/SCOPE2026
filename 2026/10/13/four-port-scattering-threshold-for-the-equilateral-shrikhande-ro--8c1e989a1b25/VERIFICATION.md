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

# Reproducibility

`verify.py` is a standalone Python 3 standard-library script. Run `python3 verify.py` from the directory containing the extracted files. It rebuilds the two graphs on \(\mathbb Z_4^2\) from explicit adjacency rules and checks:

- Degree 6, symmetry, and the strongly regular identity \(A^2=4I+2J\) for both adjacency matrices.
- Exhaustive isomorphism-canonical support of all 1-, 2- and 3-vertex induced subgraphs; unique noncommon four-clique support on 4 vertices, with exact count 8 in the rook graph and 0 in the Shrikhande graph.
- Rational inversion of \(3I-A\) and equality of all entries with the exact rank-one resolvent formula.
- Representative on-shell scattering unitarity for \(k\ell=\pi/3\).

The analytic proof in `RESULT.md` establishes the result for *all* nonexceptional positive energies. The checker alone does not prove the universal energy assertion, spectral singular energies, or the absence of equivalent published work. No independent audit has been performed.
