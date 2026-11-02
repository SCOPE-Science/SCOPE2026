# Sharp positivity of Crank–Nicolson diffusion on reflecting rectangular grids

## Finding

For integers \(m,n\ge 2\), let \(L_{m,n}\) be the unit-conductance graph Laplacian of the Cartesian product \(P_m\square P_n\), with the ordinary reflecting/no-flux graph boundary convention. Define the Crank–Nicolson end-step matrix
\[
C_{m,n}(s)=(I+sL_{m,n})^{-1}(I-sL_{m,n}),\qquad s\ge0.
\]
There exists a unique \(\sigma_{m,n}>0\) for which
\[
C_{m,n}(s)\text{ is entrywise nonnegative}
\quad\Longleftrightarrow\quad 0\le s\le\sigma_{m,n}.
\]
The first negative entries for \(s>\sigma_{m,n}\) lie precisely on the central vertex or central two/four vertices (depending on the two grid parities), and every off-diagonal entry is strictly positive for \(s>0\).

Set \(i_r=\lfloor(r+1)/2\rfloor\) for \(r\ge2\), and introduce
\[
\lambda_{r,k}=2-2\cos\frac{\pi k}{r},\qquad
\omega_{r,0}=\frac1r,\qquad
\omega_{r,k}=\frac2r\cos^2\!\left(\frac{\pi k(i_r-\tfrac12)}r\right)
\quad(1\le k<r).
\]
Then \(\sigma_{m,n}\) is exactly the unique positive solution of the finite, explicit equation
\[
\boxed{\quad
\sum_{k=0}^{m-1}\sum_{\ell=0}^{n-1}
\frac{\omega_{m,k}\omega_{n,\ell}}
{1+s(\lambda_{m,k}+\lambda_{n,\ell})}=\frac12.\quad}
\]
This is an all-rectangle characterization, not a continuum approximation or a sufficient-only time-step bound.

Every finite rectangular threshold strictly exceeds the universal square-lattice value \(s_\infty\), defined by
\[
\boxed{\quad
\frac{2}{\pi(1+4s_\infty)}
K\!\left(\frac{4s_\infty}{1+4s_\infty}\right)=\frac12,\qquad
s_\infty=0.29409864184281405742956633757\ldots.\quad}
\]
Here \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\) is the complete elliptic integral with *modulus* \(k\), not elliptic parameter \(k^2\). As \(m,n\to\infty\), \(\sigma_{m,n}\to s_\infty\). Thus the largest single time step guaranteed to preserve every nonnegative initial grid vector, uniformly over all finite reflecting rectangles, obeys
\[
\boxed{\quad\frac{\kappa\Delta t}{\Delta x^2}\le 2s_\infty
=0.58819728368562811485913267514\ldots\quad}
\]
for the cell-centered equal-spacing semidiscretization \(\dot u=-\kappa L_{m,n}u/\Delta x^2\). The classical sufficient restriction \(\kappa\Delta t/\Delta x^2\le1/2\) is strictly conservative for this model.

There is also an exact parity-sensitive leading finite-size law for squares. Let
\[
\xi=\operatorname{arcosh}\!\left(1+\frac1{2s_\infty}\right),\quad
G(s)=\frac{2}{\pi(1+4s)}K\!\left(\frac{4s}{1+4s}\right),\quad
D=-G'(s_\infty)>0,
\]
\[
A_{\rm odd}=\frac{2}{s_\infty D\sqrt{2\pi\sinh\xi}},\qquad
A_{\rm even}=A_{\rm odd}\cosh\xi.
\]
Then, as \(n\to\infty\) along each parity,
\[
\boxed{\quad
\sigma_{n,n}=s_\infty+\frac{e^{-\xi n}}{\sqrt n}
\begin{cases}
A_{\rm odd}[1+O(n^{-1})],&n\text{ odd},\\
A_{\rm even}[1+O(n^{-1})],&n\text{ even}.
\end{cases}\quad}
\]
Numerically, \(\xi=1.65023725689972312979\ldots\), \(A_{\rm odd}=2.2402178430620431044\ldots\) and \(A_{\rm even}=6.0488342804330205494\ldots\). The even-square excess is asymptotically \(\cosh\xi=2.700109857247261\ldots\) times the odd-square excess, after removing the common exponential and square-root factors.

## Assumptions and scope

The path \(P_r\) consists of \(r\) vertices and \(r-1\) unit-weight edges. The Laplacian \(L_r\) has degree one at the endpoints and degree two at interior vertices; the product Laplacian is \(L_{m,n}=L_m\otimes I_n+I_m\otimes L_n\). All grids have \(m,n\ge2\), and the complete matrix \(C_{m,n}(s)\) acts on *all* grid values, including the reflecting boundary. This is not the five-point stencil with prescribed zero boundary values, and no anisotropic weights are allowed in this theorem.

