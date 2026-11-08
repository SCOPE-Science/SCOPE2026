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

For every b>0, the weighted analytic Bergman space monomials diagonalize the radial Toeplitz operator, with eigenvalue equal to the beta-prime mass ∫_{3^{n/2} C_n} t^k/[B(k+1,b)(1+t)^{k+b+1}] dt. Even n=2m splits exactly 3^m C_{2m}=∪_{a∈D_m}(a+C_m), and odd n=2m+1 splits to √3(D_m+C_{m+1}); the latter Jacobian gives the essential √2 prefactor. Cantor-stage probability µ_m→µ and digit counting bound #{a∈D:a≤T}=O((1+T)^δ), δ=log2/log3<1, yield the fixed-mode Cantor-integer integral limits and convergent tails O(T^{δ-b-1}). For all modes k≥1, the gamma beta normalization and e^{-k/(1+t)} give uniform renormalized eigenvalue bound C_b(k+1)^{δ-1}→0, so the spectral supremum converges to the attained finite maximum; positivity follows from k=0 and a=0. Independent exact Fraction testing reconfirmed 16 nontrivial/even-stage direct-vs-digit beta-prime identities at b=1, n=0,2,4,6 and k=0..3, with renormalized k0 [0.5,0.609090909,0.64216444,0.650303469]. The all-b and all-n statements rest on the analytic tail proof, not those finite cases.

## originality

PASS

Best-of-knowledge originality judgment for the exact scoped final claim, after mathematical prior-work implication comparison. Published beta-prime finite-n formulas and norm order estimates are credited; no retrieved source establishes the two exact operator-norm subsequential limits and uniform high-mode escape bound.

## value

PASS

The sharp leading norm constants are the quantitatively natural open refinement of a known middle-third fractal concentration exponent. The theorem supplies two computable Cantor-integer limit expressions and a uniform high-degree compactness principle for the full Toeplitz norm; this is useful beyond fixed finite-stage eigenvalue tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
