# A cubic polar-area-sum deficit with smooth John-normalized witnesses

## Finding

Let \(B\) denote the Euclidean unit disk, \(K^\circ\) the polar of a convex body \(K\) containing the origin, and \(A(K)\) its area. The normalized polar-area-sum deficit is
\[
\mathcal D(K)=2\pi-A(K)-A(K^\circ).
\]
For every integer \(m\ge2\), and \(0\le t\le (m^2-1)^{-1}\), there exists a centrally symmetric planar convex body \(K_{m,t}\) with support function
\[
h_{m,t}(\theta)=1+t|\sin(m\theta)|.
\]
Its John ellipse is exactly \(B\), and \(d_H(K_{m,t},B)=t\). Its areas are **exactly**
\[
A(K_{m,t})=\pi+4t-\frac{\pi(m^2-1)}2t^2,\qquad
A(K_{m,t}^\circ)=\frac{\pi-2\arcsin t}{(1-t^2)^{3/2}}-\frac{2t}{1-t^2}.
\]
Consequently, as \(t\downarrow0\),
\[
\mathcal D(K_{m,t})=\frac{\pi(m^2-4)}2t^2+\frac{16}{3}t^3+O(t^4).
\]
The four-contact case \(m=2\) alone has a vanishing quadratic coefficient; in that case an exact positive integral expression holds:
\[
\mathcal D(K_{2,t})=\frac{t^3}{2}\int_0^{2\pi}
\frac{|\sin(2\theta)|^3(4+3t|\sin(2\theta)|)}{(1+t|\sin(2\theta)|)^2}\,d\theta.
\]
Moreover, for every sufficiently small \(t>0\), **a smooth, strictly convex, centrally symmetric** body \(\widetilde K_t\) exists with John ellipse \(B\), whose support function is
\[
\widetilde h_t(\theta)=1+t\bigl(\sqrt{\sin^2(2\theta)+t^8}-t^4\bigr),
\]
and which satisfies
\[
\lim_{t\downarrow0}\frac{\mathcal D(\widetilde K_t)}{d_H(\widetilde K_t,B)^3}=\frac{16}{3}.
\]
It follows that **no positive uniform quadratic Hausdorff-deficit lower bound** \(\mathcal D(K)\ge c\,d_H(K,B)^2\) is valid for all smooth, strictly convex, origin-symmetric planar bodies in John position, however close they are to \(B\). More generally, such a bound fails with any fixed exponent \(p<3\). No global cubic lower bound is asserted.

## Assumptions and scope

Everything is Euclidean, planar, centered at the origin. The integer \(m\) is at least two, \(t\) is real and nonnegative, and the stated range is nonempty. The regularity assertion for \(\widetilde K_t\) concerns each fixed \(0<t<1/4\); the limit is one-sided. The John ellipse means the unique maximal-area inscribed ellipse. The Hausdorff distance uses Euclidean distance without quotienting by linear maps: the affine normalization is fixed by John position. The supporting lines use outward unit normals \((\cos\theta,\sin\theta)\).

## Proof

**1. Existence and John position.** Let \(f_m(\theta)=|\sin(m\theta)|\). On each interval between its zeros, \(f_m''=-m^2f_m\). At each zero \(k\pi/m\), its first derivative jumps upward by \(2m\). Hence the distributional curvature-radius measure of \(h_{m,t}=1+tf_m\) equals the nonnegative density \(1-(m^2-1)t f_m\) plus atoms of mass \(2mt\) at these zeros. It is nonnegative whenever \(0\le t\le1/(m^2-1)\), so \(h_{m,t}\) is a convex support function. Its minimum is one, hence \(B\subset K_{m,t}\). The \(2m\) evenly spaced directions \(u_k=(\cos(k\pi/m),\sin(k\pi/m))\) are contact directions: \(h_{m,t}(u_k)=h_B(u_k)=1\). As \(\sum_{k=0}^{2m-1}u_k\otimes u_k=mI_2\) and the contacts are balanced, John's contact characterization, with weights \(1/m\), proves that \(B\) is the John ellipse. The support-function formula for Hausdorff distance gives \(d_H(K_{m,t},B)=t\).

