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

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the normalized length-\(6\) objective from the SQN recurrence using exact rational multivariate polynomial arithmetic.

For \(0\le p\le1/5\), it transforms
\[
p(1-p)^5-F(p,r,s,t)
\]
to tensor-product Bernstein form and checks all \(168\) coefficients are nonnegative.

For \(1/5\le p\le1/2\), it checks
\[
\frac{1024}{15625}-F(p,r,s,t)
\]
on eight boxes obtained by halving each of \(r,s,t\). Every box has \(168\) exact nonnegative Bernstein coefficients.

The verifier also checks the five residue-class integer inequalities used for \(q=5k+r\), \(k\ge2\), and independently solves the reduced exact integer program for \(2\le q\le15\).

The theorem for all \(q\ge10\) follows from these exact certificates and the symbolic reduction, not from the finite stress test.

Independent audit has not been performed.
