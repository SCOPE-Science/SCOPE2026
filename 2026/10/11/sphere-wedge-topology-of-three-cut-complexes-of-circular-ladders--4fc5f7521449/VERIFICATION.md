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

The accompanying `VERIFY.py` uses only Python standard-library modules and can be run with `python VERIFY.py`.

For each \(5\le n\le9\), the script reconstructs \(C_n\mathbin{\square}K_2\), all connected induced triples, all eligible four-sets, and both integer simplicial boundaries of the Alexander dual. It verifies precisely \(6n\) dual triangles and \(n\) tetrahedra, the \(2n\) ring-chord uniqueness conditions, and a determinant of absolute value one for every local square block. It independently computes the two boundary ranks over three finite fields and the resulting rational Betti count. Observed pairs \((\operatorname{rank}\partial_2,\operatorname{rank}\partial_3)\) are \((25,5)\), \((30,6)\), \((35,7)\), \((40,8)\), and \((45,9)\), ending with `VERIFY_OK`.

These finite computations are not a certificate for infinitely many parameters. The proof for all \(n\ge5\) depends instead on the combinatorial face classification, unique-chord rows, block-unit determinant, and integral Alexander duality. The script checks those finite instances but does not mechanically certify the general proof or its literature originality. Independent audit has not been performed.
