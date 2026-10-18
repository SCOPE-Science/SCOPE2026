# A Laplace–Gaussian boundary layer in weighted book Lipschitz balls

## Finding
For every integer \(m\ge2\) and edge parameter \(0<t\le2\), consider the metric space \(M_{m,t}=\{h_0,h_1,z_1,\ldots,z_m\}\), where
\[
d(h_0,h_1)=t,\qquad d(h_i,z_j)=1,\qquad d(z_i,z_j)=2\quad(i\ne j).
\]
Let \(Q_{m,t}\) be the unit ball of the real Lipschitz dual \(\operatorname{Lip}_0(M_{m,t})\), using \(h_0\) as the zero basepoint, and let \((T,Y_1,\ldots,Y_m)\) be uniformly distributed with respect to coordinate Lebesgue volume on \(Q_{m,t}\). Put
\[
H_k(t)=\frac{2^{k+1}-(2-t)^{k+1}}{k+1},\qquad
B_m(t)=4H_m(t)-4\frac{2^{m+2}-(2-t)^{m+2}}{m+2}+\frac{2^{m+3}-(2-t)^{m+3}}{m+3},
\]
and write \(v=B_m(t)/H_m(t)\), \(w=H_{m+2}(t)/(12H_m(t))\), and \(d=m+1\).

The exact volume and complete covariance matrix are
\[
\operatorname{Vol}_d(Q_{m,t})=2H_m(t),\qquad
\operatorname{Cov}(T,Y_1,\ldots,Y_m)=
\begin{pmatrix}
v&\frac v2\mathbf1^{\mathsf T}\\
\frac v2\mathbf1&wI_m+\frac v4\mathbf1\mathbf1^{\mathsf T}
\end{pmatrix},\qquad \det\operatorname{Cov}=vw^m.
\]
In particular, the exact affine-invariant isotropic constant is
\[
L(Q_{m,t})=\frac{(vw^m)^{1/(2d)}}{(2H_m(t))^{1/d}}.
\]
The covariance has eigenvalue \(w\) of multiplicity \(m-1\); its two other eigenvalues are
\[
\lambda_{\pm}=\frac12\left(v+w+\frac{mv}{4}\ \pm\sqrt{\left(v-w-\frac{mv}{4}\right)^2+mv^2}\right).
\]

The full probabilistic law has the following product representation: \(T\) has density \((2-|s|)^m/[2H_m(t)]\) on \([-t,t]\), and, independently of \(T\), there are independent \(U_i\sim\operatorname{Unif}[-1,1]\) for which
\[
Y_i=\frac T2+\left(1-\frac{|T|}{2}\right)U_i\qquad(1\le i\le m).
\]
This gives a sharp, dimension-dependent boundary layer. For any sequence \(t_m\in(0,2]\) with \(mt_m\to c\in(0,\infty]\), set \(S_m=mT_m\) and \(\overline Y_m=m^{-1}\sum_iY_i\). Then
\[
\left(S_m,\sqrt m\,\overline Y_m\right)\ \Longrightarrow\ (S_c,G),
\]
where the limits are independent, \(G\sim N(0,1/3)\), and \(S_c\) has density
\[
\frac{e^{-|s|/2}\mathbf1_{\{|s|\le c\}}}{4(1-e^{-c/2})}\quad(0<c<\infty),
\qquad\text{or}\qquad \frac14e^{-|s|/2}\quad(c=\infty).
\]
If \(mt_m\to0\), the sharper microscopic law is \((T_m/t_m,\sqrt m\,\overline Y_m)\Longrightarrow(U,G)\), with independent \(U\sim\operatorname{Unif}[-1,1]\) and the same \(G\). Thus the hub coordinate has a uniform-to-truncated-Laplace-to-Laplace crossover at the precise scale \(t_m\asymp1/m\), while the leaf average retains Gaussian fluctuations.

Finally, **uniformly over all sequences** \(0<t_m\le2\), including those with \(t_m\) exponentially small,
\[
\lim_{m\to\infty}L(Q_{m,t_m})=\frac1{\sqrt{12}}.
\]
This limiting isotropic constant is that of a cube, although the finite-dimensional bodies need not be cubes and their hub coordinate has a distinct limiting law.

## Assumptions and scope
The metric is well defined for exactly \(0<t\le2\); at \(t=2\), the hub-to-hub distance is realized by a two-edge route and the direct graph edge is metrically redundant. All functions and Banach spaces are real. The unit ball is measured in the \(m+1\) anchored function-value coordinates \((T,Y_1,\ldots,Y_m)\); the isotropic constant is invariant under an invertible change of coordinates. The finite-dimensional covariance formulas are **not** claims about the intrinsic orthonormal zero-sum realization without the corresponding linear transformation. The limit is along integer \(m\to\infty\) and may involve any sequence of permitted positive edge parameters.

