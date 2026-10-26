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

Run `python3 check.py` using Python 3 with only standard-library modules. The script iterates over all words with exactly two \(a\)'s, \(m\) \(b\)'s, and one \(c\) for \(0\le m\le35\). It computes their Parikh-matrix signature by a direct streaming subsequence count, groups them, and independently generates signatures from the three letter skeletons. For every observed signature it checks its class size against the theorem's closed formula, then verifies the exact number of classes, the total word count, and the maximal fiber. The enumerated total is \(246{,}753\) distinct words, with every assertion passing.

The symbolic proof in `RESULT.md` covers all integers \(m\ge0\). The finite checker is not a substitute for the proof; no exhaustive computer claim is made for \(m>35\). The literature-priority review cannot rule out an inaccessible or uncatalogued equivalent earlier result. Independent mathematical audit has not been performed.
