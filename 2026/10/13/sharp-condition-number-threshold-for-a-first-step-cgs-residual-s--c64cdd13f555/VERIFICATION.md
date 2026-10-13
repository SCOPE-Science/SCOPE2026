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
The universal proof is analytic. For standard CGS with \(\widetilde r_0=r_0\),
\[
r_1=(I-\alpha_0A)^2r_0,
\qquad
\alpha_0=\frac{r_0^{\mathsf T}r_0}{r_0^{\mathsf T}Ar_0}.
\]
On an SPD spectrum, the squared norm ratio is a normalized fourth central moment. Convexity moves the fixed-mean extremum to the spectral endpoints, giving
\[
\mathcal G(\kappa)=
\max_{t\ge0}
\frac{(\kappa-1)^4t(t^2-t+1)}{(1+\kappa t)^4}.
\]
The derivative in \(\kappa\) is positive for every \(t>0\), so the envelope has one crossing of one.

The embedded `verify.py` uses standard-library exact arithmetic to replay the algebraic certificate. It checks the stationary polynomial, recomputes the threshold elimination resultant by an exact Sylvester determinant over integer polynomials, verifies the reciprocal reduction to \(Q(y)\), checks the one-sign-change Descartes transformation, and isolates the unique \(\kappa>1\) root in
\[
3.442815869<\kappa<3.442815870.
\]
It also checks exactly that for
\[
A=\operatorname{diag}(1,4),
\qquad
r_0=(4,1)^{\mathsf T},
\]
CGS gives
\[
\alpha_0=\frac{17}{20},
\qquad
r_1=\left(\frac9{100},\frac{144}{25}\right)^{\mathsf T},
\]
and squared norm ratio \(331857/170000>1\).

The asymptotic result follows after \(u=\kappa t\) from the limiting maximization
\[
\max_{u\ge0}\frac{u}{(1+u)^4}=\frac{27}{256}.
\]
No finite experiment is used as a proof of the all-dimensional result.

Unproved limits are later CGS iterations, preconditioning, finite-precision residual gaps, and nonsymmetric or nonnormal matrices.
