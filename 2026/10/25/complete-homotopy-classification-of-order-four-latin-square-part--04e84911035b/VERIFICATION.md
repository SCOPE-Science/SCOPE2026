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

# Computational and topological verification

The complete finite input consists of the sixteen cell labels \(4r+c\), the cyclic addition rule \(r+c\pmod4\), and the two-bit xor rule \(r\mathbin{\mathrm{xor}}c\). The executable `verify.py` accepts no numerical approximations. It reconstructs faces from all cardinality-bounded cell combinations and independently from a monotone recursive backtracking search; the resulting face sets must be identical. The file `certificate.json` contains all triangle-orientation signs, all thirty-two ordered elementary-collapse pairs, and the exact isotopy permutations for all four reduced order-four Latin squares.

For the cyclic table, actual execution established face counts \((1,16,48,32,0)\) by cardinality (including the empty face), forty-eight edges each in two triangles, sixteen vertex links each a connected six-cycle, a connected complex, and a consistent orientation across all thirty-two triangles. Therefore the complex is a closed connected orientable surface with Euler characteristic zero, so the surface-classification theorem gives the torus, not merely torus-like Betti numbers.

For the Klein table, actual execution established face counts \((1,16,48,32,8)\); each of the thirty-two recorded pairs is present at its step, is a codimension-one inclusion, and has no competing immediate coface. After those sixty-four face deletions, the complex is exactly a connected graph of sixteen vertices and twenty-four edges, giving nine circle factors. The verifier checks remaining downward closure and graph connectivity. Enumeration of reduced squares yields exactly four, with three explicitly isotopic to the cyclic table and one to the Klein table. The total number of full transversals is respectively zero and eight.

The `make_cert.py` script regenerates the certificate algorithmically from the stated finite definitions; `verify.py` checks the saved certificate, and was executed successfully, returning `VERIFY_OK`. The proof's only noncomputational inputs are the elementary-collapse theorem for free faces, connected-graph spanning-tree reduction, and classification of compact connected orientable surfaces. The assertion is limited to order-four Latin squares and carries no independent-audit claim.
