# Sharp fraction-of-optimal decrease for the SPD Cauchy trust-region point

## Result

Consider the Euclidean trust-region subproblem
\[
\min_{\|p\|_2\le \Delta} m(p),\qquad
m(p)=g^Tp+\tfrac12 p^TBp,
\]
where \(B\succ0\), \(g\ne0\), and \(\Delta>0\). Write predicted decrease as
\(D(p)=-m(p)\), let \(p_*\) be the exact global minimizer and \(D_*=D(p_*)\),
and let \(p_C\) be the Cauchy point, i.e. the minimizer of \(m\) on the feasible
part of the ray \(\{-tg:t\ge0\}\), with \(D_C=D(p_C)\).

Set
\[
G=\|g\|_2,\qquad u=g/G,\qquad
q=u^TBu,\qquad s=u^TB^{-1}u,\qquad K=qs.
\]
Then for every trust radius,
\[
\boxed{\frac{D_C}{D_*}\ge \frac1K
=\frac{1}{(u^TBu)(u^TB^{-1}u)}.}
\]
The constant is sharp for the fixed pair \((B,g)\): for every radius large enough
to contain both unconstrained minimizers, equality holds.

If the spectrum of \(B\) is contained in \([\mu,L]\), with
\(\kappa=L/\mu\), the Kantorovich inequality gives
\[
K\le \frac{(\kappa+1)^2}{4\kappa},
\]
and hence the condition-number-only guarantee
\[
\boxed{\frac{D_C}{D_*}\ge
\frac{4\kappa}{(\kappa+1)^2}.}
\]
This second constant is also sharp for every \(\kappa\ge1\). In dimension two,
\(B=\operatorname{diag}(\mu,L)\) and a gradient with equal squared components
in the two eigendirections attain equality once the Newton step is feasible.

Thus trust-region truncation cannot make the Cauchy point worse, in relative
predicted reduction, than its full-space steepest-descent-versus-Newton ratio.

## Proof

The Cauchy step length is
\[
t_C=\min\left\{\frac{G^2}{g^TBg},\frac{\Delta}{G}\right\}
=\min\{q^{-1},\Delta/G\}.
\]
First suppose \(\Delta\ge G/q\), so the Cauchy point is untruncated. Then
\[
D_C=\frac{G^2}{2q}.
\]
The constrained optimum cannot have larger decrease than the unconstrained
Newton minimizer \(-B^{-1}g\), whose decrease is
\[
D_N=\tfrac12 g^TB^{-1}g=\frac{G^2s}{2}.
\]
Therefore \(D_C/D_*\ge D_C/D_N=1/(qs)\). If the trust region also contains
the Newton step, equality holds.

Now suppose \(0<\Delta\le G/q\), so \(p_C=-\Delta u\). Put
\(\tau=\Delta/G\in(0,1/q]\). Then
\[
D_C=G\Delta\left(1-\frac{\tau q}{2}\right).
\]
For an arbitrary feasible \(p\), write \(p=-\Delta v\), where \(\|v\|\le1\),
and set
\[
a=u^Tv,\qquad b=v^TBv.
\]
Its decrease is
\[
D(p)=G\Delta\left(a-\frac{\tau b}{2}\right).
\]
It remains to prove
\[
a-\frac{\tau b}{2}\le K\left(1-\frac{\tau q}{2}\right).
\]
The difference
\[
F(\tau)=K-a-\frac{\tau}{2}(Kq-b)
\]
is affine on \([0,1/q]\), so it is enough to check the endpoints. Since
\(K=(u^TBu)(u^TB^{-1}u)\ge1\) and \(a\le1\),
\[
F(0)=K-a\ge0.
\]
At the other endpoint,
\[
2F(1/q)=K+b/q-2a.
\]
Weighted Cauchy--Schwarz gives
\[
|a|^2\le (u^TB^{-1}u)(v^TBv)=sb,
\]
while AM--GM gives
\[
K+b/q=qs+b/q\ge2\sqrt{sb}\ge2|a|\ge2a.
\]
Thus \(F(1/q)\ge0\), hence \(F(\tau)\ge0\) throughout the interval. Taking the
maximum over all feasible \(p\) yields \(D_*\le K D_C\), proving the first bound.
The Kantorovich inequality gives the condition-number form and its standard
two-eigenspace equality case gives sharpness.

## Fraction-of-Cauchy implies fraction-of-optimal in the SPD case

