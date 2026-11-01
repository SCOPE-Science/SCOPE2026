# Unlabeled projection-width laws determine every isosceles trapezoid

## Finding
For every nondegenerate Euclidean isosceles trapezoid, the probability law of its one-dimensional orthogonal projection length under a uniformly chosen unoriented direction determines the trapezoid up to Euclidean congruence. This holds for every positive pair of base lengths, including rectangles and every transition between monotone and nonmonotone angular width profiles. An explicit radical density and a complete inverse algorithm are given below.

## Assumptions and scope
Let \(A>B>0\), \(H>0\), and let \(T\) have vertices \((-A,0),(A,0),(-B,H),(B,H)\). The longer and shorter bases have lengths \(2A\) and \(2B\), and \(H\) is the altitude. A line direction is uniform modulo \(\pi\); its projection width is the distance between the two extremal scalar products of the vertices. A rectangle, \(A=B>0\), is treated separately. The inverse uses the exact population law, not finitely many sampled widths.

Put
\[
 c=A-B,\quad s=A+B,\quad \ell=\sqrt{c^2+H^2},\quad
 \alpha=\arctan(c/H),\quad \beta=\arctan(H/s),
\]
\[
 Q=\sqrt{s^2+H^2},\qquad z=\frac{2AH}{\ell}.
\]
For a real interval \((u,v)\), write \(\mathbf 1_{(u,v)}(w)=1\) when \(u<w<v\), zero otherwise. All statements about densities concern almost-everywhere representatives away from the finitely many critical values.

**Exact density.** For \(A>B>0\), the width \(W\) has density
\[
 f(w)=\frac{2}{\pi}\left[
 \frac{\mathbf 1_{(z,2A)}(w)}{\sqrt{4A^2-w^2}}+
 \begin{cases}
  \displaystyle\frac{\mathbf 1_{(H,z)}(w)}{\sqrt{Q^2-w^2}},&\beta\le\alpha,\\[6pt]
  \displaystyle\frac{\mathbf 1_{(z,Q)}(w)+\mathbf 1_{(H,Q)}(w)}{\sqrt{Q^2-w^2}},&\beta>\alpha.
 \end{cases}
 \right].
\]
The formula is valid also at \(\beta=\alpha\), with coincident upper endpoint \(z=Q\). All indicator fractions are understood to be zero outside their indicated intervals.

**Explicit recovery.** A *square-root pole* at \(q>0\) means a left-hand singularity whose normalized coefficient is \(\lim_{w\uparrow q}\sqrt{q^2-w^2}\,f(w)>0\). For a proper trapezoid the poles and coefficients are exactly:

- If \(\beta<\alpha\): one pole, at \(2A\), coefficient \(2/\pi\).
- If \(\beta=\alpha\): two poles, at \(Q=z<2A\) and \(2A\), both coefficient \(2/\pi\).
- If \(\beta>\alpha\) and \(Q\ne2A\): two poles, at \(2A\) with coefficient \(2/\pi\) and \(Q\) with coefficient \(4/\pi\).
- If \(\beta>\alpha\) and \(Q=2A\): one pole at \(2A=Q\) with coefficient \(6/\pi\).

These patterns recover \(A\) and determine whether \(\beta>\alpha\). Let \(m\) be the left endpoint of the width support. If \(\beta\le\alpha\), then \(H=m\). The mean width determines \(P=\pi\mathbb E W/2=s+\ell>2A\), and
\[
 B=\frac{P^2-2AP-H^2}{2(P-2A)}.
\]
If \(\beta>\alpha\) and \(Q\le2A\), then again \(H=m\); if \(\beta>\alpha\) and \(Q>2A\), the finite right limit \(D=\pi f(m+)/2\) takes exactly one of the following three *distinct* values:
\[
D=\begin{cases}
 (Q^2-m^2)^{-1/2},&H=m<z,\\[2pt]
 (4A^2-m^2)^{-1/2}+(Q^2-m^2)^{-1/2},&z=m<H,\\[2pt]
 (4A^2-m^2)^{-1/2}+2(Q^2-m^2)^{-1/2},&H=z=m.
\end{cases}
\]
In the first or third cases \(H=m\). In the second case, form, for almost every \(w\),
\[
 g(w)=\frac\pi2 f(w)-\frac{\mathbf 1_{(m,2A)}(w)}{\sqrt{4A^2-w^2}}-\frac{\mathbf 1_{(m,Q)}(w)}{\sqrt{Q^2-w^2}}.
\]
Then \(g(w)=\mathbf 1_{(H,Q)}(w)/\sqrt{Q^2-w^2}\), so \(H\) is the lower endpoint of the support of \(g\), even when \(H=2A\). Once \(H\) is known in any \(\beta>\alpha\) case, recover
\[
 B=\sqrt{Q^2-H^2}-A.
\]
Thus every proper isosceles trapezoid is uniquely reconstructed from its width law.

For the rectangular case \(A=B\), the law has only one square-root pole, at \(Q=\sqrt{(2A)^2+H^2}\), with coefficient \(4/\pi\). Its support minimum is \(m=\min(2A,H)\); consequently the unordered side lengths are \(m\) and \(\sqrt{Q^2-m^2}\). Its pole signature distinguishes every rectangle from every proper trapezoid.

