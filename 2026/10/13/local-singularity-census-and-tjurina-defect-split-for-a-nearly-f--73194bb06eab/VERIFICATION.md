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

`verify.py` uses exact rational arithmetic in SymPy. It checks:

- nondegeneracy of all four conic components;
- invariance under \([x_0:x_1:x_2]\mapsto[x_0:-x_1:x_2]\);
- singular support in the two affine charts, together with smoothness of the unique projective point outside their union;
- the \(A_3\) and \(D_4\) tangent configurations;
- the two contact-order-two branch pairs at \(p_4\);
- the localized Tjurina Gröbner basis at \(p_4\) and quotient dimension \(18\);
- the global numerical identities \(\mu(C)=51\) and \(\tau(C)=47\).

The monodromy polynomial is then obtained from the verified branch-contact resolution: the first exceptional divisor has multiplicity \(5\); the two blow-ups resolving the two triple crossings have multiplicity \(7\) each; all three exceptional vertices have valency three. A'Campo's formula gives \((t-1)(t^5-1)(t^7-1)^2\).

Limits: the verifier certifies the stated explicit algebra and local invariants; it does not classify analytic moduli of general five-branch germs or other conic–line arrangements.
