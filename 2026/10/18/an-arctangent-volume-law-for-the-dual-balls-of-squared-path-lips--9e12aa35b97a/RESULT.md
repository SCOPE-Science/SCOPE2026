# An arctangent volume law for the dual balls of squared-path Lipschitz-free spaces

## Finding
For every integer \(n\ge2\), let \(G_n=P_n^2\) be the square of the \(n\)-vertex path: vertices \(i,j\in\{1,\ldots,n\}\) are joined when \(1\le|i-j|\le2\). Its unit-edge shortest-path distance is \(d(i,j)=\lceil|i-j|/2\rceil\). Let \(Q_n\) denote the unit ball of the real Lipschitz dual \(\operatorname{Lip}_0(G_n)=\mathcal F(G_n)^*\), with potential \(f(1)=0\), using Lebesgue volume in the anchored coordinate chart \((f(2),\ldots,f(n))\). Set \(V_n=\operatorname{vol}_{n-1}(Q_n)\) and \(\theta=\arctan(3/4)=2\arctan(1/3)\). Then
\[
\boxed{\sum_{n=2}^{\infty}V_nz^{n-2} =\frac{4\tan(z/2)}{z\bigl(1-3\tan(z/2)\bigr)}=\frac{2(1+\sin z-\cos z)}{z(2\cos z-1-\sin z)}},\qquad |z|<\theta.
\]
The constant term is interpreted by removable continuation at zero. Equivalently, an absolutely convergent lattice sum gives **every finite-dimensional volume**:
\[
\boxed{V_n=\frac45\sum_{k\in\mathbb Z}\frac1{(\theta+2\pi k)^n}},\qquad n\ge2.
\]
In particular,
\[
\boxed{\lim_{n\to\infty}\theta^nV_n=\frac45},\qquad
V_n=\frac45\theta^{-n}+O\bigl((2\pi-\theta)^{-n}\bigr).
\]
The first five volumes, for \(n=2,3,4,5,6\), are \(2,3,14/3,29/4,169/15\), respectively.

## Assumptions and scope
All spaces, volumes, and Lipschitz functions are **real**. Unit-edge path-square metrics have no additional distance constraints beyond the graph edges. The volume is anchored-coordinate Lebesgue volume, not Euclidean volume in the ambient zero-sum hyperplane, a normalization that differs by a dimension-dependent factor. The definition applies to every integer \(n\ge2\), including the one-dimensional segment case. The limit is along these integers. The comparison to the ordinary path uses the same anchored-coordinate normalization, under which its dual unit ball has volume \(2^{n-1}\).

## Proof
**1. Unimodular increments and an integral operator.** Put \(y_i=f(i+1)-f(i)\) for \(1\le i\le n-1\). The triangular change of coordinates from anchored potentials to increments has determinant \(1\). The graph edge inequalities are precisely \(|y_i|\le1\) and \(|y_i+y_{i+1}|\le1\). On setting \(x_i=(-1)^iy_i\), the Jacobian still has absolute determinant \(1\); the constraints become \(|x_i|\le1\) and \(|x_i-x_{i+1}|\le1\). On \(L^2([-1,1])\), define the positive symmetric Hilbert–Schmidt integral operator
\[
(Th)(x)=\int_{-1}^1\mathbf1_{\{|x-y|\le1\}}h(y)\,dy.
\]
Repeated Fubini integration gives the exact finite-volume identity \(V_n=\langle\mathbf1,T^{n-2}\mathbf1\rangle\). Therefore for \(|z|\) sufficiently small,
\[\mathcal V(z):=\sum_{n\ge2}V_nz^{n-2}=\langle\mathbf1,(I-zT)^{-1}\mathbf1\rangle.\]

