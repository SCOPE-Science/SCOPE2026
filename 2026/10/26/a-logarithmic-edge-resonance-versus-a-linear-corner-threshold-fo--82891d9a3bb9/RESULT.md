# A logarithmic edge resonance versus a linear corner threshold for square-lattice point defects

## Finding
Consider a single attractive site in a discrete Dirichlet square-lattice half-plane or quadrant. Although both geometries have a positive coupling threshold for a negative bound state, **their threshold states and the manner in which binding begins are different**. At a half-plane site of fixed depth \(j\geq1\), the critical state is not square-summable and the energy gap \(\varepsilon\) obeys a logarithmically suppressed law,
\[
\varepsilon\log(1/\varepsilon)\sim\frac{4\pi F_{H,j}^{2}}{j^{2}}(\lambda-\lambda_{H,j}).
\]
At any fixed quadrant site \((a,b)\in\mathbb N^{2}\), the critical state is an actual square-summable eigenfunction and the binding gap is linear,
\[
\varepsilon\sim\frac{F_{Q,a,b}^{2}}{B_{a,b}}(\lambda-\lambda_{Q,a,b}).
\]
All limits approach their respective critical coupling from above, with each site held fixed. The positive constants \(F_{H,j}\), \(F_{Q,a,b}\), and \(B_{a,b}\) are given explicitly by convergent Brillouin-zone integrals below. Thus the two-Dirichlet-wall corner changes the threshold spectral type **and** the order of eigenvalue detachment, not merely the critical coupling.

## Assumptions and scope
Let \(H=\mathbb Z\times\mathbb N\) and \(Q=\mathbb N^{2}\), where \(\mathbb N=\{1,2,\dots\}\). Define \(L_X\) on \(\ell^2(X)\) by \((L_X f)(u)=4f(u)-\sum_{v\in X:|u-v|_1=1}f(v)\). The diagonal remains **four** at boundary sites: this is the Dirichlet restriction of the full-plane positive lattice Laplacian, not the degree-normalized graph Laplacian. Its essential spectrum is \([0,8]\). At a specified site \(u\) set \(L_{X,u}(\lambda)=L_X-\lambda|\delta_u\rangle\langle\delta_u|\), \(\lambda>0\). We consider negative eigenenergies \(-\varepsilon\), \(\varepsilon>0\), and the bottom-of-band threshold \(0\).

Write \(\omega(k_1,k_2)=4-2\cos k_1-2\cos k_2\) and \(\langle f\rangle=(2\pi)^{-2}\int_{[-\pi,\pi]^2}f(k)\,dk\). Define, for every \(j,a,b\in\mathbb N\),
\[
N_{H,j}(k)=1-\cos(2jk_2),\qquad
N_{Q,a,b}(k)=(1-\cos(2ak_1))(1-\cos(2bk_2)),
\]
\[
F_{H,j}(\varepsilon)=\left\langle\frac{N_{H,j}}{\omega+\varepsilon}\right\rangle,\quad
F_{Q,a,b}(\varepsilon)=\left\langle\frac{N_{Q,a,b}}{\omega+\varepsilon}\right\rangle,
\quad F_{X,u}=F_{X,u}(0),
\]
\[
B_{a,b}=\left\langle\frac{N_{Q,a,b}}{\omega^2}\right\rangle,
\qquad \lambda_{H,j}=F_{H,j}^{-1},\quad \lambda_{Q,a,b}=F_{Q,a,b}^{-1}.
\]
At the isolated removable point \(k=0\), these integrands are understood almost everywhere. Both \(F\) values and \(B\) are finite and strictly positive; \(B\) is **not** defined for half-plane sites, where its analogue diverges.

**Precise claim.** For every fixed listed site, there is exactly one negative simple eigenvalue when \(\lambda>\lambda_{X,u}\) and no negative eigenvalue when \(0<\lambda\leq\lambda_{X,u}\). At equality, the canonical threshold solution of \(L_{X,u}(\lambda)\psi=0\) is a nonzero \(\ell^2\) eigenfunction for \(X=Q\), whereas on \(X=H\) that canonical solution is not in \(\ell^2\); in fact there is no nonzero \(\ell^2\) zero mode there. The two asymptotic laws in the Finding hold, with \(\varepsilon\) denoting the absolute value of the unique negative eigenenergy. The quadrant eigenfunction has multiplicity one. The result makes no claim about a joint limit as the site moves to infinity, nonlinear impurities, fractional hoppings, or scattering resonances obtained by analytic continuation.

