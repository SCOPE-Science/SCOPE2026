# Three unlabeled width statistics reconstruct a parallelogram with sharp stability

## Finding
Let \(K\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram. For a Haar-uniform unoriented line direction \(U\), write \(W_K(U)\) for the length of the orthogonal projection of \(K\) onto that line and set
\[
\mu=\mathbb E W_K,\qquad \nu=\mathbb E W_K^2,\qquad D=\max_U W_K(U).
\]
**The triple \((\mu,\nu,D)\) determines \(K\) up to Euclidean congruence.** Its reconstruction is a one-dimensional strictly monotone inversion followed by a quadratic equation. If \(s=\pi\mu/2\), then the dimensionless ratio
\[
T=\frac{s^2/2-\nu}{s^2-D^2}
\]
satisfies the sharp inequality
\[
\frac12-\frac1\pi\le T<\frac12.
\]
Equality at the lower endpoint holds precisely for rectangles; the upper endpoint is approached by flattening nondegenerate parallelograms.

Moreover, on every class with both side lengths in \([\delta,M]\) and its acute side-line angle in \([\delta,\pi/2]\), where \(0<\delta<M\) and \(\delta<\pi/2\), the inverse map from this triple to the sorted side lengths and angle is uniformly Hölder continuous with exponent \(1/2\). No larger uniform exponent is possible on a class containing a neighborhood of an equal-sided parallelogram. Away from equal side lengths the inverse is locally Lipschitz.

## Assumptions and scope
Write a translated parallelogram as
\[
K=\{tv+rw:\ -1/2\le t,r\le1/2\}.
\]
Choose the signs of the nonzero edge vectors so \(v\cdot w\ge0\), and put \(a=\|v\|>0\), \(b=\|w\|>0\), and \(\phi=\arccos((v\cdot w)/(ab))\in(0,\pi/2]\). The angle is that between the two **unoriented edge lines**; it need not equal the angle inside a specified corner of \(K\). Side-vector reversal changes only the chosen generating coordinates, not the parallelogram up to translation. An ordinary congruence class corresponds exactly to \(\{a,b\}\) and \(\phi\). Degenerate segments (\(\phi=0\) or either side length zero) are excluded. \(D\) is the diameter of \(K\), equivalently the upper endpoint of the width distribution. No direction labels are supplied.

## Proof
For \(u_\theta=(\cos\theta,\sin\theta)\), rotate coordinates to write \(v=a(1,0)\) and \(w=b(\cos\phi,\sin\phi)\). The support-function identity for a Minkowski sum of segments gives
\[
W_K(u_\theta)=a|\cos\theta|+b|\cos(\theta-\phi)|.
\]
Direct integration on the intervals cut out by the zeros of the two cosines gives
\[
\mathbb E|\cos\theta|=\frac2\pi,\quad
\mathbb E\cos^2\theta=\frac12,\quad
\mathbb E\bigl(|\cos\theta\cos(\theta-\phi)|\bigr)
=\frac{\sin\phi+(\pi/2-\phi)\cos\phi}{\pi}.
\]
Consequently,
\[
\mu=\frac{2(a+b)}{\pi},\qquad
\nu=\frac{a^2+b^2}{2}+\frac{2ab}{\pi}\left[\sin\phi+(\pi/2-\phi)\cos\phi\right].
\]
For real \(x,y\), \(|x|+|y|=\max(|x+y|,|x-y|)\). Maximizing over unit vectors therefore yields
\[
D=\max\{\|v+w\|,\|v-w\|\}=\sqrt{a^2+b^2+2ab\cos\phi}.
\]
Set \(s=\pi\mu/2=a+b\) and \(p=ab\). Substitution and cancellation show that
\[
X=s^2-D^2=2p(1-\cos\phi)>0,
\]
\[
Y=s^2/2-\nu=p\left[1-\cos\phi-\frac2\pi(\sin\phi-\phi\cos\phi)\right],
\]
so
\[
T=\frac YX=\frac12-\frac1\pi F(\phi),\qquad
F(\phi)=\frac{\sin\phi-\phi\cos\phi}{1-\cos\phi}.
\]
The critical derivative is exact:
\[
F'(\phi)=\frac{\sin\phi\,(\phi-\sin\phi)}{(1-\cos\phi)^2}>0
\quad(0<\phi\le\pi/2).
\]
Moreover \(F(0+)=0\) and \(F(\pi/2)=1\). Hence \(T\) identifies exactly one \(\phi\), and the claimed sharp bounds on \(T\) follow. The remaining parameters are recovered uniquely from
\[
p=\frac{s^2-D^2}{2(1-\cos\phi)},\qquad
\{a,b\}=\left\{\frac{s+\sqrt{s^2-4p}}2,\frac{s-\sqrt{s^2-4p}}2\right\}.
\]
The root discriminant is nonnegative because the data arise from a parallelogram. These identities include equal-sided parallelograms and rectangles without exceptional branches.

For stability, fix a stated compact nondegenerate class. The factors \(X\), \(1-\cos\phi\), and \(F'(\phi)\) then have positive lower bounds, while every variable has a finite upper bound. The formulas for \(T\), \(\phi\), and \(p\) are thus uniformly Lipschitz functions of the triple \((\mu,\nu,D)\), by elementary calculus and the inverse-function theorem on the compact interval. The sorted side lengths use only the additional operation \(z\mapsto\sqrt z\) on \(z=s^2-4p\ge0\), and \(|\sqrt z-\sqrt{z'}|\le\sqrt{|z-z'|}\). Thus for two inputs in the class,
\[
|\phi-\phi'|+\min_{\sigma\in S_2}\max_{i=1,2}|a_i-a'_{\sigma(i)}|
\le C_{\delta,M}\left(\max\{|\mu-\mu'|,|\nu-\nu'|,|D-D'|\}\right)^{1/2}.
\]
For differences larger than one, enlarge the constant using compactness. The square root becomes smooth if \(a\ne b\), proving local Lipschitz continuity there. Finally, fix \(\phi_0\in(0,\pi/2)\) and compare \((a,b)=(1,1)\) to \((1+t,1-t)\), with \(t>0\) tending to zero. All three statistics change by \(O(t^2)\) while the sorted side lengths change by \(t\). Hence no exponent greater than \(1/2\) can hold uniformly in a neighborhood containing this equal-sided point.

## Verification
Run `python3 verify.py` from the extracted package. The deterministic checker independently approximates the first two isotropic moments by directional quadrature for five parameter sets, tests the analytic diameter, reconstructs 2,000 seeded random nondegenerate parallelograms, checks discrete monotonicity, and checks the equal-side second-order obstruction. Its expected success marker is `VERIFY_OK 7019`. The proof above, not the finite tests, establishes all quantified claims.

## Relationship to prior work
Kim, Yaskin, and Zvavitch (first public preprint December 22, 2015) study distributions of projection measurements without direction labels. In their two-dimensional analysis they exhibit pairs of different convex bodies with the same projection-length distribution, and prove special positive comparisons; these do not give the present finite-statistic determination for the class of all parallelograms. Finch (first public preprint October 4, 2011) calculates first and second width moments for a square and several regular polytopes. That square computation is a special case of the displayed moment formulas, not the inverse determination for nonorthogonal parallelograms or the sharp inverse-stability exponent. Martirosyan (2023) derives orientation-dependent *chord-length* distributions and covariograms for quadrilaterals, which are not the present direction-unlabeled projection-width measurements. Standard width/perimeter and parallelogram diagonal identities supply background ingredients; neither alone implies the strict scalar inversion. These are comparisons of the mathematical implications of inspected primary results, not claims of exhaustive historical novelty.

## Limitations
The invariants are exact population statistics rather than estimates from a finite directional sample. The reconstruction is not uniformly stable as a parallelogram approaches a line segment; this is why the stability class bounds the angle and both lengths away from zero. The statement covers parallelograms only, not general centrally symmetric quadrilaterals or arbitrary convex bodies. Earlier equivalent reconstruction criteria formulated without width-distribution language may exist, and no independent mathematical audit has been performed.

## References
1. J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, December 22, 2015. https://arxiv.org/abs/1512.07289 (particularly Section 3, pp. 5–9).
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public October 4, 2011 (particularly Sections 1–2). https://arxiv.org/abs/1110.0671
3. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416–430. https://doi.org/10.3103/S1068362323060055 (particularly Sections 3–4).
