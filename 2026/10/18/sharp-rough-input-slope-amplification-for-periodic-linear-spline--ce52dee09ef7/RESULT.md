# Sharp rough-input slope amplification for periodic linear-spline orthoprojection

## Finding
On the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), let \(S_n\) be the space of continuous, periodic, piecewise-affine functions with equally spaced knots \(j/n\), \(0\le j<n\), and let \(P_n\) be the Lebesgue-\(L^2\) orthogonal projector onto \(S_n\). For each integer \(n\ge3\), define the **dimensionless sharp rough-input derivative gain**
\[
C_n=\frac1n\sup_{\|f\|_{L^\infty(\mathbb T)}\le1}\operatorname{Lip}(P_nf),
\]
where the Lipschitz seminorm uses the geodesic distance on the unit circle. Put \(q=2-\sqrt3\) and \(t=-q\), and for \(1\le j\le n\) set
\[
a_{n,j}=\sqrt3(1+q)\frac{|t^{j-1}-t^{n-j}|}{1-t^n},\qquad a_{n,n+1}=a_{n,1}.
\]
The denominator is positive. The following is an **exact finite formula** for every \(n\ge3\):
\[
\boxed{C_n=\sum_{j=1}^n\frac{a_{n,j}^2+a_{n,j+1}^2}{2(a_{n,j}+a_{n,j+1})}.}
\]
No denominator in this sum vanishes; for odd \(n\), exactly one \(a_{n,j}\) is zero. In particular \(C_3=3\), \(C_4=27/8\), and \(C_5=192/55\). The sharp **mesh-uniform** constant and its convergence rate are
\[
\boxed{0<C_n<\frac{9-\sqrt3}{2},\qquad
\lim_{n\to\infty}C_n=\frac{9-\sqrt3}{2},\qquad
0<\frac{9-\sqrt3}{2}-C_n=O(q^{n/2}).}
\]
Thus the optimal asymptotic Lipschitz amplification from a bounded, not necessarily continuous, input is \(n(9-\sqrt3)/2\), with an exponentially small, rather than algebraic, finite-circle defect. The sharp norm for each \(n\) is attained by a bounded real sign function of the derivative evaluation kernel.

## Assumptions and scope
The integer \(n\ge3\) counts *cells*; the mesh width is \(1/n\). The scalar field may be real or complex. Norms use ordinary Lebesgue measure on \(\mathbb T\); scaling this measure by a positive constant leaves \(P_n\) unchanged. The Lipschitz seminorm of a periodic piecewise-affine function equals the maximum absolute slope over its cells. The input class is \(L^\infty(\mathbb T)\); the projection is first defined on \(L^2\) and extends to bounded inputs because the domain has finite measure. The displayed finite sum is unambiguous also at the single zero coefficient in the odd case.

## Proof
Let \(\varphi_j\) be the periodic nodal hat functions with \(\varphi_j(k/n)=\mathbf1_{j=k}\). Their Gram matrix is
\[
G_n=\frac1{6n}A_n,
\]
where \(A_n\) is the \(n\)-by-\(n\) circulant matrix with diagonal entries \(4\), nearest-neighbor entries \(1\) and all other entries zero. This statement includes \(n=3\), where every off-diagonal pair consists of neighbors. Its eigenvalues \(4+2\cos(2\pi k/n)\) are at least \(2\), so the inverse exists.

For a periodic input \(f\), its projected nodal vector \(u\) satisfies
\[
u_j=6n\sum_{k=0}^{n-1}(A_n^{-1})_{jk}\int_{\mathbb T}f(y)\varphi_k(y)\,dy.
\]
Consequently the derivative on the first cell is \(n(u_1-u_0)\). Translation invariance makes its sharp norm the norm over all cells. Rescale the circle to circumference \(n\), denote its unit-width hats by \(\Phi_j\), and write
\[
d_j=6[(A_n^{-1})_{1j}-(A_n^{-1})_{0j}].
\]
Then \(C_n\) equals the \(L^1\)-norm over one period of \(D_n(x)=\sum_jd_j\Phi_j(x)\). This follows from \(L^\infty\)-\(L^1\) duality and is sharp: take the sign of \(D_n\) as input, shifted and rescaled back to \(\mathbb T\). It is not an appeal to a finite sample of inputs.

