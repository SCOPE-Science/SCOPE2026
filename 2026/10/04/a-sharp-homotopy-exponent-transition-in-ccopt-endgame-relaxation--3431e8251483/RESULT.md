# A sharp homotopy-exponent transition in CCOpt endgame relaxation

## Finding

CCOpt introduces a lower-bound endgame for a complementarity variable and, separately, a rolloff law coupling the Scholtes relaxation to the barrier parameter. Combining those formulas produces a sharp asymptotic phase transition.

Let \(x_2>0\), \(\zeta<0\), \(\mu>0\), \(\tau>0\), and \(\delta>0\). Consider the scalar local barrier model
\[
F_{\delta}(u)=\zeta u-\mu\log(u+\delta)-\mu\log(\tau-u x_2),
\qquad -\delta<u<\tau/x_2.
\]
For the rolloff law
\[
\tau(\mu)=\frac{c\mu^a}{\mu^a+b},
\qquad a,b,c>0,
\]
define
\[
D(\mu)=\mu x_2+\tau(\mu)\zeta.
\]
When \(D(\mu)>0\), the unique positive relaxation that places the minimizer of \(F_{\delta}\) exactly at \(u=0\) is
\[
\delta_*(\mu)=\frac{\tau(\mu)\mu}{D(\mu)}.
\]
There is a sharp transition at \(a=1\). If \(a>1\), then \(D(\mu)>0\) for all sufficiently small \(\mu\),
\[
\frac{\delta_*(\mu)}{\tau(\mu)}\longrightarrow\frac1{x_2},
\]
and hence \(\delta_*(\mu)\to0\), so any fixed positive cap \(\delta_{\max}\) is eventually inactive. If \(a<1\), then \(D(\mu)<0\) for all sufficiently small \(\mu\); in that regime the minimizer is strictly positive for every \(\delta>0\), so no positive lower-bound relaxation can target \(u=0\).

At \(a=1\), let \(L=x_2+(c/b)\zeta\). If \(L>0\), zero-targeting is eventually available and
\[
\frac{\delta_*(\mu)}{\mu}\longrightarrow\frac{c/b}{L}.
\]
If \(L<0\), it is eventually unavailable. On the exact boundary \(L=0\), one has \(D(\mu)>0\) for every \(\mu>0\), but
\[
\delta_*(\mu)\equiv\frac c{x_2}.
\]
Consequently, if \(\delta_{\max}<c/x_2\), the cap remains active and the local minimizer stays strictly positive.

## Assumptions and scope

The statement concerns the scalar local model used in the source's lower-bound endgame analysis, with \(x_2\), \(\zeta\), \(a\), \(b\), and \(c\) fixed as \(\mu\downarrow0\). It does not assert global convergence of CCOpt, does not replace the residual trigger for entering the endgame, and does not claim that the local model is exact away from the endgame regime. Exchanging the two complementarity coordinates gives the symmetric statement for the other lower bound.

## Proof

