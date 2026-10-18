# Sharp stability reversal for orthogonal linear-spline projection on alternating meshes

## Finding
For positive mesh lengths \(a,b\), form the two-periodic knot sequence \(x_{2k}=k(a+b)\) and \(x_{2k+1}=k(a+b)+a\), \(k\in\mathbb Z\). Let \(P_{a,b}\) be the \(L^2(\mathbb R)\)-orthogonal projector onto the closed space of continuous piecewise-linear splines with these knots. Its canonical integral-kernel extension to \(L^\infty(\mathbb R)\) has the exact norm
\[
\boxed{\|P_{a,b}\|_{L^\infty\to L^\infty}=\frac{5a^2+22ab+5b^2}{3a^2+10ab+3b^2}
=2-\frac{(a-b)^2}{3a^2+10ab+3b^2}.}
\]
Consequently, the norm equals \(2\) exactly on the uniform mesh \(a=b\), and it is strictly below \(2\) on every genuinely alternating mesh. Writing \(\theta=|a-b|/(a+b)\), the norm is \(2-\theta^2/(4-\theta^2)\); it decreases strictly for \(0<\theta<1\), and its unattained infimum over \(a,b>0\) is \(5/3\). Thus the natural global periodic distortion has the opposite strict effect from the previously considered isolated-cell perturbation of the uniform mesh.

## Assumptions and scope
All lengths \(a,b\) are arbitrary strictly positive real numbers. The ambient measure is Lebesgue measure on the full real line, not a finite interval or torus. The spline functions are continuous and affine on each \([x_j,x_{j+1}]\). The closed spline subspace is the closed linear span in \(L^2(\mathbb R)\) of the nodal hat functions \(\phi_j\), with \(\phi_j(x_i)=\delta_{ij}\). The projection is initially defined on \(L^2\); the displayed \(L^\infty\) norm refers to its canonical uniformly integrable kernel extension. The statement is an exact two-periodic classification; it does not purport to give a sharp constant for arbitrary nonperiodic meshes, finite meshes with boundaries, or higher-degree splines.

## Proof
Let \(h_j=x_{j+1}-x_j\), so \(h_{2k}=a\) and \(h_{2k+1}=b\). The hat Gram matrix \(G=(\langle\phi_i,\phi_j\rangle)\) has
\[
G_{jj}=\frac{a+b}{3},\qquad G_{j,j+1}=\frac{h_j}{6},\qquad G_{ij}=0\ \text{if }|i-j|>1.
\]
It is a bounded positive, invertible operator on \(\ell^2(\mathbb Z)\): its strictly positive quadratic form is bounded above and below by fixed multiples of the coefficient norm, since \(a,b>0\). Equivalently, the tridiagonal matrix \(6G\) is uniformly strictly diagonally dominant. Put
\[
D=2(a+b),\qquad Q(r)=ab r^2+(a^2+b^2-D^2)r+ab.
\]
The two positive roots of \(Q\) are reciprocal; let \(r\in(0,1)\) denote the smaller root. Indeed \((D^2-a^2-b^2)/(ab)>2\). Define
\[
u=\frac{a+br}{D},\qquad v=\frac{b+ar}{D},\qquad A=\frac{6}{D-au-bv}.
\]
All of \(A,u,v\) are positive, \(u,v<1\), and \(uv=r\); the last identity is precisely \(Q(r)=0\) after clearing denominators. The following signed, exponentially decaying sequence solves \(Gg=e_0\):
\[
g_0=A,\quad g_{2k}=g_{-2k}=Ar^k\quad(k\ge1),\quad
g_{2k+1}=-Au r^k,\quad g_{-(2k+1)}=-Av r^k\quad(k\ge0).
\]
Substitution into \(Dg_j+h_{j-1}g_{j-1}+h_jg_{j+1}=6\delta_{0j}\) verifies this at the origin and on both parity classes, using \(uv=r\); uniqueness holds by invertibility of \(G\). In particular, adjacent nodal values strictly alternate in sign.

