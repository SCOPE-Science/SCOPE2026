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
# Reproducibility and finite checks

Run `python3 verify.py` using a current Python 3 standard-library installation. The file reconstructs disconnected induced three-vertex subsets for each graph directly from the rook adjacency relation. Its subset enumeration is exhaustive for the three *specified* small cases only: \((m,n)=(2,3),(3,3),(3,4)\). The reconstructed Alexander duals have mod-two reduced Betti ranks respectively \(1,5,12\) in degree two and zero in all other degrees. Complete enumeration of the coordinate-permutation actions confirms the predicted reduced Lefschetz character for \(12+36+144=192\) group elements. It terminates with `VERIFY_OK` when every assertion holds.

These checks do not establish the theorem for untested parameters. The general proof is the rectangle-facet classification, relative boundary map and surjectivity, followed by integral equivariant Alexander duality. Integral torsion-freeness follows symbolically from the kernel of a homomorphism between free abelian groups and its dual, not merely from the mod-two calculations. No external audit, peer review of this particular claim, or independent validation is asserted.
