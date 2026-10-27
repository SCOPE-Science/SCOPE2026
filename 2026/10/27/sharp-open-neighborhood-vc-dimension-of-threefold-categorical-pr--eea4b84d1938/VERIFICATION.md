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

Run `python3 verify.py` in the same directory. It has no external dependencies and evaluates exact finite partition unions for the three upper-kernel restrictions, the eleven-orbit six-point obstruction, and explicit open-neighborhood witnesses. It reports the following reproducible facts: four-point cap \((2,2,4)\) has zero shattered cases among \(960\) triple partitions; five-point caps \((2,5,5)\) and \((3,3,3)\) have zero among \(43{,}264\) and \(68{,}921\); the complete six-point reduction checks \(27{,}375\) survivors of safe filters with zero shattered cases; positive witnesses of sizes three, four, five realize all \(8,16,32\) traces. These machine checks certify finite combinatorial subclaims but do not independently certify the mathematical reduction from graph neighborhoods to partition unions or literature novelty. That reduction is proved in `RESULT.md`. The exhaustive computation was run and returned `VERIFY_OK exact_three_factor_tensor_neighborhood_vc=PASS`.
