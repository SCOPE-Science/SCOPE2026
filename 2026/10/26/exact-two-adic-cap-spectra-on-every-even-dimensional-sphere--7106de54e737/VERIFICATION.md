---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Funk–Hecke on S^(2k) with alpha=k-1/2 and rational c=p/q (q even, p odd, s=nu2(q)>=1) yields multipliers from cap integrals. Gegenbauer Rodrigues integral gives Lambda_ell=(2k-1)(1-c^2)^k C_(ell-1)^(k+1/2)(c) /[ell(ell+2k-1) binom(ell+2k-2,ell) B_k(c)]. In the explicit Gegenbauer coefficient expansion all nonleading ratios have nonnegative 2-adic valuations, while c has valuation -s; unique leading term gives nu2(C_m)=-nu2(m!)-ms. In B_k a unique highest-degree monomial dominates, nu2(B_k)=-(2k-1)s; 1-c² has valuation -2s. Combining gives nu2(Lambda_ell)=-ell*s-nu2((ell+2k-1)!/(2k-2)!) including ell=0 by 2k-1 odd. Thus all multipliers nonzero, hence injective by harmonic completeness; Hilbert–Schmidt compactness means unbounded inverse. Independently integrated rational Funk–Hecke multipliers and verified exact valuations in 108 cases k=1..4, ell=0..8, c=1/2,-1/4,3/8; infinite claim follows from p-adic dominance, not finite sample.

## originality

PASS

Prior Bilyk–Mastrianni–Steinerberger (2023) Lemma 7 already contains the cap/Gegenbauer integral identity and Example 3 proves C_n^(3/2)(±1/2) never vanishes, hence the S² at ±1/2 injectivity special case is COVERED and is not claimed new. Their focus on Gegenbauer lower bounds and radius discrepancy does not give the all-k, all-even-denominator rational height 2-adic valuation formula; Frye–Efthimiou gives diagonalization, not arithmetic valuations. The proposed full two-adic spectrum and resulting dense injective family survive the narrower prior coverage.

## value

PASS

The precise prime-adic denominator formula over every even-dimensional sphere and a dense arithmetically specified family of injective moving-cap transforms is a natural harmonic-inverse invariant. It sharply separates uniqueness from ill-conditioned inversion and is not implied by one special nonvanishing cap radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
