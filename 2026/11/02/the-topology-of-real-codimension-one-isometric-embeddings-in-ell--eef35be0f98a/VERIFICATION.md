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

# Verification notes

## Reproducible finite checks

Running `python3 check_graph.py` with the Python 3 standard library enumerates all signed-injection vertices and blank-row swap edges for \(2\le n\le6\). It explicitly checks graph connectedness by breadth-first search, regularity, both counting formulas, and the resulting cycle-rank formula. Observed \((V,E,\beta_1)\) values are \((4,4,1)\), \((24,48,25)\), \((192,576,385)\), \((1920,7680,5761)\), and \((23040,115200,92161)\).

The same program runs 45,280 finite norm-preservation assertions on edge-interior matrices with exponents \(1,1.5,3,4\), dimensions \(2\) through \(5\), five internal splitting parameters, and two test vectors per matrix.

## Analytic verification and limits

The proof of the all-dimensional theorem is based on the strict scalar Clarkson sign when \(p\ne2\), unique stratification from \(n-1\) nonempty pairwise disjoint column supports in \(n\) rows, a compact-to-Hausdorff graph identification, connectivity via signed blank moves, and the spanning-tree formula. No finite enumeration is claimed to verify arbitrary dimension. No independent audit or external certification is claimed.
