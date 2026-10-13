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
# Computational verification

Run `python3 check_ideals.py` with Python 3. The program independently enumerates every subspace of the maximal ideal in row-reduced echelon form and directly tests closure under multiplication by each degree-one monomial. For each ideal it computes the minimal generator count by the rank of the linear product span. It separately computes the predicted Gaussian-binomial polynomial, comparing dictionaries of coefficients.

Exhaustive cases: dimension-parameter and field sizes `(1,2)`, `(1,3)`, `(2,2)`, `(2,3)`, with total ideal counts respectively 4, 4, 27, 46 and final `VERIFY_OK`. The verifier uses prime-field modular arithmetic; extension fields and all larger parameters are covered by the written proof, not by numerical testing.

The proof's critical equalities are \(W/VU\cong\operatorname{Sym}^2(V/U)\), the lift count \(q^{r(b_r-j)}\), and \(\mu(I)=\dim(I/\mathfrak m I)=r+j\). Each is proved in `RESULT.md`.
