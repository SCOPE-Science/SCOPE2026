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
The bundled `verify.py` uses exact symbolic algebra for the defining vector field. It checks:

1. the full equilibrium line \((\xi,0,0,-a\xi)\) when \(d=0\);
2. both isolated equilibria \(E_\sigma\) when \(d\ne0\);
3. the componentwise identity \(f_{-d}(Tq)=DT\,f_d(q)\);
4. \(L_f w=-y+d\) and \(L_f(y^2-z^2)=-2by^2+2cz^2\);
5. the quartic constraint used to prove rigidity in the equality case;
6. the nonzero residual of the fourth coordinate printed in the source; and
7. exact-to-numerical evaluation at \(a=8\), \(b=40\), \(c=15\), \(d=-1/10\).

A successful replay prints `VERIFY_OK`. The symbolic checks establish identities, not global boundedness or existence of a non-equilibrium invariant measure. The proof of the stationary identities additionally uses compact support and invariance of \(\mu\), as stated in the result.
