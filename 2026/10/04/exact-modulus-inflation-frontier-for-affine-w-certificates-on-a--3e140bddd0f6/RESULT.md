# Exact modulus-inflation frontier for affine W-certificates on a scalar quadratic
## Finding

Let
\[
f(x)=\frac a2x^2,
\qquad a>0,
\]
on \(\mathbb R\), and fix a nonoptimal evaluation center \(u\ne0\). Its true optimality gap is
\[
G=f(u)-f^*=\frac a2u^2.
\]
For \(\Delta>0\), let
\[
S(\Delta):=
\sup_{h\le f\ \mathrm{affine}} s(h,u,\Delta),
\]
where \(s\) is the descent-slowness from the affine W-certificate definition.

Write
\[
r=\frac{\Delta}{G}.
\]
Then the exact envelope over all affine minorants is
\[
S(\Delta)=
\begin{cases}
\displaystyle
\frac{2}{a|u|\left(1+\sqrt{1-r}\right)}, & 0<r<1,\\[3mm]
\displaystyle
\frac{2}{a|u|}, & r=1,\\[3mm]
+\infty, & r>1.
\end{cases}
\]

For \(0<r<1\), the supremum is attained by a unique affine minorant: the tangent to \(f\) at
\[
y_\star
=
\operatorname{sgn}(u)|u|\sqrt{1-r}.
\]
At the exact-gap boundary \(r=1\), the finite supremum is not attained by any affine minorant. For \(r>1\), the constant minorant \(h\equiv0\) already has infinite descent-slowness because its target sublevel set is empty.

As a consequence, the existence of a \((\mu,\Delta)\) affine W-certificate is completely classified. For \(0<r<1\), such a certificate exists if and only if
\[
\frac{\mu}{a}
\ge
\frac{1+\sqrt{1-r}}{1-\sqrt{1-r}}.
\]
For \(r=1\), a W-certificate exists if and only if
\[
\mu>a.
\]
For \(r>1\), it exists for every \(\mu>0\).

Thus a candidate gap below the true gap can be certified only after inflating the trial growth modulus by an explicit factor. As \(r\downarrow0\), that required factor diverges. At the exact gap, the threshold tends to the true quadratic-growth modulus \(a\), but equality is lost because the best descent-slowness is only a nonattained supremum.

## Assumptions and scope

The feasible set is all of \(\mathbb R\), the objective is the scalar strongly convex quadratic above, and the center is nonoptimal. The result concerns the affine W-certificate geometry of Section 2 of the recent source; it does not assert an oracle-complexity result for the full BLW or A-BLW algorithms.

The W-certificate definition itself only requires convexity, an affine minorant, a center, and a target descent. The global Lipschitz assumption imposed later for the nonsmooth BLW complexity theorem is therefore not needed for this calculation.

The source uses the true pointwise quadratic-growth modulus \(\mu^*\) only in analysis and an algorithmic trial modulus \(\mu\) in the certificate. Here the true modulus is exactly
\[
\mu^*=a.
\]
The distinction between \(a\) and the trial value \(\mu\) is essential to the frontier above.

## Proof

Every affine function can be written as
\[
h(x)=cx+d.
\]
The condition \(h(x)\le ax^2/2\) for every \(x\in\mathbb R\) is equivalent to
\[
d\le-\frac{c^2}{2a}.
\]
For fixed slope \(c\), increasing \(d\) toward this upper limit can only shrink the target sublevel set
\[
\{x:h(x)\le f(u)-\Delta\}
\]
and therefore can only increase its distance from \(u\). Hence an optimal minorant, whenever it exists with nonzero slope, must be tangent to \(f\).

Parameterize tangent minorants by
\[
y=\frac ca,
\qquad
h_y(x)=ayx-\frac a2y^2.
\]
By symmetry it is enough to take \(u>0\). Put
\[
L=G-\Delta.
\]
For \(y>0\), the target set is the half-line
\[
x\le
\frac{u^2+y^2-2\Delta/a}{2y}.
\]
Therefore the distance from \(u\) is
\[
d_y
=
\max\left\{0,
\frac{2\Delta/a-(u-y)^2}{2y}
\right\}.
\]
When \(0<\Delta<G\), every \(y\le0\) gives zero distance, so only positive slopes can be optimal. Define
\[
y_\star
=
\sqrt{u^2-\frac{2\Delta}{a}}.
\]
On the interval where \(d_y>0\),
\[
d_y
=u-\frac y2-\frac{y_\star^2}{2y}.
\]
The difference from its value at \(y_\star\) factors exactly as
\[
d_{y_\star}-d_y
=
\frac{(y-y_\star)^2}{2y}
\ge0.
\]
Thus the maximizer is unique and
\[
d_{y_\star}=u-y_\star.
\]
Writing
\[
r=\frac{\Delta}{G}
=
\frac{2\Delta}{au^2}
\]
gives
\[
y_\star=u\sqrt{1-r},
\]
and hence
\[
S(\Delta)
=
\frac{u(1-\sqrt{1-r})}{\Delta}
=
\frac{2}{au(1+\sqrt{1-r})}.
\]
Restoring symmetry replaces \(u\) by \(|u|\).

