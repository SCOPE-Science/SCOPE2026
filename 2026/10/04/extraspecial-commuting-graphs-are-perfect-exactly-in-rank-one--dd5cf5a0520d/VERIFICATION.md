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

For an extraspecial p-group, G/Z(G) is a 2r-dimensional symplectic vector space over F_p and commutation is exactly orthogonality. When r=1, every nonzero vector has orthogonal complement equal to its line, so the noncentral graph is exactly p+1 disjoint cliques of size p(p-1); adjoining the p central universal vertices preserves perfectness. For r>=2, the five displayed vectors in two hyperbolic planes have zero symplectic products exactly on the five cyclic pairs and nonzero products on every chord, including characteristic two, so representatives induce C5. A fresh independent pairing calculation for p=2,3,5,7,11 reproduced the cycle pattern; the package verifier separately checks the rank-one blow-up and the witness for four primes. The symbolic argument, not the finite checks, proves all primes and all ranks.

## originality

PASS

The closest checked structural source identifies the extraspecial commuting relation with symplectic orthogonality and treats the rank-one geometry, while Britnell--Gill's perfect-commuting-graph classification is centered on quasisimple groups and general component restrictions. Neither inspected statement gives the all-extraspecial perfectness boundary or the uniform induced-C5 obstruction in every symplectic rank at least two. Resultary searches found the assigned finding and related extraspecial graph invariants but no earlier equivalent perfectness theorem. Best-of-knowledge originality therefore passes, with a disclosed access risk because an authorized retrieval attempt for the complete Britnell--Gill source was safety-blocked and was not retried.

## value

PASS

Perfectness is a standard structural property of commuting graphs, and extraspecial p-groups form a natural infinite family. The theorem gives a complete sharp rank boundary valid for every prime and both extraspecial types, with an explicit uniform five-vertex obstruction above the boundary. This is a natural classification rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
