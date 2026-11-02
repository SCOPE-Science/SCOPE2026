# Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles

## Finding

For every pair of semiaxes \(a\ge b>0\), independently choose three parameters \(\Theta_1,\Theta_2,\Theta_3\) uniformly on \([0,2\pi)\), and form the Euclidean triangle with vertices \((a\cos\Theta_j,b\sin\Theta_j)\). Put \(\tau=(a^2-b^2)/(a^2+b^2)\) and \(\operatorname{Li}_2(z)=\sum_{k\ge1}z^k/k^2\). The triangle is acute with probability

\[
\boxed{P(a,b)=\frac14-\frac{3}{2\pi^2}\operatorname{Li}_2(\tau^2).}
\]

This is a probability for **uniform eccentric anomaly**, equivalently the pushforward of normalized angular measure on the circle under \(\operatorname{diag}(a,b)\). It is **not** the probability for uniform Euclidean arclength on the ellipse.

Writing \(r=a/b\ge1\), the probability strictly decreases as \(r\) increases from \(1\) to infinity. Its range for nondegenerate ellipses is \((0,1/4]\), with maximum \(1/4\) attained only for circles. If \(s=\log r\to0\), then

\[
P(r)=\frac14-\frac{3}{2\pi^2}s^2+\frac{5}{8\pi^2}s^4+O(s^6).
\]

At the opposite, slender-ellipse limit,

\[
P(r)=\frac{6}{\pi^2r^2}(2\log r+1-\log4)
+O\!\left(\frac{\log r}{r^4}\right),\quad r\to\infty.
\]

An exact probabilistic coincidence follows: this acuteness probability equals the **known** probability that a triangle of three independent uniform points on the unit circle contains a specified point at distance \(\tau\) from the circle's center. This identity concerns probabilities, not equality of the corresponding triangle events.

## Assumptions and scope

All triangles use the ordinary Euclidean angle, and acuteness means that all three interior angles are strictly less than \(\pi/2\). Independent continuous sampling makes repeated vertices and right-angle cases probability-zero events. Semiaxes may be swapped without altering the law, so \(a\ge b\) loses no generality. The limit \(b/a\to0\) is a degeneration, not an additional ellipse included in the theorem.

## Proof

**Chord-direction reduction.** Fix the first vertex at parameter \(\alpha\). Write the other two parameters modulo a full revolution as \(\alpha+2U\) and \(\alpha+2V\), with \(U,V\) independent uniform variables on \((0,\pi)\). For \(w\in(0,\pi)\), the circle chord from angle \(\alpha\) to \(\alpha+2w\) has direction
\[
(-\sin(\alpha+w),\cos(\alpha+w))
\]
multiplied by a positive scalar. Consequently its affine ellipse image has direction \(\operatorname{diag}(a,b)\) applied to this vector.

Let \(\Delta=U-V\) and let \(m=\alpha+(U+V)/2+\pi/2\), taken modulo \(\pi\). The signed difference has density \((\pi-|\Delta|)/\pi^2\) for \(|\Delta|<\pi\). Because \(\alpha\) is independent uniform on the full circle, \(m\) is uniform modulo \(\pi\) and is independent of \(\Delta\). The dot product of the two ellipse chord vectors has the sign of
\[
\cos\Delta+\tau\cos(2m),
\quad\tau=\frac{a^2-b^2}{a^2+b^2}.
\]
(The positive factors omitted from the chord lengths cannot affect the sign.)

**Obtuse probability.** For fixed \(m\), an obtuse angle at the first vertex is equivalent to \(|\Delta|>d(m)\), where \(d(m)=\arccos(-\tau\cos2m)\). The triangular law gives
\[
\Pr(|\Delta|>d)=\frac{(\pi-d)^2}{\pi^2}.
\]
Therefore
\[
\Pr(\text{first angle obtuse})
=\frac1{2\pi^3}\int_0^{2\pi}\arccos(\tau\cos t)^2\,dt
=\frac14+\frac1{2\pi^3}\int_0^{2\pi}\arcsin(\tau\cos t)^2\,dt.
\]
The cross term vanishes by replacing \(t\) with \(t+\pi\).

