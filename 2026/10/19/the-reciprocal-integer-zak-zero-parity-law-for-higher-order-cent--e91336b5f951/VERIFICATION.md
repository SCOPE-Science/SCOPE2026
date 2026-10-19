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

The result is established by the analytic Fourier-dilation/refinement identity and the previously published uniqueness of the centered unit-scale B-spline Zak zero. The checker is a *finite* independent algebraic/numerical cross-check, not proof of the theorem for unbounded \(n,m\).

Run `python3 verify_b_spline_reciprocal_zak.py` with Python 3. The checker uses `fractions.Fraction` to compute each B-spline at rational arguments with the truncated-power formula, constructs the Laurent coefficient dictionaries of both sides of the dilation identity independently, and asserts equality exactly in 216 cases (orders \(3\) through \(8\), refinement integers \(2\) through \(7\), six rational spatial locations). It also checks 252 root-line values numerically at nontrivial roots of unity (tolerance stated in the code). It completed with:

`VERIFY_OK 468 exact rational polynomial and numerical root checks; n=3..8, m=2..7`

The finite checks do not independently certify the classical unit-scale theorem and do not substitute for the universal analytic factorization. At exceptional even-scale points the proof asserts only a lower bound for frequency multiplicity.