For the nearest edge site \(j=1\), \(F_{H,1}=1-2/\pi\), giving \(\lambda_{H,1}\simeq2.7519383939\) and logarithmic coefficient \(4\pi F_{H,1}^{2}\simeq1.6593287933\). At \((a,b)=(1,1)\), numerical quadrature yields \(F_{Q,1,1}\simeq0.302347273686\), \(B_{1,1}\simeq0.136619772\), critical coupling \(\lambda_{Q,1,1}\simeq3.3074549931\), and linear coefficient approximately \(0.66911160\). These approximate numbers are illustrations, not additional claims of rigorous numerical enclosures.

## Proof
**1. Reduction to the diagonal Green function.** The horizontal Fourier transform and vertical sine transform diagonalize \(L_H\); a product of two sine transforms diagonalizes \(L_Q\). Directly normalizing the transforms of a point mass gives exactly the two integrals \(F_{H,j}(\varepsilon)\) and \(F_{Q,a,b}(\varepsilon)\) above. Equivalently they are the reflected full-lattice Green function differences: one image subtraction for \(H\) and the four-image inclusion-exclusion for \(Q\). The corresponding free operators have spectrum \([0,8]\), no free zero eigenvector, and nonnegative quadratic forms. Rank-one Birman–Schwinger says that \(-\varepsilon<0\) is an eigenvalue exactly when \(\lambda F_{X,u}(\varepsilon)=1\). Because \(F_{X,u}(\varepsilon)\) is continuous and strictly decreasing from \(F_{X,u}>0\) to zero, the asserted strict threshold and simplicity follow.

**2. Boundary vanishing and finiteness.** As \(k\to0\), \(\omega(k)=|k|_2^2+O(|k|_2^4)\), \(N_{H,j}(k)=2j^2k_2^2+O(|k|_2^4)\), and \(N_{Q,a,b}(k)=4a^2b^2k_1^2k_2^2+O(|k|_2^6)\). Thus \(N/\omega\) is locally integrable in both cases. Moreover \(N_{Q,a,b}/\omega^2\) is bounded around the origin and hence integrable, whereas the leading angular average of \(N_{H,j}/\omega^2\) is of order \(|k|_2^{-2}\) and has a logarithmically divergent integral. This proves the stated finiteness and divergence assertions.

**3. The critical threshold vector.** In the unitary sine/Fourier representation, the canonical formal solution \(\psi=L_X^{-1}\delta_u\) has amplitude \(\widehat\delta_u(k)/\omega(k)\); it is understood by this explicit spectral formula, not by treating the unbounded inverse as defined everywhere. Its value at the impurity is the finite integral \(\psi(u)=F_{X,u}\). Consequently \((L_X-\lambda_{X,u}|\delta_u\rangle\langle\delta_u|)\psi=0\), first distributionally and pointwise. Plancherel gives \(\|\psi\|_2^2=\langle N_{X,u}/\omega^2\rangle\), finite precisely in the quadrant. If \(\varphi\in\ell^2(X)\) is any zero mode at criticality, then \(L_X\varphi=\lambda_{X,u}\varphi(u)\delta_u\). Since \(\ker L_X=\{0\}\), \(\varphi(u)\neq0\) and \(\varphi\) must coincide, up to scaling, with the displayed transform \(\widehat\delta_u/\omega\). Therefore the half-plane has no critical \(\ell^2\) zero eigenfunction, and the quadrant has exactly a one-dimensional critical zero eigenspace.

**4. The half-plane logarithm and its coefficient.** Subtracting the two Green integrals gives
\[
F_{H,j}(0)-F_{H,j}(\varepsilon)=\varepsilon\left\langle\frac{N_{H,j}}{\omega(\omega+\varepsilon)}\right\rangle.
\]
Split the torus into a small disk and its complement. The complementary contribution is \(O(\varepsilon)\). In the disk, replace \(N_{H,j}\) by \(2j^2k_2^2\) and \(\omega\) by \(|k|_2^2\); Taylor estimates bound the induced error by \(O(\varepsilon)\) for fixed \(j\). The leading polar integral is
\[
\frac{2j^2\varepsilon}{(2\pi)^2}\int_0^{2\pi}\!\sin^2\theta\,d\theta\int_0^\eta\!\frac{r\,dr}{r^2+\varepsilon}
=\frac{j^2}{4\pi}\varepsilon\log(1/\varepsilon)+O_j(\varepsilon).
\]
The \(O_j(\varepsilon)\) statement uses fixed \(\eta>0\) and the rest of the torus. Thus the logarithmic coefficient is exact.

