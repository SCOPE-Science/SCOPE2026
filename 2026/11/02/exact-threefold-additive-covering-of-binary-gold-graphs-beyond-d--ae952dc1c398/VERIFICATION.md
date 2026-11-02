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

`python3 artifacts/verify_gold.py` computes entire ordered pair-image multisets for all \(1\le m\le8\) and \(1\le r\le m\). It tests polynomial irreducibility, the cardinality of directly enumerated twofold sumsets, every theorem regime against direct finite-field multiplication, and odd relative-degree representation multiplicities. The resulting console line is `VERIFY_OK exact_gold_cases=36 full_cover_cases=24 odd_fiber_cases=22`. The unrestricted proof rests on the relative-trace image theorem, multiplicative power subgroup index, and two exhaustive subfield cases, none of which follows from finite testing. No independent audit or external certification has been performed.
