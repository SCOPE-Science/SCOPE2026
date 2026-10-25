# Dilogarithmic acuteness law for uniform-angle triangles on an ellipse

## Finding
Let \(T:\mathbb R^2\to\mathbb R^2\) be invertible, with singular values \(a\ge b>0\). Let \(\Theta_1,\Theta_2,\Theta_3\) be independent and uniform on \([0,2\pi)\), and put \(X_j=T(\cos\Theta_j,\sin\Theta_j)\). The probability that the Euclidean triangle with vertices \(X_1,X_2,X_3\) is acute is exactly
\[
 \Pr(\text{acute})=\frac14-\frac{3}{2\pi^2}\operatorname{Li}_2\!\left(\left(\frac{a^2-b^2}{a^2+b^2}\right)^2\right),
\]
where \(\operatorname{Li}_2(z)=\sum_{m=1}^{\infty}z^m/m^2\) for \(0\le z\le1\).
Consequently the circle is the unique maximizer (up to similarities) with probability \(1/4\), and the probability strictly decreases with the axis ratio \(a/b\). With \(s=\log(a/b)\), the near-circular stability law is
\[
 \Pr(\text{acute})=\frac14-\frac{3}{2\pi^2}s^2+O(s^4)\quad(s\to0).
\]
With \(t=b/a\), the flat-ellipse law is
\[
 \Pr(\text{acute})=\frac{6t^2}{\pi^2}\left(1-\log(4t^2)\right)+O(t^4|\log t|)\quad(t\downarrow0),
\]
so the leading term is \(12t^2\log(1/t)/\pi^2\). Intriguingly this entire probability equals the **previously known** probability that a triangle from three uniform circle points contains a fixed point at normalized distance \((a^2-b^2)/(a^2+b^2)\) from the center. The claim here is the elliptic acuteness law and this cross-model identity, *not* priority for the dilogarithmic off-center containment formula.

## Assumptions and scope
The sampling law is the pushforward of **uniform angular measure on the circle** under \(T\). In coordinates \((a\cos\theta,b\sin\theta)\), the parameter \(\theta\) is uniform. Except when \(a=b\), this is **not** uniform Euclidean arclength on the ellipse and is not uniform area measure inside it. The triangle is nondegenerate almost surely; the right-angle boundary has probability zero. Translations, rotations and common positive scaling have no effect. The statement holds for every finite axis ratio \(a/b\ge1\), and the flat limit is taken through positive \(b\), not at a singular ellipse.

## Proof
Write \(T=U\operatorname{diag}(a,b)V\) by singular-value decomposition. Common rotations and a uniform shift of the original angle do not affect the law, so \(T\) may be taken diagonal. Set \(k=(a^2-b^2)/(a^2+b^2)\in[0,1)\). Fix the first unit-circle point at angle \(\Theta_1\). If \(\beta=(\Theta_2-\Theta_1)\bmod2\pi\in(0,2\pi)\), then the directed chord from the first point to the second has positive scalar multiple of unit direction angle \(\Theta_1+\pi/2+\beta/2\), by the sine subtraction identity. The corresponding angle for the third chord is \(\Theta_1+\pi/2+\gamma/2\) with independent \(\gamma\) uniform on \((0,2\pi)\). Thus the difference \(\delta=|\beta-\gamma|/2\in[0,\pi]\) has density \(2(\pi-\delta)/\pi^2\); the common phase \(\phi\) is uniform modulo \(2\pi\) and independent of \(\delta\).

The Euclidean dot product of these two chord vectors *after* the linear transformation has the sign of
\[
 a^2\cos\phi\cos(\phi+\delta)+b^2\sin\phi\sin(\phi+\delta)
 =\frac{a^2+b^2}{2}\bigl(\cos\delta+k\cos(2\phi+\delta)\bigr).
\]
For \(0<k<1\), the conditional probability that this angle is obtuse therefore equals \(q_k(\delta)\), where
\[
q_k(\delta)=\begin{cases}
0,&\cos\delta\ge k,\\
\pi^{-1}\arccos(\cos\delta/k),&|\cos\delta|<k,\\
1,&\cos\delta\le-k.
\end{cases}
\]
In particular \(q_k(\pi-\delta)=1-q_k(\delta)\). The case \(k=0\) follows by continuity, with \(q_0(\delta)\) the indicator of \(\delta>\pi/2\). A nondegenerate triangle cannot have more than one obtuse angle. By exchangeability, its acute probability is one minus three times the probability that the angle at the first vertex is obtuse.

