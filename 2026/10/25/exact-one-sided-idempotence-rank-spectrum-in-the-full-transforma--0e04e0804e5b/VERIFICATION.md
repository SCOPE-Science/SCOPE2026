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

# Verification and scope

The proof is algebraic and bijective. The `verify.py` file is a reproducibility aid rather than an infinite certificate.

## Executed checks

`python3 verify.py` ran successfully. The verifier enumerates all full transformations, recognizes idempotents by the equation on actual value tuples, composes every ordered pair of idempotents for sizes \(1\) through \(6\), and checks each rank-triple count against the exact rational-number coefficient formula. A structurally separate method selects every candidate \(f\)-root set for a fixed \(e\)-idempotent and counts permitted mappings for sizes \(1\) through \(4\). Support nonvanishing is also checked through size \(14\).

Recorded exhaustive totals for sizes \(1\) through \(6\): \(1,9,94,1417,28856,746179\). The terminal marker was `VERIFY_OK_IDEMPOTENT_PRODUCT_RANK_TRIPLES` with 196 compared rank-profile cells, including boundary-zero cases.

## Limits

Finite checks cannot establish a theorem for every \(n\). Universal correctness follows from the three-case product-idempotence criterion and the reversible exponential generating function proof in `RESULT.md`. Independent audit was not performed, and the historical-priority uncertainties listed there remain.
