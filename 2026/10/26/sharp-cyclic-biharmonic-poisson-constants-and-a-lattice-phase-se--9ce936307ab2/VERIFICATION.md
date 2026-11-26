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

The second difference of d(n−d) and its square gives L_nb=g, including the cyclic wrap at zero; the two displayed power sums make b mean zero, and L_ng=δ_0−1/n. Connectedness ensures uniqueness on the mean-zero domain. At d=floor(n/2) the kernel numerator is −7n⁴/8−5n²−11 for even n and −7n⁴/8−5n²/4+17/8 for odd n, both negative; monotonicity on the half cycle gives the exact cutoff including possible zeros. All absolute row and column sums agree. A row-sign vector and a unit impulse attain the respective norms on the full counting-measure spaces, not on the mean-zero restriction. Zero row sum and symmetry yield four times the half-weighted positive-side sum; expanding t(t+2) gives the stated Faulhaber form. In its Euler–Maclaurin expansion, f(ξ)=0 and f′(0)=0 remove the order-n³ term and the lower derivative term. The upper shift δ=k−nξ contributes f′(ξ)(δ²/2+δ/2+1/12); k=nξ−{r_n}+O(n⁻¹) with bounded δ makes the remainder uniform O(n). Irrationality of ξ and the continuous periodic extension of B₂ give all and only the claimed limits, since every tail of the irrational rotation is dense. Read the frozen checker without executing it. Independent `python /workspace/branches/review-computations/check_finite.py` used (L²+11ᵀ/n)⁻¹−11ᵀ/n to reproduce the exact kernels, cutoffs and attained row norms at n=3…13; universal and asymptotic claims are proved analytically, not by the sample.

## originality

PASS

The supported distinct result is the sharp full-space endpoint norm of the squared inverse and its exact nonconstant second-order phase law. Biharmonic Green spectra and first-inverse cycle norm/phase methods have substantive antecedents, and no standalone priority for the quartic kernel is asserted. The closest distinct catalogue finding concerns L_n^†, not (L_n²)^†, and does not decide the latter norm or phase. Neither positive bibliographic evidence nor catalogue labels alone establish historical priority.

## value

PASS

The exact constant and attaining forcing patterns quantify worst-case amplification for the canonical cyclic biharmonic Poisson solve on the stated full spaces. The nondegenerate order-n² correction interval shows that even the second coefficient in a continuum-based power expansion cannot be a constant. That is a precise discretization effect on a natural operator norm, not just a new evaluation of a biharmonic distance or trace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
