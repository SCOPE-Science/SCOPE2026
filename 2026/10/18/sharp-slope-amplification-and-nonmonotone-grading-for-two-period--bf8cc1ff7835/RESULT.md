# Sharp slope amplification and nonmonotone grading for two-periodic linear spline orthoprojections

## Finding
Fix \(r>0\) and consider the bi-infinite linear-spline grid \(t_{2k}=k(1+r)\), \(t_{2k+1}=k(1+r)+1\). Let \(P_r\) be orthogonal projection in \(L^2(\mathbb R)\) onto the closed span of the nodal hat functions. For the sharp global seminorm \(\operatorname{Lip}(g)=\sup_{x\ne y}|g(x)-g(y)|/|x-y|\), define
\[
G(r)=\sup_{\|f\|_{L^\infty(\mathbb R)}\le1}\operatorname{Lip}(P_rf).
\]
Write \(s=3r^2+8r+3\), \(q=2r/[s+\sqrt{s^2-4r^2}]\), \(d=2(1+r)\), \(\beta=(r+q)/d\), and \(u=d/[d(d-1)-r(r+q)]\). All denominators are positive and \(0<q<1\). Set
\[
F(r)=3u+\frac{6u}{1-q}\left[r\frac{1+\beta^2}{1+\beta}+\frac{\beta^2+q^2}{\beta+q}\right].
\]
The exact sharp norm for every positive mesh contrast is
\[
\boxed{G(r)=\max\{F(r),r^{-1}F(1/r)\}.}
\]
The two terms are respectively the sharp gains on the unit-length and length-\(r\) cells. Their maximizing inputs may be taken to be signs of the corresponding derivative evaluation kernels. In particular,
\[
F(1)=\frac{9-\sqrt3}{2},\quad F'(1)=\frac{2-\sqrt3}{8}>0,\quad F(2)=\frac{65}{14}-\frac{\sqrt{105}}{10}<F(1).
\]
Since the unit cell is the winning branch at and just above \(r=1\), and also at \(r=2\), the global sharp Lipschitz amplification increases initially under a slight grading, but at ratio \(2\) is smaller than for equal knot spacings. Thus it is nonmonotone on \([1,2]\).

## Assumptions and scope
Every knot gap is positive; there are no finite endpoints. The Hilbert-space spline space consists of \(L^2\) functions globally continuous and affine on each cell. The underlying measure is Lebesgue measure, with no interval-length normalization. The output seminorm uses Euclidean distance on \(\mathbb R\). The bounded-input operator is the canonical kernel extension from \(L^2\cap L^\infty\); it is not an unrelated choice of extension. Since outputs are continuous piecewise affine and bounded, their Lipschitz seminorm is exactly the maximum absolute cell slope.

## Proof
Let \(N_j\) be the nodal hat at \(t_j\), and put \(h_j=t_{j+1}-t_j\). Its mass matrix has diagonal \((h_{j-1}+h_j)/3=(1+r)/3\) and off-diagonal entry \(h_j/6\). In other words \(6M=DAD\), where \(D_{jj}=(-1)^j\), \(A_{jj}=d=2(1+r)\), and \(A_{j,j+1}=A_{j+1,j}=-h_j\). Strict diagonal dominance and positivity give a positive exponentially decreasing inverse \(A^{-1}\); for instance the Neumann series based on the diagonal \(d\) converges because \((1+r)/d=1/2\).

Consider the derivative on the unit cell \([t_0,t_1]\). Its numerator is \((P_rf)(t_1)-(P_rf)(t_0)\). By the sign-conjugated inverse mass matrix, its kernel is
\[
-6\sum_{j\in\mathbb Z}(-1)^jz_jN_j(y),\qquad z_j=(A^{-1})_{0j}+(A^{-1})_{1j}>0.
\]
Reflection about the midpoint of this particular cell interchanges indices \(j\) and \(1-j\), so \(z_0=z_1=u\), \(z_{-1}=z_2=\beta u\), and, for all \(k\ge0\),
\[
z_{-2k}=z_{1+2k}=uq^k,\qquad z_{-(2k+1)}=z_{2+2k}=\beta uq^k.
\]
The recurrence \(Az=e_0+e_1\) at the exterior odd sites gives \(\beta=(r+q)/d\), and its two-step characteristic equation is \(rq^2-(3r^2+8r+3)q+r=0\). The center equation \((d-1)u-r\beta u=1\) gives the stated value of \(u\). These recurrences determine the unique bounded Green solution because \(A\) has a bounded inverse.

