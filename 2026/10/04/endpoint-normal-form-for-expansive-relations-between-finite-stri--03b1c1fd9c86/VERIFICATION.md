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

The proof is symbolic and covers every pair of positive integers \(m,n\). The executable check is independent finite corroboration.

`verify.py` constructs every binary relation between \(C_m\) and \(C_n\) for \(1\le m,n\le4\). For each relation it tests source totality, forward confluence, and backward confluence directly from the quantified definitions. It separately computes every nonempty row minimum and maximum and tests the proposed endpoint criterion. The predicates agree for every relation in the tested range.

For every tested pair \((m,n)\), the checker also verifies the existence threshold \(m\le n\), the weighted endpoint-sum count, minimum size \(m\), maximum size \(m(n-m+1)\), uniqueness of the maximum relation, and exactly \(\binom{n}{m}\) minimum-size relations.

Running the packaged checker prints `VERIFY_OK`. The exhaustive finite computation is not used to prove the general theorem; the proof in `RESULT.md` establishes all claims for arbitrary positive \(m,n\).

## Limits

No assertion is made for branching frames, clustered preorders, reflexive-chain conventions, or relations that are not source-total.
