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

Run `python checker.py` in the directory containing this file. Expected output:

`VERIFY_OK radial_exact=17 slice_ranks_mod_1000003=14 ternary_fourier=10 edge_identities=2`

The checker was executed against the included path. It computes the exact second Krawtchouk polynomial, its minimizing indices, the sharp values and resonance formulas for 17 cases; verifies all spectral inequalities of explicit nonradial examples using exact fractions; checks 14 nontrivial slice-evaluation ranks modulo the fixed prime `1000003`; checks two exact edge-additive polynomial identities, and numerically evaluates ten selected direct ternary Fourier coefficients for dimensions 6 and 8 with tolerance `2e-11`. The general proof does not rely on these finite ranks or floating-point transform checks. The equality-classification kernel argument must be read in `RESULT.md` for unrestricted parameters.

The source paper's 2019-04-07 public date is independently visible in the arXiv v1 submission record; neither later revisions nor journal dates determine that date. All scientific literature comparisons and outstanding bibliographic risks are stated in `REVIEW.md` and `AUDIT.json`. No independent audit has been carried out.