## Proof
**1. Reduction to a quarter-turn.** Width is unchanged by reversal of direction and by reflection across the trapezoid's symmetry axis. Therefore \(\theta\) may be taken uniform on \([0,\pi/2]\), with density \(2/\pi\). Taking maxima and minima of the four vertex projections directly gives
\[
 W(\theta)=\begin{cases}2A\cos\theta,&0\le\theta\le\alpha,\\
 s\cos\theta+H\sin\theta=Q\cos(\theta-\beta),&\alpha\le\theta\le\pi/2.
 \end{cases}
\]
The branches agree at \(\alpha\), with common value \(z\). The first branch is strictly decreasing. The second has an interior maximum \(Q\) exactly when \(\beta>\alpha\), equivalently \(H^2>cs\).

**2. Exact pushforward.** On each strictly monotone branch, \(|dW/d\theta|=\sqrt{M^2-W^2}\), with \(M=2A\) for the first branch and \(M=Q\) for the second. If \(\beta\le\alpha\), the second branch decreases from \(z\) to \(H\). If \(\beta>\alpha\), it rises from \(z\) to \(Q\) and then falls from \(Q\) to \(H\). Summing inverse derivatives with angular density \(2/\pi\) yields the displayed density, including both boundary configurations. This pushforward is normalized because the corresponding monotonic angular intervals partition \([0,\pi/2]\).

**3. Exhaustive pole classification.** The first branch always supplies a pole at \(2A\) with coefficient \(2/\pi\) when \(A>B\); \(z<2A\) because \(H<\ell\). The second branch supplies no pole when \(\beta<\alpha\), supplies one endpoint pole at \(Q=z\) with coefficient \(2/\pi\) when \(\beta=\alpha\), and supplies two preimages near the interior maximum \(Q\), giving coefficient \(4/\pi\), when \(\beta>\alpha\). The latter pole merges with the first when \(Q=2A\), adding their coefficients to \(6/\pi\). There can be no other square-root poles because all other branch endpoints have nonzero derivatives. At \(\beta=\alpha\), \(Q=z<2A\), so the larger of the two equal-coefficient poles identifies \(2A\). These cases recover \(A\) without ambiguity.

**4. Recovering height and smaller base.** Since the branch minima are \(z\) and \(H\), \(m=\min(z,H)\). If \(\beta\le\alpha\), then \(H^2\le cs\) gives \(\ell^2=H^2+c^2\le2Ac<4A^2\), hence \(H<z\) and \(m=H\). Cauchy's perimeter formula or direct integration of the two branches gives \(\mathbb E W=2(s+\ell)/\pi\). Squaring \(P-A-B=\sqrt{(A-B)^2+H^2}\) yields the stated formula for \(B\); its denominator is positive since \(P>2A\).

If \(\beta>\alpha\) and \(Q\le2A\), then \(H^2\le4A^2-s^2<4A^2-c^2\), so \(\ell<2A\) and \(H<z\). Thus \(m=H\). If \(\beta>\alpha\) and \(Q>2A\), reading off which of the three density indicators begins at \(m\) gives the three distinct displayed finite limits. In the sole case \(z=m<H\), subtraction of the known first and increasing-second branches leaves precisely the decreasing-second contribution \(g\), whose support begins at \(H\). Finally \(Q^2=s^2+H^2\) and \(s=A+B\) recover \(B\). This proves global injectivity and provides a finite procedure in every phase.

**5. Rectangles.** If \(A=B\), then \(\alpha=0\), and the only nonempty angular branch is \(W(\theta)=2A\cos\theta+H\sin\theta\). Its unique interior maximum is \(Q\) with two preimages and coefficient \(4/\pi\). Its minimum is the smaller of the two side lengths; Pythagoras yields the other length. The proper-trapezoid pole patterns exclude any cross-class collision.

## Verification
The standalone \(check.py\) uses only Python's standard library. It independently computes vertex-projection widths and an angular-preimage CDF, differentiates that CDF away from critical points, and compares it with the claimed density on a deterministic set of aspect ratios spanning the monotone, stationary-boundary, peak-merger, support-merger, and rectangular regimes. It also checks exact antiderivatives, normalization, the mean identity and both reconstruction formulas. Execute \(python3 check.py\); the successful output ends in `ALL_CHECKS_PASSED`. Finite checks corroborate but do not replace the proof above.

## Relationship to prior work
Akiyama and Kamae (2022, arXiv:2201.06736) derive a general representation of polygonal widths as sums of edge projections and study the mean, second moment, and width deviation, including local truncations of a regular triangle. Those forward results motivate the inverse question but do not establish full width-law injectivity for the entire isosceles-trapezoid class. Martirosyan (2023, DOI:10.3103/S1068362323060055) treats *orientation-dependent random chord lengths* and covariograms of quadrilaterals; these are different data from a width value observed after discarding the direction. Related published inverse-width results for triangles and parallelograms concern different geometric families; rectangles are acknowledged as a special known boundary case rather than claimed as a distinct advance.

## Limitations
The theorem is an exact-law identification statement for isosceles trapezoids, not arbitrary quadrilaterals. It does not provide finite-sample statistical error bounds or a uniform Lipschitz modulus across the transition surfaces. Its density's square-root poles can become difficult to observe from noisy finite samples when the shorter base approaches the longer base. Historical mathematical priority remains subject to independent literature review; a general forward formula does not by itself certify or refute novelty of this inverse result.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736, first posted 2022-01-18. https://arxiv.org/abs/2201.06736
2. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, J. Contemp. Math. Anal. 58 (2023), 416–430, DOI:10.3103/S1068362323060055. https://doi.org/10.3103/S1068362323060055
