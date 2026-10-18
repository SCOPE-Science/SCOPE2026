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

The exact-one-error channel is implemented directly from its letter-level definition in `verify.py`. Run the checker with `python3 verify.py` from the folder containing this file. It constructs all parents, their distinct duplicated outputs, the confusability graph, every confusability triple, the common-output intersections, and the two predicted triple counts.

The enumeration ranges are \(q=2\), \(1\le n\le10\); \(q=3\), \(1\le n\le7\); \(q=4\), \(1\le n\le6\). All \(28{,}232\) enumerated confusability triangles match the upper/no-common versus lower/unique-common dichotomy. For size \(s\ge4\), direct clique enumeration additionally checks every eligible size in binary lengths up to 8, ternary lengths up to 6, and four-letter lengths up to 5. The checker also independently calculates the largest received-word parent set and confirms \(\lfloor(n+1)/2floor\) throughout the test ranges. It prints `TANDEM_TRIANGLE_HELLY_PASS triples 28232` on success.

The argument in `RESULT.md` proves the statements for every allowable length and alphabet size; these finite tests cannot certify the infinite claims or establish historical originality. Independent external audit has not been performed.
