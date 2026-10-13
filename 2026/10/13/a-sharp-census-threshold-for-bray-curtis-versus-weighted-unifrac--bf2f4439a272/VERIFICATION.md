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

# Verification and reproducibility

Run `python verify.py` with Python 3 and the standard library. The verifier computes normalized weighted UniFrac directly from the four tree edges (two sister pendants, outgroup pendant, and sister clade stem), without using the \((k,c)\) representation, and compares it with the closed formula; all arithmetic uses exact fractions.

Execution returned:

```
VERIFY_OK pair identities 10584 ordered comparison checks 218484
```

The verification covers integers \(3\le N\le9\), seven rational interior branch ratios, every ordered nonidentical sample pair, and every ordered distinct third sample for a shared-reference reversal. Additional algebraic checks in the proof establish the all-\(N\), all-real-\(t\) result: integer lattice gap \(k-\ell\ge1\), upper bound \(c\le N-3\), and an explicit witness attaining \(c=N-3\). These arguments, not the finite enumeration, prove the infinite statement. At a phase boundary, the strictness is exact. No independent audit has occurred.
