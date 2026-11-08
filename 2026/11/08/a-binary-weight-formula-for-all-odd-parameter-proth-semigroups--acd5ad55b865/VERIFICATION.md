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

# Reproducibility

Run `python3 check_proth.py` in a standard Python 3.10+ environment (no external dependencies). It calculates the proposed formula using binary Hamming weights and independently computes the Frobenius number by Dijkstra's shortest paths on residues modulo the smallest generator. All checks use exact integers.

Recorded execution from these exact source bytes:

```text
APERY_OK pairs=119 residue_classes=599039 s_gt_1=43 s_ge_3=1
GREEDY_OK additional_parameter_pairs=2115
EXAMPLE m=3 n=6 h=2 t=2 s=1 F=37443
EXAMPLE m=7 n=6 h=3 t=2 s=2 F=202052
EXAMPLE m=31 n=6 h=5 t=4 s=1 F=3950151
EXAMPLE m=63 n=7 h=6 t=4 s=2 F=65084552
EXAMPLE m=127 n=8 h=7 t=4 s=3 F=1057257737
EXAMPLE m=255 n=9 h=8 t=5 s=1 F=17047088649
EXAMPLE m=511 n=10 h=9 t=6 s=1 F=273810969611
```

The first 119 parameter pairs exhaust every odd coefficient from 3 to one below the power of two for each \(3\le n\le7\). The second test selects 2115 larger pairs and compares the binary formula with independently computed greedy representations; it does not independently calculate the Frobenius number for those large pairs. These finite computations do not establish the universal claim. The exact proof uses the previously published Apéry and monotonicity theorems together with the explicit binary-splitting and borrow analysis in `RESULT.md`.