At \(\Delta=G\), the target level is zero. For every positive tangent slope,
\[
d_y=
\max\left\{0,u-\frac y2\right\}.
\]
Hence
\[
\sup_{y>0}d_y=u,
\]
but equality would require \(y=0\). The zero-slope tangent is \(h\equiv0\), whose zero sublevel set is all of \(\mathbb R\), so its distance is zero. Lower affine minorants cannot improve on their tangent envelopes. Thus
\[
S(G)=\frac{u}{G}=\frac{2}{au}
\]
and the supremum is not attained.

If \(\Delta>G\), then the target level \(G-\Delta\) is negative. For \(h\equiv0\), the set
\[
\{x:0\le G-\Delta\}
\]
is empty. By the source convention its distance is \(+\infty\), so \(S(\Delta)=+\infty\).

Finally, the W-certificate inequality is
\[
s(h,u,\Delta)^2
\ge
\frac{2}{\mu\Delta}.
\]
For \(0<r<1\), the maximum is attained, so existence is equivalent to
\[
S(\Delta)^2\ge\frac{2}{\mu\Delta}.
\]
Substituting the exact envelope gives
\[
\mu
\ge
\frac{2}{\Delta S(\Delta)^2}
=
a\frac{(1+\sqrt{1-r})^2}{r}
=
a\frac{1+\sqrt{1-r}}{1-\sqrt{1-r}}.
\]
At \(r=1\), the formal threshold is \(\mu=a\), but it is not attained because \(S(G)\) is not attained; therefore existence is exactly \(\mu>a\). For \(r>1\), infinite descent-slowness makes the certificate inequality true for every positive trial modulus.

## Verification

The standalone script `artifacts/verify_w_certificate_quadratic.py` checks the tangent-minorant envelope and the W-threshold in exact rational arithmetic after parameterizing
\[
r=1-q^2
\]
with rational \(q\in(0,1)\). It also checks finite-slope behavior at the exact-gap boundary and the strict loss of attainment there.

These finite checks support the algebra but do not replace the proof over all affine minorants and all positive parameters.

## Relationship to prior work

Jiang, Tang, and Zhang introduce descent-slowness for affine minorants and define the affine W-certificate by the inequality
\[
s(h,\bar x,\Delta)^2\ge\frac{2}{\mu\Delta}.
\]
Their Proposition 2.3 and Corollary 2.5 convert such a certificate into an optimality-gap bound under quadratic growth and distinguish the algorithmic trial modulus from the true modulus. Their full text also includes conditioned quadratic experiments, but it does not state the exact scalar envelope over all affine minorants, the trial-modulus inflation law above, or the nonattained exact-gap boundary.

Zhang and Sra previously introduced a W-stationarity certificate for piecewise-smooth optimization under quadratic growth. Their certificate is built from a W-gap over a radius and multiple local support models, with a different search subroutine and different parameters. The inspected full text does not reduce that construction to the affine descent-slowness frontier derived here.

Lan's accelerated bundle-level framework supplies the level-set and prox-center architecture underlying later bundle-level methods. It controls upper/lower gaps and level-set projections, but predates the affine W-certificate, and the inspected paper contains neither descent-slowness nor a quadratic-growth certificate of this form.

The present result therefore calibrates the new affine W-certificate itself on the canonical strongly convex quadratic. It does not claim novelty for tangent minorants or scalar quadratic algebra separately.

## Limitations

The classification is one-dimensional and unconstrained. In higher dimensions, the optimal affine-minorant geometry can depend on the orientation of the center, the Hessian, and the feasible set. For constrained quadratics, a minorant's target set can interact with the boundary and change both attainment and the optimal slope.

The result does not imply that BLW will actually generate the globally optimal affine minorant at a given center and target. It characterizes what is geometrically possible over the entire class of affine minorants.

Because the scalar derivation is elementary once the 2026 certificate is defined, an equivalent calibration could in principle occur in earlier bundle or error-bound literature under different terminology. Targeted searches and the closest full texts inspected did not reveal such a statement; this remains the main historical-originality risk.

## References

1. L. Jiang, K. Tang, Z. Zhang, *Optimal Parameter-Free First-Order Methods for Convex Optimization with Unknown Growth and Smoothness*, arXiv:2607.11878v1, 2026.
2. Z. Zhang, S. Sra, *Linearly Convergent Algorithms for Nonsmooth Problems with Unknown Smooth Pieces*, arXiv:2507.19465v1, 2025.
3. G. Lan, *Bundle-Level Type Methods Uniformly Optimal for Smooth and Nonsmooth Convex Optimization*, arXiv:1309.5547v1, 2013.
