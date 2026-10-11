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
The arbitrary-\(n\) proof is given in `RESULT.md`.

Critical checks:
- the line-stochastic affine dimension is \((n-1)^3\);
- the plane-stochastic affine dimension is \(n^3-3n+2\);
- the coordinate hyperplanes are the source facet family in the stated range;
- independent index permutations act transitively and orthogonally on coordinates;
- projector trace therefore gives \(\|\Pi_Te_{ijk}\|^2=\dim(T)/n^3\);
- the uniform entries are \(1/n\) for line stochasticity and \(1/n^2\) for plane stochasticity;
- total tensor sums are \(n^2\) and \(n\), respectively;
- summing all coordinate clearance inequalities gives the sharp global radius bound;
- equality forces all coordinates equal and hence proves center uniqueness.

`verify.py` constructs the two equality matrices for \(n=3,4\), selects exact independent constraint rows, computes the corresponding rational orthogonal projectors, verifies the source ranks and constant projector diagonals, and checks the two radius identities. Finite computation is corroborative only and does not assess originality.
