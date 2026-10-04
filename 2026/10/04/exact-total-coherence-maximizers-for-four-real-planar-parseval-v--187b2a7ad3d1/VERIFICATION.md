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

The proof is analytic. The bundled `verify.py` is a replay check, not a replacement for the Ky Fan argument.

It checks the following facts with exact arithmetic:

- all \(64\) order-four Seidel sign matrices reduce by diagonal sign switching to the normalized three-sign form, with residual-negative counts \(8,24,24,8\);
- the \(48\) middle cases have characteristic polynomial \((x^2-1)(x^2-5)\), hence top-two eigenvalue sum \(1+\sqrt5\), while the two extreme classes have top-two sum \(2\);
- the displayed matrix \(P_0\) satisfies \(P_0^2=P_0\) and \(\operatorname{tr}P_0=2\) in \(\mathbb Q(\sqrt5)\);
- its ordered total coherence is exactly \(1+\sqrt5\);
- the scalar identities used for the explicit frame, \(a+d=1/2\) and \(ad=c^2\), hold exactly.

The finite enumeration does not establish the infinite optimization by itself; the universal step is the variational characterization over all rank-two projections.
