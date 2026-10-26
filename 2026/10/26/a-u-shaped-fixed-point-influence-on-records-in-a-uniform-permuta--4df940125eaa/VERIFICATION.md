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

# Reproducible verification

Run `python verify.py` with Python 3. No third-party modules are required. The program enumerates all permutations for \(2\le n\le8\), computes fixed-point indicators, strict upper-record indicators, their complete cross-moments, and exact aggregate covariances using `fractions.Fraction`. It additionally checks symbolic binomial identities and the full sign classification at sizes \(5\le n\le100\). Expected final line:

`VERIFY_OK 46232 enumerated permutations; 10325 exact assertions`

The general proof is the three-case conditional probability calculation in `RESULT.md`. Exhaustive finite checks are corroboration only; sizes above eight are not exhaustively enumerated, and the symbolic checks through 100 do not constitute an infinite proof. Originality priority has not received independent adjudication.