**Exact series.** The analytic function \(f(z)=\arcsin^2 z\) satisfies \((1-z^2)f''(z)-zf'(z)=2\), with \(f(0)=f'(0)=0\). Coefficient comparison gives the convergent expansion
\[
\arcsin^2 z=\frac12\sum_{k=1}^{\infty}
\frac{(2z)^{2k}}{k^2\binom{2k}{k}},\qquad |z|<1.
\]
Since \(\frac1{2\pi}\int_0^{2\pi}\cos^{2k}t\,dt=\binom{2k}{k}/4^k\), termwise integration (valid for \(0\le\tau<1\)) yields
\[
\frac1{2\pi}\int_0^{2\pi}\arcsin^2(\tau\cos t)\,dt
=\frac12\sum_{k=1}^{\infty}\frac{\tau^{2k}}{k^2}
=\frac12\operatorname{Li}_2(\tau^2).
\]
Thus the probability of an obtuse angle at a specified vertex is \(1/4+\operatorname{Li}_2(\tau^2)/(2\pi^2)\). At most one interior angle in a nondegenerate triangle can be obtuse, and all three labels are exchangeable. Subtracting three times this probability from one proves the displayed exact acuteness law.

**Strict ordering and limits.** For \(r\ge1\), \(\tau=(r^2-1)/(r^2+1)=\tanh(\log r)\) increases strictly for \(r>1\). Each coefficient of \(\operatorname{Li}_2(\tau^2)\) is positive, proving strict decrease and uniqueness of the circular maximizer. Continuity and \(\operatorname{Li}_2(1)=\pi^2/6\) give the entire range and the zero degeneration limit. Expanding \(\tanh^2 s=s^2-2s^4/3+O(s^6)\) and \(\operatorname{Li}_2(z)=z+z^2/4+O(z^3)\) gives the circular stability expansion. Finally set \(\delta=1-\tau^2=4r^2/(r^2+1)^2\). The elementary reflection identity \(\operatorname{Li}_2(1-\delta)=\pi^2/6-\operatorname{Li}_2(\delta)-\log\delta\log(1-\delta)\) yields \(P=\frac3{2\pi^2}\delta(1-\log\delta)+O(\delta^2|\log\delta|)\), which gives the slender-ellipse expansion.

## Verification

Run `python checker.py` using Python 3.11 or newer. The checker compares independently computed Simpson quadrature of the arcsine-square integral with the dilogarithm series and checks direct random-triangle Euclidean dot products at several axis ratios. It also tests limiting behavior and strict shape ordering numerically. These numerical checks are corroboration; the preceding analytic argument proves the infinite and asymptotic assertions.

## Relationship to prior work

The circle probability \(1/4\) is classical. The off-center circle-containment formula with precisely the same dilogarithm function was obtained in a 2018 public solution (and later revisited by Ismailov in 2026); **that formula is not new here**. The contribution is the exact Euclidean-acuteness law for affine-uniform sampling on a noncircular ellipse, its strict anisotropy ordering, and the explicit equality of two otherwise distinct random-triangle probabilities.

Akopyan, Edelsbrunner and Nikitenko (2020) study spherical random triangles and three-dimensional ellipsoids with homeoid distributions; their displayed acute-triangle result concerns the round sphere. Helman, Garcia and Reznik (2020) study deterministic loci of centers of ellipse-inscribed triangles. Neither examined statement gives the present two-dimensional affine-uniform acuteness law. A 2024–2025 public discussion of ellipse triangle acuteness instead uses **arclength-uniform sampling** and gives an integral, not the present pushforward-law formula.

## Limitations

The result does not address arclength-uniform sampling, area-uniform interior sampling, arbitrary convex curves, or higher-dimensional simplex acuteness. Numerical verification is not independent certification. The identical dilogarithm profile in the prior circle-containment problem is a substantial historical-priority and potential reduction risk; the novelty claim is solely the distinct ellipse model and its separately proved ordering and asymptotics, not the special function itself.

## References

1. 2018 public calculation of the probability that a random unit-circle triangle contains an off-center point, https://math.stackexchange.com/questions/2641793/probability-that-a-random-triangle-with-vertices-on-a-circle-contains-an-arbitra .
2. A. Akopyan, H. Edelsbrunner, A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere* (first posted 2020-07-15), https://arxiv.org/abs/2007.07783 .
3. M. Helman, R. Garcia, D. Reznik, *Intriguing Invariants of Centers of Ellipse-Inscribed Triangles* (first posted 2020-10-19), https://arxiv.org/abs/2010.09408 .
4. A. Ismailov, *With what probability does an inscribed triangle contain a given point?* (first posted 2026-01-06), https://arxiv.org/abs/2601.02929 .
5. *Probability that Triangle on Ellipse is Acute*, question from 2024-12-22 and integral response 2025-01-24 (different sampling convention), https://math.stackexchange.com/questions/5014676/probability-that-triangle-on-ellipse-is-acute .