Direct differentiation gives
\[
F_{\delta}'(u)=\zeta-\frac{\mu}{u+\delta}+\frac{\mu x_2}{\tau-u x_2},
\]
and
\[
F_{\delta}''(u)=\frac{\mu}{(u+\delta)^2}+\frac{\mu x_2^2}{(\tau-u x_2)^2}>0.
\]
Also \(F_{\delta}(u)\to+\infty\) at both endpoints of its domain. Thus there is a unique minimizer, and since \(F_{\delta}'\) is strictly increasing, its sign relative to zero is determined by
\[
F_{\delta}'(0)=\zeta+\frac{\mu x_2}{\tau}-\frac{\mu}{\delta}
=\frac{D(\mu)}{\tau}-\frac{\mu}{\delta}.
\]
If \(D(\mu)\le0\), then \(F_{\delta}'(0)<0\) for every \(\delta>0\), so the minimizer lies at \(u>0\). If \(D(\mu)>0\), the unique threshold satisfying \(F_{\delta}'(0)=0\) is
\[
\delta_*(\mu)=\frac{\tau\mu}{D(\mu)}.
\]
Moreover, the minimizer is positive for \(0<\delta<\delta_*\), zero for \(\delta=\delta_*\), and negative for \(\delta>\delta_*\). Therefore clipping \(\delta_*\) from above by a positive cap cannot move the local minimizer to the negative side.

Substituting the rolloff law yields
\[
\frac{D(\mu)}{\mu}=x_2+\zeta\frac{c\mu^{a-1}}{\mu^a+b}.
\]
For \(a>1\), the second term vanishes and the right-hand side tends to \(x_2>0\), while
\[
\frac{\delta_*}{\tau}=\frac1{D(\mu)/\mu}\longrightarrow\frac1{x_2}.
\]
For \(a<1\), \(\mu^{a-1}\to\infty\) and \(\zeta<0\), so \(D(\mu)/\mu\to-\infty\).

For \(a=1\),
\[
\frac{D(\mu)}{\mu}=x_2+\frac{c\zeta}{\mu+b}\longrightarrow L=x_2+\frac cb\zeta.
\]
The signs \(L>0\) and \(L<0\) give the two eventual regimes. If \(L=0\), then \(c\zeta=-b x_2\), so exactly
\[
D(\mu)=\frac{x_2\mu^2}{\mu+b}>0,
\qquad
\tau(\mu)=\frac{c\mu}{\mu+b},
\]
and substitution gives \(\delta_*(\mu)=c/x_2\) for every \(\mu>0\).

## Verification

The accompanying script checks the minimizer-sign trichotomy numerically, the two strict exponent regimes at progressively smaller \(\mu\), and the critical \(a=1\), \(L=0\) identity using exact rational arithmetic. It prints `VERIFY_OK` when all checks pass.

A sign consistency point matters when reconstructing the source formula: differentiating its displayed local objective gives the positive term \(+\mu x_2/(\tau-u x_2)\). This derivative is consistent with the source's subsequent denominator \(\mu x_2+\tau\zeta\) in its zero-target formula. The proof here uses the displayed objective and direct differentiation.

## Relationship to prior work

Pozharskiy, Pacaud, Diehl, and Nurkanović derive the scalar endgame model and the zero-target lower-bound formula in their equations (28)--(31), then introduce the separate rolloff law \(\tau(\mu)=c\mu^a/(\mu^a+b)\) in equation (32). They report \(a=2\), \(b=10^{-6}\), and \(c=1\) as a good benchmark choice. The source does not state the exponent phase transition or the critical coefficient law obtained by coupling equations (30) and (32).

DeMiguel, Friedlander, Nogales, and Scholtes develop the foundational two-sided relaxation scheme and strict-interior rationale for equilibrium-constrained programs, but the inspected source does not contain the CCOpt-specific local denominator or rolloff coupling. A later comparison of relaxation methods covers broad convergence and numerical behavior, not this local coupled asymptotic law.

## Limitations

This is a local-model theorem, not a global statement about all CCOpt iterates. The multiplier estimate and the second complementarity coordinate are held fixed while \(\mu\downarrow0\); their variation in a full nonlinear solve can change when the asymptotic regime becomes visible. The conclusion identifies availability of the local zero-target mechanism, not a global iteration-complexity rate or a guarantee of B-stationarity. Literature searching cannot prove historical uniqueness, so an older equivalent calculation under different notation remains a residual originality risk.

## References

1. A. Pozharskiy, F. Pacaud, M. Diehl, and A. Nurkanović, *CCOpt: an Open-Source Solver for Large-Scale Mathematical Programs with Complementarity Constraints*, arXiv:2604.18726, 2026. See equations (28)--(32) and Appendix A.
2. V. DeMiguel, M. P. Friedlander, F. J. Nogales, and S. Scholtes, *A two-sided relaxation scheme for Mathematical Programs with Equilibrium Constraints*, SIAM Journal on Optimization 16 (2005), DOI:10.1137/04060754X.
3. T. Hoheisel, C. Kanzow, and A. Schwartz, *Theoretical and numerical comparison of relaxation methods for mathematical programs with complementarity constraints*, Mathematical Programming 137 (2013), DOI:10.1007/s10107-011-0488-5.
