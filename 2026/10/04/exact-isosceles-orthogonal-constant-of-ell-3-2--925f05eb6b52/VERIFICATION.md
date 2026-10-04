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

The mathematical verification is exact and has two layers.

First, the primary-source reduction is applied only after checking that the standard axes make the real plane \(\ell_3^2\) a symmetric Minkowski plane. This gives the one-variable function \(F(t)\) on \([0,\infty)\). The identities \(U(1/t)=t^{-3}V(t)\), \(V(1/t)=t^{-3}U(t)\), and \(W(1/t)=t^{-3}W(t)\) imply \(F(1/t)=F(t)\), so no parameter outside \([0,1]\) is omitted.

Second, the global bound on \([0,1]\) is analytic. Concavity of \(s\mapsto s^{2/3}\) reduces it to \(U+V\le9W\). On \([0,1/2]\) the difference is exactly \(18t^2\). On \([1/2,1]\) it is \(2(1-6t+21t^2-8t^3)\); writing the cubic as \(1+t(-8t^2+21t-6)\), the quadratic factor is increasing there and already equals \(5/2\) at \(t=1/2\). Hence the bound is global and strict away from the appropriate equality point.

The bundled script `verify_omega_l3.py` reconstructs these polynomial identities using integer arithmetic and performs rational-point checks of the reciprocal symmetry. A successful run prints `VERIFY_OK`. These computations are corroborative; they are not a finite substitute for the proof of the continuous supremum.

No claim is made beyond the real plane \(\ell_3^2\).
