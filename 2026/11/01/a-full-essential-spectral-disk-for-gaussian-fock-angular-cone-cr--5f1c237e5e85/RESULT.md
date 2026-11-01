# A full spectral disk from angular-cone Fock commutators

## Finding

On normalized analytic Bargmann–Fock space in two complex variables, a bounded commutator between a discontinuous angular-cone Toeplitz operator and the *unbounded* coordinate-creation operator has a completely explicit spectrum and essential spectrum. For every \(0<t<1\), both spectra equal the closed disk of radius
\[
R_t=\sqrt{\frac{1-t}{2\pi}}.
\]
The essential operator norm is exactly \(R_t\), but the ordinary operator norm can be strictly greater. The operator has **no eigenvalues**, despite its full-disk spectrum. It is the orthogonal direct sum of compact quasinilpotent unilateral weighted shifts. These statements, including the exact radius and absence of point spectrum, comprise a single spectral classification.

## Assumptions and scope

Let \(\mathcal F^2(\mathbb C^2)\) be the entire functions with squared norm
\[
\|f\|^2=\frac1{\pi^2}\int_{\mathbb C^2}|f(z)|^2e^{-|z_1|^2-|z_2|^2}\,dA(z_1)dA(z_2).
\]
Its normalized monomials are \(e_{n,m}(z)=z_1^nz_2^m/\sqrt{n!m!}\) for integers \(n,m\ge0\). Write \(P\) for the Gaussian orthogonal projection. For \(t\in(0,1)\), put
\[
\Omega_t=\{z\ne0:|z_1|^2>t(|z_1|^2+|z_2|^2)\},\qquad T_t=P\,\mathbf1_{\Omega_t}|_{\mathcal F^2}.
\]
The multiplication operator \(M_{z_1}\) is unbounded, so \(C_t=[T_t,M_{z_1}]\) is **initially** defined only on the dense polynomial subspace. The theorem concerns its unique bounded extension to the whole Fock space, not an unspecified product of unbounded operators. The essential spectrum is the Fredholm essential spectrum (the Calkin-algebra spectrum).

## Proof

**1. Exact weights.** Separately radial invariance makes \(T_t\) diagonal. Under the probability density \(|e_{n,m}|^2\pi^{-2}e^{-|z|^2}\,dA(z_1)dA(z_2)\), the squared moduli \(|z_1|^2\) and \(|z_2|^2\) are independent gamma variables with shapes \(n+1\) and \(m+1\). Their ratio has the \(\operatorname{Beta}(n+1,m+1)\) distribution. Therefore
\[
T_te_{n,m}=\lambda_{n,m}e_{n,m},\quad
\lambda_{n,m}=\Pr\{\operatorname{Bin}(n+m+1,t)\le n\}.
\]
Pascal's identity gives
\[
\lambda_{n+1,m}-\lambda_{n,m}
=(1-t)\binom{n+m+1}{n+1}t^{n+1}(1-t)^m.
\]
Since \(M_{z_1}e_{n,m}=\sqrt{n+1}\,e_{n+1,m}\), the commutator equals the positive-weight shift
\[
C_te_{n,m}=w_{n,m}(t)e_{n+1,m},\quad
w_{n,m}(t)=\sqrt{n+1}(1-t)\binom{n+m+1}{n+1}t^{n+1}(1-t)^m.
\tag{1}
\]
All weights are strictly positive.

