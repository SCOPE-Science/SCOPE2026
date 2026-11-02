# Exact Pareto conditioning for random-periodic tent-spline Gabor frames

## Finding

For the centered triangular B-spline \(b(t)=(1-|t|)_+\), an integer \(m\ge2\), and arbitrary phases \(x_1,\ldots,x_m\in\mathbb T=\mathbb R/\mathbb Z\), consider the indexed Gabor system
\[
\mathcal G_x=\{e^{2\pi i k t}b(t-n-x_j):n,k\in\mathbb Z,\ 1\le j\le m\}\subset L^2(\mathbb R).
\]
Its **optimal** upper and lower frame bounds are
\[
\boxed{B_x=m,\qquad A_x=4\min_{y\in\mathbb T}\sum_{j=1}^m d_{\mathbb T}(y,x_j)^2,}
\]
where \(d_{\mathbb T}\) is shorter-arc distance in the unit-circumference circle. In particular, \(\mathcal G_x\) is a frame if and only if the \(m\) phases are not all identical modulo one.

If \(X_1,\ldots,X_m\) are independent uniform points of \(\mathbb T\), then for **every** \(0<a<1/4\) (not only asymptotically),
\[
\boxed{\mathbb P(A_X<a)=\frac{\sqrt m\,\pi^{(m-1)/2}}{2^{m-1}\Gamma((m+1)/2)}\,a^{(m-1)/2}.}
\]
Consequently, the optimal condition number \(\kappa_m=B_X/A_X\) has the exact upper tail
\[
\boxed{\mathbb P(\kappa_m>K)=\frac{m^{m/2}\pi^{(m-1)/2}}{2^{m-1}\Gamma((m+1)/2)}K^{-(m-1)/2}\quad(K>4m).}
\]
For each fixed \(p>0\),
\[
\boxed{\mathbb E[\kappa_m^p]<\infty\quad\Longleftrightarrow\quad p<(m-1)/2.}
\]
Thus two or three random translation classes give a frame almost surely but have **infinite mean optimal condition number**; four translation classes are the first with finite mean. For \(m=2\), the full tail is \(\mathbb P(\kappa_2>K)=2K^{-1/2}\) for \(K\ge4\).

## Assumptions and scope

The integer frequency step is exactly one, as is the period of the translated classes. The triangular window has height one and support \([-1,1]\) (no \(L^2\)-normalization). All indexed translates count in the frame sums, even if deterministic offsets coincide. The random offsets are independent Haar-uniform modulo one; \(m\ge2\) is a fixed integer. Distances \(d_{\mathbb T}\) take values in \([0,1/2]\). The upper/lower bounds are the optimal bounds in the squared-norm frame inequalities on \(L^2(\mathbb R)\). Statements about finite moments concern \(p>0\) only. No assertion is made for noninteger modulation spacing, other splines, or nonuniform sampling laws.

## Proof

**1. Exact Zak multiplier.** Use the unitary Zak transform with
\[
(Zf)(t,\xi)=\sum_{n\in\mathbb Z} f(t+n)e^{2\pi i n\xi},\qquad (t,\xi)\in[0,1)^2.
\]
The identity \(Z(M_kT_nf)=e^{2\pi i(kt+n\xi)}Zf\) for integers \(n,k\), followed by Parseval for the torus exponentials, makes the frame operator unitarily equivalent to multiplication by
\[
S_x(t,\xi)=\sum_{j=1}^m |Zb(t-x_j,\xi)|^2.
\]
Write \(v_j=\{t-x_j\}\in[0,1)\). Writing \(t-x_j=\ell_j+v_j\), with \(\ell_j\in\mathbb Z\), the Zak series for the hat window is exactly \(e^{-2\pi i\ell_j\xi}[(1-v_j)+v_j e^{-2\pi i\xi}]\), since exactly two translates meet each open unit cell. Hence
\[
S_x(t,\xi)=\sum_{j=1}^m\bigl[1-2v_j(1-v_j)(1-\cos(2\pi\xi))\bigr].
\]
Every coefficient \(v_j(1-v_j)\) is nonnegative. Thus **the same frequency** \(\xi=1/2\) simultaneously minimizes every summand, and \(\xi=0\) simultaneously maximizes them. The maximum is exactly \(m\). At the minimum, \((1-2v_j)^2=4d_{\mathbb T}(t,x_j+1/2)^2\); translating \(t\) by half a period yields the asserted \(A_x\). Continuity of the periodic sum, despite the individual Zak quasi-periodicity, makes these essential extrema actual extrema. A sum of nonnegative squared distances vanishes exactly when all \(x_j\) are one circle point. This proves the sharp constants and deterministic frame criterion.

**2. A genuine small-ball identity.** Condition on \(X_1\) and rotate so it is zero. The relative offsets \(Y_j=(X_j-X_1)\bmod1\), for \(2\le j\le m\), are independent uniform points of \((-1/2,1/2]\). Put \(Y_1=0\), \(d=m-1\), and
\[
Q(Y)=\min_{s\in\mathbb R}\sum_{j=1}^m(s-Y_j)^2
=\sum_{j=1}^m(Y_j-\overline Y)^2
=Y^\top\left(I_d-\frac{\mathbf 1\mathbf 1^\top}{m}\right)Y.
\]
Here \(Y\) on the right is the column of the last \(d\) coordinates. Fix \(0<a<1/4\). If \(A_X<a\), let \(s\) minimize its circular squared-distance functional. Each \(d_{\mathbb T}(s,X_j)<\sqrt a/2\). Therefore all \(X_j\) have uniquely chosen lifts in the real arc of length \(\sqrt a<1/2\) centered at \(s\). Translate those lifts by an integer so the lift of \(X_1\) is zero; the other lifts then coincide with the canonical \(Y_j\), because they are all within \(\sqrt a<1/2\) of the first lift. In a neighborhood of \(s\) the circular objective is the ordinary quadratic function of these lifts. Its minimizing derivative vanishes, so \(s=\overline Y\) modulo the common integer and \(A_X=4Q(Y)<a\).

