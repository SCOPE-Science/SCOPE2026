# Quartic orientation-reversal cusp for random shortest-geodesic triangles on thin flat Klein bottles

## Finding
Let \(K_{a,b}\) be the flat Klein bottle obtained from \(\mathbb R^2\) by identifying under the two isometries
\[
 A(x,y)=(x+a,-y),\qquad B(x,y)=(x,y+b),\qquad a\ge b>0.
\]
Choose three points independently according to normalized Riemannian area measure. Join the points cyclically by shortest geodesics, unique almost surely. Define \(p(a,b)\) to be the probability that the resulting closed curve is *orientation reversing*, meaning that its deck transformation reverses orientation. For every \(a\ge b>0\),
\[
 \boxed{\left|p(a,b)-\frac14-\frac1{120}\left(\frac ba\right)^4\right|\le\frac7{64}\left(\frac ba\right)^6.}
\]
Consequently the first nonconstant term in the thin-bottle limit is quartic, not quadratic:
\[
 p(a,b)=\frac14+\frac1{120}\left(\frac ba\right)^4+O\!\left((b/a)^6\right),\qquad a/b\longrightarrow\infty.
\]
The explicit inequality also proves \(p(a,b)>1/4\) whenever \(a/b>\sqrt{105/8}\). The latter threshold is sufficient and is not claimed sharp.

## Assumptions and scope
Use the half-open fundamental domain \(0\le x<a\), \(-b/2\le y<b/2\); its area is \(ab\). All three sampled points are independent. A shortest geodesic between each pair is unique except on the cut locus, a null set. The product of deck transformations of a lifted closed polygon determines an orientation character in \(\{+1,-1\}\), independent of the chosen lifts. The event considered here is a topological property of the piecewise-geodesic *loop*, not the area enclosed by a simple triangle; self-intersections are permitted. The bound is asserted only for \(a\ge b\), while the asymptotic is for \(b/a\to0\).

## Proof
**1. Exact geodesic parity reduction.** Define \(d_b(t)=\min_{k\in\mathbb Z}|t-kb|\). For two representatives \((x_i,y_i),(x_j,y_j)\) in the fundamental domain, the shortest squared length among orientation-preserving deck images is
\[
 \ell_{ij,+}^2=|x_i-x_j|^2+d_b(y_i-y_j)^2,
\]
and among orientation-reversing deck images is
\[
 \ell_{ij,-}^2=(a-|x_i-x_j|)^2+d_b(y_i+y_j)^2.
\]
Indeed every deck element is of the form \(A^kB^m\); even powers of \(A\) have horizontal displacement in \(2a\mathbb Z\), odd powers in \(a+2a\mathbb Z\), and the sign flip changes the vertical difference to a sum, modulo \(b\). Since \(|x_i-x_j|<a\), the indicated even and odd horizontal images are closest in their classes.

Put \(X_i=x_i/a\), \(z_{ij}=d_b(y_i+y_j)^2-d_b(y_i-y_j)^2\), and \(u_{ij}=z_{ij}/(2a^2)\). Each \(X_i\) is uniform on \([0,1]\), independent of the vertical coordinates, and \(|u_{ij}|\le\delta\), where \(\delta=b^2/(8a^2)\le1/8\). The \(ij\)-edge reverses orientation precisely if
\[
 B_{ij}=\mathbf1\{|X_i-X_j|>1/2+u_{ij}\}=1.
\]
The orientation character of the closed three-edge loop is the product of those of its edges; hence the loop reverses orientation exactly when \(B_{12}+B_{13}+B_{23}\) is odd.

**2. A uniform cubic conditional estimate.** Condition on the three \(y\)-coordinates; write \(h_i=1/2+u_i\) for the three edge thresholds. For two distinct edges (which share one endpoint), direct integration over their shared coordinate gives
\[
 I(h,k)=\Pr(|X_1-X_2|>h,|X_1-X_3|>k)
 =2\left[\frac{(1-m)^3}{3}+\frac{(m-\ell)(1-m)^2}{2}\right]+\frac{(1-h-k)_+^3}{3},
\]
where \(m=\max(h,k)\), \(\ell=\min(h,k)\), and \(t_+=\max(t,0)\). Setting \(h=1/2+u\), \(k=1/2+v\), the exact expansion is
\[
 I=\frac1{12}-\frac{u+v}{4}+uv+R(u,v),\qquad
 R(u,v)=\frac{M^3}{3}-M^2L+\frac{(-u-v)_+^3}{3},
\]
with \(M=\max(u,v)\), \(L=\min(u,v)\). Thus \(|R(u,v)|\le4\delta^3\).

