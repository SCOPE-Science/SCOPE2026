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

`verify_width2.py` builds the directed cover lattice implicitly from ideals of every canonical width-at-most-two rooted forest of order 1–15. It computes lower and upper cover counts by independent bitmask checks against the analytical polynomial formulas, checks injectivity, fibre multiplicities, the first collision sizes, and 120 factorization identities. Run `python3 verify_width2.py`; see `verification_output.txt` for the actual run, which reports `VERIFY_OK` and 323 tested isomorphism classes. The script uses Python standard library only. The all-order theorem is established by closed-form algebra and canonical shape classification; enumeration is a cross-check, not an infinite proof. The verification does not assess literary novelty or independent publication priority.