On a cell of length \(h\), an affine function joining nonzero values \(a\) and \(-b\), with \(a,b>0\), has exact absolute integral \(h(a^2+b^2)/[2(a+b)]\). The alternating signs of the coefficients above therefore give the unit-cell kernel absolute integral as follows: the central cell contributes \(3u\), and the reflected tails contribute the geometric series
\[
\frac{6u}{1-q}\left[r\frac{1+\beta^2}{1+\beta}+\frac{\beta^2+q^2}{\beta+q}\right].
\]
This proves the formula \(F(r)\) exactly, with equality attained by a measurable sign function of the derivative kernel. Reflection and two-step translations make all unit cells equivalent. Interchanging the two cell-length types and rescaling lengths by \(r\) gives the other cell slope norm \(F(1/r)/r\). Taking the maximum of the two yields \(G(r)\); there is no additional optimization over locations, since every output is affine within each cell.

At \(r=1\), the smaller root is \(q=7-4\sqrt3\), so exact substitution gives \(F(1)=(9-\sqrt3)/2\). The characteristic root satisfies \(q(r)=q(1/r)\), so \(q'(1)=0\). Differentiating the explicit rational expression for \(F\) at this root gives \(F'(1)=(2-\sqrt3)/8\). At \(r=2\), the root is \(q=(31-3\sqrt{105})/4\); exact substitution gives \(F(2)=65/14-\sqrt{105}/10\). The latter is strictly smaller than \(F(1)\); one elementary certificate is \(\sqrt{105}>51/5\) and \(\sqrt3<7/4\), which imply \(\sqrt{105}/10>1/7+\sqrt3/2\).

For \(r>1\) sufficiently close to one, the two branches separate in favor of \(F(r)\): the right derivative at \(1\) of their difference is \(2F'(1)+F(1)>0\). At \(r=2\), the other branch \(F(1/2)/2\) is smaller (this also follows from its explicit root formula, or from the generic \(\|P_2\|_{\infty\to\infty}\le2\) and the elementary long-cell slope bound \(2\|P_2\|_\infty/2\le2<F(2)\)). Thus \(G(r)>G(1)\) just to the right of one whereas \(G(2)<G(1)\), proving nonmonotonicity.

## Verification
The accompanying stand-alone `CHECK.py` directly inverts finite even-period periodic hat mass matrices, integrates each signed affine derivative kernel by the exact two-value formula, and compares the unit/long-cell results with the infinite-volume expressions for nine distinct ratios. All 18 independent period-24 edge comparisons were within \(2\cdot10^{-6}\) of the infinite formula. The checker also checks the two closed special values, the sign of the crossover, and the derivative by centered differences. Its finite-period tests corroborate but do not prove the bi-infinite identity: the proof is the inverse-mass recurrence and absolutely convergent kernel integration given above.

## Relationship to prior work
Passenbrunner and Shadrin (2013, arXiv:1308.4824, Theorem 1.2) establish broad inverse-Gram decay for spline orthoprojections, rather than exact derivative amplification on a two-periodic grid. Foucart's 2005 preprint on the max-norm of spline orthoprojectors studies sup norms of projections across knot sequences, not their sharp Lipschitz gains. Passenbrunner's 2016 periodic-spline work addresses uniform boundedness and convergence, not this explicit two-branch derivative norm. The known exact sup-norm projector law on this two-periodic mesh is a different invariant; it does not yield the sharp slope norm. The known uniform-mesh sharp slope law is recovered at \(r=1\) but does not imply this graded nonmonotone behavior.

## Limitations
The result is for continuous degree-one splines on a bi-infinite exactly two-periodic mesh. It does not cover bounded intervals, arbitrary nonperiodic grids, higher-order splines, or derivative bounds in other \(L^p\) norms. The formula proves existence, but not uniqueness, of an interior maximizing grading contrast. Historical priority under different spline inverse-Gram and finite-element terminology remains uncertain. Rong-Qing Jia's 1987 multiple-geometric-mesh article could not be read in full; only title/bibliographic information was accessible and the equivalence risk is noted. No independent mathematical audit has been performed.

## References
1. M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824 (first public version, 22 August 2013). Full text: https://arxiv.org/pdf/1308.4824.
2. S. Foucart, *On the value of the max-norm of the orthogonal projector onto splines with multiple knots*, preprint dated 14 December 2005, https://foucart.github.io/publi/SplineProj2.pdf.
3. S. Foucart, *Open questions around the spline orthoprojector*, https://foucart.github.io/publi/OpenPb.pdf.
4. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720, https://arxiv.org/html/1608.06720v2.
5. R.-Q. Jia, *\(L^\infty\)-boundedness of \(L^2\)-projections on splines for a multiple geometric mesh*, Mathematics of Computation 48 (1987), 675–690, DOI:10.2307/2007836 (full text not inspected).
