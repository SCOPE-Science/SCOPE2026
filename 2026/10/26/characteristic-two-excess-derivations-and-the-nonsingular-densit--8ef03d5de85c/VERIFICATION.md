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

The standalone `check.py` was run with Python 3. It builds the structure constants and full derivation linear system, checks Jacobi on every basis triple at dimensions 6, 8, 10 and 12 over the prime fields of characteristics 2, 3, 5, and 7, reconstructs sample derivations from free coordinates, and independently computes matrix determinants. The computed derivation dimensions are respectively (10,9,9,9), (14,12,12,12), (18,15,15,15), and (22,18,18,18) across the listed fields. It exhausts all 1024 derivations of the six-dimensional case over the binary field. The observed terminal marker was `Q_FILIFORM_DERIVATIONS_OK`.

The computational tests do not address infinite-dimensional families by themselves; the general assertion follows from the coefficient proof in `RESULT.md`. No separate mathematical audit or external certification has been performed.
