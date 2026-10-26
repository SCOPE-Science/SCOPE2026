# Finite-time blow-up contradicts a global atmospheric-bore Liénard theorem

## Finding

For every parameter \(\eta\in(1,2)\), the initial-value problem
\[
\widehat f''+\widehat f\widehat f'+\widehat f-\eta\widehat f'=0,\qquad
\widehat f(0)=2\eta,\qquad \widehat f'(0)=0
\]
does not have a solution defined for all \(X\ge 0\). Instead, its unique maximal forward solution satisfies \(\widehat f(X)\to-\infty\) at a finite time. This contradicts the globality assertion for this initial-value problem in Theorem 1 of Constantin and Johnson, *Atmospheric undular bores* (first publicly available 29 April 2023).

## Assumptions and scope

Fix \(\eta\in(1,2)\). The right-hand side of the equivalent first-order polynomial system is smooth, so the initial-value problem has a unique local solution and a unique maximal interval of existence. The claim concerns only the specific initial data stated above and the homogeneous Liénard equation used in the cited theorem. It does not classify every orbit, nor does it by itself invalidate the separate piecewise-forced construction in the paper.

## Proof

Use the first-order formulation
\[
\widehat f'=\widehat g-\tfrac12\widehat f^2+\eta\widehat f,\qquad
\widehat g'=-\widehat f,
\]
and set \(f=-\widehat f\), \(g=-\widehat g\). Then
\[
f'=g+\tfrac12 f^2+\eta f,\qquad g'=-f,\qquad
(f(0),g(0))=(-2\eta,0). \tag{1}
\]
Differentiating (1) gives
\[
f''=(f+\eta)f'-f. \tag{2}
\]

Define \(L=f^2+g^2\). Along (1),
\[
L'=2ff'+2gg'=f^2(f+2\eta). \tag{3}
\]
At \(X=0\), direct differentiation of (1) gives
\[
f(X)=-2\eta+\eta X^2-\tfrac{\eta^2}{3}X^3+O(X^4),\qquad
g(X)=2\eta X-\tfrac{\eta}{3}X^3+O(X^4),
\]
hence
\[
L(X)=4\eta^2+\tfrac43\eta^3X^3+O(X^4)>4\eta^2
\]
for all sufficiently small \(X>0\). While \(-2\eta<f<0\), (3) makes \(L\) strictly increasing. In that strip, \(g>0\) and
\[
g>\sqrt{4\eta^2-f^2}>-\,\tfrac12 f^2-\eta f.
\]
For the second inequality, put \(s=-f/\eta\in(0,2)\). Since \(\eta<2\),
\[
\eta s(1-s/2)<s(2-s)<\sqrt{4-s^2};
\]
the last inequality follows from \(s^2(2-s)<2+s\) on \(0<s<2\). Multiplying by \(\eta>0\) gives
\[
-\tfrac12 f^2-\eta f<\sqrt{4\eta^2-f^2}.
\]
Thus \(f'=g+\tfrac12 f^2+\eta f>0\) as long as \(f<0\). If \(f\) never reached zero, it would increase to a limit \(\ell\le0\), while \(g\) would increase. If \(g\) were bounded, then \(g\to g_\infty>0\); the possibility \(\ell<0\) would make \(g'=-f\) bounded below by a positive constant, so \(\ell=0\), and then (1) would give \(f'\to g_\infty>0\), a contradiction. Thus \(g\) is unbounded. Since \(\tfrac12 f^2+\eta f\) is bounded for \(f\in[-2\eta,0]\), (1) then forces \(f'\to+\infty\), so \(f\) must cross zero in finite time. Therefore there is a finite \(X_0>0\) with \(f(X_0)=0\). By (3), \(L(X_0)>4\eta^2\); since \(g(X_0)>0\), this gives
\[
f'(X_0)=g(X_0)>2\eta>2. \tag{4}
\]

For \(X\ge X_0\) while the solution exists, (2) and (4) imply
\[
f''=f(f'-1)+\eta f'>0
\]
whenever \(f\ge0\) and \(f'\ge2\). Hence \(f\) stays nonnegative and increasing, and \(f'>2\) persists. Treat \(f'\) as a function of the increasing variable \(f\). From (2),
\[
\frac{df'}{df}=\frac{f''}{f'}
=f+\eta-\frac{f}{f'}
\ge \eta+\frac f2.
\]
Integration from \(f(X_0)=0\) yields
\[
f'(X)\ge f'(X_0)+\eta f(X)+\frac{f(X)^2}{4}
\ge \frac{f(X)^2}{4}.
\]
The solution reaches \(f=1\) in finite time because \(f'>2\). Thereafter,
\[
\frac{dX}{df}\le\frac4{f^2},
\qquad
\int_1^\infty\frac4{f^2}\,df=4<\infty.
\]
Thus \(f\) diverges to \(+\infty\) in finite additional time. Since \(\widehat f=-f\), the original solution blows down to \(-\infty\) in finite forward \(X\), proving the claim. \(\square\)

## Verification

The proof uses the exact polynomial system, a Taylor expansion at the initial point, the monotonicity identity (3), and the differential inequality \(f'\ge f^2/4\) once \(f\ge1\). No numerical integration is used to infer the infinite-time behavior. The finite-time conclusion follows from the convergent integral \(\int_1^\infty 4f^{-2}\,df\).

## Relationship to prior work

The primary source is A. Constantin and R. S. Johnson, “Atmospheric undular bores,” *Mathematische Annalen* 388 (2024), first published online 29 April 2023, DOI 10.1007/s00208-023-02624-8. Its Theorem 1 asserts global existence for the same equation and initial data when \(\eta\in(1,2)\); Theorem 2 asserts global oscillatory behavior for all nontrivial solutions. The argument above directly contradicts the first assertion for its stated initial-value problem. It is a correction of that precise claim, not a new classification of the full atmospheric model.

The article also cites general phase-plane literature, including G. Villari, “A survival kit in phase plane analysis: some basic models and problems” (2016). Exact-equation and theorem-name searches of indexed mathematical research records returned no exact matching correction. Nearby indexed Liénard results concern different vector fields or different asymptotic regimes.

## Limitations

The proof does not determine the exact blow-up time or the blow-up rate. It does not establish whether other initial data have global solutions, and it does not independently settle the existence of the paper’s separate piecewise-forced bore profile. A later erratum or unindexed discussion could exist; none was identified in the searches recorded for this finding.

## References

1. A. Constantin and R. S. Johnson, “Atmospheric undular bores,” *Mathematische Annalen* 388 (2024), 4011–4036. DOI: 10.1007/s00208-023-02624-8. First public date: 2023-04-29. Official full text: https://link.springer.com/article/10.1007/s00208-023-02624-8.
2. G. Villari, “A survival kit in phase plane analysis: some basic models and problems,” in *Nonlinear Water Waves*, Lecture Notes in Mathematics 2158, Springer (2016), pp. 197–228. This general reference was identified through the primary source’s bibliography; its full text was not inspected.
