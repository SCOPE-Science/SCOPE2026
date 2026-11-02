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

# Reproduction and proof boundary

Run `python3 verify.py` (Python standard library only). Its output is

`VERIFY_OK all_connected_labelled_triangle_free_orders_2_to_6=3801 larger_samples=3 all_coefficients_matched=True`

The program enumerates all connected labelled triangle-free graphs on 2 through 6 vertices and independently counts maximal independent sets of the corresponding central graphs by the Bron--Kerbosch algorithm applied to the complement. The 3 larger graphs are \(C_8\), \(K_{4,4}\), and \(C_{10}\). All integer polynomial coefficients match the closed formula. At input order two the checker tests the general polynomial description only; the stated optimum formula is explicitly restricted to input order at least three.

The infinite result uses a three-type proof, not interpolation or extrapolation from these finite tests. No formal proof-assistant certification or independent audit has been performed.
