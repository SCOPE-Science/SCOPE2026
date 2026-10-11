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
The critical algebraic checks are:
\[
\|U+V\|_4^4+\|U-V\|_4^4
-2\bigl(\|U\|_4^4+\|V\|_4^4\bigr)
=4\|UV^*\|_2^2+2\|U^*V+V^*U\|_2^2,
\]
and, with \(k=2-\sqrt2\),
\[
(a^4+b^4)-(a^2+b^2-kab)^2=2kab(a-b)^2.
\]
Both are exact identities, not asymptotic estimates. For unit operators \(A,B\), substitute \(U=A+B\), \(V=A-B\), and divide the factorizations by positive sums of radicals to obtain the displayed P-angle defect. This establishes the sharp constant and equality classification on all Hilbert-space dimensions at least two.

The standalone checker `verify.py` tests the scalar factorization symbolically, the trace identity on exact integer matrices of sizes two through four, the diagonal maximizer with exact radicals, and representative noncommuting normalized pairs numerically. These finite checks supplement the general trace proof; numerical random testing is not exhaustive and plays no role in the continuum argument.

No independent audit or independent validation has been performed.
