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

The supplied `verify_neighborhood_cycle_products.py` uses no external package. It constructs Cartesian-product adjacency, enumerates each common-open-neighbor simplex independently of the predicted model, and checks a stated sequence of 23,920 elementary face-coface collapses, individually confirming uniqueness of each free coface. For every \(4\le m\le7\) and \(5\le n\le8\) it checks the remaining simplices against the exact proposed row-boundary, cross-edge, and fan-triangle core. It verifies that the crown-graph cross-edge relation is connected and independently computes the homology over \(\mathbb F_2\) from the original simplicial boundary matrices. The observed ranks equal the claimed integral wedge homology reduced modulo two in all sixteen cases.

To replay from this package, place `verify_neighborhood_cycle_products.py` in an ordinary directory and run `python3 verify_neighborhood_cycle_products.py`. Expected terminal prefix: `VERIFY_OK complexes=16 elementary_collapses=23920`.

Finite computations do not prove a statement for arbitrary parameters and cannot detect all possible integral torsion; the explicit cell cancellation proof is the basis of the integral homotopy theorem. The verification supplies a reproducible independent finite stress test, not an independent scientific audit.
