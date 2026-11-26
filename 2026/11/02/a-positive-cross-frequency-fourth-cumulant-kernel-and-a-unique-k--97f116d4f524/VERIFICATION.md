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

At D_r=1 use ordered gaps u,v,w and P=e^(−u−w). The angular four-point is P(1/4+e^(−4v)/8) by the zero-total-charge constraint, while the direct and crossed products of angular two-points are P/4 and Pe^(−2v)/4. Expand the independent speed by Wick and subtract each product using its paired speed factors. For the constant-speed coefficient the resulting integrand is P(e^(−4v)/8−e^(−2v)/2), which integrates with factor 24 to −21/4. Put L(x)=6/x+3/(x+4)−6/(x+2). The direct and crossed contributions to the λμ² kernel sum to 3/[2(1+q)]+(q+2)² L(q)/(q+1)². The λ² kernel is 3/[4(q+1)(r+1)]+(q+r+2)² L(q+r)/[2(q+1)²(r+1)²]; here the two crossed pairings give the outer factors 1/[(q+1)(r+1)] and the symmetrized mean of (q+1)^−2 and (r+1)^−2. Combining fractions gives the stated a and b, so a pair of distinct atoms contributes 2b(q,r), not b(q,r). Every surviving term is exponentially bounded in all three gaps using the spectral gap and finite measure, also after multiplying by u+v+w. Thus the exact finite-window weight (t−u−v−w)_+ gives K₄t+O(1) and the gap rescaling restores D_r^−3. Integrating the two-point correlation and adding independent thermal variance gives K₂; thermal noise adds no fourth cumulant. Positive kernels give a single positive root for μ≠0, and no sign change for μ=0, λ>0. For K₂>0 the normalized cumulant at the root is O(t^−2).

## originality

PASS

Credit the one-OU physical model, earlier exact moment methods, and standard cumulant identities. Pass the distinct evaluated off-diagonal positive coefficient, extension to arbitrary finite gapped positive spectra, and the resulting unique long-time sign threshold for the nonzero mean case. Do not claim the one-OU setting itself or transient kurtosis reversals as new.

## value

PASS

An explicit positive mixed term answers a question that checking one relaxation time cannot settle: whether combining modes preserves a single reversal as speed variance increases. The theorem handles continuous spectra and explains the disappearance of the inverse-time kurtosis term at the unique nonzero-mean threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
