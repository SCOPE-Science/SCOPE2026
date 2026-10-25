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

Run `python3 verify.py` in the same directory as the bundled script and compare its one-line JSON output byte-for-byte with `certificate.json`. The checker enumerates labeled, disjoint sample subsets independently of the formula's absence-indicator proof and uses only exact integer fractions. It checks all abundance partitions with total census size \(4\) through \(8\) for two-person samples, all positive sample-size pairs over census sizes up to \(7\), the singleton–doubleton phase in \(2595\) cases, and explicit extremes. These finite checks support implementation correctness, not proof for infinite families. The proof in `RESULT.md` establishes the unrestricted statements by counting. No independent scientific audit has yet been performed.