**2. Uniform binomial peak.** Set \(N=n+m+1\), \(j=n+1\), and \(p=j/N\). The right side of (1) is \((1-t)\sqrt j\) times the point mass \(\Pr\{\operatorname{Bin}(N,t)=j\}\). The binomial relative-entropy bound gives
\[
\Pr\{\operatorname{Bin}(N,t)=j\}\le e^{-N D(p\|t)},\quad
D(p\|t)=p\log\frac pt+(1-p)\log\frac{1-p}{1-t}.
\]
For any fixed \(\eta>0\), the weights with \(|p-t|\ge\eta\) tend uniformly to zero as \(N\to\infty\). In the complementary region \(|p-t|<\eta\), where \(p\) remains inside a compact subset of \((0,1)\), uniform Stirling asymptotics give
\[
w_{n,m}(t)=\frac{1-t}{\sqrt{2\pi(1-p)}}e^{-ND(p\|t)}(1+O_t(N^{-1})),
\]
with the error uniform for fixed sufficiently small \(\eta\). Since \(D\ge0\), letting \(\eta\downarrow0\) yields
\[
\limsup_{n+m\to\infty}w_{n,m}(t)\le R_t.
\]
Conversely choose \(j=\lfloor tN\rfloor\), \(n=j-1\), \(m=N-j\), along integers \(N\to\infty\); then \(ND(p\|t)\to0\), proving equality:
\[
\limsup_{n+m\to\infty}w_{n,m}(t)=R_t.
\tag{2}
\]
A stronger useful conclusion is that for every fixed integer \(k\ge1\), there are arbitrarily large \(m\) and starting indices \(n\) for which \(k\) consecutive weights \(w_{n+i,m}(t)\), \(0\le i<k\), all tend to \(R_t\). Indeed choose \(m\to\infty\) and \(n=\lfloor tm/(1-t)\rfloor\); the corresponding \(k\) ratios \(p\) differ from \(t\) by \(O_t(k/m)\), so the uniform Stirling formula applies.

Equation (2) proves the weights are bounded, hence the polynomial commutator extends uniquely to a bounded operator. Since \(C_t^*C_t\) is diagonal with entries \(w_{n,m}^2\), the distance to the compact operators equals the limsup of the weights on escaping indices. Thus
\[
\|C_t\|_{\mathrm{ess}}=R_t.
\tag{3}
\]

**3. Compact quasinilpotent fibers.** For each fixed \(m\), the subspace \(\mathcal H_m=\overline{\mathrm{span}}\{e_{n,m}:n\ge0\}\) is reducing for \(C_t\), and its restriction \(B_m\) is a unilateral weighted shift. At fixed \(m\), formula (1) gives \(w_{n,m}(t)\to0\) exponentially as \(n\to\infty\). Thus \(B_m\) is compact. A unilateral forward shift with nonzero weights has no nonzero eigenvalues; by compactness, its spectrum is exactly \(\{0\}\). In particular, every \(B_m\) is quasinilpotent.

**4. Resolvent outside the disk.** Fix \(|\lambda|>R_t\). Formula (2) and decay along fixed fibers imply
\[
\lim_{m\to\infty}\|B_m\|=R_t.
\]
Hence for all sufficiently large \(m\), \(\|B_m\|<|\lambda|\), and \(B_m-\lambda I\) has uniformly bounded inverse by a Neumann series. The finitely many remaining fibers also have bounded inverses because \(\sigma(B_m)=\{0\}\). Consequently \(C_t-\lambda I=\bigoplus_{m\ge0}(B_m-\lambda I)\) is invertible.

