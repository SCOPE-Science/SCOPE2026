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

# Verification of the rational double cover

The included standalone `verify.py` was executed with Python 3 and SymPy. Its exact symbolic calculations verify the cubic and quadric substitutions, the rational inverse on the stated dense chart, and the identity \(F|_{b=c=0}=d^3\), certifying the triple contact. The polynomial defining the elliptic cone section has no nonzero common projective zero of its partial derivatives. The endpoint quartic \(u(u^3+v^3)\) is squarefree; the binary-quartic invariants are \(I=0\), \(J=-27\), and discriminant factor \(-729\), giving \(j=0\).

The analytic singularity classification also uses (i) the standard equivalence between a double plane branched over smooth curves with intersection multiplicity three and a transverse \(A_5\) germ, and (ii) the weighted \((1,1,2)\) simple elliptic normal form for a nondegenerate binary quartic. These are mathematical deductions, not exhaustively machine-certified computations. No independent audit or publication-priority certification has been performed.
