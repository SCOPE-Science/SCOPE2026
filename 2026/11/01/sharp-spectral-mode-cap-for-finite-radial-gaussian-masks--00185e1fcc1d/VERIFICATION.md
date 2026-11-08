---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Monomial diagonalization follows by polar integration. Integration of d(t^{n+1}e^{-t}) yields (n+1)!(lambda_{n+1}-lambda_n)=F(n+1) with 2K distinct endpoint exponentials (or fewer if a_1=0). The Rolle induction for real exponential polynomials bounds their zero count by 2K-1; adjacent sign reversals force separate zeros, and alternating peak/gap signs give <=K strict maxima including the one-sided n=0 case. For every K the separated intervals [M_j,M_j+1/2] have positive F(M_j) and negative F(M_j+1), and newly appended large M preserves old strict maxima; expansions 1/(8M) and -3/(8M), compared to O(B^{M+1}), prove the induction, realizing K modes and 2K-1 changes. Finitely many 90-digit examples are illustrative only, not evidence for all K.

## originality

PASS

The general exponential variation bound is classical and is NOT claimed new. Knutsen works out one ring and Halvdansson treats rearranged finite-annulus spectra, while the specific simultaneous sharp bound and all-K realization in natural monomial order is not found in inspected close works or Resultary. Best-of-knowledge only; older total-positivity sharpness constructions might cover it.

## value

PASS

A sharp component-count bound with attainable 2K−1 oscillations for a natural radial spectral concentration operator supplies structural spectral-complexity information independent of asymptotic eigenvalue rearrangements. Attainability for arbitrarily many annuli is a motivated, nonroutine construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
