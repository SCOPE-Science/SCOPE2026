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

On normalized source monomial e_{ℓ+n}, differentiating gives (ℓ+n)!/ℓ!, and converting the output coefficient at qℓ+j to the normalized target basis gives the factors (ℓ+n+1)^{(β₁−1)/2}(qℓ+j+1)^{(1−β₂)/2}. Each fixed nonzero band is asymptotic to p_j c_q ℓ^{−Δ/2}; output indices are distinct within a column, giving unboundedness when Δ<0. A finite sum of bounded bands gives boundedness for Δ≥0. At Δ=0 each residue block is a Hardy shift band weighted by a convergent diagonal, so discarding the finite differentiation kernel gives the column of analytic multipliers modulo compact operators. The Gram model is the scalar Toeplitz compression of H. Its quadratic form places the spectrum in [min H,max H]; normalized Szegő kernels are weakly null and give a Weyl sequence at each attained value by continuity and kernel concentration. Thus the Fredholm essential spectrum is the full scaled interval and the essential norm is c_q sqrt(max H) by the essential C*-identity (equivalently using an off-diagonal block on the source-target direct sum). The only kernel is the first n source monomials, by polynomial density, continuity of holomorphic evaluations and injectivity of multiplication/composition after differentiation. Hence zero in the essential spectrum contradicts closed range, while a positive lower edge gives Fredholm Gram and closed range. At Δ>0 finite-column truncation bounds s_N above and qL>deg P provides disjoint supports for columns ℓ=Lm and the min–max lower bound. The p-series endpoint diverges, including for quasi-norm Schatten parameters below 1. The verifier was inspected, not executed. An independent exact Gaussian-integer coefficient calculation (python3 reproductions/frozen_math_checks.py, polyphase) checked 300 complex Gram comparisons; this is not spectral evidence for the infinite theorem. The original checker uses real coefficients in its Fourier comparisons, so its exponent-sign comment does not test the complex orientation; the analytic Toeplitz form is unaffected.

## originality

PASS

Pass the explicit critical essential Gram interval and common-root boundary for the stated nonlinear power, arbitrary polynomial multiplier and coefficient-index differentiation family, combined with the all-region classification. Neither standard Toeplitz tools nor the known monomial index-counting cutoff are credited as new. A later catalogue record has substantial overlap in the exact limiting model but concerns a different operator; earlier priority beyond the inspected statements is not established.

## value

PASS

The result classifies a natural operator family's critical positive spectrum, not merely scalar boundedness. The P=1+z and P=1+z² example at q=2 distinguishes closed range for identical coefficient magnitudes and shows why the exact residue grouping matters. That structural diagnostic and the compact-side endpoint are useful beyond an isolated norm calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
