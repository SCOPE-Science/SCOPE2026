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

Run `python3 verify.py` beside `certificate.json`.

The first engine directly constructs the alternating-arch extremal word and exhausts all candidate subsequences of the shortest absent length for \(2\le\sigma\le5\) and \(1\le k\le5\). It checks both subsequence absence and the claimed weak-zigzag condition for every candidate.

The second engine counts the same objects as walks in the threshold graph \(i+j\ge\sigma-1\). It is checked against the independent reverse-accumulate recurrence through \(\sigma=9\) and length \(12\).

A third finite stress test exhausts every full-alphabet binary and ternary word through length \(7\), computes its universality index and shortest-absent-subsequence count, and confirms the bound for indices \(1\) and \(2\).

The infinite extremality comparison across all words is supplied by the cited published theorem; the package independently verifies the new exact evaluation and its structural bijections.

Independent audit has not been performed.
