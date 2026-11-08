---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all n>=6, reflection length is n-c(pi); the central Jucys polynomial acts on irrep lambda with coefficient sum E_lambda(p)=sum_{r>=1}a_r r^p. At hook (n-2,1,1), the signed Laplace integral of (1-z)(1-2z)prod_{j=1}^{n-3}(1+jz) has one negative interval 0<t<log2 and one positive interval t>log2. Weight t^{-1-p} strictly tilts their ratio; F_m(0)=-1 and F_m(1)=(m+1)! yield the unique beta_n in (0,1). Multiplying the integrand by (1+(m+1)e^{-t}) shifts the root strictly lower; the stated explicit integral bounds establish beta_n<100/m! for m>=50. At n=6 the exact rational checker bounds the root and checks all ten nontrivial irreducible branches; f^(4,1,1)=10 gives nullity 100 and centered rank 619. Independently reconstructed the 11 S6 content polynomials/eigensigns and numerical root ~0.1541377738, separate from the exact Fraction certificate. No exact wp_n asserted for n>=7.

## originality

PASS

Classical Jucys content diagonalization and general negative-type interval theorems are prior art. Neither those nor relevant transposition Cayley graph adjacency work yields the fractional exponent obstruction, its factorial n-growth, or exact S6 negative-type endpoint and nullspace. Best-knowledge, not historical uniqueness.

## value

PASS

Infinite family of exponentially shrinking-in-exponent negative-type obstructions for a classical and natural permutation metric, plus sharp finite S6 exponent and exact 100-dimensional endpoint kernel. The structural signed-integral argument and representation-theoretic branch check are mathematically consequential, not a renamed routine table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