The row and column sums of \(C_{m,n}(s)\) equal one. Hence its entrywise nonnegativity is equivalent to preservation of nonnegative initial vectors and to the maximum/minimum principle for one full step. Only the end-step map, not internal stages of an implementation, is considered. \(s\) includes *half* the physical time-step factor in the displayed physical scaling.

The finite exact characterization concerns every rectangle. The explicit parity asymptotic concerns squares with both dimensions \(n\to\infty\); it does not assert the same constants for long thin strips. All statements are in exact arithmetic.

## Proof

**1. The problem reduces to diagonal resolvent entries.** Define \(R_s=(I+sL_{m,n})^{-1}\). For \(s>0\), \(I+sL_{m,n}\) is an irreducible nonsingular \(M\)-matrix. Thus every entry of \(R_s\) is strictly positive, and \(R_s\mathbf1=\mathbf1\). The elementary resolvent identity gives
\[
C_{m,n}(s)=2R_s-I.
\]
Every off-diagonal entry of \(C_{m,n}(s)\) is strictly positive, and all possible sign failures are on the diagonal. Consequently
\[
C_{m,n}(s)\ge0\quad\Longleftrightarrow\quad
\min_v(R_s)_{vv}\ge\frac12.
\]
This general criterion is established prior work; the contribution below identifies the minimizing grid sites, the exact finite root, and its sharp two-dimensional finite-size behavior.

**2. The diagonal minimum occurs exactly at the center.** For any path length \(r\), the diagonal heat kernel has the reflection identity
\[
(e^{-tL_r})_{ii}=q_t^{(2r)}(0)+q_t^{(2r)}(2i-1),\qquad t>0,
\]
where \(q_t^{(2r)}(a)\) is the transition kernel of continuous-time unit-rate nearest-neighbor diffusion on the cycle of length \(2r\), with offsets taken modulo \(2r\). To see strict spatial monotonicity of the cycle return, write \(q_j=q_t^{(2r)}(j)\) and \(d_j=q_j-q_{j+1}\) for \(0\le j<r\). The symmetry \(q_j=q_{2r-j}\) and the heat equation give
\[
\dot d_0=-3d_0+d_1,\qquad
\dot d_j=d_{j-1}-2d_j+d_{j+1}\ (1\le j<r-1),\qquad
\dot d_{r-1}=d_{r-2}-3d_{r-1}.
\]
At \(t=0\), \(d_0=1\) and the other differences vanish. This system is generated by an irreducible Metzler matrix, so \(d_j(t)>0\) for all \(j\) and all \(t>0\). Hence \(q_0>q_1>\cdots>q_r\). The two central path sites (one if \(r\) odd) uniquely minimize the heat-kernel diagonal, with precisely the symmetry-implied ties.

The product heat semigroup factorizes, and its diagonal at \((i,j)\) is
\[
(e^{-tL_{m,n}})_{(i,j),(i,j)}=
(e^{-tL_m})_{ii}(e^{-tL_n})_{jj}.
\]
Both factors are strictly positive. Therefore the diagonal is smallest exactly at the Cartesian combinations of the central path positions for every \(t>0\). The resolvent has the Laplace representation
\[
R_s=\int_0^\infty e^{-u}e^{-suL_{m,n}}\,du,
\]
which preserves this strict ordering. Thus precisely the central grid positions minimize \((R_s)_{vv}\).

**3. The finite characteristic equation and its unique root.** The normalized eigenvectors of \(L_r\) can be chosen as
\[
\phi_{r,0}(i)=r^{-1/2},\qquad
\phi_{r,k}(i)=\sqrt{2/r}\cos\left(\frac{\pi k(i-\tfrac12)}r\right)
\quad(1\le k<r),
\]
with eigenvalues \(\lambda_{r,k}\). The square weights at the center are precisely \(\omega_{r,k}\) displayed above. Product diagonalization yields the double sum for the central \(R_s\) diagonal. Its derivative is strictly negative, because some nonzero eigenvalue has nonzero central spectral mass. The diagonal decreases continuously from \(1\) at \(s=0\) to \(1/(mn)<1/2\) at infinity. Thus there is a unique positive crossing, proving the full finite classification and central first sign loss.

