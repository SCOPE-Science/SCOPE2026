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
With \(Y=X_N-I\), the published density is
\[
f_Y(y)=\frac{y}{\beta^2}e^{-y/\beta},\qquad y>0,
\]
so \(Y\sim\Gamma(2,\beta)\).

The survival is
\[
S_Y(y)=\left(1+\frac y\beta\right)e^{-y/\beta}.
\]
Solving \(S_Y(y)=1-p\) gives
\[
Q(p)=I+\beta\left[-1-W_{-1}\left(-\frac{1-p}{e}\right)\right].
\]
The lower branch is forced because \(1+y/\beta\ge1\).

For \(t\ge I\), direct integration gives
\[
\int_t^\infty S(x)\,dx=(t-I+2\beta)e^{-(t-I)/\beta},
\]
which yields
\[
m(t)=\beta\frac{t-I+2\beta}{t-I+\beta}.
\]
Its derivative is negative.

The included checker evaluates the source CDF, Lambert-W formulas, survival integral, and residual-life derivative at several parameter values. Finite calculation is not used as proof.
