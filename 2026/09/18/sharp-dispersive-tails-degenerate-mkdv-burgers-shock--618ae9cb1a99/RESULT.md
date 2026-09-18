# Sharp dispersive tails of the degenerate mKdV–Burgers shock

## Statement

Consider the modified KdV–Burgers equation
\[
 u_t+(u^3)_x=\mu u_{xx}-\kappa u_{xxx},\qquad \mu>0,\ \kappa>0,
\]
and its monotone degenerate Oleinik travelling wave \(U(\xi)\), \(\xi=x-3s^2t\), connecting
\[
 U(-\infty)=-2s,\qquad U(+\infty)=s,\qquad s>0.
\]
The integrated profile equation is
\[
 (U-s)^2(U+2s)=\mu U'-\kappa U''.
\tag{1}
\]
Assume the monotonicity condition
\[
 36\kappa s^2\le \mu^2.
\tag{2}
\]
The source paper proves existence, uniqueness up to translation, monotonicity, and dispersion-uniform two-sided exponential/algebraic bounds for this profile. The following sharpens those bounds at both ends.

### 1. Exact upstream exponent in the strict monotone regime

If
\[
 36\kappa s^2<\mu^2,
\]
then there is a translation-dependent constant \(A_->0\) such that
\[
 \boxed{
 U(\xi)+2s=A_-e^{\Lambda_-\xi}(1+o(1)),\qquad \xi\to-\infty,
 }
\tag{3}
\]
with
\[
 \boxed{
 \Lambda_-=
 \frac{\mu-\sqrt{\mu^2-36\kappa s^2}}{2\kappa}
 =\frac{18s^2}{\mu+\sqrt{\mu^2-36\kappa s^2}}.
 }
\tag{4}
\]
Moreover,
\[
 U'(\xi)=\Lambda_-A_-e^{\Lambda_-\xi}(1+o(1)).
\tag{5}
\]
Thus the sharp upstream exponent is dispersion-dependent. It increases continuously from the purely viscous value \(9s^2/\mu\) as \(\kappa\downarrow0\) to \(18s^2/\mu\) as the monotonicity boundary is approached.

### 2. Jordan tail at the monotonicity boundary

At the endpoint
\[
 36\kappa s^2=\mu^2,
\]
the two upstream spatial eigenvalues coalesce. Writing
\[
 \Lambda_c=\frac{18s^2}{\mu},
\]
there is a translation-dependent \(A_c>0\) such that
\[
 \boxed{
 U(\xi)+2s=A_c(-\xi)e^{\Lambda_c\xi}(1+o(1)),\qquad \xi\to-\infty.
 }
\tag{6}
\]
The extra factor \((-\xi)\) is the generalized-eigenvector contribution of the repeated spatial root. Hence the boundary of the monotone regime has a genuine polynomial-times-exponential tail rather than a pure exponential.

### 3. Universal downstream logarithmic correction

For the entire monotone range (2), there is a translation-dependent constant \(C_+\) such that
\[
 \boxed{
 \frac{1}{s-U(\xi)}
 =\frac{3s}{\mu}\,\xi
 -\left(\frac{1}{3s}+\frac{6\kappa s}{\mu^2}\right)\log\xi
 +C_++o(1),
 \qquad \xi\to+\infty.
 }
\tag{7}
\]
Equivalently,
\[
 \boxed{
 s-U(\xi)
 =\frac{\mu}{3s\,\xi}
 +\left(\frac{\mu^2}{27s^3}+\frac{2\kappa}{3s}\right)
 \frac{\log\xi}{\xi^2}
 +\frac{\widetilde C_+}{\xi^2}
 +o(\xi^{-2}).
 }
\tag{8}
\]
The leading \(\xi^{-1}\) contact tail is independent of dispersion, but the first translation-invariant correction is not. In particular, the coefficient of \(\log\xi\) gives an exact asymptotic fingerprint of \(\kappa\).

