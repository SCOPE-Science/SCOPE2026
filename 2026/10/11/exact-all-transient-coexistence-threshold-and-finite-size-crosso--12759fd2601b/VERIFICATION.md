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

The standalone `verify.py` requires Python 3.10+ and the standard library. Execute `python3 verify.py` from the directory holding the extracted scientific files. The observed output was `PASS: 8488 exact assertions`.

The script independently enumerates binary ring configurations, evolves the rule directly, and checks the fixed-state partition against both forbidden-run enumeration and matrix traces. It also compares direct evolution with every-position radius growth, including cyclic wrapping, and checks the critical algebra with rational arithmetic. All test assertions use exact integers or rational numbers.

The universal theorem is proved in `RESULT.md` by Boolean dynamics, a primitive matrix, the exact Perron root equation, and an analytic eigenvalue expansion. Finite enumeration neither exhausts all \(p,N\) nor proves the thermodynamic limit. No external independent audit or validation was performed.
