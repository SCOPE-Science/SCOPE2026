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
Let
\[
H=\mathcal L(T\mid T>0),
\qquad
\mu_+=\operatorname{E}(T\mid T>0),
\]
and
\[
L_H(\lambda)=\operatorname{E}(e^{-\lambda T}\mid T>0).
\]
The analytic identity checked is
\[
r_T(\lambda)
=
\frac{\mu_+}{1-L_H(\lambda)}
-
\frac1\lambda.
\]

The packaged checker uses a two-point positive law, evaluates the profile at several rates, and reconstructs
\[
L_H(\lambda)
=
1-\frac{\mu_+}{r_T(\lambda)+1/\lambda}.
\]
It also computes the unconditional numerator and denominator after adding different masses at zero and verifies that their ratio is unchanged.

For the complete-data expression, it checks
\[
\widehat r_n(\lambda)
=
\frac{\sum_iT_i}{\sum_i(1-e^{-\lambda T_i})}
-
\frac1\lambda
\]
and verifies invariance after inserting zero observations.

The finite computations support reproducibility. The identification theorem itself follows from the analytic identity, the high-rate limit, and uniqueness of Laplace transforms.
