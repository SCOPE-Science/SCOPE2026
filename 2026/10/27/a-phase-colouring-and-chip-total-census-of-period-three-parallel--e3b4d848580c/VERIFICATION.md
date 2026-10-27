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

# Mathematical verification

The attached `verify.py` enumerates every chip assignment with \(0\le x_v<2d_v\) on each selected finite graph and tests \(F^3(x)=x\ne F(x)\) directly. It separately enumerates phase assignments and their weighted predecessor counts, and compares the full chip-total histogram with the interval-product polynomial on five cases. `verification_output.txt` records the results. The restriction to the finite box for the general recurrence theorem is justified by the backward-time periodicity lemma in RESULT.md, not inferred from experiments.

No independent audit, external mathematical validation or certification has been performed. The results are proven for finite, simple, connected graphs with at least one edge; small enumerations are corroboration, not an infinite proof.
