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

Let
\[
0=\sum_{i=0}^d\lambda_i p_i,
\qquad
\lambda_i>0,
\qquad
\sum_i\lambda_i=1.
\]
Then the opposite-facet intersection identity is
\[
-\frac{\lambda_i}{1-\lambda_i}p_i
=
\sum_{j\ne i}\frac{\lambda_j}{1-\lambda_i}p_j.
\]
Thus the gauge of the outer simplex in direction \(-p_i\) is exactly
\[
\frac{1-\lambda_i}{\lambda_i}.
\]
The inclusion \(K\subset P\) and symmetry \(K=-K\) yield
\[
\|p_i\|_K\ge\frac{1-\lambda_i}{\lambda_i}.
\]
The only global inequality then needed is
\[
\sum_i\frac1{\lambda_i}\ge(d+1)^2,
\]
which is Cauchy--Schwarz.

For the equality family \(K=\Delta-\Delta\), with \(\sum_i a_i=0\), the point \(-a_i/d\) is the average of the other \(d\) vertices. Hence
\[
\frac{d+1}{d}a_i\in\Delta-\Delta.
\]
The centered barycentric functional associated with vertex \(a_i\) is bounded by \(1\) on the difference body and takes the value \(d\) at \((d+1)a_i\), proving the reverse gauge inequality and therefore exact norm \(d\).

`verify.py` checks the reciprocal identity and lower bound with rational barycentric data in dimensions \(2\) through \(12\), verifies equality for uniform barycentric weights, and exactly checks the coefficient model for the simplex difference-body equality family.

No finite experiment is used to justify the all-dimensional theorem. The unrestricted vertex index of the three-dimensional \(T-T\) family is not verified or asserted.
