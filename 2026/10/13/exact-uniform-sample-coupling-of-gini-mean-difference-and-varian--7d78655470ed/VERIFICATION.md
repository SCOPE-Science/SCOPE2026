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

The proof is analytic for every \(n\ge2\) and every nondegenerate uniform interval.

`checker.py` derives the required moments independently with exact rational arithmetic. It integrates the conditional polynomials
\[
a(x)=x^2-x+\frac12,
\qquad
b(x)=\frac12\left(x^2-x+\frac13\right)
\]
over \([0,1]\), obtains same-pair absolute-difference moments from the exact triangular integral, and reconstructs the order-two U-statistic overlap decomposition.

The checker verifies the three closed second-moment formulas, the correlation identity, the exact correlation deficit, and the contrast variance for every \(2\le n\le10000\). It also checks as a polynomial identity that the centered conditional kernels satisfy
\[
a(x)-\frac13
=
2\left(b(x)-\frac1{12}\right),
\]
which is the degeneracy mechanism.

The bounded loop is a consistency check only. The universal statement follows from the exact algebra in the proof.
