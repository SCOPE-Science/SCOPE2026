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
The embedded `verify_degree_eigenvector_boundary.py` performs an exact replay using only the Python standard library and the embedded connected Graph Atlas table.

For each graph it:
1. computes degree maximizing vertices directly;
2. computes the adjacency characteristic polynomial exactly by Newton identities;
3. isolates the Perron root by rational Sturm sequences;
4. uses principal characteristic cofactors to compare eigenvector coordinates exactly;
5. retains only graphs for which both maximizing sets are singletons and the leaders differ.

The diagonal adjugate identity gives
\[
\det(\lambda I-A_{-i})
=
\frac{p'(\lambda)}{\lVert x\rVert^2}x_i^2,
\]
so the exact cofactor comparison has the same ordering as the Perron eigenvector coordinates.

The replay verifies:
- connected unlabeled counts \(1,2,6,21,112,853\) for graph orders \(2,\ldots,7\);
- conflict-class counts \(0,0,0,0,0,5\);
- all five seven-vertex representatives;
- their degree and eigenvector leaders;
- automorphism orders \(12,2,2,4,2\);
- orbit sizes \(420,2520,2520,1260,2520\);
- total labeled first-conflict count \(9240\).

Run:

`python3 verify_degree_eigenvector_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite input table is a compact connected subset of the standard Read--Wilson Graph Atlas through seven vertices.
