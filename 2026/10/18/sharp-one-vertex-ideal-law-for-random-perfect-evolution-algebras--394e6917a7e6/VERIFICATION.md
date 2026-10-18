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

# Verification
The provided `verify.py` is standalone Python 3 and uses no third-party packages. Run `python3 verify.py`. The checker enumerates the full matrix space in seven small prime-power configurations, checks invertibility by exact elimination, tests strong connectivity by forward and transpose reachability, separately checks every proper outgoing cut by subset enumeration, and verifies singleton cut multiplicities using the exact group-order formula. It returned `VERIFY_OK` for \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\).

This finite replay tests no asymptotic range. The ideal-coordinate theorem, block-counting identity, Bonferroni estimate and middle-cut tail bound are proved in `RESULT.md` independently of observed small cases. No independent external audit has been performed.
