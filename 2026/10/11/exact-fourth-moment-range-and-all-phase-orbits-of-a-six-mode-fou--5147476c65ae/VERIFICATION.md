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

# Verification and reproducibility

The mathematical proof relies on two exact identities. Splitting the polynomial into the two column polynomials \(A(z)+wB(z)\) and using character orthogonality gives the autocorrelation identity in `RESULT.md`. Substitution of \(x=\cos(v/2)\), \(y=\cos(u-t/2)\), and \(z_0=\cos((v-t)/2)\) yields the displayed sum of nonnegative terms, which proves the continuous lower bound and yields the complete equality conditions. The upper bound comes from \(\sum_h|R(h)|^2\le\sum_hN_h^2=114\), with each nearest-neighbor correlation saturating only for a character-phase array.

Run `python3 checker.py`; no third-party packages are required. Its exact Gaussian-integer enumeration checks all 64 binary and all 4096 quaternary arrays, including 8 and 192 minimum cases. It checks the three normalized minimizers and the maximizing character phases. The numerical finite-Fourier checks use grids with no relevant aliasing. These finite checks cannot establish the infinitely many continuously varying phases by themselves; the symbolic sum-of-squares argument supplies that proof.

The algebraic phase-alphabet count assumes an exact \(q\)-th-root alphabet; it is not a finite-precision classification. For the compact-group and finite-grid statements the fifteen-character separation is a necessary stated hypothesis. Priority comparisons used accessible published primary text, but older specialized single-array tables may exist. Independent audit has not been performed.