**2. Exact areas.** The planar support-area identity, valid for Lipschitz support functions by smooth approximation, is
\[
A(K)=\frac12\int_0^{2\pi}\bigl(h^2-(h')^2\bigr)\,d\theta.
\]
Direct subdivision into \(2m\) equal angular intervals gives
\[
\int_0^{2\pi}f_m\,d\theta=4,\quad
\int_0^{2\pi}f_m^2\,d\theta=\pi,\quad
\int_0^{2\pi}(f_m')^2\,d\theta=m^2\pi.
\]
These establish the first area formula. The polar radial function is \(1/h_{m,t}\), so
\[
A(K_{m,t}^\circ)=\frac12\int_0^{2\pi}(1+t f_m)^{-2}\,d\theta
=\int_0^\pi(1+t\sin u)^{-2}\,du.
\]
For \(0\le t<1\), define \(J(t)=\int_0^\pi(1+t\sin u)^{-1}\,du=(\pi-2\arcsin t)/\sqrt{1-t^2}\), derived by the tangent-half-angle substitution. The last polar integral is \(J(t)+tJ'(t)\), giving the displayed closed form.

**3. Exact deficit and critical cubic order.** The elementary identity, for \(y\ge0\), is
\[
(1+y)^{-2}=1-2y+3y^2-\frac{y^3(4+3y)}{(1+y)^2}.
\]
Combining the support-area formula and the polar-area formula yields, for every \(m\ge2\),
\[
\mathcal D(K_{m,t})=\frac{\pi(m^2-4)}2t^2
+\frac{t^3}{2}\int_0^{2\pi}
\frac{f_m^3(4+3tf_m)}{(1+t f_m)^2}\,d\theta.
\]
In particular the deficit is positive for every \(t>0\). The exact third moment \(\int_0^{2\pi}f_m^3\,d\theta=8/3\) gives the asserted expansion with cubic coefficient \(16/3\), uniformly for each fixed \(m\). The quadratic coefficient vanishes exactly when \(m=2\).

**4. Smooth strictly convex cubic witnesses.** Set \(\delta=t^4\) and \(f_\delta(\theta)=\sqrt{\sin^2(2\theta)+\delta^2}-\delta\). This is nonnegative, smooth, periodic under quarter-turns, and zero at the four coordinate-axis normals. Writing \(s=\sin2\theta\), \(c=\cos2\theta\), \(H=\sqrt{s^2+\delta^2}\), an explicit derivative gives
\[
f_\delta''=\frac{4\delta^2c^2}{H^3}-\frac{4s^2}{H}\ge-4.
\]
Therefore \(1+t(f_\delta+f_\delta'')\ge1-4t>0\) for \(0<t<1/4\): the support describes a smooth strictly convex body. The same four axis contacts and John decomposition fix its John ellipse to \(B\). Let
\[
C_\delta=\frac12\int_0^{2\pi}\bigl((f_\delta')^2-4f_\delta^2\bigr)\,d\theta.
\]
On each quarter-turn interval, \(f_\delta\) vanishes at both endpoints; the sharp Dirichlet Poincaré inequality gives \(C_\delta\ge0\). Moreover \(f_\delta\to |\sin2\theta|\) in \(H^1(S^1)\) with derivative \(L^2\)-error \(O(\sqrt\delta)\): away from zeros the pointwise derivative difference is \(O(\delta^2/\sin^2 2\theta)\), while the union of regions where \(|\sin2\theta|\le\delta\) has length \(O(\delta)\). Thus \(C_\delta=O(\sqrt\delta)\). The same exact algebra as in Step 3 gives
\[
\mathcal D(\widetilde K_t)=t^2C_\delta+
\frac{t^3}{2}\int_0^{2\pi}\frac{f_\delta^3(4+3tf_\delta)}{(1+t f_\delta)^2}\,d\theta.
\]
With \(\delta=t^4\), the first term is \(O(t^4)\); the integral tends to \(4\cdot8/3\), giving \(\mathcal D(\widetilde K_t)=\frac{16}{3}t^3+O(t^4)\). Finally, \(d_H(\widetilde K_t,B)=t(\sqrt{1+t^8}-t^4)=t+O(t^5)\). These prove the cubic limit and the failure of any uniform lower bound with exponent below three.

## Verification

The standalone `verify_area_sum.py` uses independent circumscribed-polygon and polar-polygon shoelace computations, compares their areas with the displayed closed forms at multiple values of \(m\), \(t\), and resolution, and evaluates smoothed quadrature and limiting coefficients. It ran successfully with 68 assertions/checks under Python 3. No finite test is used to justify the general theorem; the distributional support criterion, John contact decomposition, integral identities, and \(H^1\) approximation supply the proof. Run with `python3 verify_area_sum.py` from the directory containing the extracted files.

## Relationship to prior work

Böröczky and Makai, *A strengthening of the Blaschke–Santaló inequality for origin-symmetric planar convex bodies*, arXiv:2602.14750 (first posted 2026-02-16), Theorem 1.1, establish \(A(K)+A(K^\circ)\le2\pi\) in John or Löwner position. Their Theorem 1.3 and Example 1.4 concern stability of the **area product**, not the sharp order of the **area sum** at the disk. The new result identifies a smooth cubic near-equality mechanism for the latter and rules out an a priori plausible quadratic Hausdorff stability strengthening. Standard support-function curvature and area identities, as for example discussed by Zhang (2019), are used as tools; the explicit degeneracy, exact two-regime fan formula, and smoothed obstruction are the proposed additions. Earlier lower-bound stability studies of planar polar area products concern a different extremal inequality.

## Limitations

The result proves an obstruction to exponents below three; it does not prove a global cubic Hausdorff lower bound, or determine an optimal global constant. For \(m\ge3\), the displayed positive quadratic coefficient applies to the specified rotational fan family, not to every body with \(2m\) John contacts. The nonsmooth family is convex but need not have smooth boundary; smooth strict convexity is separately proved for \(\widetilde K_t\). Mathematical novelty remains subject to historical-priority verification and no independent mathematical audit was performed.

## References

1. K. J. Böröczky and E. Makai Jr., *A strengthening of the Blaschke–Santaló inequality for origin-symmetric planar convex bodies*, arXiv:2602.14750v1, 2026-02-16, https://arxiv.org/abs/2602.14750 .
2. Z. Zhang, *Inequalities for curvature integrals in Euclidean plane*, Journal of Inequalities and Applications (2019), article 163, https://doi.org/10.1186/s13660-019-2116-5 .
3. K. J. Böröczky, E. Makai Jr., M. Meyer, and S. Reisner, *Volume product of planar polar convex bodies—lower estimates with stability*, arXiv:1507.01481, https://arxiv.org/abs/1507.01481 .
