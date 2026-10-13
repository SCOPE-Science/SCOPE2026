# YellowFin's robust region has a sharp switching-instability threshold
## Finding

YellowFin's central robustness lemma identifies a region in which every individual momentum operator has the same spectral radius. The defining paper explicitly warns that equal per-step spectral radii do not guarantee stability of products of different operators.

For two-period curvature switching, that caveat has an exact threshold.

Consider source-form Polyak momentum on a scalar time-varying quadratic model:
\[
x_{t+1}=x_t-\alpha h_t x_t+\mu(x_t-x_{t-1}),
\]
with
\[
\alpha>0,\qquad 0<\mu<1.
\]
Set
\[
r=\sqrt{\mu}.
\]
YellowFin's robust-region condition is
\[
(1-r)^2\le\alpha h_t\le(1+r)^2.
\]

With state
\[
z_t=\begin{bmatrix}x_t\\x_{t-1}\end{bmatrix},
\]
the one-step operator is
\[
A_t=
\begin{bmatrix}
1+\mu-\alpha h_t&-\mu\\
1&0
\end{bmatrix}.
\]
Define
\[
c_t=1+\mu-\alpha h_t.
\]
The robust-region condition is exactly
\[
-2r\le c_t\le2r.
\]
Each individual \(A_t\) then has spectral radius \(r\).

For two phases \(c_1,c_2\in[-2r,2r]\), the two-step monodromy matrix
\[
P=A(c_2)A(c_1)
\]
has
\[
\det P=\mu^2,
\qquad
\operatorname{tr}P=c_1c_2-2\mu.
\]
Thus
\[
-6\mu\le\operatorname{tr}P\le2\mu.
\]

The two-period system is Schur stable for every pair of robust-region phases if and only if
\[
\boxed{\mu<3-2\sqrt2.}
\]

At
\[
\boxed{\mu_c=3-2\sqrt2,}
\]
alternating the two robust-region endpoints has a Floquet multiplier \(-1\). For
\[
\mu>\mu_c,
\]
that endpoint alternation is unstable even though each individual one-step matrix has spectral radius \(\sqrt{\mu}<1\).

At the endpoints
\[
\alpha h_-=(1-r)^2,
\qquad
\alpha h_+=(1+r)^2,
\]
the exact two-step multipliers are
\[
\boxed{\lambda_\pm=-\mu(3\pm2\sqrt2).}
\]

YellowFin's minimal robust momentum for generalized condition number
\[
\nu=\frac{h_{\max}}{h_{\min}}
\]
is
\[
\mu_\star=
\left(
\frac{\sqrt{\nu}-1}{\sqrt{\nu}+1}
\right)^2.
\]
The switching threshold is therefore
\[
\boxed{\nu_c=3+2\sqrt2.}
\]
For
\[
\nu>\nu_c,
\]
the minimal robust YellowFin momentum permits an unstable alternating sequence between the two robust-region curvature endpoints.

## Assumptions and scope

The theorem concerns the scalar momentum operator used in YellowFin's robustness analysis and deterministic two-period generalized-curvature switching.

Every phase satisfies the source robust-region inequality. The instability is therefore a composition effect, not a violation of the one-step lemma.

The alternating curvature sequence is an abstract time-varying quadratic model. No claim is made that every fixed smooth objective generates this exact sequence.

Only two-period switching is classified. Arbitrary switching words, stochastic tuning, clipping, and asynchronous feedback are outside the theorem.

## Proof

Write
\[
A(c)=
\begin{bmatrix}
c&-\mu\\
1&0
\end{bmatrix}.
\]
Then
\[
P=A(c_2)A(c_1)
=
\begin{bmatrix}
c_2c_1-\mu&-c_2\mu\\
c_1&-\mu
\end{bmatrix}.
\]
Hence
\[
T:=\operatorname{tr}P=c_1c_2-2\mu,
\qquad
D:=\det P=\mu^2.
\]

