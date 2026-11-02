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

# Reproducible checks and limits

Execute `python3 verify.py` with Python 3 standard library only. Its sparse-polynomial arithmetic in \(\mathbb F_7[x,t]\) checks the seven Hasse-recursion stages, the factorization of the ordinary order-five Wronskian, the order-six vanishing and order-seven nonvanishing on the exceptional curve, and the equality \(B_7(x,0)(x^8+1)=x(1-x^{48})/2\). The script independently checks the three nonzero Hasse--Witt coefficients as contextual cross-checks; it does not claim a new Hasse--Witt classification. It verifies the numerical degree of the divisor. The recorded standard output is `verify_output.txt`.

The proof, rather than the script, supplies the complete bicanonical basis, the Hasse-order determinant criterion, the globalization of the Hasse Wronskian, and local valuations at the branch points and both points at infinity. The recurrence is an identity of polynomials in the free parameter, rather than a sample of parameter values. Literature comparisons remain a same mathematical model historical-priority assessment, not independent peer review.
