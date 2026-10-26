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

# Verification of the one-perfect flag-rank classification

The source file `verification/verify.py` is executable using the Python standard library. Running `python verification/verify.py` must terminate with `VERIFY_OK`; the observed output is bundled in `verification/verify_output.txt`.

The verifier builds explicit parity-check images in prime fields at \((q,\alpha)=(2,3),(2,4),(3,3),(5,3)\). It computes flag-rank weights by independently reducing each upper-right corner block over the relevant field, rather than trusting syndrome algebra alone. It checks all \(11{,}346\) classified one- and two-weight configurations for nonzero syndromes, verifies distinct one-error syndromes and explicit weight-three kernel words, and checks the exact code-count expression at \((q,\alpha)=(2,3)\).

For the smallest perfect parameter \((q,\alpha,n)=(2,3,7)\), the verifier independently enumerates all \(2^{13}=8{,}192\) matrices supported on the diagonal and first superdiagonal; the weight-zero/one/two populations are \((1,7,45)\). It additionally checks each single entry on higher superdiagonals has the expected flag-rank weight. The infinite-field-size and composite-prime-power cases are mathematical deductions, not claims of exhaustive machine verification.

Actual printed output must match the packaged execution record. Neither a separate reviewer nor an independent mathematical audit is represented by this file.
