---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

RESULT.md lines 11–51 are correct in their two separate regimes. Competing reset/jump clocks make event times Exp(r+2d) independently of marks. Repeated trials select the single-trial success law. A route of length L+2 has exactly one extra opposite pair; premature hits are precisely the K minimal routes followed by either two-hop return in the marked coordinate. The subtraction is 2K even when m_j=0; c_j≥L. Parity plus a geometric bound controls both the tail and its first moment at fixed d,m. The duration conditional on N=n is exactly Gamma(n,1) after scaling; the leading signed mixture correction has only Gamma(L+2) minus Gamma(L), whose densities cross at sqrt(L(L+1)). In high dimension the Bessel integral is the unrestricted walk series, and first-hit convolution gives the quotient of Green functions. The remainder bounds follow by factoring I0^p−1−px² (Taylor in I0−1, using 0≤I0−1≤x²e^{2x}, I0≤e^{2x}) and expanding the I2 factor separately; e^{-(1−2c)s} dominates the polynomial remainders uniformly at q=c/d, c=(α+2)^{-1}<1/2. Integration gives the q⁴ terms 12d−8 and 2d in the numerator and denominator, hence 10d−8 in the first-hit series. To justify the hop moment without differentiating big-O, use positivity: choose fixed λ>1 with λc<1/2 and bound n q^n≤C_λ(λq)^n, applying the same tail bound at λq. The resulting mixture and expectation errors are O_α(d^{-2}). At α=2, c=1/4 yields 5/8 and 5/4 as stated. No optimum is inferred. Independent replay: python3 /workspace/review-evidence/reproduce.py 5 (log /workspace/review-evidence/5.txt); 120 signed starting sites, independent interleaving/renewal counts in seven dimensions through order ten, and numerical quadrature of five TV constants. These are bounded corroboration, not uniform-tail certificates. The supplied verifier was inspected, not run.

## originality

PASS

The supported distinction is the explicit coordinate-marked first-detour law and quantitative successful-segment corrections in two limits. The reset model, observation that the last route localizes, exact unmarked transforms, and general geodesic dominance are prior. The scalar transform implicitly determines the unmarked hop and duration laws; their extraction and the uniform/error calculations are refinements, not a new renewal principle. No checked statement covers the combined marked law with the sharp corrections.

## value

PASS

The two-hop cutoff is fixed by lattice parity, not chosen to maximize an effect, and the high-dimensional scaling is motivated by a published measurement of exactly this successful segment. The directional split identifies the transverse source of the first localization error, and the explicit TV coefficient measures the accuracy of a usable leading Gamma approximation. These are useful refinements of the known scalar mechanism, not a claim of a general renewal theorem or of optimal resetting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
