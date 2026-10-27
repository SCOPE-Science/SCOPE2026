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

# Reproducibility and limits

Run `python3 verify_vt_two_deletion.py` with standard-library Python 3. It enumerates all length-(n-2) received words for n=2,...,11 and 24 deterministic random samples for each of n=12,15,20,26,35,45, for 1,167 received words. For each received word it constructs the actual distinct two-insertion words, groups them by VT syndrome, verifies the sharp worst-case bound, checks pairwise disjoint one-deletion intermediate sets and canonical singleton words, and verifies all checksum-increment conditions. Every n in 2,...,11 independently checks sharpness for the all-zero descendant and syndrome zero. `verification_output.txt` contains the recorded successful output. These calculations corroborate, rather than prove, the all-length result.

The critical mathematical proof steps are intermediate-shadow disjointness from classical VT one-deletion uniqueness; the single-run necessity for singleton shadows; pairwise distinct canonical integer checksum increments within the range 0 to 2n-1; and the exact zero-syndrome matching witness. No standalone large-scale search is needed to establish the infinite theorem.
