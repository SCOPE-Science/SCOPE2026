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

The analytic verification starts from the exact source parameterization
\[
\lambda(t)=(\lambda_2+1)\frac{(1+t^k)^k}{(t+\cdots+t^{k-1})(1+t+\cdots+t^{k-1})^k}.
\]
With \(t=e^s\), reciprocal symmetry makes \(\log(\lambda(e^s)/\lambda_c)\) even. The second derivative at zero is obtained exactly from the variances of three finite uniform integer sets:
\[
\frac{k^3}{4}-\frac{k(k-2)}{12}-\frac{k(k^2-1)}{12}
=\frac{k(2k^2-k+3)}{12}.
\]
This positive coefficient proves the local quadratic minimum and, by analytic inversion, the square-root branch. Since \(a/c=t^k\), the contrast is exactly \(M=\tanh(ks/2)\), which gives the stated amplitude and remainder.

The bundled `verify.py` checks the finite-sum variance identity exactly for \(2\le k\le200\), substitutes the parameterized solutions back into both source equations for representative parameters, and numerically checks approach to the predicted amplitude. These finite checks do not establish the all-parameter theorem; they only replay consequences of the analytic proof.

No assertion is made about other Gibbs-measure classes, extremality, stability, or free energy.