**4. The exact square-lattice limit.** Let \(p_t(x)\) be the continuous-time nearest-neighbor heat kernel on \(\mathbb Z\). The same reflection identity in image form is
\[
(e^{-tL_r})_{ii}=
\sum_{j\in\mathbb Z}\left[p_t(2rj)+p_t(2i-1+2rj)\right].
\]
Each summand is nonnegative, and the \(j=0\) term \(p_t(0)\) in the first bracket is the infinite-line return probability. At the central path positions, as \(r\to\infty\), the additional image terms vanish for fixed \(t\). Dominated convergence in the Laplace resolvent gives the two-dimensional limit
\[
G(s)=\frac1{(2\pi)^2}\int_{-\pi}^\pi\!\int_{-\pi}^\pi
\frac{d\theta\,d\varphi}
{1+s(4-2\cos\theta-2\cos\varphi)}.
\]
The classical square-lattice Green-integral evaluation gives the stated complete-elliptic-integral expression; it follows alternatively by first integrating one angle and applying the standard reduction to \(K\). Its derivative is strictly negative, \(G(0)=1\), and \(G(s)\to0\) as \(s\to\infty\). Hence its unique level-\(1/2\) root is \(s_\infty\). At every finite center the image sum contains strictly positive nonzero images for \(s>0\), so the finite diagonal is strictly greater than \(G(s)\). In particular \(\sigma_{m,n}>s_\infty\) for all finite rectangles. Since the central finite resolvents converge to \(G\), their unique crossings converge to \(s_\infty\) as both side lengths tend to infinity.

**5. Sharp square finite-size asymptotics.** Define the massive square-lattice Green kernel
\[
g_s(a,b)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
\frac{e^{i(a\theta+b\varphi)}}{1+s(4-2\cos\theta-2\cos\varphi)}\,d\theta\,d\varphi.
\]
It is strictly positive, and \(g_s(0,0)=G(s)\). Integrating one angular variable first gives, for integer \(r\ge0\),
\[
g_s(r,0)=\frac1{2\pi}\int_{-\pi}^{\pi}
\frac{\exp[-r\eta_s(\varphi)]}{2s\sinh\eta_s(\varphi)}\,d\varphi,
\quad
\eta_s(\varphi)=\operatorname{arcosh}\left(2+\frac1{2s}-\cos\varphi\right).
\]
This positive phase has its unique nondegenerate minimum at \(\varphi=0\), equal to \(\xi(s)=\operatorname{arcosh}(1+1/(2s))\), with \(\eta_s''(0)=1/\sinh\xi(s)\). One-dimensional Laplace asymptotics, uniformly for \(s\) in a compact neighborhood of \(s_\infty\), therefore gives
\[
g_s(r,0)=\frac{e^{-r\xi(s)}}{2s\sqrt{2\pi r\sinh\xi(s)}}
\left[1+O(r^{-1})\right].
\]

For a central point of \(P_n\), its nearest nonzero one-dimensional reflection images have offsets \(\pm n\) when \(n\) is odd, and offsets \(n-1\) and \(-(n+1)\) when \(n\) is even. The two-dimensional product image sum therefore shows
\[
G_{n,n}(s)-G(s)=
\begin{cases}
4g_s(n,0)[1+O(n^{-1})],&n\text{ odd},\\
2\{g_s(n-1,0)+g_s(n+1,0)\}[1+O(n^{-1})],&n\text{ even}.
\end{cases}
\]
To control all omitted images rigorously, take a parameter \(\alpha\) satisfying
\[
\tfrac12\xi(s)<\alpha<\operatorname{arcosh}\left(1+\frac1{4s}\right).
\]
Such a choice exists because doubling the right-hand inverse hyperbolic cosine strictly exceeds \(\xi(s)\). A positive exponential-moment bound for the lattice resolvent then gives \(g_s(a,b)\le M_\alpha e^{-\alpha(|a|+|b|)}\). Every remaining image has Manhattan distance at least \(2n-O(1)\), so their total is \(O(e^{-2\alpha n})=o(e^{-\xi(s)n}/n^{3/2})\). This justifies the relative \(O(n^{-1})\) remainder above. For even \(n\), comparison of the two axis terms with \(g_s(n,0)\) yields the multiplicative factor \(2\cosh\xi(s)\); the odd case yields factor \(4\) directly.

