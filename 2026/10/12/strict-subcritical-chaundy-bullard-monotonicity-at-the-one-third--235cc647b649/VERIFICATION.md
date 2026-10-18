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

Coupling Bin(3k,p) and independent Bin(3,p), cancelling internal tail terms, gives q_k-q_(k+1)=P(X=k)(1-p)R_k(p). The exact degree-two rational R_k has derivative (3k+1)(6kp-5k+4p-4)/(2(k+1)(2k+1)) <0 on (0,1/3] and R_k(1/3)=2(3k+2)/(9(k+1)(2k+1))>0. Within sizes 3j-2,3j-1,3j the threshold j is fixed and the upper-tail probability strictly increases; therefore every size is dominated by 3. Boundary p=0 is deliberately excluded. Independent rational recurrence checks 57 adjacent pairs; symbolic proof carries the continuum.

## originality

PASS

The starting 2023 paper explicitly frames the subcritical binomial-tail generalization as unknown; classical Chaundy–Bullard covers p=1/3 only for this a=3 case, and arbitrary-stake isolated reciprocal p does not imply all subcritical p. A 2022 centered-tail result does not reach thresholds above the mean. Resultary nearby two-trial phase threshold is a different increment. Best-of-knowledge after direct source comparison.

## value

PASS

Closes a specifically posed subcritical continuum of the generalized Chaundy–Bullard binomial-tail problem, with strict order for every k and a unique equal-stake optimum, exceeding classical single-p endpoint. The restricted scope is mathematically meaningful even though general unequal-stake optimization is still open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
