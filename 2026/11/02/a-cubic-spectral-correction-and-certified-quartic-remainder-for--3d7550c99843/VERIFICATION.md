---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a_i=λ_i−1/n, the normalized Gaussian square representation gives Dirichlet(1/2,...,1/2) spherical squares. Independently, E[(X−1)^j]=n^j j!/(n/2)_j times the degree-j coefficient of ∏_i(1−a_i t)^(−1/2). The linear coefficient vanishes; expanding exp(∑_(j≥2) A_j t^j/(2j)) gives exactly the second, third and fourth moments in (4). On writing r=√x, the scalar cubic residual factors as (r−1)^4(r²+4r+5)/16, including at x=0. Rewriting in powers of x−1 gives the asserted kernel; its derivative in r has sign −2r²−10r−16, hence its multiplier is in (0,5/16]. This proves both bounds in every dimension, including singular H. The fourth-moment to variance-squared ratio is at most 15n(n+2)/[(n+4)(n+6)]≤15, by A_4≤A_2². Cauchy–Schwarz then bounds the cubic by √15 v^(3/2); effective-rank divergence makes v→0, and when A_2>0 the relative error to v/8 tends to zero. The two-band positive spectra realize the leading constant, and the equal-A_2 profiles have A_3=±6δ³ and A_4=18δ⁴, giving exactly the stated difference and its sign. The supplied verifier and recorded output were inspected, not used to certify the analytic result.

## originality

PASS

The prior functional, exact variance and qualitative effective-rank criterion are established. The inspected prior sources do not give the signed cubic correction or a uniform two-sided quartic enclosure on the full semidefinite domain; neither their coarse variance bound nor their exact integral representations directly supply that statement. The sharper relative leading law is a consequence of the checked refinement. This is bounded distinctness, not a priority guarantee.

## value

PASS

This gives an explicit interval for a deterministic coefficient used in hard-edge analysis, uniform up to zero eigenvalues and without a pointwise perturbation assumption. The locality of the ordinary square-root Taylor expansion is a real issue at that boundary. The relative leading constant and signed equal-purity discrimination add spectral information beyond the earlier coarse upper bound. It is a useful refinement of the coefficient, not an improvement in the underlying universality error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
