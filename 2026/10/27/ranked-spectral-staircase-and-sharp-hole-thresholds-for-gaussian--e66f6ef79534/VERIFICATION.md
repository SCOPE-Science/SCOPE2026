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

# Verification record

## Direct reproducible checks

Run `python3 check_spectral_staircase.py` with the Python standard library. The checker run on the packaged source returned:

`CHECK_OK: 735 exact coefficients, 224 spectral tests, 18 asymptotic tests`

The program checks exact rational binomial coefficients and selected floating-point spectral comparisons and asymptotics; the test parameters are explicit in its source. It does not certify the infinite theorem. The general proof uses an exact one-sign-change polynomial, strict discrete unimodality, and uniform expansions of a factorial-geometric-mean integral.

## Analytical boundaries

The claims require \(s>0\), integers \(N\ge1\) and \(k\ge0\), and the standard one-dimensional Gaussian Fock normalization. Thresholds are for annuli of *fixed area* \(s\); asymptotic error constants fix the parameters stated in the theorem. No higher-dimensional, other-window or uniform double-scaling result is asserted.

## Source checks

The primary full texts compared were arXiv:2607.28376 (introduction and sections on Ky Fan concentration and proof), arXiv:2503.07069 (radial spectral formulas, Theorems 1.3/1.5 and Section 4), and the accessible author-hosted full text of Grudsky--Vasilevski (2002) on radial Toeplitz operators. The older first-pair annulus formula \(A_{0,1}(s)=s/(e^s-1)\) is expressly prior, not claimed new. Equivalent unindexed spectral-order descriptions remain a residual priority risk.

Independent audit has not been performed.