Finally \(G(s_\infty)=1/2\), \(D=-G'(s_\infty)>0\), and the implicit crossing equation \(G_{n,n}(\sigma_{n,n})=1/2\) gives
\[
\sigma_{n,n}-s_\infty
=\frac{G_{n,n}(s_\infty)-G(s_\infty)}{D}
\left[1+o(n^{-1})\right]
\]
(the root shift is exponentially small, so derivative perturbations and quadratic terms are negligible compared with the displayed \(n^{-1}\) relative accuracy). Substitution of the Laplace asymptotics gives the stated coefficients and completes the proof.

## Verification

The standalone `artifacts/verify.py` uses exact rational linear algebra to check the full amplification and inverse matrices on small rectangles, including the identity \(C=2R-I\), stochastic row sums, strict positivity of all off-diagonal entries, and central diagonal minimizers. It independently compares the finite spectral roots with full-matrix sign changes on further rectangles, checks the elliptic Green formula against independent one-angle quadrature, and tests both odd and even finite-size laws at high precision up to side length eighteen. The extracted program returned **2806 passed checks**. The plaintext output in `artifacts/verification.txt` records numerical roots and normalized asymptotic ratios. These experiments only supplement the proof of all-size and asymptotic statements.

For exact reproduction, run `python artifacts/verify.py` with Python 3, `sympy` and `mpmath`. Decimal values above are numerical evaluations of explicitly defined analytic constants, not unproved rational bounds or certification of independent mathematical review.

## Relationship to prior work

Faragó and Horváth (2006) establish the equivalence of nonnegativity and discrete maximum-principle properties for parabolic time-stepping, and their Theorem 6.2 and Remark 6.3 give the **sufficient** \(d\)-dimensional finite-difference Crank–Nicolson step-size restriction. Their paper treats Dirichlet-type conditions and does not give the present sharp all-rectangle reflecting-graph threshold, center-first violation, elliptic limit, or parity-sensitive correction. The source's full-text statements in Sections 5–7, especially Theorem 6.2 and Remark 6.3, were compared directly. The general resolvent identity for Markov-chain Crank–Nicolson positivity, including its diagonal-return criterion, is likewise prior work and is explicitly used in Step 1 rather than claimed as new.

Kraaijevanger (1992) studies maximum-norm contractivity of heat discretizations, and Sun (2009) and Gao–Sun (2012 first public) develop different compact methods for Neumann heat problems. Higueras–Roldán (2023) give sharp finite-grid one-dimensional Dirichlet Crank–Nicolson positivity results. The latter was inspected as an open full-text preprint; its Dirichlet domain, spatial matrix and one-dimensional asymptotics are not the two-dimensional reflecting product analyzed here. Morita's square-lattice Green formula is classical, as is the Laplace-method decay of massive lattice resolvents; neither fact in isolation is claimed as new. The assessed contribution is their combination into the exact sharp finite reflecting-grid positivity theorem and the explicit parity-sensitive exponentially small square correction, not the general Cayley identity, elliptic integral, or Fourier diagonalization separately.

## Limitations

The theorem concerns unit-weight, equal-spacing, graph-reflecting finite-volume grids with no prescribed Dirichlet boundary data, and positivity of a *single* exact Crank–Nicolson end step. It says nothing about variable diffusion, other boundary closures, anisotropic spacing, internal Runge–Kutta stages, nonlinear limiters, or how quickly negative values emerge over many steps. Finite arithmetic tests and numeric root approximations are not replacements for the all-size proof. Priority could be affected by less accessible specialist work on sharp Neumann heat positivity, especially compact-scheme and maximum-norm references; a distinct full-text bibliographic audit remains useful. No independent mathematical audit has been performed.

## References

1. I. Faragó and R. Horváth, “Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems,” *SIAM Journal on Scientific Computing* **28** (2006), 2313–2336, published online 21 December 2006, https://doi.org/10.1137/050627241.
2. J. F. B. M. Kraaijevanger, “Maximum norm contractivity of discretization schemes for the heat equation,” *Applied Numerical Mathematics* **9** (1992), 475–492.
3. Z.-Z. Sun, “Compact difference schemes for heat equation with Neumann boundary conditions,” *Numerical Methods for Partial Differential Equations* **25** (2009), 1320–1341, first published 7 January 2009, https://doi.org/10.1002/num.20402.
4. G.-H. Gao and Z.-Z. Sun, “Compact difference schemes for heat equation with Neumann boundary conditions (II),” *Numerical Methods for Partial Differential Equations* **29** (2013), 1459–1486, first published 18 December 2012, https://doi.org/10.1002/num.21760.
5. I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066 (2023), https://arxiv.org/abs/2301.01066.
6. T. Morita, “Useful Procedure for Computing the Lattice Green's Function—Square, Tetragonal, and bcc Lattices,” *Journal of Mathematical Physics* **12** (1971), 1744–1747, https://doi.org/10.1063/1.1665800.
7. “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains,” online research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