If
\[
 d:=-\lim_{\xi\to\infty}
 \frac{\frac1{s-U(\xi)}-\frac{3s}{\mu}\xi}{\log\xi},
\]
then
\[
 \boxed{
 d=\frac1{3s}+\frac{6\kappa s}{\mu^2},
 \qquad
 \kappa=\frac{\mu^2}{6s}\left(d-\frac1{3s}\right).
 }
\tag{9}
\]
Likewise, in the strict regime the upstream exponent determines
\[
 \boxed{
 \kappa=\frac{\mu\Lambda_--9s^2}{\Lambda_-^2}.
 }
\tag{10}
\]
Both diagnostics are invariant under translation of the shock profile.

## Proof

### Upstream, strict regime

Set
\[
 q(\xi)=U(\xi)+2s.
\]
From (1),
\[
 \kappa q''-\mu q'+9s^2q=6sq^2-q^3.
\tag{11}
\]
The linearization at \(q=0\) has characteristic polynomial
\[
 \kappa\lambda^2-\mu\lambda+9s^2,
\]
whose roots are
\[
 \Lambda_\pm=\frac{\mu\pm\sqrt{\mu^2-36\kappa s^2}}{2\kappa}.
\tag{12}
\]
For strict inequality in (2), these are distinct and positive. Standard hyperbolic asymptotics therefore give a linear combination of the two modes as \(\xi\to-\infty\).

