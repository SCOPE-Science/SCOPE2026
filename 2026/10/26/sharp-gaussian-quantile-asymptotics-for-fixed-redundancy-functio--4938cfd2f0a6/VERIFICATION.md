---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Fix s>=1 while t tends to infinity. The imported exact Rajput–Jagatti–Rajan/Harper two-class criterion is |N_{2t}(I_M)|-M<=2^n-2^k for all class sizes M<=2^{k-1}. The balanced choice M=2^{k-1}=p_s2^n, p_s=2^{-s-1}, has binomial radius quantile j=n/2-z_s sqrt(n)/2+o(sqrt n), z_s=Phi^-1(1-p_s). The ball B_{j-1+2t} lies inside its 2t-neighborhood, violating capacity whenever n/t^2<c_s=4/z_s^2. For all M, the simplicial-initial-segment containment bounds the neighborhood increment by 2t+1 consecutive binomial layers. Uniform Berry–Esseen gives interval mass Phi(x+a)-Phi(x)+O(n^-1/2), x<=-z_s+O(n^-1/2), a=(2t+1)/(sqrt n/2), so for n>=(c_s+epsilon)t^2 one has a<2z_s and the interval mass lies strictly below 1-2^-s with uniform margin. This proves universal eventual success for ALL k above threshold and matching liminf using one balanced counterexample at each c<c_s. Verified script verify_threshold.py logic and short-cube neighborhood and integer-binomial tests; finite t checks do not establish the asymptotic. Restrictions s<=2t hold automatically for all large t with s fixed.

## originality

PASS

The 2026 primary Rajput–Jagatti–Rajan work states the exact finite neighborhood criterion, a quadratic upper bound, and highlights the growth-order gap; those statements are correctly imported as prerequisites rather than claimed new. The assigned theorem gives a matching lower obstruction from balanced classes and an exact sharp Gaussian-quantile constant for every fixed redundancy. Harper isoperimetry and Berry–Esseen are classical ingredients, but neither their isolated statements nor the cited finite-code paper explicitly yields the quantified all-class asymptotic without the interval optimization argument.

## value

PASS

Determining the threshold at which EVERY two-valued function admits a short nonsystematic error-protection encoder is a natural universal coding-theory question. A sharp redundancy-dependent constant closes the prior gap for fixed s and separates balanced worst-case obstructions from unrestricted nonlinear encoders. The result is not merely a numerical recalibration of a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
