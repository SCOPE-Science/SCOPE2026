# Sharp two-choice rectangular maximal bounds and geometric rigidity

## Finding
For each integer \(d\ge1\) and parameter \(0<\theta<1\), the two-choice rectangular averaging maximal operator \(\mathcal R_{\theta,d}\) on \(\ell^2(\mathbb Z^d)\), defined below, has the **exact** norm
\[
\|\mathcal R_{\theta,d}\|_{\ell^2\to\ell^2}=\left(\frac{2}{2-\theta}\right)^{d/2}.
\]
Every nonzero one-dimensional extremizer, and only such an extremizer, is a translate and nonzero scalar multiple of the geometric half-line
\[
 n\longmapsto\rho^{n}\mathbf1_{\{n\ge0\}},\qquad \rho=\frac{1-\theta}{2-\theta}.
\]
A precise nonnegative deficit identity holds in one dimension. In particular, the unweighted adjacent-two-point operator at \(\theta=1/2\) has sharp rectangular norm \((4/3)^{d/2}\). The dimension dependence is exponentially growing, unlike synchronous cube averages. For higher dimensions, tensor products of one-dimensional geometric half-lines attain the displayed sharp norm; uniqueness of higher-dimensional extremizers is not asserted.

## Assumptions and scope
Work over complex-valued \(\ell^2(\mathbb Z^d)\) with counting measure. Let \((S_jf)(n)=f(n-e_j)\), where \(e_j\) is the \(j\)-th standard unit vector. For \(\varepsilon\in\{0,1\}^d\), put \(T_{j,0}=I\) and \(T_{j,1}=(1-\theta)I+\theta S_j\). The commuting operators \(T_{j,\varepsilon_j}\) define
\[
 (\mathcal R_{\theta,d}f)(n)=\max_{\varepsilon\in\{0,1\}^d}\left|T_{1,\varepsilon_1}\cdots T_{d,\varepsilon_d} f(n)\right|.
\]
This is a *rectangular*, independently selectable, two-length maximal operator, not the synchronous centered-cube maximal function. At \(\theta=1/2\), each coordinate may use either the one-point kernel or the equally weighted adjacent two-point kernel.

## Proof
**Exact scalar certificate.** Set \(c=\theta/(2-\theta)\). For every pair of complex numbers \(u,v\), direct expansion gives
\[
 |u|^2+c|v|^2-|\,(1-\theta)u+\theta v\,|^2
 =c\,|(2-\theta)u-(1-\theta)v|^2.
\]
Because \(c>0\), taking the maximum of the two alternatives yields the exact identity
\[
 |u|^2+c|v|^2-\max\{|u|^2,|(1-\theta)u+\theta v|^2\}
 =c\min\{|v|^2,|(2-\theta)u-(1-\theta)v|^2\}.
\tag{1}
\]

**One dimension.** Insert \(u=f(n)\), \(v=f(n-1)\) in (1) and sum over all integers. Since shifts preserve \(\ell^2\)-norm, all sums converge absolutely and give
\[
 \frac{2}{2-\theta}\|f\|_2^2-\|\mathcal R_{\theta,1}f\|_2^2
 =\frac{\theta}{2-\theta}\sum_{n\in\mathbb Z}\min\bigl\{|f(n-1)|^2, |(2-\theta)f(n)-(1-\theta)f(n-1)|^2\bigr\}.
\tag{2}
\]
This proves the upper bound and a **global exact stability identity**. Equality in (2) requires at each integer either \(f(n-1)=0\) or \(f(n)=\rho f(n-1)\), where \(0<\rho<1\). If a nonzero \(\ell^2\) solution had no first nonzero position, this recurrence propagated backward would force a nondecaying, indeed geometrically growing, left tail. Hence its nonzero support has a first point \(n_0\), and the recurrence forces all subsequent values to equal \(f(n_0)\rho^{n-n_0}\), with no later zeros. Conversely this sequence makes every term in (2) vanish. Thus the upper bound is attained, and this is the full one-dimensional complex equality classification.

