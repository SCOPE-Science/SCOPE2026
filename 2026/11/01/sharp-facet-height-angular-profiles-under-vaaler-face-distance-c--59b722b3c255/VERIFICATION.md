---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The prefix-constrained Gaussian orthoscheme q1=s=h², r_k=sum_{j<=k}q_j>=k has minimal feasible closed prefix sequence r*_k=max(k,s), q*_j=r*_j-r*_{j-1}. Abel summation against ordered squares makes the quadratic exponent >= the q* exponent, yielding the exact Gaussian supremum. After ordered-square change, Psi_n(sqrt s) equals an expectation of a strictly decreasing positive Jacobian factor times a nonincreasing exponential; hence it decreases, with derivative jumps at s=2,...,n from newly active (z_k²-z_{k+1}²). For s>=n, integrate z2..zn to get Psi=n2^{n-1}Gamma(n/2)/(pi^{n/2}h^{n-1}). The cited Rogers/Karasev orthoscheme flag-area contraction transfers the Gaussian comparison to each facet under full affine-face-distance hypotheses; summation gives the surface bound. Direct radial Jacobian yields sharp high-height truncated-cube infimum. In n=2, elementary angular Gaussian integration and the stated trapezoid give all intermediate h equality. Independently checked the n=2 piecewise formula and threshold numeric samples and the algebraic q* prefix logic. Residual correctness risk: inaccessible full text of the crucial Zwierzyński surface-area extension prevents line-by-line external validation of the transferred estimate, though the proof states the exact needed comparison and its scope; this is a limitation, not a false assertion of reading.

## originality

PASS

Zwierzyński’s extension proves the global sharp surface area n2^n, Karasev proves underlying flag contraction in low dimensions, and Resultary equality rigidity covers the all-unit Gaussian optimizer. None of these *inspected statements* supplies the retained exact h-dependent Gaussian supremum, its individual facet angular ratio, thresholds, or sharp planar trapezoids. Since the strongest source was accessible only in summary form, possible implicit profile coverage remains an explicit risk. Best-of-knowledge PASS based on actual statement comparisons rather than indexing absence.

## value

PASS

The old Vaaler surface lower bound is global. A facetwise sharp h-dependent coefficient with exact Gaussian extremal profile, n-1 strict analytic phase thresholds, complete planar equality construction and a high-height geometric limiting realization resolves natural local quantitative questions. The intermediate-dimensional geometric sharpness is explicitly *not* overclaimed. This is a motivated nontrivial refinement of the global inequality, not a routine equality restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
