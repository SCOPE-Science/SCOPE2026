---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

1. **Fixed matrix.** The definitions \(F_t=u(f+t w)^{\mathsf T}\) and \(V_t=V+tuw^{\mathsf T}\) satisfy \(F_t-V_t=F-V=J\) identically.
2. **Invertibility.** With \(s=w^{\mathsf T}V^{-1}u\ge0\), the matrix determinant lemma gives a nonzero factor \(1+ts\) for every \(t\ge0\). Sherman--Morrison therefore gives the claimed inverse.
3. **Regularity boundary.** Because \(F_t\ge0\) automatically, the transferred pair is regular exactly when the explicit Sherman--Morrison inverse is entrywise nonnegative. No stronger automatic-preservation assertion is used.
4. **Spectral radius.** A nonnegative rank-one matrix \(ab^{\mathsf T}\) has spectral radius \(b^{\mathsf T}a\). Applying this first to \(FV^{-1}\) and then to \(F_tV_t^{-1}\) proves the exact fractional-linear law.
5. **Threshold geometry.** Subtracting \(1\) gives \(R_t-1=(R_0-1)/(1+ts)\). If \(s,t>0\), the multiplier lies strictly in \((0,1)\), so the side of threshold is preserved and the distance to threshold is strictly reduced.
6. **Concrete source formulas.** For positive \(A,B,C,D\), direct subtraction from the two displayed formulas yields \(R_a-1=[AD-B(C+D)]/[B(C+2D)]\) and \(R_c-1=[AD-B(C+D)]/[B(C+D)]\). Their quotient is \((C+D)/(C+2D)\in(1/2,1)\).
7. **Limits.** No claim is made about unaligned transfers, higher-rank \(F\), or values of \(t\) for which inverse positivity fails. No finite experiment or numerical approximation is used as an infinite proof.
