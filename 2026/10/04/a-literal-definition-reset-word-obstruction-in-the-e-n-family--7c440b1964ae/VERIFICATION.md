---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n>=5, under literal b(i)=i+1 modulo n and a(1)=2,a(2)=3,a(i)=i (i>=3), B=a²b^(n-2) sends [1,n] to [1,n-2], and [1,m] to [1,m-2] for m>=4. With r=floor((n-2)/2), B^r reaches [1,2] (even n) or [1,3] (odd n), and a² sends either to singleton {3}. Thus w=B^r a² synchronizes; length nr+2 differs from alleged n²−3n+2 by n(n−4)/2 for even n>=6 and n(n−3)/2 for odd n>=5, strictly positive. I independently replayed n=5,6,7,8,20 from the literal tables; verifier artifact enumerates full power automata only n<=12, not a universal certificate. Boundaries n=4 excluded from strict violation. The source Figure 6 does NOT define this literal table; no claim about intended E_n exact threshold.

## originality

PASS

Best-of-knowledge new explicit infinite-family consistency obstruction confined to the printed cyclic-b formula, not the intended Figure-6 theorem; literal word and length absent in read primary passages.

## value

PASS

Motivated source-correction for a named infinite synchronizing-automata family: provides a uniform explicit witness separating literal stated transition data from a headline theorem and guards reproducibility. Not a mere tiny numerical counterexample and correctly limits implication to the literal table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
