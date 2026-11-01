# A sharp John-ellipsoid contact transition and strict volume-ratio ordering for simplex frusta

## Finding
For each integer \(d\ge3\), set
\[
F_{d,a}=\left\{x\in\mathbb R^d:x_i\ge0\ (1\le i\le d),\quad a\le \sum_{i=1}^d x_i\le1\right\},\qquad 0<a<1.
\]
This is a simplex with a parallel slice removing its original vertex at the origin. Write \(e=\mathbf1/\sqrt d\) and \(a_*=(d-1)/(d+1)\). Its unique maximum-volume inscribed ellipsoid is
\[
E_{d,a}=\big\{c+Q^{1/2}u:\|u\|_2\le1\big\},\quad
c=\frac{s}{d}\mathbf1,\quad Q=\alpha^2ee^T+\beta^2(I-ee^T),
\]
with the exact two-phase formulas
\[
(s,\alpha^2,\beta^2)=
\begin{cases}
\left(\dfrac{d}{d+1},\dfrac1{d(d+1)^2},\dfrac1{d(d+1)}\right),&0<a\le a_*,\\[4pt]
\left(\dfrac{1+a}{2},\dfrac{(1-a)^2}{4d},\dfrac{a}{d(d-1)}\right),&a_*\le a<1.
\end{cases}
\]
Both expressions agree at \(a=a_*\). Every coordinate facet and the facet \(\sum_i x_i=1\) is tangent to the ellipsoid; the newly added facet \(\sum_i x_i=a\) is tangent if and only if \(a\ge a_*\).

Moreover, the affine-invariant **John volume fraction**
\[
J_d(a)=\frac{\operatorname{Vol}_d(E_{d,a})}{\operatorname{Vol}_d(F_{d,a})}
\]
is strictly increasing for \(0<a<1\). In particular, with \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\),
\[
J_d(a)=\frac{\kappa_d d!}{1-a^d}\times
\begin{cases}
\dfrac{1}{d^{d/2}(d+1)^{(d+1)/2}},&a\le a_*,\\[5pt]
\dfrac{(1-a)a^{(d-1)/2}}{2d^{d/2}(d-1)^{(d-1)/2}},&a\ge a_*.
\end{cases}
\]
Consequently
\[
\lim_{a\uparrow1}J_d(a)=\frac{\kappa_d(d-1)!}{2d^{d/2}(d-1)^{(d-1)/2}},
\]
a limit not attained within the full-dimensional family.

## Assumptions and scope
The ambient metric is Euclidean, and volumes are ordinary \(d\)-dimensional Lebesgue volumes. Each \(F_{d,a}\) is full-dimensional for \(0<a<1\). A John ellipsoid is the *unrestricted* largest-volume ellipsoid contained in a convex body: it is not assumed in advance to be axis-aligned, centered on the symmetry axis, or tangent to particular facets. The theorem treats every \(d\ge3\), and all such \(a\). The limiting body at \(a=1\) is lower-dimensional and is excluded.

## Proof
**1. Reduction without assuming the shape.** A full-dimensional compact convex body has a unique maximum-volume inscribed ellipsoid. Any permutation of the \(d\) coordinates preserves \(F_{d,a}\); by uniqueness the ellipsoid is permutation-invariant. The fixed vectors and symmetric matrices under every coordinate permutation have, respectively, the form \(c=(s/d)\mathbf1\) and \(Q=\alpha^2ee^T+\beta^2(I-ee^T)\), with \(\alpha,\beta>0\). This handles all possible translations, tilts and anisotropies of competing ellipsoids.

**2. Exact facet inequalities.** The support width of the ellipsoid in direction \(v\) is \(\sqrt{v^TQv}\). In the sum direction \(\mathbf1\), it equals \(\sqrt d\,\alpha\). For every coordinate direction, it is
\[
\sqrt{Q_{ii}}=\sqrt{\frac{\alpha^2+(d-1)\beta^2}{d}}.
\]
Put \(R=\sqrt d\,\alpha\). Containment in all \(d+2\) defining halfspaces is *equivalent* to
\[
s-R\ge a,\qquad s+R\le1,\qquad
\frac{s}{d}\ge\sqrt{\frac{R^2/d+(d-1)\beta^2}{d}}.
\]
The last inequality rearranges to
\[
\beta^2\le\frac{s^2-R^2}{d(d-1)}.
\]
In particular, feasibility forces \(0<R\le (1-a)/2\).

