---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Pinned RESULT.md reduces the STFT localization operator by frequency Plancherel to multiplication by m(t)=pi^{-1/2}int_E exp(-(t-y)^2)dy. Its derivative is (2exp(-t^2)/sqrt(pi))[exp(-a^2)sinh(2at)-exp(-b^2)sinh(2bt)]. x coth(x) strictly increasing makes sinh(2bt)/sinh(2at) monotone for t>0, giving a unique threshold and no other extrema. At the threshold q=ae^{-a²}-be^{-b²}=0, the derivative cubic coefficient is -8c(b²-a²)/(3sqrt(pi)), hence m(0)-m(t)=2c(b²-a²)t^4/(3sqrt(pi))+O(t^6). The IFT at t²=0 proves square-root peak splitting and quadratic norm gain. Near noncritical simple peaks Taylor gives s^{1/2}; nonconstant analytic finite-monotone-branch m gives only absolutely continuous multiplication spectrum [0,M], no eigenvalues. Independently evaluated nine critical fourth-order ratios for three widths, including w=1, a_c=0.271702319209... . The smooth-spectral expansion is not inferred from those finite tests.

## originality

PASS

Best-of-knowledge published-result and primary-literature implication comparison; concrete matching/overlap and residual risks stated, not a novelty certification.

## value

PASS

The family is a natural frequency-unrestricted Gaussian localization multiplier, with an exact spectral-edge bifurcation (coalescing maxima) and explicit 1/4 critical exponent/unfolding coefficient. That stronger spectral statement is more than calculating one Gaussian integral; it distinguishes continuous essential spectral edge from a compact-localization eigenvalue count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
