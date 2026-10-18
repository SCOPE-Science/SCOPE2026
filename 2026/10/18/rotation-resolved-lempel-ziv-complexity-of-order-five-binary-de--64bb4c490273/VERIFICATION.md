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

Run `python3 verify.py` in this directory. The program requires Python 3 and no third-party packages. It enumerates all 65536 local switch assignments and independently all Eulerian edge tours starting with the unique zero edge; both accepted sets contain 2048 words and are equal. Each word is checked for all 32 distinct length-five cyclic factors. All 32 rooted linearizations of every cycle are parsed by two distinct algorithms that agree on every case. The checker asserts the exact histogram and per-cycle minimum/maximum tables and prints `VERIFY_OK` only after all checks complete.

The two parsers allow copying from earlier *starts* even when the source overlaps its destination. They count a last fully reproducible phrase. This is the complete-component convention; implementations that discard a noninnovative last phrase may give different values. The claimed completeness is finite and follows from the explicit graph enumeration, not from testing a random sample. Only order five is claimed. The program was executed with success and its output checked before acceptance. The present review is a self-review, not an independent audit.
