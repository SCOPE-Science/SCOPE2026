---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Under a fixed rank permutation pi and inter-block weak order, the first two blocks of eight terms supply five consecutive Van der Laan four-window equalities E_s=0 and fifteen weak-rank, block-order and nonnegativity inequalities I_j<=0. The exact 23 certificate rows in certificates.json express x0+x1+x2+x3 as sum of nonnegative multiples of I_j plus rational multiples of E_s, for every nonidentity pi. A fresh independent BigInt rational-linear-form evaluator reconstructed every E_s/I_j from the permutations, checked unique coverage of all 23 nonidentity permutations, nonnegative inequality multipliers and all 23 coefficientwise identities with zero errors; hence the first block must be zero and the four-window condition propagates all subsequent terms to zero. For identity pi the hypotheses mean global monotonicity and force a_{n+3}=a_n+a_{n+1}, equivalently a_n=a_{n-2}+a_{n-3} for n>=4, with exactly 0<=u<=v<=w<=u+v; elementary induction preserves monotonicity. This certifies ALL infinite sequences with the stated fixed 4-block restriction, not merely sampled initial terms.

## originality

PASS

Nacin 2023 proves globally nondecreasing sequences (identity pattern) and nonmonotone fixed block order patterns only through length three. The new exclusion of all nonidentity four-block patterns is not stated or implied by Nacin's increasing-case theorem; without the 23 inequalities nonidentity sequences are not known to reduce to it.

## value

PASS

Completes the first unclassified block length after the established length-three order types, proving a sharp collapse of all 23 nonidentity weak rank patterns by finite exact rational certificates. The structural rigidity theorem is a natural, motivated boundary extension of the Van der Laan sequence classification, not a routine Padovan rebranding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
