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

# Verification

Run `python verify.py` with Python 3 and SymPy 1.14. All entries in the degree-one through degree-four coefficient matrices of the Jacobian map are computed exactly in \(\mathbb Q[t]\), then separated by parity and reduced to Smith normal form. The printed nonunit invariant factors are asserted against the supplied complete factor list, including zero-diagonal multiplicities; because Smith row and column transformations are unimodular over \(\mathbb Q[t]\), they preserve rank under every complex parameter specialization. The code also checks two explicit Jacobian relations, all four line-restriction discriminants, and conic passage through the square vertices. The independent geometry argument counts every singularity by pairwise component intersections and Bézout. No numerical sampling is substituted for the parameter-uniform rank proof.

For the generic fiber, the relation spaces in degrees \(1,2,3,4\) have dimensions \(0,0,0,4\). For \(t=8\), they have dimensions \(0,0,3,8\). For \(t=16\), they have dimensions \(0,1,3,8\). These dimensions and the geometry establish the claimed minimal Jacobian degree and Tjurina values; the published near-free criterion is an external mathematical theorem, not proved by the checker.

The calculation is over characteristic zero. It does not address the reducible quadratic at \(t=0\), arbitrary conic deformations, or the exhaustion of the world literature.
