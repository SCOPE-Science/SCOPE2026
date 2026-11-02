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

The exact statement, quantifiers and proof are in `RESULT.md`. The original Stirling–Bernoulli partition identity is given as published equations (5.2) and (5.4) of arXiv:2111.08766v1. The decisive new comparison is the bound on the finite-partition terms with \(d<T\): \(\nu_2\Lambda(u)\le(w+d)/2\) and \(r-d>B=2^h-a\) establish strict domination when \(B\ge2t_b\). All other terms are handled by the constant carry valuation at \(d\ge T\). This is a formal infinite proof; the script is not used to extrapolate.

Run `python3 verify.py` using the standard library. It computes 19,812 positive Stirling coefficients modulo \(2^{32}\) from the recurrence, independently computes target valuations from integer binomial coefficients and bit counts, checks 18,537 certified-range positions and their carry identities, and verifies every observed disagreement lies in the proven envelope. It also reconstructs the exact rational partition identity for 55 pairs with \(1\le k\le n\le10\). All expected valuations are strictly less than 32 and hence exactly determined modulo \(2^{32}\). Expected output:

`VERIFY_OK tests=19812 certified=18537 observed_disagreements=433 identity_pairs=55`

Remaining scope limits: the exact count and valuations of exceptions are not classified, and all experiments cover only \(1\le c\le12\), \(1\le h\le7\). Separate independent scientific validation has not been performed.
