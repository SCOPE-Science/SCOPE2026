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

The proof is analytic. The packaged checker `artifacts/verify.py` verifies algebraic identities and samples the stated inequalities on deterministic finite test sets; these computations are corroborative and do not replace the universal proof.

The checked analytic chain is: product-test acceptance reduces to \(P_{\mathrm{PT}}=(1+s)/2\); the published generalized-W overlap formula reduces in the high-entanglement branch to \(\omega=4pqr/(1-2s)\); the fixed-\(s\) trigonometric parametrization gives the sharp product lower bound; the induced \(w(t)=(2+t)^2/[9(1+t)]\) is increasing; and its inverse is the stated \(T(\omega)\). In the high-overlap branch, the largest-coefficient formula plus \(q^2+r^2\le(q+r)^2\) gives the sharp boundary.

The checker also verifies the endpoint values \(P_{\mathrm{PT}}=2/3\) and dimension-free value \(19/27\) at \(\omega=4/9\), hence deficit \(1/27\), and confirms the exact factorization of the deficit for representative values throughout \([4/9,1/2]\).

Limits: no computation here enumerates all pure three-qubit states, and no such enumeration is used by the claim. The theorem is restricted to generalized W states. Independent audit has not been performed.
