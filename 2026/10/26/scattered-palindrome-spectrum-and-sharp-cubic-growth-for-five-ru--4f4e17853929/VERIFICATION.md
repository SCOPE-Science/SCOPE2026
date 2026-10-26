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

Run `python3 verify.py` with the Python standard library. The verifier explicitly accumulates every distinct scattered subsequence string through a set recursion and then filters by reversal equality. Thus its finite enumeration does not rely on the proof's run-pattern classification.

The test exhausts all \(1024\) parameter tuples with \(1\leq a,b,c,d,e\leq4\), comparing the exact coefficient at every subsequence length and the total. It separately enumerates compositions of lengths \(5\) through \(30\) and computes finite maxima as a check on sample extremizers. Seven multiple-of-six construction parameters are checked against the exact polynomial expression. It prints `VERIFY_OK` if all assertions hold.

Verification is finite. The theorem for all positive lengths, the full generating-polynomial identity, and asymptotic rigidity are justified in RESULT.md, not inferred from test coverage. Independent audit status remains not performed.