**5. The quadrant derivative and matching to coupling.** By dominated convergence using \(N_{Q,a,b}/\omega^2\in L^1\),
\[
F_{Q,a,b}(0)-F_{Q,a,b}(\varepsilon)=\varepsilon B_{a,b}+o(\varepsilon).
\]
In either geometry, with \(\delta\lambda=\lambda-\lambda_{X,u}\downarrow0\), the secular equation implies
\[
F_{X,u}(0)-F_{X,u}(\varepsilon)=F_{X,u}^2\,\delta\lambda+o(\delta\lambda).
\]
Inverting the respective strictly increasing left-side differences yields the two asserted detachment laws. In particular, the half-plane energy is \(o(\delta\lambda)\) while the quadrant energy is asymptotically a positive multiple of \(\delta\lambda\), so the distinction cannot be erased by a different finite positive energy or coupling normalization.

## Verification
The accompanying `verify.py` uses only the Python standard library. It computes midpoint approximations to both Brillouin-zone integrals, a separate one-dimensional reduction of the edge Green function, and the corner derivative check. A working run checks the critical constants near the first edge and corner sites and that the corner finite difference approaches its derivative. Its finite numerical tests corroborate but do not replace the analytic proof. The equality \(F_{H,1}=1-2/\pi\) follows by integrating the horizontal Fourier variable and then setting \(t=\sin(k_2/2)\): the residual integral becomes \((2/\pi)\int_0^1\sqrt{(1-s)/(1+s)}\,ds=1-2/\pi\).

## Relationship to prior work
Molina's 2006 analysis supplies the foundational reflected Green-function formula and discusses bound-state thresholds for generalized surface impurities, explicitly including edges and corners. Its rank-one equation already supplies the existence criterion, which is **not claimed as new here**. Molina's 2021 extension analyzes a linear boundary impurity numerically in the fractional model, including the nonfractional limit. The distinction asserted here is the mathematical classification at the **critical energy itself** and the explicit inequivalent edge/corner near-threshold expansions for every fixed depth/site. Hiroshima–Muminov–Kuljanov (2018) treat a different full-lattice finite multi-delta potential and develop an abstract eigenvalue-versus-resonance distinction. Noja–Raso Stoia (2026) obtain a physically analogous geometry-dependent threshold classification for a **continuum self-adjoint point interaction**; their singular renormalized interaction and unbounded continuum domains are not the present bounded finite-rank lattice perturbation. Thus the broad geometrical mechanism is related prior knowledge, not represented as a newly discovered universal phenomenon.

## Limitations
This is a mathematical discrete model, not a proof for a continuum wall or for the fractional graph Laplacian. The asymptotics hold as \(\lambda\downarrow\lambda_c\) at each **fixed** site; constants and error bounds need not be uniform if the site depth grows. The half-plane 'resonance' refers to the canonical non-\(\ell^2\) zero-energy Green-vector solution, not to an independently established meromorphic scattering pole. Existence thresholds and the reflected secular equation were previously known. The comparison with the recent continuum work and the full-lattice multi-delta literature leaves ordinary historical-priority risk for the exact discrete detachment laws; an inaccessible specialized treatment could change that assessment.

## References
1. M. I. Molina, *Nonlinear surface impurity in a semi-infinite two-dimensional square lattice: Green function approach*, arXiv:nlin/0604060, first publicly submitted 2006-04-24; Phys. Rev. B **74**, 045412 (2006), DOI 10.1103/PhysRevB.74.045412. https://arxiv.org/abs/nlin/0604060
2. M. I. Molina, *Fractional nonlinear surface impurity in a 2D lattice*, arXiv:2112.04308, first submitted 2021-12-08. https://arxiv.org/abs/2112.04308
3. F. Hiroshima, Z. Muminov, U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on n-dimensional lattice*, arXiv:1804.05339, first submitted 2018-04-15. https://arxiv.org/html/1804.05339v1
4. D. Noja and F. Raso Stoia, *The Dirichlet Laplacian with a point interaction on unbounded Lipschitz domains*, arXiv:2607.04349, first submitted 2026-07-05. https://arxiv.org/abs/2607.04349
