---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The assigned RESULT.md blob d7d36258290321c75374ce91ddfc22165156a4a7 defines F_c(z)=√c exp(i[-log c/π] Log[(1+z)/(1−z)]) for every 0<c<1. Right-half-plane W and principal branch give c≤|F_c|≤1, bounded inverse (hence outer) and unimodular radial values on lower semicircle I, modulus c on upper. L_c(g)=2∫_I g* conjugate(F_c*)dm is weak-star continuous norm≤1 and L_c(F_c)=1. E_N,c=z^(N−1)H∞∩ker L_c has exact codimension N: for any odd k≥N−1, L_c(z^kF_c)=2/(π i k)≠0, independent of N−1 Taylor kernels. If a norm≤1 representative h of F_c+E has L_c(h)=1, equality in the boundary-average disk forces h*=F_c* a.e. on I; Privalov boundary uniqueness gives h=F_c. Thus coset has norm one, unique norm minimizer, is exposed/extreme in H∞/E, and finite quotient dimension N upgrades extreme to strongly extreme by compactness. Every inner Θ has ||F_c−Θ||∞≥1−c due to upper semicircle modulus. Exact complex/Fourier computations independently checked odd/even coefficients and the boundary formula; no sampling is used for the universal analytic proof. No invariant-ideal or infinite-dimensional quotient conclusion.

## originality

PASS

PASS on bounded comparison with Dyakonov arXiv:2603.29103 full primary Section 1: Theorem 1.3 treats ordinary quotient extremity and the final paragraph asks about strong quotient extremity with a unique inner minimizer. The stated finite-codimensional kernel construction directly disproves necessity for unrestricted weak-star closed subspaces. The related 2023 strong-extreme theorem concerns finite-codimensional SUBSPACES, not finite-dimensional QUOTIENTS. A generic exposed-point argument might have previously implied similar examples; residual priority risk is explicit.

## value

PASS

Refuting the expressly formulated 2026 unrestricted Hardy-quotient conjecture is a concrete motivated mathematical result. The exact finite-codimensional analytic construction works in every quotient dimension, has a uniquely minimizing invertible non-inner outer representative arbitrarily far below unit boundary modulus, and clearly exposes which missing invariance assumption might be essential. An elementary construction is scientifically useful when it settles a stated natural yes/no criterion, without claiming an infinite-dimensional classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
