---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The binomial–harmonic identity cancels one factor per summand and gives P_n(r)/n! with P_n the derivative of the rising factorial. An independent product-rule recurrence (python3 /workspace/audit_evidence/hyperharmonic.py) checked the printed factorial and residue, all 14 local zeros and congruences, P_45(R) mod 45!, and three exact rational samples. The integer polynomial makes the root persist for every k≥0; the full integrality set is periodic modulo 45!, so its natural density exists and is at least 1/45!. The lower exclusion can be proved independently of access to the cited theorem. If p divides n and the interval r,…,r+n−1 has a unique entry of maximum p-adic valuation, the product omitting that entry is the unique derivative term of least valuation. For each power p^j, removing the maximal entry leaves at most floor((n−1)/p^j) multiples, by spacing. Thus v_p(P_n(r))≤v_p((n−1)!)<v_p(n!). For even n use p=2: two distinct equal-maximum 2-adic valuations would have a higher valuation between them. For n=p^a, exactly one entry is divisible by p^a. Any odd nonsquarefree n with two prime factors is at least 3²·5=45, so these exclusions cover all smaller nonsquarefree indices >1.

## originality

PASS

Pass for the least nonsquarefree index 45 and an explicit positive residue class at that index, not for the derivative reformulation or the prior exclusions. The closest distinct indexed result fully classifies the orders at 45 but is recorded on 2026-11-02, after the 2026-10-27 frozen record. It gives mathematical overlap but no demonstrated earlier priority; the inspected earlier literature establishes other indices and methods but not the needed root at 45. Publication priority is bounded by the available evidence.

## value

PASS

Nonsquarefreeness marks exactly the regime not previously represented by the squarefree index 33. The first feasible odd nonsquarefree non-prime-power index is shown to work, and the local certificate converts what could have been an isolated large computation into an explicit set of integer orders of positive density. No claim of exact density or of the first index overall is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
