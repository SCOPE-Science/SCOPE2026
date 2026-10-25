# Exact mean-section-body volumes and cubical stability for rectangular boxes

## Finding
Let \(a,b,c>0\) and \(K=[-a,a]\times[-b,b]\times[-c,c]\subset\mathbb R^3\). Define \(\overline M_2K\) using the probability-normalized Radon transform of the planar projection-area function as in [1]. Put \(r_1=bc\), \(r_2=ac\), \(r_3=ab\), and let \(D_i=\{x\in\mathbb R^3:x_i=0,\ \|x\|_2\le1\}\). Then
\[
\overline M_2K=\frac8\pi(r_1D_1+r_2D_2+r_3D_3).
\]
Set
\[
H={}_3F_2\left(\begin{matrix}-\frac14,\frac14,\frac12\\1,1\end{matrix};1\right)=0.958091398682850128\ldots,
\qquad C=\sqrt2\pi^2H=13.372779524499367\ldots.
\]
The exact three-dimensional volume is
\[
\boxed{\operatorname{vol}_3(\overline M_2K)=\left(\frac8\pi\right)^3\left(2\pi\sum_{i\ne j}r_i^2r_j+C r_1r_2r_3\right).}
\]
Consequently, with \(\Gamma=\frac8{\pi^3}(12\pi+C)=13.177174904080237\ldots\), the **exact stability identity** is
\[
\boxed{\frac{\operatorname{vol}_3(\overline M_2K)}{\operatorname{vol}_3(K)^2}-\Gamma
=\frac{16}{\pi^2}\left(\frac{(a-b)^2}{ab}+\frac{(a-c)^2}{ac}+\frac{(b-c)^2}{bc}\right).}
\]
Thus, among rectangular boxes of any prescribed positive volume, the unique minimizer of the mean-section-body volume, up to translation and rotation, is the cube. The normalized volume is unbounded above along increasingly eccentric boxes.

## Assumptions and scope
The boxes are full-dimensional and orthogonal, with arbitrary positive half-side lengths. \(\mathrm{Gr}^{u}_{2,3}\) denotes the two-planes containing the line \(\mathbb Ru\), equipped with invariant probability measure. The operator is defined by
\[
h(\overline M_2K,u)=\int_{E\in\mathrm{Gr}^{u}_{2,3}}\operatorname{area}(K|E)\,d\nu_u(E),\quad u\in S^2.
\]
This fixes the normalization; no unnormalized affine-section operator is being used. Minkowski sums in the formulas are sums of **filled disks**, not convex hulls of disks. The theorem gives an exact fixed-volume comparison only for rectangular boxes, not for all convex bodies.

## Proof
**Projection support.** Let \(v\) be a unit normal to \(E\). The area of the shadow of the box is the sum of areas of its three pairs of projected coordinate facets:
\[
\operatorname{area}(K|v^\perp)=4\bigl(bc|v_1|+ac|v_2|+ab|v_3|\bigr).
\]
For a fixed unit \(u\), the unoriented plane normal \(v\) is uniform on the circle in \(u^\perp\); integrating the absolute coordinate of a circle point gives \(\mathbb E|v_i|=\frac2\pi\sqrt{1-u_i^2}\). Therefore
\[
h(\overline M_2K,u)=\frac8\pi\sum_{i=1}^3r_i\sqrt{1-u_i^2}.
\]
Since \(h(D_i,u)=\sqrt{1-u_i^2}\), equality of support functions proves the asserted Minkowski-disk decomposition.

**Two repeated disk factors.** By Minkowski's volume polynomial, the volume of \(r_1D_1+r_2D_2+r_3D_3\) has no pure-cube terms. For \(i\ne j\), the coefficient of \(r_i^2r_j\) is \(3V(D_i,D_i,D_j)\). The volume of \(D_i+tD_j\), to first order in \(t\downarrow0\), is the area \(\pi\) of \(D_i\) times the normal width \(2t\) of \(tD_j\), namely \(2\pi t+o(t)\). Thus \(3V(D_i,D_i,D_j)=2\pi\).

