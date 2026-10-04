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
The core non-Gaussianity argument is analytic.

The bundled checker uses the source formulas with
\[
f(I)=g(I)=\frac{I}{1+I},
\]
the stated epidemic parameters, and a single unit-rate jump atom with
\[
\eta_1=0.1,\qquad \eta_2=\eta_3=0.
\]
It verifies the source assumptions numerically, reconstructs
\[
\widetilde{\mathcal R}_0^s\approx26.6251093071>1,
\]
finds the positive quasi-endemic root, and builds the drift matrix \(A\).

All eigenvalues of \(A\) have negative real part. The script then evaluates
\[
\int_0^\infty
\left[
\ln(1.1)\,
e_1^\top e^{As}e_1
\right]^4 ds
\]
and obtains a strictly positive value. Strict positivity also follows without quadrature because the integrand is continuous and positive at \(s=0\).

The checker additionally verifies that
\[
\ln(1.1)^2
\]
is unequal to
\[
2(0.1-\ln(1.1)),
\]
so the source's local covariance coefficient is not the true log-jump second-cumulant rate.

The numerical work is finite verification of the explicit witness, not evidence for a general infinite-time claim.
