---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For any positive period n, equality of Laurent principal ideals permutes the finite x-support by I ↦ A^n I − u. A power of that permutation fixes every support difference; no eigenvalue of A has modulus one, so the difference must be zero. The periodic primes are therefore precisely vertical primes, all fixed by F_r. On an infinite orbit only finitely many primes could be contracted by the birational marking. A block of contracted primes between noncontracted ones sends a divisor of X to a lower-dimensional center and then reappears as a divisor. The intermediate center must be in the indeterminacy of the corresponding further iterate, since a morphism there could not raise its dimension. The divisor criterion for NS stability rules this out. After removing the finitely many fixed contracted primes, codimension-one correspondence identifies all remaining torus primes with the primes of X off the inverse-exceptional boundary. Divisor localization thus gives the exact boundary sequence, with kernel generated freely by x_i, y_j and inverted vertical equations modulo constants, and Pic(X)=NS(X) since X is smooth projective rational. Pullback of an effective boundary divisor is effective and remains on the boundary: a nonboundary prime is a prime of the surviving open and its forward image is the corresponding nonboundary prime. The principal-divisor formula intertwines the kernel action A ⊕ I and the quotient NS action. Stability and birational invariance of the first dynamical degree give quotient spectral radius |α|; the boundary matrix consequently has spectral radius |α| and peripheral eigenvalue α. Perron–Frobenius forbids its phase: equality of powers of α and its conjugate would give a repeated root of a rational cubic, hence a rational repeated root and a rational integral third root β^m in (0,1). The example was independently checked by exact determinant evaluation for tI−A at t=−1,0,1,2 (values −3,−1,1,9), determinant 1, and cubic discriminant −31; sign and rational-root tests give the required irreducible spectral type. The uploaded example checker was inspected, not executed, and does not verify the assertion over all models.

## originality

PASS

The supported increment is identity products on arbitrary smooth projective birational models for this cubic family. Neither rank-three nonexistence nor the toric identity-product obstruction is new. The closest non-toric product theorem specifically requires independent translations and omits the identity.

## value

PASS

This resolves a specified family in an explicitly raised identity-product problem without assuming toricity. The argument identifies exactly which contracted divisors are harmless and how their invariant units affect the spectral obstruction, rather than merely checking that adding eigenvalues one leaves the toric obstruction unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
