# Exact tilted spectrum and Gaussian peak-clearance fluctuations in zigzag order polytopes

## Finding
For each integer \(m\ge1\), let the canonical alternating-fence order polytope be
\[
Z_m=\bigl\{x\in[0,1]^{2m+1}:x_{2j-1}\le x_{2j},\ x_{2j+1}\le x_{2j}\quad(1\le j\le m)\bigr\}.
\]
If \(X\) has normalized Lebesgue-uniform distribution in \(Z_m\), define the total *peak clearance*
\[
B_m=\sum_{j=1}^{m}\left(X_{2j}-\frac{X_{2j-1}+X_{2j+1}}2\right),\qquad 0\le B_m\le m.
\]
Each summand is the mean of the two nonnegative slacks at a local upper element of the fence. Let \(K_t\) be the self-adjoint integral operator on \(L^2[0,1]\) with kernel
\[
K_t(x,z)=\exp\!\left(-\frac{t(x+z)}2\right)\int_{\max(x,z)}^1e^{ty}\,dy,\qquad t\in\mathbb R.
\]
Its largest eigenvalue \(\lambda(t)>0\) is simple and is *explicitly* determined as follows:
\[
\lambda(t)=\begin{cases}
\bigl(k(t)^2+t^2/4\bigr)^{-1},&t<2,\\
1,&t=2,\\
\bigl(t^2/4-\kappa(t)^2\bigr)^{-1},&t>2,
\end{cases}
\]
where \(k(t)\in(0,\pi)\) uniquely solves \(k\cot k=t/2\), and \(\kappa(t)>0\) uniquely solves \(\kappa\coth\kappa=t/2\). In particular \(\lambda(0)=4/\pi^2\).

For every real \(t\), the exact tilted-volume identity and its pressure limit are
\[
\int_{Z_m}e^{tB_m(x)}\,dx=\langle\mathbf1,K_t^m\mathbf1\rangle,
\qquad
\lim_{m\to\infty}\frac1m\log\mathbb E[e^{tB_m}]
=\Lambda(t):=\log\frac{\lambda(t)}{\lambda(0)}.
\]
The following laws hold with explicit constants:
\[
\mu=\frac4{\pi^2},\qquad
\sigma^2=\frac{24}{\pi^4}-\frac2{\pi^2}>0,
\]
\[
\mathbb EB_m=m\mu+O(1),\quad
\operatorname{Var}(B_m)=m\sigma^2+O(1),\quad
\frac{B_m-m\mu}{\sqrt m}\ \Longrightarrow\ N(0,\sigma^2).
\]
Moreover, the bounded sequence \(B_m/m\) satisfies a full large-deviation principle at speed \(m\) with the good convex rate function
\[
I(a)=\sup_{t\in\mathbb R}\{ta-\Lambda(t)\};
\]
that is, the usual closed-set upper and open-set lower bounds hold with this rate function. The finite \(m\) transform, rather than the asymptotic mean alone, is the principal exact invariant.

## Assumptions and scope
The dimension is \(2m+1\), with coordinate inequalities exactly as displayed and ordinary ambient-coordinate Lebesgue measure. No result is asserted for different fence compositions or for Euclidean distances after a nonisometric affine transformation. The 2023 snake-matroid correspondence identifies the underlying polytopal family *up to affine equivalence*; the peak-clearance random variable is defined in the stated canonical order-polytope coordinates. All limits let the positive integer \(m\) tend to infinity. The parameter \(t\) ranges over all real values; complex parameters are only used locally about zero in the central-limit argument.

## Proof
**1. Exact tilted transfer operator.** Rename the odd coordinates \(u_0,u_1,\ldots,u_m\), and even coordinates \(v_1,\ldots,v_m\). The constraints become \(u_{j-1},u_j\le v_j\le1\) for \(1\le j\le m\); the peak-clearance statistic is \(\sum_j(v_j-(u_{j-1}+u_j)/2)\). Fubini integration over each \(v_j\) yields exactly the kernel \(K_t(u_{j-1},u_j)\), proving the \(m\)-fold operator formula, including its Lebesgue-volume normalization. In particular \(\operatorname{vol}(Z_1)=1/3\), and more generally \(\operatorname{vol}(Z_m)=\langle1,K_0^m1\rangle\).