The probability that all three edge thresholds are exceeded is
\[
 T=\frac13\sum_{1\le i<j\le3}(1-h_i-h_j)_+^3\le8\delta^3.
\]
To derive this formula, sort the three \(X\)-coordinates. In each of the six orders, the two adjacent distances must exceed their thresholds, and their sum then automatically exceeds the third threshold because \(2(1/2-\delta)>1/2+\delta\) for \(\delta\le1/8\). The resulting integral over the two positive gaps is a cubic simplex volume.

Finally use the exact Boolean identity for odd parity,
\[
 \mathbf1_{\mathrm{odd}}=\sum_iB_i-2\sum_{i<j}B_iB_j+4B_1B_2B_3.
\]
Since \(\Pr(B_i=1)=(1-h_i)^2\), the preceding formulas imply, uniformly for \(|u_i|\le\delta\),
\[
 \Pr(\mathrm{odd}\mid y_1,y_2,y_3)
 =\frac14+2\sum_i u_i^2-\left(\sum_i u_i\right)^2+E,
 \qquad |E|\le 56\delta^3.
\]
Here the three pair remainders contribute at most \(24\delta^3\) and the triple term at most \(32\delta^3\).

**3. Fourier evaluation and cancellation.** The continuous periodic squared-distance function has the absolutely convergent Fourier expansion
\[
 d_b(t)^2=\frac{b^2}{12}+\frac{b^2}{\pi^2}\sum_{n\ge1}\frac{(-1)^n}{n^2}\cos\left(\frac{2\pi n t}{b}\right).
\]
Consequently,
\[
 z_{ij}=-\frac{2b^2}{\pi^2}\sum_{n\ge1}\frac{(-1)^n}{n^2}
 \sin\left(\frac{2\pi n y_i}{b}\right)
 \sin\left(\frac{2\pi n y_j}{b}\right).
\]
Independent uniform vertical coordinates and trigonometric orthogonality give
\[
 \mathbb Ez_{ij}=0,\qquad \mathbb Ez_{ij}^2=\frac{b^4}{\pi^4}\sum_{n\ge1}\frac1{n^4}=\frac{b^4}{90},
 \qquad \mathbb E(z_{ij}z_{jk})=0\quad(i\ne k).
\]
The cross moment vanishes because a vertex appearing in only one sine factor has zero average. Therefore
\[
 \mathbb E\left[2\sum_i u_i^2-\left(\sum_i u_i\right)^2\right]
 =\sum_i\mathbb Eu_i^2=\frac{3}{4a^4}\frac{b^4}{90}=\frac{b^4}{120a^4}.
\]
Taking expectations in the conditional estimate gives the claimed bound, since \(56\delta^3=7(b/a)^6/64\). The positive-correction condition follows by comparing the explicit quartic term with this remainder.

## Verification
An accompanying standalone Python program evaluates the exact conditional pair and triple integrals, checks the Fourier-moment coefficients and remainder arithmetic, and independently simulates the three lifted shortest-geodesic parity decisions for four aspect ratios. The script may be run with `python3 klein_triangle_checker.py` and requires `numpy`. Its successful final line is `ALL_CHECKS_PASSED`. The analytic calculations above prove the universal bound; Monte Carlo sampling is corroboration only.

## Relationship to prior work
Davis and Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles* (arXiv:1912.07411, first posted 2019-12-16), study shortest-geodesic selection, cut loci, and motion-planning complexity on Klein-bottle-type quotients, but not orientation characters of random closed three-edge geodesics or their aspect-ratio asymptotics. Glorieux and Yarmola, *Random triangles on flat tori* (arXiv:2003.08190, first posted 2020-03-18), investigate homotopy probabilities for random shortest-geodesic triangles on orientable flat tori. Their rectangular-torus results do not imply the orientation-reversing event here: a torus has no orientation-reversing loops. The standard periodic squared-distance Fourier series and elementary order-statistic integrals are classical ingredients, not claimed as new. The specific quartic cancellation and explicit uniform error for the flat Klein-bottle orientation character were not found in the inspected sources. Historical priority remains provisional.

## Limitations
The result is a sharp *leading asymptotic coefficient*, not an exact formula for \(p(a,b)\) at finite aspect ratio. The explicit sixth-order remainder is rigorous but not claimed optimal. The sufficient threshold \(\sqrt{105/8}\) for positivity is not claimed sharp. No assertion is made about shorter than unit aspect ratios, nonflat Klein-bottle metrics, other geodesic choices on null cut-locus sets, or polygons with more than three vertices. Full historical priority cannot be certified by limited source inspection, and independent mathematical audit has not been performed.

## References
1. D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411 (public preprint 2019-12-16), https://arxiv.org/abs/1912.07411.
2. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190 (public preprint 2020-03-18), https://arxiv.org/abs/2003.08190.