On the whole integer line the tridiagonal inverse has the exact Green matrix
\[
(A_\infty^{-1})_{ij}=\frac{(-q)^{|i-j|}}{2\sqrt3}.
\]
Indeed, the right side is summable and \(4g_j+g_{j-1}+g_{j+1}=\mathbf1_{j=0}\), since \(q+q^{-1}=4\). Periodizing this Green matrix gives, with \(0\le r<n\),
\[
(A_n^{-1})_{0r}=\frac{t^r+t^{n-r}}{2\sqrt3(1-t^n)}.
\]
Thus, labeling the residue \(0\) as \(j=n\),
\[
d_j=\sqrt3(1+q)\frac{t^{j-1}-t^{n-j}}{1-t^n},\quad1\le j\le n.
\]
The nonzero \(d_j\) have opposite signs at consecutive residues, apart from a single zero at \(j=(n+1)/2\) for odd \(n\). This follows directly by comparing the parity and size of the two powers of \(t\): for even \(n\) the signs alternate everywhere; for odd \(n\) the alternating pattern reverses across the unique zero. The integral of the absolute affine interpolant between coefficients of opposite signs and magnitudes \(u,v\) equals \((u^2+v^2)/(2(u+v))\); the same holds if one is zero. Summing cell by cell proves the exact formula.

To obtain the sharp uniform limit, define the infinite-line derivative kernel
\[
D_\infty(x)=\sqrt3\sum_{j\in\mathbb Z}
\big[t^{|1-j|}-t^{|j|}\big]\Phi(x-j),
\qquad\Phi(s)=\max(1-|s|,0).
\]
Its nodal values are \(-a,+a\) at \(0,1\), with \(a=\sqrt3(1+q)\), and their magnitudes decay by a factor \(q\) per subsequent step on either tail. Hence the central-cell absolute integral is \(a/2\). The two tails contribute
\[
\frac{a(1+q^2)}{1-q^2},
\]
and elementary simplification yields
\[
\|D_\infty\|_1=a\left(\frac12+\frac{1+q^2}{1-q^2}\right)=\frac{9-\sqrt3}{2}.
\]
The finite kernel is precisely the absolutely convergent periodization \(D_n(x)=\sum_{m\in\mathbb Z}D_\infty(x+mn)\). The triangle inequality therefore gives \(C_n\le\|D_\infty\|_1\). It is **strict**: on a positive-length subinterval of \((0,1)\), the central copy and the copy shifted by \(n\) have opposite signs. If \(n\) is even, use \((1/2,1/(1+q))\); if odd, use \((0,1/2)\). Equality in the integrated triangle inequality is impossible.

Let \(I_n=[(1-n)/2,(1+n)/2]\). Periodization and \(L^1\) triangle inequalities yield
\[
0<\|D_\infty\|_1-C_n\le2\int_{\mathbb R\setminus I_n}|D_\infty(x)|\,dx.
\]
The explicit nodal decay makes this tail \(O(q^{n/2})\). This completes the universal bound, the limiting constant, and the exponential rate.

## Verification
An independently assembled exact-rational inverse of \(A_n\) for \(3\le n\le20\) was compared with the closed Green formula and the absolute affine-integral formula. A standalone pure-Python checker, `checks/periodic_spline_gain.py`, performs the computations directly and verifies the low-degree rational constants, alternating signs, the strict upper bound in sampled degrees, and the exponential convergence prediction. It is not used as an infinite proof. The complete inequalities for arbitrary \(n\) follow from the periodization argument above. The checker makes no external data requests.

## Relationship to prior work
Passenbrunner's 2011 study of uniformly spaced *interval* spline projectors determines monotonicity of the ordinary \(L^1\)/\(L^\infty\) Lebesgue norm and exhibits the tridiagonal inverse recurrence, not the periodic rough-input-to-slope gain. Passenbrunner's 2016 periodic theorem establishes uniform \(L^\infty\) boundedness and almost-everywhere convergence for arbitrary periodic knots and spline orders; the present result optimizes the norm **after differentiation** at the natural inverse-mesh scale. These bounds do not imply the numerical constant \((9-\sqrt3)/2\) or the exact finite-cell formula by their stated conclusions. Classical finite-element inverse inequalities motivate the scale but are not treated as novelty evidence.

## Limitations
The theorem concerns periodic **continuous degree-one** splines on a **uniform** mesh, and rough-input-to-derivative stability, not the norm of the projector itself or derivative stability in terms of a derivative of its input. The rate \(O(q^{n/2})\) is an upper bound on the deficit, not an asserted two-sided asymptotic equivalent. The bibliographic search cannot establish historical uniqueness: an earlier exact derivative kernel or finite-element inverse-stability formula under another terminology might imply this result. All scientific review is same-model, with no independent audit or certification.

## References
1. M. Passenbrunner, *Monotonicity of the Lebesgue constant for equally spaced knots*, arXiv:1103.1949v1, first posted 2011-03-10, https://arxiv.org/abs/1103.1949.
2. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720v1, first posted 2016-08-24, https://arxiv.org/abs/1608.06720.
3. P. Oswald, *\(L^\infty\)-Bounds for the \(L^2\)-Projection onto Linear Spline Spaces*, 2012, DOI 10.1007/978-1-4614-4565-4_24 (abstract consulted; full text unavailable during review).
4. C. de Boor, *On the (bi)infinite case of Shadrin's theorem concerning the \(L^\infty\)-boundedness of the \(L^2\)-spline projector*, 2011/2012 (bibliographic abstract consulted).
