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

The proof is all-parameter and does not depend on computational extrapolation. The accompanying `verify.py` performs three independent finite checks of its definitions and boundary behavior.

First, it computes the partition expression \(qk-C_k(w)\) and compares it with a literal search over supersequences, with universality tested by enumerating all length-\(k\) subsequences. This covers 240 full-support tiny instances.

Second, for \(q=2,3,4\) over bounded ranges through \(n=9\), it exhaustively checks every full-support word, verifies the objectwise coverage lower bound \(C_k(w)\ge\min\{n,q+k-1\}\), and confirms that the maximum insertion distance equals \(\max\{qk-n,(q-1)(k-1)\}\). This comprises 69 parameter triples and 20,644 word checks aggregated across their tested \(k\)-values.

Third, it evaluates the stated extremal family directly on 2,376 further parameter triples through \(q=12\), \(n=q+17\), and \(k=12\).

A replay of the supplied file produced:

`VERIFY_OK literal_cases=240 exhaustive_parameter_cases=69 full_support_words_checked=20644 witness_grid_cases=2376`

Limits: these computations are finite and are not an exhaustive proof for unbounded parameters. The infinite claim is justified by the partition identity, the refinement lemma, and the matching extremal family in `RESULT.md`.
