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

## Reproducible checks

Run `python verify_example.py` using a standard Python 3 interpreter. The script enumerates all chains in the two four-element posets, builds the simplicial boundary matrices over the rationals, and checks the face counts, first Betti numbers, and minimal-open difference. It also verifies the normalized formula for several values of \(N\).

Expected output:

- `PASS: P has f-vector (4, 4, 0) and beta_1=1.`
- `PASS: P+ has f-vector (4, 5, 2) and beta_1=0.`
- `PASS: exactly one minimal open changes by one point.`
- `PASS: normalized discrepancy equals 1/N^2 for N=4,5,10,100.`

The integral homology is verified by the explicit descriptions: a four-cycle has integral first homology \(\mathbb Z\), and two triangles glued along a common edge form a disk. The persistence diagram follows exactly from the discrete, middle, and indiscrete stages. No numerical approximation or external data is used.

## Limits

The example establishes failure of a dimension-independent bound for the stated discrepancy over abstract finite-topology filtrations. It does not assess metric-generated subclasses or stronger hypotheses. Independent audit and independent validation remain unperformed.