Suppose an approximate trust-region solver returns a feasible step \(p\) with
\[
D(p)\ge \gamma D_C,\qquad 0<\gamma\le1.
\]
Then automatically
\[
\boxed{D(p)\ge \frac{\gamma}{K}D_*
\ge \gamma\frac{4\kappa}{(\kappa+1)^2}D_*.}
\]
The condition-number conversion factor is sharp if only the fraction-of-Cauchy
assumption is known. On the two-dimensional equality family above, take a large
radius and a point \(x p_C\) on the Cauchy segment with
\(2x-x^2=\gamma\); it has exactly \(\gamma D_C\) decrease.

This gives a direct conversion between two standard sufficient-decrease notions
for uniformly positive-definite quadratic models. The conversion is not available
with a positive constant independent of conditioning.

## Metric trust regions

For an ellipsoidal trust region \(p^TMp\le\Delta^2\), \(M\succ0\), define the
metric Cauchy direction by \(-M^{-1}g\). Under the change of variables
\(y=M^{1/2}p\), the result applies verbatim to
\[
\widetilde B=M^{-1/2}BM^{-1/2},\qquad
\widetilde g=M^{-1/2}g.
\]
In particular, with \(\kappa=\kappa_2(\widetilde B)\), the same sharp universal
fraction \(4\kappa/(\kappa+1)^2\) holds.

## Why positive definiteness matters

No analogous positive constant exists for arbitrary indefinite models. For example,
with \(B=\operatorname{diag}(1,-M)\), \(g=e_1\), and \(\Delta\ge1\), the Cauchy
point gives decrease \(1/2\), whereas the feasible point \(p=(0,\Delta)^T\)
gives decrease \(M\Delta^2/2\). The Cauchy-to-optimal ratio can therefore be made
arbitrarily small.

## Computational model and limitations

The theorem is for exact arithmetic, a real SPD quadratic model, a Euclidean ball
(or the stated fixed SPD metric after change of variables), and predicted quadratic
model reduction. The Cauchy point requires the gradient, one product \(Bg\), and
inner products; the exact trust-region minimizer is used only as the benchmark.
The result does not claim closeness of the steps themselves, actual reduction for a
nonquadratic objective, floating-point backward stability, or superiority to dogleg,
Steihaug-CG, Lanczos, or exact/secular-equation trust-region solvers. For indefinite
models the stated positive factor fails, as shown above.

The deterministic numerical artifact checks sharp equality families and the
radius-uniform fixed-gradient bound. It is supporting evidence, not part of the
proof.

## Literature context

The Cauchy point and fraction-of-Cauchy decrease are classical trust-region tools.
Conn--Gould--Toint treat the Cauchy point as the inexpensive baseline against the
exact trust-region model minimizer. Conn--Scheinberg--Vicente explicitly distinguish
fraction-of-Cauchy decrease from the stronger fraction-of-optimal-decrease notion in
trust-region analysis. The Kantorovich inequality classically gives the sharp
steepest-descent condition-number factor in the unconstrained SPD setting.

Searches of these literatures and newer trust-region material did not locate the
radius-uniform inequality above, the sharp conversion from fraction-of-Cauchy to
fraction-of-optimal decrease for SPD models, or its condition-number equality
classification. Because broad classical monographs and older trust-region papers
are extensive, hidden equivalent historical coverage cannot be excluded.

## References

1. A. R. Conn, N. I. M. Gould, P. L. Toint, *Trust Region Methods*, SIAM, 2000, Chapter 7. https://doi.org/10.1137/1.9780898719857.ch7
2. A. R. Conn, K. Scheinberg, L. N. Vicente, “Global Convergence of General Derivative-Free Trust-Region Algorithms to First- and Second-Order Critical Points,” *SIAM Journal on Optimization* 20(1), 2009, 387–415. https://doi.org/10.1137/060673424
3. A. R. Conn, K. Scheinberg, L. N. Vicente, *Introduction to Derivative-Free Optimization*, SIAM, 2009, Chapter 10. https://doi.org/10.1137/1.9780898718768.ch10
4. M. Lin, “On an operator Kantorovich inequality for positive linear maps,” *Journal of Mathematical Analysis and Applications* 402(1), 2013, 127–132; its introduction states the classical vector Kantorovich inequality. https://doi.org/10.1016/j.jmaa.2013.01.015
