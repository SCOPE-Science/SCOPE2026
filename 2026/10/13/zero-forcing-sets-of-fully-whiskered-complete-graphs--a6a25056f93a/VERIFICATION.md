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

The proof is analytic and valid for every integer \(n\ge2\); the computation below is a finite corroboration, not a replacement for the proof.

The standalone `artifacts/verify.py` constructs \(K_n\odot K_1\) directly. For every subset it independently simulates the standard zero forcing color-change rule and compares the outcome with the empty-pair criterion. It then compares the complete coefficient vector against
\[
(2x+x^2)^n+n\big((2x+x^2)^{{n-1}}-x^{{n-1}}\big),
\]
and checks the minimum value, minimum-set count, and total count.

Tested range: \(2\le n\le8\), with graph order at most \(16\).

Exact replay output:

`VERIFY_OK n_range=2..8 subset_checks=87376 criterion_checks=87376 coefficient_checks=77 minimum_checks=21 max_order=16`

The theorem for arbitrary \(n\ge2\) rests on the structural proof in `RESULT.md`.
