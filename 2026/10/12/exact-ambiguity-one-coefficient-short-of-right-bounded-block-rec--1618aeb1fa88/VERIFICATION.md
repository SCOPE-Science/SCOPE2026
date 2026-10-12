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

Run `python3 verify.py` beside `certificate.json`.

The algebraic engine enumerates all nonnegative run vectors with
\[
1\le m\le8,\qquad 0\le |w|_b\le9,
\]
groups them by all retained Pascal moments, and checks that every fibre is exactly the predicted family \(s+t\,v\) with the stated integer interval for \(t\).

A separate word-level engine enumerates binary words through length \(12\). It computes \(\binom{w}{a^\ell b}\) by generic subsequence dynamic programming, without using the run-vector moment formula, and verifies the same collision families and exact ambiguity counts.

The verifier also checks the binomial annihilation identity for \(1\le m\le20\). The infinite theorem rests on the symbolic rank, kernel, primitivity, and nonnegativity argument in `RESULT.md`; finite enumeration is supplementary.

Independent audit has not been performed.
