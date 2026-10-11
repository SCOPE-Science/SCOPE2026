---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Affine normalization and character restriction reduce every dimension to the 27-point local cube with multiplicity \(3^{d-3}\). The finite local claim is exact: every four evaluation rows have rank at least three, so any zero set of size at least four contains a rank-three triple determining the coefficient hyperplane. Exhaustive exact Eisenstein arithmetic over all triples shows that every such admissible hyperplane has intersection size three or five, while explicit nonzero coefficient vectors realize zero counts zero, one, two, three, and five. A fresh independent Eisenstein-arithmetic replay in this audit reproduced 216 rank-three triples with three-point intersections and 648 with five-point intersections among all-nonzero cofactor vectors.

## originality

PASS

The closest Kronecker-Fourier work gives global Hamming-number/rank-deficiency bounds, and Bonami-Ghobber treat different finite Abelian families and uncertainty minima. Neither inspected source determines the complete fixed affine-simplex spectrum on \(\mathbb F_3^3\), the forbidden 23-cell, or the exact local hyperplane-section set. Resultary searches surfaced related sparse-Fourier classifications but no dominating ternary-simplex theorem.

## value

PASS

An affine 3-simplex is the canonical four-point full-rank support in ternary vector spaces. The exact spectrum and forbidden cell give a complete sharp uncertainty slice with a nontrivial finite-geometric obstruction, making this a natural exact invariant rather than an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
