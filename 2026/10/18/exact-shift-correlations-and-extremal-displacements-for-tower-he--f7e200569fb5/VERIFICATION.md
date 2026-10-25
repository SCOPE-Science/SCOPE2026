---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: The smallest forbidden prime exponent for h(n)>k is T_k by induction on factorization height, T1=2,T(j+1)=2^{T_j}. For fixed t and prime p, conditioning on v_p(n)=a relative to r=v_p(t) yields joint-forbidden gamma_{p,k}(r), including p=2 cancellation case, and local good probability 1-2beta+gamma. CRT gives finite-prime exact densities and uniform high prime-power tail O(sum_{p>Y}p^{-T_k})+o_X(1), proving convergence of the product for fixed k>=2 and t!=0. Gamma=0 iff r<T_k since forbidden exponents are unbounded; hence exactly T_k-free minimizing shifts. Local factors are <=1-beta, with strict loss at p not dividing any fixed t; dominated convergence along factorial displacements gives supremum c_k (not attained), and covariance changes from negative at shift 1 to eventually positive at factorial shifts.

## originality

PASS

PASS (best of knowledge): De Koninck–Verreault establish the tower-height recursion and one-point c_k; Srichan et al Theorem 1.1 gives the two-point product for n,n+1 (covered Q_k(1)); Mirsky handles usual power-free sets with contiguous forbidden exponents. The present gappy tower forbidden-exponent set, arbitrary displacement p-adic overlap law, complete minimizer set, unattained supremum and covariance sign reversal go beyond these statements.

## value

PASS

PASS: Shifts of a natural multiplicative height-level set create a meaningful two-point correlation problem. The exact p-adic law resolves an infinite family of integer displacements, identifies all extremizers by an explicit T_k-free condition and exhibits both correlation signs, information not implied by the one-point density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