**Arbitrary dimension.** On nonnegative functions on \(\mathbb Z^d\) define \(M_j h=\max\{h,(1-\theta)h+\theta S_jh\}\). By the proved one-dimensional estimate and Fubini, \(\|M_j h\|_2\le\sqrt{2/(2-\theta)}\|h\|_2\) for each coordinate. Positivity and commutation of the linear averages give the pointwise majorization
\[
 \mathcal R_{\theta,d}f\le M_d\cdots M_1|f|,
\]
by induction: a positive averaging operator applied to a pointwise maximum dominates the application to any member of that maximum. Iteration proves the sharp-constant upper bound in every \(d\).

For the reverse inequality choose \(f(n_1,\ldots,n_d)=\prod_{j=1}^d\rho^{n_j}\mathbf1_{\{n_j\ge0\}}\). Every rectangular average factors coordinatewise and is nonnegative; hence \(\mathcal R_{\theta,d}f=\prod_{j=1}^d\mathcal R_{\theta,1}h(n_j)\), with \(h(n)=\rho^n\mathbf1_{n\ge0}\). Taking squared norms and using (2) proves equality and therefore sharpness.

## Verification
The standalone `CHECK.py` uses only Python's rational arithmetic to check the scalar identity and the geometric equality profile at several rational weights. It additionally checks finite truncations; these tests are supplementary, not a substitute for the all-parameter and all-dimension proof. To reproduce, run `python CHECK.py` from the extracted package directory. The proof of the full claim consists of the algebraic identity, the one-dimensional \(\ell^2\) equality argument, positivity and tensor-product sharpness, all supplied here.

## Relationship to prior work
Mirek, Szarek and Wróbel (2026) establish **dimension-free** \(\ell^p\) bounds for discrete maximal functions built from *synchronous, centered cubes*, using multiplier estimates; their full text and the distinction between their kernels and independently chosen rectangular one-/two-point choices were examined. The present operator is a different maximal family, and indeed has an exact **exponentially dimension-dependent** \(\ell^2\) norm; there is no implication either way from that dimension-free result. Ciccone, Hormozi, Madrid, Niksiński and Wróbel (2026) determine sharp norms for certain continuous positive semigroup and centered Hardy–Littlewood maximal operators; the complete inspected paper does not state the one-step weighted discrete rectangular formula or its equality classification. Earlier sharp discrete maximal-gradient work treats variations and derivatives rather than this \(\ell^2\) norm. The one-coordinate scalar identity is elementary, but its exact deficit, all equality cases, and sharp tensorized rectangular growth are the assessed combined statement. The literature searches are not a proof of priority; an unindexed or earlier equivalent calculation remains possible.

## Limitations
The result covers \(\ell^2\), two coordinatewise averaging choices, and \(0<\theta<1\); it is not a theorem for arbitrary windows or higher spatial averaging lengths. It does not claim a full higher-dimensional equality classification, sharp behavior for the conventional centered-cube operator, or stability under stochastic perturbations. The sharp rectangular constant is separate from known dimension-free cube results. The precise dependence on \(\theta\) follows from the specified normalization and cannot be carried over to different averaging conventions without recomputation.

## References
1. M. Mirek, T. Z. Szarek and B. Wróbel, *Dimension-free estimates for discrete maximal functions over cubes in* \(\mathbb Z^d\), arXiv:2609.24030v1 (first submitted 2026-09-21), https://arxiv.org/html/2609.24030v1.
2. V. Ciccone, M. Hormozi, J. Madrid, J. Niksiński and B. Wróbel, *On* \(L^p\) *norms of maximal operators*, arXiv:2610.10247v1 (2026-10-07), https://arxiv.org/html/2610.10247v1.
3. S.-Y. Liao, J. Madrid, E. Palsson and J. Weigt, *Sharp higher order regularity of discrete maximal functions*, arXiv:2607.10753 (2026-07-12), https://arxiv.org/abs/2607.10753.