## Proof
**1. Complete halfspace description and conditional product law.** With \(f(h_0)=0\), set \(T=f(h_1)\) and \(Y_i=f(z_i)\). The Lipschitz inequalities reduce exactly to
\[
|T|\le t,\qquad |Y_i|\le1,\qquad |Y_i-T|\le1.
\]
The remaining \(z_i,z_j\) constraints are automatic because \(|Y_i-Y_j|\le|Y_i|+|Y_j|\le2\). At fixed \(|T|\le t\), each \(Y_i\) ranges independently in
\[
[\max(-1,T-1),\min(1,T+1)],
\]
whose center is \(T/2\) and length \(2-|T|\). Fubini's theorem gives
\[
\operatorname{Vol}_d(Q_{m,t})=\int_{-t}^t(2-|s|)^m\,ds=2H_m(t).
\]
Disintegrating uniform Lebesgue measure into these fibers proves the stated exact product representation, not just an approximate sampling rule.

**2. Exact moments.** Symmetry \((T,Y)\mapsto(-T,-Y)\) gives zero means. With \(H_m(t)=\int_0^t(2-s)^m\,ds\), integration yields
\[
\mathbb E[T^2]=\frac{\int_0^t s^2(2-s)^m\,ds}{H_m(t)}
=\frac{B_m(t)}{H_m(t)}=v.
\]
Conditionally on \(T\), \(\mathbb E[Y_i\mid T]=T/2\), \(\operatorname{Var}(Y_i\mid T)=(2-|T|)^2/12\), and the \(Y_i\) are independent. Hence \(\mathbb E[TY_i]=v/2\), \(\mathbb E[Y_iY_j]=v/4\) for \(i\ne j\), and \(\mathbb E[Y_i^2]=v/4+w\), because \(w=\mathbb E[(2-|T|)^2]/12=H_{m+2}(t)/(12H_m(t))\). These equalities give every covariance entry. The unit-determinant linear coordinate change \((T,Y_i)\mapsto(T,Y_i-T/2)\) transforms the covariance into \(\operatorname{diag}(v,wI_m)\), proving the determinant formula. In an orthonormal basis consisting of the hub coordinate, the common-leaf coordinate, and \(m-1\) leaf contrasts, the remaining \(2\times2\) block is \(\left(\begin{smallmatrix}v&\sqrt m v/2\\\sqrt m v/2&w+mv/4\end{smallmatrix}\right)\); its quadratic formula gives \(\lambda_\pm\). The isotropic-constant identity follows from its standard volume-and-covariance definition.

**3. The exact critical window and joint independence.** For \(S_m=mT_m\), its density is proportional to
\[
\mathbf1_{\{|s|\le mt_m\}}\left(1-\frac{|s|}{2m}\right)^m.
\]
The last factor tends pointwise to \(e^{-|s|/2}\) and is bounded above by that integrable function. If \(mt_m\to c\in(0,\infty]\), dominated convergence evaluates the normalizer and proves convergence to the displayed truncated or full two-sided exponential density. If \(mt_m\to0\), the law of \(T_m/t_m\) has density proportional to \((1-t_m|u|/2)^m\) on \([-1,1]\), which converges uniformly to one because \(mt_m\to0\), proving the uniform limit.

In all regimes \(S_m\) is tight (when \(mt_m\le1\), it is bounded; otherwise the normalized exponential envelope gives a uniform tail bound). Thus \(\sqrt m\,T_m\to0\) in probability, and \(A_m=1-|T_m|/2\to1\). By the independent representation,
\[
\sqrt m\,\overline Y_m=\frac{\sqrt m\,T_m}{2}+A_m\frac1{\sqrt m}\sum_{i=1}^m U_i.
\]
The classical central limit theorem gives \(m^{-1/2}\sum_iU_i\Longrightarrow N(0,1/3)\). This sum is independent of the complete hub variable for every \(m\). Joint convergence, Slutsky's theorem, and the vanishing first term therefore prove both stated **independent** joint limits. No Gaussian assertion is made for the hub coordinate.

