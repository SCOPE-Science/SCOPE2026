---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

σ_k^{-1} prime-power values are -(1+p^k), p^k, and 0 for exponents 1,2,≥3. Prime-cube cases have J_k+3>4^k+3; squarefree even cases are growing sums of two positive products; squarefree odd cases have growing difference D_r-2. For cube-free nonsquarefree n=ab², F=b^k[μ(a)σ_k(a)+J_k(a)J_k(b)]+3 with coprime squarefree a,b. For μ(a)=1 direct lower bound yields equality at a=1,b=2 only; for μ(a)=-1, σ_k(a)/J_k(a)<ζ(k)²/ζ(2k)≤5/2 yields T>2^k, including the delicate b=2,k=2 strict endpoint. Independent divisor-convolution calculations n<600 for k=2,3,4 show minima (19,4),(67,4),(259,4). Finite checks corroborate an all-exponent proof.

## originality

PASS

The original September 2026 detector and a related published parameter-stability result prove its prime zero-set, but zero-set stability does not determine the exact unique smallest composite residual. The uniform sharp separation is additional.

## value

PASS

The exact nonzero composite separation margin and unique smallest false-positive residual are natural quantitative invariants of a published prime-zero detector; no computational speedup is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
