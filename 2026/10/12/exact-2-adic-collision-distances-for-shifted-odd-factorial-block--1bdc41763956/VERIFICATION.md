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

Run `python3 verify.py` in a directory containing the standalone verifier. Expected terminal status: `VERIFY_OK`. The companion `verify_output.txt` is the actual output of the packaged script. It checks exact large-integer products over eight block sizes, modular products over four larger block sizes, reflected equalities, powered differences, and entire modular image fibers. The proof's independent induction on reciprocal odd-pair sums establishes the universal valuation; no finite search can replace this step. Scope excludes truncated odd blocks and other prime bases. No independent audit has been performed.