The projector kernel satisfies \(K(x_i,y)=\sum_j(G^{-1})_{ij}\phi_j(y)\). At \(x_0=0\), \(K(0,\cdot)\) is the continuous piecewise-linear interpolation of the nodal values \(g_j\). On a cell of length \(h\) whose endpoint values are \(c>0\) and \(-d<0\), the exact absolute integral is
\[
\int_{\mathrm{cell}}|K(0,y)|\,dy=\frac{h(c^2+d^2)}{2(c+d)}.
\]
Sum the four alternating geometric tails of cells to obtain
\[
\mathcal L_0:=\int_{\mathbb R}|K(0,y)|\,dy
=\frac{A}{2(1-r)}\left[
a\frac{(1+v)(1+u^2)}{1+u}
+b\frac{(1+u)(1+v^2)}{1+v}
\right].
\]
The identity \(uv=r\) is used to collect each pair of opposite-side tails. Substituting the definitions of \(u,v,A\), clearing denominators, and reducing the resulting numerator modulo \(Q(r)\) gives exactly
\[
\mathcal L_0=\frac{5a^2+22ab+5b^2}{3a^2+10ab+3b^2}.
\]
An independent exact symbolic polynomial-divisibility check of this final simplification, plus explicit finite-matrix cross-checks, is provided in `verify.py`.

Translation by \(a+b\) takes each even knot into another even knot. Reflection \(y\mapsto a-y\) interchanges even and odd knots and preserves the complete two-periodic knot set. Therefore all the functions \(K(x_j,\cdot)\) have the same \(L^1\) norm \(\mathcal L_0\). At a point \(x=(1-t)x_j+t x_{j+1}\), \(0\le t\le1\), the hat expansion gives
\[
K(x,\cdot)=(1-t)K(x_j,\cdot)+tK(x_{j+1},\cdot),
\]
whence \(\|K(x,\cdot)\|_1\le\mathcal L_0\). The kernel is uniformly absolutely integrable because \(G^{-1}\) has exponential decay. Thus \(\|P_{a,b}\|_{L^\infty\to L^\infty}\le\mathcal L_0\). The bounded function \(f(y)=\operatorname{sgn}K(0,y)\), with an arbitrary sign at its isolated zeros, attains \(|P_{a,b}f(0)|=\mathcal L_0\), giving equality. Here \(f\) is an admissible \(L^\infty\) input and the kernel extension, not an \(L^2\)-bounded-input assumption, is used.

Finally,
\[
\mathcal L_0=2-\frac{(a-b)^2}{4(a+b)^2-(a-b)^2}
=2-\frac{\theta^2}{4-\theta^2}.
\]
Since \(0\le\theta<1\), this proves the sharp equality, strict-inequality, monotonicity, and limiting assertions. No finite truncation is used to prove the infinite-line statement.

## Verification
The standalone Python checker `verify.py` requires Python 3 with SymPy and NumPy. Run `python verify.py` from the extracted file directory. It carries out an exact polynomial-division certificate for the Green-row simplification, verifies the contrast formulas, tests multiple positive rational length pairs, compares independently assembled periodic finite Gram inverses against the infinite-line result, and performs exact-rational finite-cycle checks. It reported `PASS: 144 independent symbolic, exact rational, and finite-cycle checks`. These finite calculations are reproducibility aids; the infinite statement follows from the explicit inverse Gram row and exact kernel integration proved above.

## Relationship to prior work
The earlier studies of orthogonal spline projections with arbitrary knots established general boundedness and inverse-Gram localization, not the present exact two-periodic norm. In particular, Passenbrunner's August 2016 preprint addresses periodic spline projections on a torus and proves knot-independent bounds, while Passenbrunner and Shadrin's 2013 preprint treats arbitrary knots and almost-everywhere convergence. The present result is an infinite-line exact parameter classification, not a refinement claimed for all meshes. An isolated perturbation of one cell is a different configuration and does not imply the two-periodic formula. Historical exact formulas in other spline and finite-element terminology remain a priority risk.

## Limitations
Only degree-one continuous splines on a full-line, strictly positive, two-periodic mesh are treated. The norm for general or finite meshes, and nonperiodic local defects, is not determined by this theorem. The kernel is initially obtained by \(L^2\) orthogonal projection and then extended to \(L^\infty\). The exact constant has not undergone independent mathematical or bibliographic validation. Some plausible historical literature on sharp spline projection norms could not be inspected in full.

## References
1. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720v1 (first publicly posted 2016-08-24), https://arxiv.org/abs/1608.06720.
2. M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824v1 (2013), https://arxiv.org/abs/1308.4824.
3. P. Oswald, *L-infinity bounds for the L2-projection onto linear spline spaces*, 2013, https://doi.org/10.1007/978-1-4614-4565-4_24 (full text not inspected).
4. R.-Q. Jia, *L-infinity boundedness of L2-projections on splines for a multiple geometric mesh*, 1987, https://doi.org/10.2307/2007836 (full text not inspected).
