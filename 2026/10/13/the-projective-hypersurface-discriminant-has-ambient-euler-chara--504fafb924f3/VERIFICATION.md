---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n,d>=2 over C and N=binom(n+d-1,d), choose diagonal one-parameter subgroup with weights 1,B,...,B^(n-1), B>d. Degree-d monomial weights are pairwise distinct by base-B representation, so ambient P^{N-1} fixed locus consists of N coordinate monomials. Every monomial defines a singular projective hypersurface except xy for (n,d)=(2,2): a pure power is nonreduced, and for n>=3 distinct coordinate components meet; binary reduced monomial xy exists only at d=2. Thus the smooth coefficient-space U fixed locus is empty except one point for binary quadrics. Algebraic C* Euler localization gives chi_c(U)=0 or 1 respectively, and additivity gives chi(D)=N or 2. The independent checker verified 2969 monomial cases with exact weight distinctness; infinite proof is symbolic.

## originality

PASS

Classical discriminants, the nonsingular form open set, Euler localization, and torus weighting are prior tools. Alper–Isaev arXiv:1407.6838 studies the same nonvanishing-discriminant open forms but concentrates on associated forms/invariant theory, not coefficient-space Euler characteristics. Searches in discriminant/topological Euler/Veronese dual/smooth parameter space language and Resultary uncovered no earlier precise all-(n,d) ambient-Euler identity with the binary-quadratic exception. Significant folklore risk given short localization.

## value

PASS

The discriminant is a fundamental projective parameter-space boundary. A uniform characteristic across all dimensions and degrees, plus the exceptional pair and compactly-supported complement vanishing, is a reusable exact invariant distinguishing coefficient spaces from moduli quotients. The fixed-locus classification is object-dependent, not a generic numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
