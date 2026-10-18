---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For c>=5 every q in (c/2,c] has v_q(c!)=1 because q^2>c. Exact Legendre parity computes s(1!)..s(10!)=(1,2,6,6,30,5,35,70,70,7). The direct prime count for 11<=c<=50 is at least 2; for c>=51 Nagura at x=c/2 and x=5c/6 yields disjoint q1 in (c/2,3c/5), q2 in (5c/6,c); both divide s(c!), so it is composite. Independent integer program recomputed kernels through 199 and c=11..50 windows. This proves exactly c=2,6,10, not merely a finite observation.

## originality

PASS

Best-of-knowledge originality PASS for the exact all-c one-prime-support classification of the squarefree factorial set. OEIS has the exact input sequence and finite table; Nagura's theorem is a published premise; a search did not identify the stated unbounded prime stratum. The large-source access failure and the elementary nature of the deduction lower confidence, not scientific correctness.

## value

PASS

This identifies all prime members of a natural arithmetic parameter set used in the factorial-square problem, supplying an exact exceptional-support boundary across infinitely many factorials. Despite a short proof, the concrete all-c classification is independently useful beyond a prefix table; it does not claim a new prime-gap theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
