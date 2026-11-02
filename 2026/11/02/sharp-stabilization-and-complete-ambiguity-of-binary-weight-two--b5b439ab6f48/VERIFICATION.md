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

Execute `python3 verify.py` with Python 3.9 or later and no nonstandard dependencies. The implementation enumerates every pair of one-marker positions for \(2\le k\le11\) and \(3k-2\le n\le3k+8\), computes the full multiplicity-preserving ordered \(k\)-mer spectrum, partitions the sources by clipped-zero-gap labels, and confirms equality of both partitions. It verifies the exact count \(3k^2-4k+3\) at and after \(3k-1\) and the exact one-profile deficit at \(3k-2\). These finite tests cover 110 parameter combinations and 31,240 source words. The general all-parameter proof in RESULT.md does not rely on exhaustive computational certification.

Limits: No exhaustive claims outside the tested ranges, and no external independent audit was performed. The run does not attempt to simulate sequencing errors or altered observables.