**2. Solve the resolvent without an unproved spectral assumption.** Write \(F=(I-zT)^{-1}\mathbf1\). The kernel is invariant under simultaneous sign reversal, so \(F\) is even. With \(I=\int_0^1F(x)\,dx\), for \(0\le x\le1\) the resolvent equation is
\[F(x)=1+z\left(I+\int_0^{1-x}F(u)\,du\right).\]
Thus \(F'(x)=-zF(1-x)\), \(F''(x)=-z^2F(x)\), and the boundary data are \(F(0)=2F(1)-1\), \(F'(0)=-zF(1)\). Solving this elementary boundary-value problem near \(z=0\), with removable singularities understood, gives
\[
F(x)=\frac{(1+\sin z)\cos(zx)-\cos z\sin(zx)}{2\cos z-1-\sin z}\quad(0\le x\le1).
\]
Integrating \(2I\) yields the displayed generating function. As both expressions are holomorphic near \(z=0\), equality holds as an identity of Taylor series.

**3. An exact lattice expression.** The elementary half-angle identity gives \(\tan(\theta/2)=1/3\). Simplification yields
\[
\mathcal V(z)=\frac2{5z}\left[\cot\left(\frac{\theta-z}{2}\right)-\cot\left(\frac\theta2\right)\right].
\]
The classical cotangent partial-fraction identity, applied to a *difference* to secure absolute convergence, is
\[
\frac12\left[\cot\left(\frac{\theta-z}{2}\right)-\cot\left(\frac\theta2\right)\right]
=\sum_{k\in\mathbb Z}\left(\frac1{\theta+2\pi k-z}-\frac1{\theta+2\pi k}\right).
\]
Consequently
\[\mathcal V(z)=\frac45\sum_{k\in\mathbb Z}\frac1{(\theta+2\pi k)(\theta+2\pi k-z)}.\]
For \(|z|<\theta\), the geometric expansions are absolutely and locally uniformly summable, so coefficient extraction at degree \(n-2\) gives the exact lattice sum. Its term \(k=0\) dominates; all remaining bases have absolute value at least \(2\pi-\theta>\theta\). Uniformly summing those tails proves the asserted error estimate and limit.

## Verification
Run the complete independent finite checker `VERIFY_VOLUME.py` with Python, SymPy, NumPy and SciPy. It computes iterated-integral volumes exactly for dimensions \(1\) through \(12\); independently enumerates all vertices and triangulates the corresponding rational polytopes in dimensions \(1\) through \(5\), with exact determinant arithmetic; compares twelve exact Taylor coefficients with the resolvent formula; checks eight coefficients against rational cotangent-derivative recurrences; and checks the boundary conditions and integrals of the positive leading eigenfunction at \(\theta\). Its finite computations corroborate the analytic proof; none is used as proof for all dimensions. SciPy chooses triangulations numerically, but exact rational determinants evaluate the selected simplices.

## Relationship to prior work
Sanyal and Stump study directed Lipschitz polytopes of posets with order-based, asymmetric constraints; these are not the symmetric edge-difference polytopes considered here. Dilworth, Kutzarova and Ostrovskii study structural properties of finite-metric Lipschitz-free spaces, and Alexander, Fradelizi, García-Lirola and Zvavitch establish finite Lipschitz-free geometric and volume-product theory. These frameworks motivate the dual-ball invariant but do not in their inspected results evaluate this graph family or the exact arctangent series. Generic transfer-operator theory gives an integral representation, not the evaluated resolvent or its coefficient formula. There is an earlier facet count for this graph family; a facet count alone does not determine these volumes. Prior literature may contain equivalent formulas under different graph-polytope terminology.

## Limitations
The theorem evaluates the **dual** Lipschitz ball of squared paths in anchored coordinates, not the primal transportation-ball volume, the Mahler product or every graph power. The asymptotic gives the leading exponential rate and an exponentially smaller error; no probabilistic limit theorem is asserted. Bibliographic novelty is a best-knowledge claim after specific comparisons, not a proof that no unpublished or unindexed equivalent exists. Independent scientific validation is not claimed.

## References
1. Raman Sanyal and Christian Stump, *Lipschitz polytopes of posets and permutation statistics*, arXiv:1703.10586v1 (first public 2017-03-30).
2. Stephen Dilworth, Denka Kutzarova and Mikhail Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (first public 2018-07-10).
3. Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola and Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (first public 2019-11-24).
