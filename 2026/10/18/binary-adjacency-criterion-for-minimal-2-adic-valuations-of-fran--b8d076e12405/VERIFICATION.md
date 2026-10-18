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

Run `python3 verify.py` using Python 3 with only its standard library. The checker computes Franel numbers directly as cubes of binomial coefficients, independently sums Strehl's nonzero terms, checks each term's valuation against the two binary carry counts, and checks the count of minimal-valuation terms.

Observed result:

```text
VERIFY_OK indices=257 positive_strehl_terms=16641 recurrence_instances=255 fibonacci_lengths=14
```

The computations cover indices \(0\) through \(256\), 16,641 positive summands, 255 instances of the classical Franel recurrence, and binary lengths \(0\) through \(13\). These finite tests verify the packaged implementation and representative instances but cannot establish an all-index theorem. The infinite mathematical guarantee comes from the displayed equality \(\nu_2(g_{n,k})=s_2(n)+c_1+c_2\), the carry-free-subset bijection, and the parity argument in `RESULT.md`.

The first publicly posted arXiv version of Sun's source is dated 2011-12-05. The 2014 research report is dated August 2014 without an invented day. Any additional broader theorem could affect originality, so independent literature assessment remains outstanding.
