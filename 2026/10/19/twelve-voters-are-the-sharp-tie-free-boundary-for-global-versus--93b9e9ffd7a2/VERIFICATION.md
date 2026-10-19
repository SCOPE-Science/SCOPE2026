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

# Reproducibility and verification

The companion `verify_pav.py` is self-contained Python 3 code, relying only on the standard library. Run `python3 verify_pav.py` in a directory containing this file. It independently computes twice the global harmonic PAV score from each of the seven nonempty ballot types and also the first- and second-round greedy scores. It enumerates **every anonymous profile** with between one and twelve voters: exactly 50,387 integer vectors (stars-and-bars enumeration, omitting the empty electorate).

Observed counts of profiles with a **unique most-approved candidate excluded from the unique globally optimal pair**, by electorate size \(n=1,\ldots,12\), were \((0,0,0,0,0,0,0,0,0,3,3,9)\). The corresponding counts with a **strict second greedy choice** were \((0,0,0,0,0,0,0,0,0,0,0,6)\). Exact assertions check the profile with twelve voters, its three two-seat scores, and both greedy marginal scores. Execution completed with `VERIFICATION PASSED`.

The **infinite-family** claim and all-profile necessity of at least twelve voters rest instead on the complete algebraic proof in `RESULT.md`, including its integer identity and second-round difference. The finite test independently corroborates its first boundary; it does not substitute for the proof or for independent literature-priority verification.
