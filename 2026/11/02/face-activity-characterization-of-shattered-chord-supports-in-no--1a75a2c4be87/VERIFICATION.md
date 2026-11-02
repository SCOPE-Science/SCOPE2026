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

Run `python3 verify_noncrossing.py` using Python 3.10 or newer, without external dependencies. The program independently constructs Catalan noncrossing matchings; for every all-positive-feasible chord support of cardinality at most the number of matching edges through \(n=6\), it compares all labeling projections with the face-activity predicate. It separately checks a cyclic rotation of every noncrossing perfect matching through \(n=7\) is edge-disjoint from the original, and computes exact adaptive dimension recursively for \(n\le5\). `verification_output.txt` stores the exact output of an executed run.

The finite verification comprises 4,786 all-positive-feasible chord supports for \(n\le6\), 624 cyclic rotations for \(2\le n\le7\), and dynamic-programming dimensions for \(1\le n\le5\). Supports that cannot be extended to a positive-labeling perfect matching are rejected directly by the analytical necessity in Step 1; the enumeration also constructs all such candidates from the union of actual matching edges. These checks are finite and do not constitute an infinite proof. The unrestricted result uses the face-completion and cyclic-rotation arguments in `RESULT.md`. Independent mathematical validation has not been performed.
