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
# Exact finite checks and proof limits

The attached `verify.py` is a standalone Python 3 program using only its standard library. Run with `python3 verify.py`. It enumerates all simplices from closed graph neighborhoods, tests each asserted elementary collapse by checking the free face has a unique remaining strict coface, constructs the expected residual independently from square boundaries, and checks equality. It also computes mod-two simplicial Betti numbers with exact bitset elimination.

The verified examples are the rectangular \(3\times4\) grid, the four-cycle, a \(C_5\mathbin{\square}P_3\) cylinder, a \(C_5\mathbin{\square}C_5\) torus grid, the three- and four-dimensional hypercubes, and the Petersen graph. The checker also exhaustively enumerates 429 labeled simple graphs with at most five vertices satisfying the triangle and common-neighbor restrictions (including disconnected computational tests). It rejects a \(K_{2,3}\) input as inadmissible.

For the \(5\times5\) torus grid it verifies reduced-mod-two ranks of two in dimension one and 26 in dimension two, alongside connectedness. Its computation does not directly certify the integral cup product, whose nonvanishing instead follows from the established torus CW summand and the standard integral cohomology ring of \(T^2\). No finite test proves the theorem's unbounded graph quantifier: that part depends on the explicit combinatorial collapse and cell-attachment argument in `RESULT.md`.
