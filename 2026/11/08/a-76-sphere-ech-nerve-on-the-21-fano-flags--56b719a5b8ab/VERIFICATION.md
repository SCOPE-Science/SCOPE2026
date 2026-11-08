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
# Exact finite verification

The file `verify_cech.py` is a standalone Python 3 program using only the standard library. Running it enumerates the Fano flags and their 42 line-graph edges, applies the exact intrinsic graph Čech rule at scale three, and checks face counts in two independent ways. It also enumerates mod-two boundary ranks and verifies two distinct complete acyclic discrete-Morse matchings by topologically sorting all oriented Hasse incidences.

Expected outputs include: 21 vertices, 42 graph edges, 42 six-dimensional Čech facets, 3,395 nonempty faces, 13,755 Hasse incidences, 1,659 matched pairs per order, exactly one critical vertex and 76 critical two-cells, and reduced mod-two Betti number 76 in degree two. Both matching orders have been executed. At scale two it also confirms one critical vertex and eight critical one-cells (and mod-two first Betti rank eight).

The output in `verification_output.json` was produced by the program before packaging, not reverse-engineered from an expected value. If the checker fails on another system, do not treat the claimed result as externally certified.

The finite acyclic matching supplies an integral homotopy proof for this single finite graph. No extension to other graphs or independent external audit is asserted.