It remains to exclude a pure fast mode. In the normalization
\[
 z=U/s,\qquad \zeta=s^2\xi/\mu,\qquad \nu=\kappa s^2/\mu^2,
\]
the source proves the pointwise bound
\[
 z'\le2(z-1)^2(z+2).
\tag{13}
\]
With \(Q=z+2\), this gives
\[
 \frac{Q'}{Q}\le2(3-Q)^2\to18
\qquad (\zeta\to-\infty).
\tag{14}
\]
But the fast normalized root is
\[
 \lambda_+=\frac{1+\sqrt{1-36\nu}}{2\nu}>18
\qquad (0<\nu<1/36).
\]
Hence the heteroclinic cannot be tangent only to the fast eigendirection. Its slow coefficient is nonzero; positivity of \(q\) makes that coefficient positive. This proves (3)–(5).

### Critical upstream tail

When \(36\kappa s^2=\mu^2\), equation (11) factors as
\[
 \kappa(D-\Lambda_c)^2q=q^2(6s-q),
 \qquad \Lambda_c=18s^2/\mu.
\tag{15}
\]
The equilibrium remains hyperbolic, but its linearization has a size-two Jordan block. Standard asymptotic integration gives
\[
 q(\xi)=e^{\Lambda_c\xi}\big(A+B\xi+o(|\xi|)\big).
\tag{16}
\]
To show that the generalized mode is actually present, set
\[
 r(\xi)=e^{-\Lambda_c\xi}q(\xi).
\]
Equation (15) yields
\[
 \kappa r''=e^{-\Lambda_c\xi}q^2(6s-q)>0.
\tag{17}
\]
Meanwhile the strict form of (14) away from the endpoint gives \(q'/q<\Lambda_c\), hence \(r'<0\). If \(B=0\), then (16) would imply \(r'\to0\) as \(\xi\to-\infty\); integrating (17) from \(-\infty\) would instead force \(r'>0\), a contradiction. Thus \(B<0\), and (6) follows with \(A_c=-B>0\).

### Downstream logarithmic correction

Let
\[
 y(\xi)=s-U(\xi)>0,
 \qquad v(\xi)=U'(\xi)>0.
\]
Near \(y=0\), the profile trajectory can be written on its center manifold as \(v=v(y)\). Since \(y'=-v\), one has \(U''=-v\,dv/dy\), and (1) becomes
\[
 \kappa v\frac{dv}{dy}+\mu v=3sy^2-y^3.
\tag{18}
\]
Seeking
\[
 v=a_2y^2+a_3y^3+O(y^4)
\]
and matching powers in (18) gives
\[
 a_2=\frac{3s}{\mu},
 \qquad
 a_3=-\frac{\mu^2+18\kappa s^2}{\mu^3}.
\tag{19}
\]
Now set \(X=1/y\). Then
\[
 X'=\frac{v}{y^2}
 =\frac{3s}{\mu}
 -\left(\frac1\mu+\frac{18\kappa s^2}{\mu^3}\right)\frac1X
 +O(X^{-2}).
\tag{20}
\]
First, (20) gives \(X\sim(3s/\mu)\xi\). Substituting this back once yields
\[
 X'=\frac{3s}{\mu}
 -\left(\frac{1}{3s}+\frac{6\kappa s}{\mu^2}\right)\frac1\xi
 +O\!\left(\frac{\log\xi}{\xi^2}\right).
\]
The remainder is integrable, so integration gives (7). Expanding the reciprocal gives (8). Equations (9) and (10) are algebraic rearrangements of the sharp coefficients.

## Relation to the source result

The source theorem proves dispersion-uniform two-sided bounds: exponential decay on the left and \(\xi^{-1}\) decay on the right. It therefore correctly identifies the coarse decay scales needed for its stability argument. The sharper asymptotics above reveal information deliberately invisible to those uniform bounds:

- the exact upstream exponential rate varies with \(\kappa\);
- the monotonicity threshold carries a Jordan \((-\xi)\) factor;
- the first translation-invariant correction to the downstream algebraic tail is logarithmic and depends linearly on \(\kappa\).

Thus “the same decay scales as the purely viscous profile” does not imply equality of the sharp spatial asymptotics.

## Verification

`artifacts/verify_tail_asymptotics.py` symbolically checks the center-manifold coefficients, the reciprocal logarithmic coefficient, both upstream characteristic roots, and the critical repeated-root factorization. The accompanying output records the checks and two sample parameter values. This computation supports the algebra in the proof; it is not independent validation.

## Originality scope

The following are standard or prior and are not claimed as new: the mKdV–Burgers travelling-wave reduction, phase-plane classification of its shocks, hyperbolic/Jordan asymptotics, center-manifold expansions, and the existence and monotonicity theorem of arXiv:2609.20591v1.

The source-specific claim is the sharp tail package (3)–(10) for the degenerate Oleinik profile treated in arXiv:2609.20591v1, especially the universal downstream logarithmic correction and the critical Jordan tail, together with the translation-invariant dispersion recovery formulas. To the best of our knowledge, these statements are not given in the source paper or in the related literature inspected during review.

## Limitations

The result concerns only the monotone degenerate shock connecting \(-2s\) to \(s\) under (2). It does not address oscillatory profiles outside the monotone regime, nondegenerate or undercompressive shocks, or the nonlinear time-asymptotic error of solutions converging to the shock. The constants \(A_-\), \(A_c\), \(C_+\), and \(\widetilde C_+\) depend on translation. Only the exponents and the displayed logarithmic coefficients are translation invariant.

The 1995 Jacobs–McKinney–Shearer paper was identified as the most relevant older phase-plane reference, but its full text was not available through the sources inspected. This leaves residual originality risk for endpoint asymptotics stated there under different terminology. Available later descriptions of that work emphasize classification and explicit undercompressive profiles rather than the degenerate Oleinik logarithmic tail considered here.

## References

1. N. Eun, S. Han, J. Kim, *Large-Time Behavior towards Composite Waves of Degenerate Shock and Rarefaction Wave for Modified KdV–Burgers Equation*, arXiv:2609.20591v1 (2026). https://arxiv.org/abs/2609.20591
2. D. Jacobs, W. R. McKinney, M. Shearer, *Travelling wave solutions of the modified Korteweg-de Vries-Burgers equation*, J. Differential Equations 116 (1995), 448–467. https://doi.org/10.1006/jdeq.1995.1043
3. G. A. El, M. A. Hoefer, M. Shearer, *Dispersive and Diffusive-Dispersive Shock Waves for Nonconvex Conservation Laws*, SIAM Review 59 (2017), 3–61. https://doi.org/10.1137/15M1015650
4. F. Huang, Y. Wang, J. Zhang, *Time-asymptotic stability of composite waves of degenerate Oleinik shock and rarefaction for non-convex conservation laws*, Math. Ann. 392 (2025), 1–46; arXiv:2408.06801. https://arxiv.org/abs/2408.06801
5. J. Dodd, *Spectral stability of undercompressive shock profile solutions of a modified KdV-Burgers equation*, Electron. J. Differential Equations 2007(135), 1–13. https://ejde.math.txstate.edu/Volumes/2007/135/abstr.html