Put \(\alpha=\arcsin k\), and integrate the conditional probability against the triangular density, using the reflection symmetry. The deviation of the first-vertex obtuse probability from its circular value \(1/4\) is
\[
 \frac4{\pi^2}\int_0^{\alpha}s\left[\frac12-\frac1\pi\arcsin\left(\frac{\sin s}{k}\right)\right]ds.
\]
Integrating by parts (the boundary term vanishes) and setting \(\sin s=k\sin u\) gives
\[
 \Pr(\text{acute})=\frac14-\frac6{\pi^3}\int_0^{\pi/2}\arcsin^2(k\sin u)\,du.\tag{1}
\]
For \(0\le z<1\), the power series identity
\[
 \arcsin^2z=\frac12\sum_{m=1}^{\infty}\frac{4^m z^{2m}}{m^2\binom{2m}{m}}
\]
and the beta-integral identity
\[
 \int_0^{\pi/2}\sin^{2m}u\,du=\frac\pi2\frac{\binom{2m}{m}}{4^m}
\]
yield, by nonnegative termwise integration,
\[
 \int_0^{\pi/2}\arcsin^2(k\sin u)\,du=\frac\pi4\operatorname{Li}_2(k^2).
\]
Substitution into (1) proves the exact law. The \(k=0\) case follows directly; the limit \(k\uparrow1\) follows from monotone convergence, since \(\operatorname{Li}_2(1)=\pi^2/6\).

For strictness, \(k\) increases strictly with \(a/b>1\), while \(\operatorname{Li}_2\) increases strictly on \((0,1)\). For small \(s\), \(k=\tanh s\) and \(\operatorname{Li}_2(k^2)=s^2+O(s^4)\). For small \(t\), let \(d=1-k^2=4t^2/(1+t^2)^2\). Using the elementary dilogarithm endpoint expansion \(\operatorname{Li}_2(1-d)=\pi^2/6+d\log d-d+O(d^2|\log d|)\) gives the stated flat-ellipse expansion.

## Verification
The standalone script `verify.py` evaluates the exact dilogarithm formula, the **independently derived** integral (1), two endpoint asymptotic estimates, and direct Cartesian dot products of 220,000 independently sampled triples at multiple axis ratios. Its successful run reports `ALL_AFFINE_ELLIPSE_ACUTENESS_CHECKS_OK`. These computations are consistency tests and are not an infinite-dimensional or all-ratio certificate. The analytic identity above is the proof.

## Relationship to prior work
The circle value \(1/4\) is classical. Koroleva–Nikitin (first available arXiv version, 7 January 2013) study perimeter and area extremes for triangles and polygons from independent uniform **circle** points, not acuteness after anisotropic scaling. Hall (1982) studies random triangles from **area-uniform points inside** Euclidean balls, a distinct probability model. Banerjee's (2009) thesis includes a circle-to-ellipse Monte Carlo experiment for **interior-uniform** triangle vertices, not the boundary pushforward model in this theorem.

An important exact prior match must be distinguished: a 2018 solution by Jeremy Tan Jie Rui to the probability that three uniform points on a circle form a triangle **containing a fixed off-center point** gives the same dilogarithm function; Ismailov (2026) states and independently proves that formula. Those works determine a different geometric event on the circle. The present theorem derives the corresponding law for **Euclidean acuteness after arbitrary nonsingular affine deformation**, with the nontrivial parameter identification \(k=(a^2-b^2)/(a^2+b^2)\). It does not claim a new dilogarithm evaluation or that the off-center theorem was previously unknown. No source checked here directly stated or implied the affine-ellipse acuteness identity without a new geometric argument. Historical priority remains provisional.

## Limitations
The model excludes arclength-uniform ellipse vertices, points drawn uniformly from the ellipse interior, and arbitrary convex curves. The limiting degenerate ellipse has zero acute probability but is not covered as a positive-area body. Search and accessible-source inspection cannot rule out unlocated equivalent literature, especially alternate formulations relating affine acute angles to circle containment. Independent mathematical review has not occurred.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1 (7 January 2013), especially introduction and random circumference sampling model.
2. G. R. Hall, *Acute Triangles in the n-Ball*, Journal of Applied Probability **19** (1982), 712–715, DOI: 10.2307/3213533 (interior-sampling problem; abstract verified).
3. N. Banerjee, *Random Obtuse Triangles and Convex Quadrilaterals*, MIT M.Sc. thesis (2009), Section 3.8 (interior ellipse Monte Carlo).
4. Jeremy Tan Jie Rui (Parcly Taxel), answer dated 10 February 2018 to *Probability that a random triangle with vertices on a circle contains an arbitrary point inside said circle*, Mathematics Stack Exchange question 2641793 (original off-center dilogarithm law).
5. A. Ismailov, *With what probability does an inscribed triangle contain a given point?*, arXiv:2601.02929v1 (6 January 2026), Theorem 1.1 and discussion of the 2018 derivation.