**Three distinct disks.** Write \(S(v)=[-v,v]\). Every unit disk admits the zonoid representation
\[
D_i=\frac14\int_0^{2\pi}S(v_i(\theta))\,d\theta
\]
where \(v_i(\theta)\) runs around its unit circle; the identity follows because the integral support in each in-plane direction is \(4\). The mixed-volume coefficient of three segments is \(6V(S(v_1),S(v_2),S(v_3))=8|\det(v_1,v_2,v_3)|\). Choosing
\[
v_1=(0,\cos\alpha,\sin\alpha),\quad
v_2=(\cos\beta,0,\sin\beta),\quad
v_3=(\cos\gamma,\sin\gamma,0),
\]
we obtain for the coefficient of \(r_1r_2r_3\)
\[
\frac18\int_{[0,2\pi]^3}|\cos\alpha\sin\beta\cos\gamma+\sin\alpha\cos\beta\sin\gamma|\,d\alpha\,d\beta\,d\gamma
=\frac12\int_{[0,2\pi]^2}\sqrt{\cos^2\alpha\sin^2\beta+\sin^2\alpha\cos^2\beta}\,d\alpha\,d\beta.
\]
The integrand is \(2^{-1/2}\sqrt{1-\cos(2\alpha)\cos(2\beta)}\). Averaging its binomial expansion over the two independent circles removes odd powers. The standard even cosine moments give
\[
\frac1{(2\pi)^2}\int_{[0,2\pi]^2}\sqrt{1-\cos(2\alpha)\cos(2\beta)}\,d\alpha\,d\beta
=\sum_{m=0}^\infty\frac{(-\frac14)_m(\frac14)_m(\frac12)_m}{(m!)^3}=H.
\]
The summation converges absolutely (indeed the nonconstant coefficients are negative and summable), and the binomial series passes to the integral by bounded convergence. This gives \(C=\sqrt2\pi^2H\) and proves the volume polynomial.

**Rigidity and exact defect.** Since \(\operatorname{vol}_3K=8abc\) and \(r_1r_2r_3=(abc)^2\), divide the volume formula by \(64(abc)^2\). Its only nonconstant part is \(\frac{16}{\pi^2}\sum_{i\ne j}r_i/r_j\). Group the six ratios into three pairs, use \(t+t^{-1}-2=(t-1)^2/t\), and note \(r_i/r_j\) is a ratio of the corresponding half-side lengths. This yields the boxed exact identity. Every summand is nonnegative and all vanish exactly for \(a=b=c\); taking \(a\to\infty\) with \(abc\) fixed shows unboundedness.

## Verification
The standalone script `verify_volume.py` computes \(H\) by high-precision hypergeometric evaluation, independently integrates the two-circle determinant integral by a \(512\times512\) midpoint rule, and compares exact analytic volumes with convex hulls of Minkowski sums of inscribed regular polygonal disks (three distinct radius triples, three polygon resolutions each). For the three-circle term, direct quadrature gives \(13.3727800199277\), versus the derived \(13.3727795244994\). For unit radii, the analytic volume is \(51.0718913675769\), while the 12-, 20-, and 28-vertex inner-polytope volumes are \(48.784609690827\), \(50.264710907651\), and \(50.659081039525\), respectively, approaching it from below. Exact stability algebra is independent of finite experiments. Execute with Python, NumPy, SciPy and mpmath as specified in `requirements.txt`.

## Relationship to prior work
Brauner, Ortega-Moreno and Schuster [1, eq. (1.1), Corollary 3.3] define the probability-normalized Radon projection operator and prove Aleksandrov–Fenchel-type inequalities. This supplies the operator, not the displayed box volume polynomial, hypergeometric triple-disk coefficient or exact anisotropy-defect identity. Goodey [2] treats injectivity of Radon projection transforms; Goodey, Kiderlen and Weil [3] study section and projection means. The full publicly posted text of [3] was inspected across its definitions, Crofton identities and operator theory; it contains no corresponding box or three-disk evaluation. Only the abstract of [2] was available, leaving a specific historical-priority uncertainty. Standard mixed-volume polynomial and zonoid identities are classical. Computing a convex **hull** of orthogonal disks is a distinct operation from their Minkowski **sum** and does not imply the coefficient above.

## Limitations
The source comparison establishes only best-knowledge originality, not an exhaustive priority guarantee. The full text of [3] was inspected; [2] was abstract-only. Unindexed instances of the specific box calculation remain a residual risk. The numerical tests are not proof; the analytic mixed-volume and support-function calculations establish the infinite statement. No claim about the original (non-even) mean section body of an arbitrary noncentrally symmetric body, nor about general non-box convex-body minimizers, is made.

## References
[1] L. Brauner, O. Ortega-Moreno and F. E. Schuster, *Radon Transforms of Projection Functions and Aleksandrov–Fenchel Inequalities*, arXiv:2610.18268v1 (first posted 2026-10-13), https://arxiv.org/html/2610.18268v1.

[2] P. Goodey, *Radon transforms of projection functions*, Math. Proc. Cambridge Philos. Soc. 123 (1998), 159–168, DOI:10.1017/S0305004197001928.

[3] P. Goodey, M. Kiderlen and W. Weil, *Section and projection means of convex bodies*, Monatsh. Math. 126 (1998), 37–54, DOI:10.1007/BF01312454.
