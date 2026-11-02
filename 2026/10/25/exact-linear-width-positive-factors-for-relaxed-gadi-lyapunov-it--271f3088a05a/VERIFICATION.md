---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Eliminating the source fixed-shift two-stage GADI equations with alpha>0, 0<=omega<2, F positive stable, Q=C^T C and X0=0 gives exactly X_{k+1}=c X_k+b T X_k T^T+E E^T with c=omega/2, b=1-c>0, H=(alpha I+F)^-1, T=2alpha H^T-I, E=sqrt(2alpha b)H^T C^T. As identity and congruence operators commute, the binomial theorem yields X_k=sum_{j=0}^{k-1}w_{k,j}T^j E E^T(T^T)^j, w_{k,j}=b^j sum_{r=j}^{k-1}binom(r,j)c^{r-j}>0, giving exact PSD factor with kp columns. Its rank is the dimension of rational Krylov span, and diagonal distinct eigenvalues with p=1 yield rank min(k,n) by Vandermonde. Separate exact rational nonsymmetric 2x2 verification k=1..5 confirms both forms; infinite claim rests on algebraic identities.

## originality

PASS

Zhang–Xun gives the exact source recurrence and exponential-width direct factor for nonzero relaxation, while equation (7) gives k p columns in unrelaxed ADI. The positive binomial Krylov factor for relaxed GADI is not stated in the inspected primary equations; its conceptual basis is standard but the exact stated compression is a motivated family-specific identity. Qualified against equivalent weighted Smith methods.

## value

PASS

Shows the same relaxed GADI Lyapunov iterate admits a transparent, exact positive low-rank factor with linear rather than exponentially growing column count (k p versus (2^k−1)p in the source construction). The positive weights and rank-span identity are structurally relevant to storage and redundancy, while no finite-precision acceleration is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