**5. No Fredholm points inside the disk.** Fix \(0<|\lambda|<R_t\) and choose \(\rho\) with \(|\lambda|<\rho<R_t\). For arbitrary \(k\), choose a fiber \(m\) and start \(n\) having \(k\) consecutive weights at least \(\rho\). Because \(B_m\) is quasinilpotent, its resolvent admits the norm-convergent series
\[
(B_m-\lambda I)^{-1}e_{n,m}=-\sum_{r=0}^{\infty}\lambda^{-r-1}B_m^re_{n,m}.
\]
The summands lie on pairwise orthogonal monomials, so
\[
\|(B_m-\lambda I)^{-1}e_{n,m}\|\ge\frac{\rho^k}{|\lambda|^{k+1}}.
\]
This is unbounded as \(k\to\infty\), preventing a bounded inverse of the orthogonal direct sum. Moreover \(C_t-\lambda I\) is injective and has dense range, since every block \(B_m-\lambda I\) is invertible. Were it Fredholm, its range would be closed, hence it would be bijective with bounded inverse, a contradiction. Therefore every \(0<|\lambda|<R_t\) belongs to the Fredholm essential spectrum. At \(\lambda=0\), the range is orthogonal to all \(e_{0,m}\), \(m\ge0\), so its cokernel is infinite-dimensional: zero is also non-Fredholm. Closedness of the essential spectrum adds the boundary \(|\lambda|=R_t\). Together with step 4,
\[
\boxed{\sigma(C_t)=\sigma_{\mathrm{ess}}(C_t)=\{\lambda\in\mathbb C:|\lambda|\le R_t\}.}
\]
There are no eigenvalues: the first coefficient of an eigenvector for nonzero \(\lambda\) must vanish in every fiber, and induction kills the rest; at zero, positivity of all weights implies injectivity.

**6. A norm/spectrum separation.** At \(t=4/5\), (1) gives \(w_{1,0}=16\sqrt2/125\), which strictly exceeds \(R_{4/5}=1/\sqrt{10\pi}\) (equivalently \(\pi>15625/5120\)). Consequently \(\|C_{4/5}\|>\|C_{4/5}\|_{\mathrm{ess}}=r(C_{4/5})\). This distinguishes the essential spectral radius from the operator norm without requiring a formula for the latter.

## Verification

The standalone Python program `CHECK.py` checks beta/binomial identities exactly over a finite rational grid, checks the coordinate-shift formula, compares the predicted local-binomial peak to large finite fibers, and verifies the strict norm/spectral separation at \(t=4/5\). The infinite-dimensional statements are proved above, not inferred from finite computations. Run: `python3 CHECK.py`.

## Relationship to prior work

Dewage and Ólafsson (arXiv:2107.01465, first posted July 3, 2021) provide the general quasi-radial Fock Toeplitz diagonalization; that diagonalization is prior work, not claimed here. Wu and Zheng (arXiv:2103.03458) and Hagger (arXiv:2002.02344) study general Fock Toeplitz boundedness/algebras rather than the particular creation commutator's Fredholm spectrum. Dong's 2020 monomial-type Fock Toeplitz commutator article concerns finite-rank classifications for a different symbol family; full text was inaccessible at the time of comparison. At the bisector \(t=1/2\), sharp norm and finite-degree concentration trace formulas by themselves do not determine the spectral disk or point spectrum. A weighted-Bergman angular-cone result concerns a *compact* commutator with bounded coordinate multiplication and does not imply the present Fock noncompact spectral conclusion.

## Limitations

The theorem applies only to the indicated homogeneous angular cone, Gaussian Fock normalization and the first coordinate creation operator. It does not give the exact ordinary norm for arbitrary \(t\), spectral multiplicity in a functional calculus, or a result for different radial weights. A mathematically equivalent earlier theorem about direct sums of binomially weighted shifts remains a residual historical-priority risk. Full-text comparison with Dong (2020) could not be completed; its available abstract concerns different monomial-type symbols, so no claim of whole-document noncoverage is made. No independent mathematical audit has been performed.

## References

1. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first publicly posted 2021-07-03), https://arxiv.org/abs/2107.01465.
2. S. Wu and D. Zheng, *Toeplitz operators on the Fock space via the Fourier transform*, arXiv:2103.03458 (2021), https://arxiv.org/abs/2103.03458.
3. R. Hagger, *Essential commutants and characterizations of the Toeplitz algebra*, arXiv:2002.02344 (2020), https://arxiv.org/abs/2002.02344.
4. X.-T. Dong, *Commutators and Semi-Commutators of Toeplitz Operators on the Fock Space*, Indian J. Pure Appl. Math. **51** (2020), 195–215, DOI:10.1007/s13226-020-0395-7.