**3. Scalar determinant maximization.** The ellipsoid volume is \(\kappa_d\alpha\beta^{d-1}=\kappa_d R\beta^{d-1}/\sqrt d\). At fixed feasible \(R\), its value increases strictly with \(\beta\); its maximal allowed value increases with \(s\), so optimality forces \(s=1-R\) and
\[
\beta^2=\frac{(1-R)^2-R^2}{d(d-1)}=\frac{1-2R}{d(d-1)}.
\]
Hence the remaining objective is, up to a positive dimension constant,
\[
f_d(R)=R(1-2R)^{(d-1)/2},\qquad 0<R\le\frac{1-a}{2}.
\]
Its logarithmic derivative is \(1/R-(d-1)/(1-2R)\), strictly positive for \(R<1/(d+1)\) and strictly negative for \(R>1/(d+1)\). Thus its unique maximum is at
\[
R=\min\left\{\frac1{d+1},\frac{1-a}{2}\right\}.
\]
Substitution yields the asserted exact semiaxes, center, and threshold. The equalities in Step 2 show the tangency statements; the coordinate facet contacts occur at each corresponding minimum-coordinate supporting point, while the lower facet reaches tangency precisely when \(s-R=a\).

**4. Strict ordering of volume fractions.** The frustum is the difference of two homothetic simplices, so \(\operatorname{Vol}_d(F_{d,a})=(1-a^d)/d!\). The ellipsoid determinant gives the two displayed formulas for \(J_d(a)\).

In the first phase, the numerator is constant and \(1-a^d\) decreases strictly. In the second phase, after cancellation of \(1-a\), its varying factor is
\[
g_d(a)=\frac{a^{(d-1)/2}}{1+a+\dots+a^{d-1}}.
\]
For \(p=(d-1)/2>0\), the reciprocal \(1/g_d(a)=\sum_{j=0}^{d-1}a^{j-p}\) is a sum of symmetric exponent pairs \(a^t+a^{-t}\), plus possibly a central constant. Each pair with \(t>0\) strictly decreases as \(a\) increases through \((0,1)\), because
\[
\frac{d}{da}(a^t+a^{-t})=t(a^{t-1}-a^{-t-1})<0.
\]
Therefore \(g_d\), and hence \(J_d\), increases strictly throughout the second phase. Equality of the two formulas at \(a_*\) proves strict increase across the transition. Finally, \(1-a^d\sim d(1-a)\) proves the stated sharp boundary limit. \(\square\)

## Verification
The standalone `verify.py` uses only Python's standard library. For each dimension from 3 through 15, it checks coordinate supports, top and lower support inequalities, phase agreement, the determinant objective against 301 deterministic feasible axial radii and 50 seeded random radii per parameter, and the boundary limit. It also samples a grid of truncation values to check numerical nonreversal of the normalized volume fraction. The script exits with `ALL_CHECKS_PASSED`; these finite calculations supplement, but do not replace, the analytic proof for all dimensions and all real parameters.

## Relationship to prior work
John's theorem on uniqueness and extremal ellipsoids is classical. Ivanov and Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions* (first arXiv version, December 22, 2022, arXiv:2212.11781), give much more general optimality conditions; their work does not supply the present explicit frustum semiaxes, contact threshold, or strict volume-ratio profile. Results on untruncated simplex ellipsoids recover the first phase only. Horwitz's treatment of ellipses in quadrilaterals addresses two-dimensional cases rather than the dimensions treated here. Related research on one-vertex simplex truncations gives mixed-volume coefficients for opposite bodies; those formulas do not determine maximum inscribed ellipsoids. The result claimed here is the exact two-regime John optimization and its strict affine-invariant relative-volume ordering.

## Limitations
The family is a single-vertex parallel truncation of a simplex. It does not describe arbitrary truncating directions, truncations at multiple vertices, or non-Euclidean maximal ellipsoids. The derivation uses known John-ellipsoid existence and uniqueness. The finite verification program is not a general proof. Searches and inspection of the most relevant accessible sources found no direct coverage, but historical priority is not exhaustively established, especially for less-indexed older polytope/ellipsoid literature.

## References
- G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781 (first version December 22, 2022), https://arxiv.org/abs/2212.11781.
- A. Eydelzon, *From Steiner Inellipse to John Ellipsoid of Simplex: Corner-Volume Characterization*, arXiv:2609.08045 (2026), https://arxiv.org/abs/2609.08045. This is background on the untruncated simplex, not an eligible lead source.
- A. Horwitz, *The locus of centers of ellipses inscribed in quadrilaterals*, arXiv:math/0312403 (2003), https://arxiv.org/abs/math/0312403.
- Classical John maximal-inscribed-ellipsoid uniqueness and contact theorem, as reviewed in Ivanov–Naszódi above.
