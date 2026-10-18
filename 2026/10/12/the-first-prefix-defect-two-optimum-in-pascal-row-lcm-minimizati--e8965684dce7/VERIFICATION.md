---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Reconstructed finite prime-power exclusion DP over every admissible row, with subset-of-omissions bit masks and each prime exponent budget. Independently implemented integer-binomial/valuation arithmetic and rechecked all n=42..57; minimum-defect sequence is (1,1,1,0,...,0,2), n57 at row120. Computed a57=34745667272226689670077824806669345127280961600 and optimal full-row exclusion {39,40,60} with saving 41*61=2501; selected 57 indices 0..58 omit39,40 have defect2. Exhaustive prefix <=57 search yields minimum row118 65841579578883348912626466335327204421864343200=(451/238)a57; prefix<=56 minimum row119 (451/120)a57. Candidate cutoff r=176 checked via binomial lower bound, and Huber provides n<=41 including δ41=3. The optimizer enumeration is finite and constrained by proven row reduction; no later n or all-support-classification claim.

## originality

PASS

PASS (best of knowledge): Huber's prime-power exclusion and finite-row reduction are acknowledged and relied upon; his inspected arXiv abstract/proposition descriptions certify prior transitions through n41, but do not state δ57=2. The new finite exact classification of intermediate n42..57 and first occurrence of the skipped natural defect value is not a consequence of simply knowing δ41=3. Full source supplement inaccessible, so possible pre-existing n57 tabulation is an explicit originality risk.

## value

PASS

PASS: After a known first jump δ41=3, the next missing natural defect value 2 is a concrete structural question raised by Huber's study of the size/frequency of optimal-support defects. A proved first-occurrence n=57 with sharp forbidden prefixes answers that meaningful exact finite boundary, rather than picking an arbitrary row or merely replaying a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
