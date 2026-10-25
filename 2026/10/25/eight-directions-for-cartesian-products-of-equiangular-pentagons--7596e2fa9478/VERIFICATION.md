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

The general geometric reduction is an analytic proof: each equiangular pentagon has illumination arcs of angular length \(3\pi/5\), centered at five equally spaced angles. Their maximal common-direction vertex sets are consecutive pairs. A product direction therefore illuminates at most one cyclic \(2\times2\) tile. The five-row counting obstruction proves at least eight tiles are necessary, and an explicit eight-tile cover shows sufficiency. Summed vertex constraints and all 25 equal-weight tiles prove the fractional value.

Run `python3 verify.py` in the directory containing this file. The verifier uses only the Python standard library and exact integer and `Fraction` arithmetic. It checks the row-incidence obstruction, the full eight-tile coverage with stated multiplicities, uniqueness of all 25 maximal incidence sets, and exact total weight \(25/4\).

This test is a reproducible finite certificate for the combinatorial step; it is not an independent external audit and cannot replace the general cone proof or settle historical originality.