**2. Principal eigenvalue and its boundary-value equation.** The kernel factors as a Gram integral
\[
K_t(x,z)=\int_0^1
\bigl[e^{-tx/2}{\bf1}_{x\le y}e^{ty/2}\bigr]
\bigl[e^{-tz/2}{\bf1}_{z\le y}e^{ty/2}\bigr]\,dy.
\]
Thus \(K_t\) is compact, self-adjoint, positive semidefinite, and strictly positivity-improving on nonzero nonnegative functions. By the compact positive-operator theorem, its largest eigenvalue is positive, algebraically simple, and strictly dominates in modulus the other eigenvalues. Let \(T_t=M_{e^{-t x/2}}K_tM_{e^{t x/2}}\), a boundedly similar positive integral operator. For an eigenfunction \(f\) of \(T_t\), put \(g(x)=\int_0^x f(z)\,dz\). Its eigen-equation is
\[
\lambda e^{tx}g'(x)=\int_x^1e^{ty}g(y)\,dy.
\]
Differentiation, with the endpoint conditions, gives
\[
g''+tg'+\lambda^{-1}g=0,\quad g(0)=0,\quad g'(1)=0.
\]
Writing \(u=e^{tx/2}g\) reduces this to \(u''+(\lambda^{-1}-t^2/4)u=0\), with \(u(0)=0\) and \(u'(1)=tu(1)/2\). For the strictly positive principal eigenfunction the lowest mode is \(u(x)=\sin(kx)\) if \(t<2\), the zero-frequency limit \(u(x)=x\) at \(t=2\), or \(u(x)=\sinh(\kappa x)\) if \(t>2\). Its right-end boundary condition gives the stated unique root equations and eigenvalues. Monotonicity of \(k\cot k\) from \(1\) to negative infinity on \((0,\pi)\), and of \(\kappa\coth\kappa\) from \(1\) to infinity on \((0,\infty)\), ensures uniqueness. At \(t=0\), \(k=\pi/2\).

**3. Spectral pressure and central limit.** The constant function has strictly positive inner product with the positive principal eigenfunction. Compactness and the strict spectral gap imply, for each real \(t\),
\[
\langle1,K_t^m1\rangle=\lambda(t)^m\bigl(A(t)+O(\rho_t^m)\bigr),\qquad A(t)>0,\quad0\le\rho_t<1.
\]
Analyticity of the kernel in operator norm and simplicity of the eigenvalue make \(\lambda(t)\) and \(A(t)\) analytic in a complex neighborhood of zero, with an error uniform in a smaller neighborhood. Dividing by the same expansion at \(t=0\) gives the pressure identity and an analytic cumulant expansion. Implicit differentiation of \(k\cot k=t/2\) at \(t=0\) gives
\[
k(t)=\frac\pi2-\frac{t}{\pi}-\frac{2t^2}{\pi^3}+O(t^3),\quad
\Lambda'(0)=\frac4{\pi^2},\quad
\Lambda''(0)=\frac{24}{\pi^4}-\frac2{\pi^2}.
\]
Positivity of the variance follows, for example, from \(\pi^2<12\). Differentiating the analytic cumulants establishes the mean and variance expansions. Substitute \(t=is/\sqrt m\) in the normalized characteristic function, using the linear centering, to obtain convergence to \(\exp(-\sigma^2s^2/2)\). The limiting law is therefore Gaussian.

**4. Large deviations.** The strictly simple principal eigenvalue is differentiable for every real \(t\), including the matching point \(t=2\) (analytic perturbation of the integral operator). The limiting log-moment generating function \(\Lambda\) exists for all real \(t\), and \(0\le B_m/m\le1\) gives exponential tightness. The differentiable full-domain Gärtner–Ellis theorem yields the stated full large-deviation principle and Legendre-transform rate function. No claim is made that the rate has a simpler elementary closed form.

## Verification
A standalone numerical script, `check_fence.py`, performs ten independent Nyström-versus-root principal-eigenvalue comparisons across both trigonometric and hyperbolic regimes, checks the exactly integrable one-peak moments \(\mathbb EB_1=3/8\) and \(\operatorname{Var}(B_1)=11/320\), checks three asymptotic cumulant identities, and tests six finite-dimensional transfer-operator approximations. The script, when run with Python, NumPy, and SciPy, reported `VERIFY_OK` with 22 comparisons. Quadrature approximations have explicit finite tolerances. Infinite-dimensional assertions follow from the analytic operator argument, not from these computations.

## Relationship to prior work
Benedetti, Knauer, and Valencia-Porras (arXiv:2303.10458; first submitted March 18, 2023) characterize snake matroid base polytopes as the matroid polytopes affinely equivalent to fence order polytopes. That identification and the classical volume/alternating-permutation theory of Stanley are preexisting. Shonkwiler and Theis, *Direct Sampling of Confined Polygons in Linear Time*, analyze zigzag-order-polytope sampling and prove a limiting one-coordinate/chord-length mean, implying the first-order peak-clearance mean by symmetry. The stand-alone value \(\mu=4/\pi^2\) is consequently *not* claimed as an isolated novel result. What is assessed here is the exact exponentially tilted clearance-volume transform, its explicit one-parameter principal spectral branch, the nonzero variance coefficient and central-limit theorem, and the full large-deviation rate for the total adjacent-slack observable. Their cited sources address combinatorial/Ehrhart geometry or single-coordinate sampling rather than this correlated sum's moment-generating spectrum. The literature comparison is not a proof of global novelty; classical transfer-operator work may contain an equivalent calculation under different terminology.

## Limitations
The result is coordinate-specific, not affine-invariant. It concerns only perfectly alternating odd-dimensional fences and the displayed average of incident slacks. The density of the full clearance distribution for finite \(m\) is not evaluated in elementary form. The eigenvalue branch suffices for large-deviation rates but not for an explicit elementary inversion. Matching a mean from previous work does not independently establish the variance or the Gaussian law. A related transfer-operator identity elsewhere would limit novelty; independent peer verification has not been performed. Numerical diagnostics cannot certify arbitrary dimensions or establish global originality.

## References
1. C. Benedetti, K. Knauer, J. Valencia-Porras, *On lattice path matroid polytopes: alcoved triangulations and snake decompositions* (2023 preprint; updated as *Order and Gorenstein properties for lattice path matroid polytopes*), arXiv:2303.10458, https://arxiv.org/abs/2303.10458, especially Theorem 1.1 and Section 3.
2. R. P. Stanley, *A Survey of Alternating Permutations*, arXiv:0912.4240, https://arxiv.org/abs/0912.4240; order-polytope/Euler-number connection.
3. C. Shonkwiler and K. Theis, *Direct Sampling of Confined Polygons in Linear Time*, open manuscript, https://www.math.colostate.edu/~clayton/research/papers/confined-sampling.pdf, especially the limiting coordinate/chord-length law.
4. H. H. Schaefer, *Banach Lattices and Positive Operators*, Springer, 1974; compact positive-operator spectral theory (standard background).
5. R. S. Ellis, *Entropy, Large Deviations, and Statistical Mechanics*, Springer, 1985; differentiable log-moment-generating-function large deviations (standard background).