**4. Uniform isotropic-constant limit.** Write \(\alpha=\min(t,1/m)\). Elementary bounds, valid for every \(m\ge2\) and \(0<t\le2\), are
\[
2^{m-1}\alpha\le H_m(t)\le2^{m+1}\alpha,
\qquad \frac{\alpha^2}{12}\le v\le32\alpha^2.
\]
For the first lower bound integrate over \([0,\alpha]\), using \((1-1/(2m))^m\ge1/2\); for its upper bound use \((1-s/2)^m\le e^{-ms/2}\). For the second lower bound integrate \(s^2\) over \([0,\alpha]\) and divide by the upper \(H_m\) bound. For the upper bound use \(v\le t^2\) when \(t\le1/m\), and otherwise use \(\int_0^\infty s^2e^{-ms/2}\,ds=16/m^3\) and the lower \(H_m\) bound. Likewise \(\mathbb E|T|=O(1/m)\) **uniformly in** \(t\): if \(t\le1/m\), use \(|T|\le t\); otherwise bound its unnormalized first moment by \(2^m\int_0^\infty se^{-ms/2}\,ds=4\cdot2^m/m^2\) and normalize with the lower \(H_m\) bound. Consequently \(w=\mathbb E[(2-|T|)^2]/12\to1/3\) uniformly.

The inequalities show \(\sqrt v/H_m(t)=2^{-m}\Theta(1)\), with constants independent of both \(m\) and \(t\). Thus, with \(d=m+1\),
\[
L(Q_{m,t})=\left(\frac{\sqrt v}{H_m(t)}\right)^{1/d}\frac{w^{m/(2d)}}{2^{1/d}}\longrightarrow\frac12\cdot\frac1{\sqrt3}=\frac1{\sqrt{12}},
\]
uniformly along all permitted parameter sequences. This completes the theorem.

## Verification
The standalone Python standard-library checker `verify_book_bulk.py` uses independent binomial-polynomial integrals (rather than the closed expressions in the theorem), checks every second-moment and determinant identity exactly with rational arithmetic, and covers \(m=2,\ldots,10\) at \(t=1/4,1/2,1,3/2,2\). Its successful output is `EXACT_WEIGHTED_BOOK_MOMENT_CHECKS_PASS 45 cases`. An independent halfspace-intersection/convex-hull calculation of the *actual dual polytopes* used floating-point Euclidean simplex integration and matched volume and every covariance entry for \(m=2,3,4\) at \(t=1/3,1,3/2,2\) (12 cases, maximum error below \(3.2\times10^{-15}\)). Both computations test finite instances only. The proof for all dimensions, all real parameters, and the asymptotic limits is analytic and does not rely on finite extrapolation.

## Relationship to prior work
Aliaga and Pernecká (arXiv:1810.11278, first posted October 26, 2018; primary MSC 46B20) identify extreme molecules in Lipschitz-free spaces. Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, first posted November 24, 2019) develop finite-dimensional Lipschitz-free convex-body geometry, graph representations, and volume-product questions. These provide the natural Banach-space setting, but the present theorem concerns the **uniform interior law** and its critical-window fluctuations, not just faces, extreme molecules, or Mahler products. The existing book-graph face enumerator and a published exact Löwner ellipsoid for the unit-edge book concern combinatorial face structure and optimal enclosing ellipsoids; neither statement evaluates uniform interior covariance nor implies the independent two-scale fluctuation law. The integer-valued random Lipschitz-height literature addresses a distinct discrete measure and is not silently identified with Lebesgue-uniform real potentials. The scalar volume formula is used here as a normalization identity, not presented as a stand-alone novelty claim.

## Limitations
The covariance matrix is tied to the specified anchor and coordinate realization, whereas the isotropic constant is affine invariant. The asymptotic theorem concerns book metrics with exactly two hubs and uniform leaf-to-hub distance one, not arbitrary finite graph metrics. The window \(mt_m\to c\) describes all convergent-window subsequences; it does not claim a single limiting law if the scaling parameter oscillates. An equivalent calculation may exist under different graph-Lipschitz or polytope-probability terminology; the literature comparison is a documented best-knowledge search, not a proof of uniqueness. The external independent scientific audit has not yet been performed.

## References
1. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278, first public version 2018-10-26. https://arxiv.org/abs/1810.11278.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public version 2019-11-24. https://arxiv.org/abs/1911.10642.
3. R. Peled, W. Samotij and A. Yehudayoff, *Lipschitz functions on expanders are typically flat*, Combinatorics, Probability and Computing 22 (2013), 566–591, doi:10.1017/S0963548313000163 (integer-valued random Lipschitz functions; different model).
4. *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes*, publicly available mathematical research record, 2026-10-11. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-sharp-l-wner-ellipsoid-edge-invisibility-threshold-for-book-gr--87e035ae5886/RESULT.md.
