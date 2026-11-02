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

# Verification record

`checker.py` enumerates all \((n+1)^n\) attacker arrays for \(n=1,2,3,4,5\) with independent choice probabilities \(p=2/5\) and \(a/n=3/(5n)\). It computes cyclic-basin membership by tracing pointers, counts stable extensions by enumerating all subsets under Dung's stability rule, and compares every finite size mass with the weighted-forest formula using exact rational arithmetic. It checks the all-size property \(\Pr(U_n=0)=\Pr(Z_n=1)=2/5\) in those five sizes. Run with `python checker.py` (Python 3 standard library only); successful output terminates with `ALL_CHECKS_OK`.

The finite computation covers 8,476 attacker arrays in total, and cannot establish the asymptotic limit, its joint form, or priority. Those rely on the proofs and literature discussion in RESULT.md. The primary remaining priority risk is the unresolved relationship to historical random mappings with an attracting centre; the check provides no independent scientific audit.