Conversely, if \(Q(Y)<a/4\), choose \(s=\overline Y\). Since circle distances never exceed differences between any real lifts, \(A_X\le4Q(Y)<a\). Thus, **exactly on this entire interval**, the events \(\{A_X<a\}\) and \(\{Q(Y)<a/4\}\) agree. No limiting approximation has been used.

**3. Exact ellipsoid volume.** The quadratic-form matrix \(H=I_d-m^{-1}\mathbf 1\mathbf 1^\top\) has eigenvalues \(1\) with multiplicity \(d-1\) and \(1/m\) once. Therefore \(\det H=1/m\). The ellipsoid \(\{Q(Y)<a/4\}\) is entirely contained in the uniform cube: writing each \(Y_j=(Y_j-\overline Y)-(Y_1-\overline Y)\) and applying Cauchy--Schwarz gives \(|Y_j|^2\le2Q(Y)<a/2<1/8\). Its uniform probability is consequently its untruncated Euclidean volume,
\[
\frac{\operatorname{vol}(B_d)}{\sqrt{\det H}}\left(\frac a4\right)^{d/2}
=\sqrt m\,\frac{\pi^{d/2}}{\Gamma(d/2+1)}\frac{a^{d/2}}{2^d},
\]
which is the displayed exact formula.

**4. Pareto law and moments.** Almost surely the offsets are not all equal, so \(A_X>0\) and \(\kappa_m=m/A_X\). Set \(a=m/K\) in the preceding equality for \(K>4m\). This proves the exact Pareto tail and its constant. The layer-cake identity \(\mathbb E\kappa_m^p=p\int_0^\infty t^{p-1}\mathbb P(\kappa_m>t)\,dt\) shows finiteness exactly when \(p<(m-1)/2\), including logarithmic divergence at equality. Finally, for \(m=2\), write \(\delta=d_{\mathbb T}(X_1,X_2)\). The minimizing center lies midway along their shorter arc, giving \(A_X=2\delta^2\); \(\delta\) is uniform on \([0,1/2]\) with density two. Hence \(\kappa_2=\delta^{-2}\ge4\) and the asserted full tail follows.

## Verification

The optional standalone file `CHECK.py` implements the exact piecewise-quadratic circular minimization on rational phase tuples, checks the closed formula for two shifts, and compares deterministic grid samples of the Zak multiplier with the exact bounds. Running `python CHECK.py` requires only the Python standard library. Its finite checks are supplementary; the all-parameter and probability statements follow from the four analytical steps above.

## Relationship to prior work

Raj and Sivananthan (arXiv:2503.20259, first public 2025-03-26) study precisely random-periodic time-frequency sets, derive the Zak multiplier criterion (their Lemma 3.1), and give high-probability sufficient estimates for large numbers of shifts (Theorem 3.2), mentioning B-splines in the examples. Their theorem does not identify optimal deterministic frame bounds or any exact conditioning distribution. The present result uses the same setting for the particular centered tent window but extracts a sharp circular-variance identity and an exact finite-\(m\) lower tail.

Buck, Frederick, Okoudjou and Stangl (arXiv:2603.16986, first public 2026-03-17) analyze Gram matrices and finite-section spectral properties for B-spline Gabor systems on rectangular lattices. Those single-lattice statements are different from a union of randomly offset integer translation lattices and do not give the asserted Pareto law. Work on lattice frame bounds and on the Zak zeros of B-splines supplies background, not an implication of the exact random-multicoset tail.

## Limitations

The sharp small-bound law is proved **exactly** for \(0<a<1/4\), and the resulting condition-number tail exactly for \(K>4m\). No closed form for the full distribution at intermediate condition numbers is asserted when \(m\ge3\). For \(m=2\) a separate full-tail formula is supplied. Only the triangular spline, unit-frequency modulation, independent uniform shift phases, and fixed integer \(m\ge2\) are covered. Published historical works not available in full may contain equivalent statements; lack of a matching search result is not a proof of novelty.

## References

1. S. Raj and S. Sivananthan, *Gabor frames generated by Random-Periodic time-frequency shifts*, arXiv:2503.20259v1 (2025-03-26), https://arxiv.org/html/2503.20259v1. Relevant material: Sections 2.2, 3 (Zak multiplier and high-probability sufficient frame bounds), 4 (B-splines).
2. M. Buck, C. Frederick, K. A. Okoudjou, and A. Stangl, *On the structure of the Gram matrix for Gabor systems generated by B-splines*, arXiv:2603.16986v1 (2026-03-17), https://arxiv.org/html/2603.16986v1. Relevant material: Sections 3--5 (lattice Gram blocks, finite-section spectra).
3. O. Christensen, H. O. Kim, R. Y. Kim, *On Gabor frame sets for compactly supported continuous functions*, Journal of Inequalities and Applications (2016), https://link.springer.com/article/10.1186/s13660-016-1021-4. Context: rectangular-lattice B-spline frame sets.