Because
\[
|c_i|\le2\sqrt{\mu},
\]
we have
\[
-4\mu\le c_1c_2\le4\mu,
\]
so
\[
-6\mu\le T\le2\mu.
\]

The characteristic polynomial is
\[
\lambda^2-T\lambda+\mu^2.
\]
The second-order Jury criterion gives Schur stability exactly when
\[
1-\mu^2>0,
\]
\[
1-T+\mu^2>0,
\]
and
\[
1+T+\mu^2>0.
\]
The first condition holds for \(0<\mu<1\). The second is worst at \(T=2\mu\) and becomes
\[
(1-\mu)^2>0.
\]
The third is worst at \(T=-6\mu\) and becomes
\[
1-6\mu+\mu^2>0.
\]
For \(0<\mu<1\), this is equivalent to
\[
\mu<3-2\sqrt2.
\]

The worst trace is attained by opposite endpoint phases,
\[
c_1=2\sqrt{\mu},
\qquad
c_2=-2\sqrt{\mu}.
\]
Then
\[
\lambda^2+6\mu\lambda+\mu^2=0,
\]
so
\[
\lambda_\pm=-\mu(3\pm2\sqrt2).
\]

For the condition-number form, let \(s=\sqrt{\nu}\). Since
\[
\sqrt{\mu_\star}=\frac{s-1}{s+1},
\]
setting \(\sqrt{\mu_\star}=\sqrt2-1\) gives
\[
s=1+\sqrt2,
\]
hence
\[
\nu=(1+\sqrt2)^2=3+2\sqrt2.
\]

## Verification

The accompanying `verify.py` reconstructs the YellowFin momentum matrices, checks the robust-region one-step spectral radius, verifies the two-step trace and determinant formulas, tests the Jury threshold on a dense deterministic grid of phase pairs, and confirms the endpoint Floquet multipliers.

It also checks the exact equivalence between the momentum threshold \(3-2\sqrt2\) and the generalized-condition-number threshold \(3+2\sqrt2\).

The grid tests are transcription guards. Uniformity over all two-phase robust-region pairs is proved analytically above.

## Relationship to prior work

Zhang and Mitliagkas define YellowFin's robust region by
\[
(1-\sqrt{\mu})^2\le\alpha h_t\le(1+\sqrt{\mu})^2.
\]
Their robustness lemma proves that each corresponding one-step momentum operator has spectral radius \(\sqrt{\mu}\).

The defining paper itself explicitly warns that a product of different operators need not inherit the behavior suggested by their individual spectral radii. It therefore does not claim that the one-step robust-region lemma alone proves stability under arbitrary curvature variation.

The same source defines the generalized condition number and the minimal robust momentum
\[
\mu_\star=
\left(
\frac{\sqrt{\nu}-1}{\sqrt{\nu}+1}
\right)^2.
\]
The inspected full text does not give a switched-curvature counterexample, a sharp two-period threshold, or the constants \(3\pm2\sqrt2\).

Broader robust-control work on heavy-ball methods shows that fixed-quadratic intuition can overstate robustness on larger function classes. That literature motivates switched-system analysis, but the available inspected material did not state this YellowFin-interval two-period classification.

Focused published-record searches for YellowFin alternating curvature, robust-region switching, and time-varying heavy-ball products did not identify an implication-equivalent result.

## Limitations

The theorem classifies arbitrary two-period switching, not arbitrary switching of every period.

The exact unstable sequence uses the two robust-region endpoints.

The switched curvature signal is not asserted to be generated by every fixed smooth objective.

The threshold concerns deterministic linear stability and does not directly predict the stochastic or clipped YellowFin implementation.

## References

1. Jian Zhang and Ioannis Mitliagkas, “YellowFin and the Art of Momentum Tuning,” arXiv:1706.03471v1, first submitted 2017-06-12; SysML 2018.
2. Laurent Lessard, Benjamin Recht, and Andrew Packard, “Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints,” SIAM Journal on Optimization 26(1), 2016.
