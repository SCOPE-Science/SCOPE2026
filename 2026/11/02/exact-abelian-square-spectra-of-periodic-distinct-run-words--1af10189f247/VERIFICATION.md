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

# Reproduction and limits

Run with Python 3 standard library from the same extracted directory:

`python3 verify.py`

Output observed during this review:

`VERIFY_OK literal_cases=997 half_length_profiles=14021 distinct_abelian_squares=24087 circular_arc_tests=4340 all_equal=TRUE`

The verifier enumerates distinct factor strings literally and compares every half-length profile against the proposed circular criterion. It checks the parity-split total independently using integer arithmetic, and separately exhausts adjacent circular windows over additional run vectors. Parameter families are \(q=3\) with lengths \(1\)–\(4\) and powers \(1\)–\(6\); \(q=4\) with lengths \(1\)–\(3\) and powers \(1\)–\(5\); \(q=5\) with lengths \(1\)–\(2\) and powers \(1\)–\(4\); plus 80 deterministic pseudorandom parameter cases of \(3\le q\le6\), runs at most \(7\), and powers at most \(6\). The circular arc lemma is separately checked over all run vectors of lengths at most \(4\) for \(q=3\) and at most \(3\) for \(q=4\).

Checks do not establish the theorem for infinitely many run lengths and powers; the complete proof in `RESULT.md` supplies that implication. They do not certify literature originality, independent audit status, or cases with repeated letter-runs.
