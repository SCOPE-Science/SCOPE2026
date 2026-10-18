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

# Verification and limits

The claim is established by a uniform symbolic argument. Its critical coefficient input is the two-term expansion of \(f_s(t)^{(3-1)/2}=f_s(t)\) in characteristic \(3\). Direct coefficient extraction in the basis \(t^{i-1}dt/y\) yields a partial signed permutation matrix; since coefficients are in the prime field, all inverse-Frobenius twists are identical. Row indices written in ternary provide the exact universal survival counts.

Reproduce the finite corroboration from this package with `python3 cartier_check.py`. It builds the coefficient map from the polynomial's two exponents, checks at most one nonzero per column and row, validates all individual base-three transitions, and iterates matrix paths. For each \(s\) from \(1\) to \(6\) it reproduces every rank through power \(2s+1\), printing `VERIFY_OK digit_shift_and_exact_rank_profiles s=1..6` on success. All calculations are exact integers. No full-size generic matrix or external dependency is required.

The independent mathematical assertion for every \(s\) uses the proof's arbitrary-length ternary counting, not the finite runs. The Mordell–Weil consequence relies on the explicitly checked hypotheses of Katsura, Theorem 4.1, rather than on program output.

Remaining limitations: absence of full Newton polygons and Ekedahl–Oort types; no comprehensive historical-priority certification; no independent audit performed.
