# The four-particle sign reversal of extreme-edge covariance under synchronous Brownian resetting

## Finding
Consider a stationary one-dimensional gas of \(N\ge2\) independent Brownian particles of diffusion coefficient \(D>0\), all simultaneously reset to the origin at the events of a Poisson process of rate \(r>0\). Let \(M_N\) and \(L_N\) be the rightmost and leftmost positions at a stationary observation time. Then
\[
\operatorname{Cov}(M_N,L_N)>0\quad(N=2,3),\qquad
\operatorname{Cov}(M_N,L_N)<0\quad(N\ge4).
\]
The transition occurs **exactly at four particles**, irrespective of the positive physical parameters. More precisely,
\[
\operatorname{Cov}(M_2,L_2)=\frac{D}{2r},\quad
\operatorname{Cov}(M_3,L_3)=\frac{2D}{r}\left(\frac9{16}-\frac{\sqrt3}{\pi}\right),
\]
\[
\operatorname{Cov}(M_4,L_4)=\frac{2D}{r}\left[-\frac3\pi+\frac9{16}
\left(1+\frac2\pi\arcsin\frac13\right)^2\right].
\]
In addition, the large-population covariance and correlation obey
\[
\operatorname{Cov}(M_N,L_N)
=-\frac{4D}{r}\left(1-\frac\pi4\right)\log N+o(\log N),
\qquad \operatorname{Corr}(M_N,L_N)\longrightarrow-1.
\]
The sign reversal is a property of the **joint opposite-edge fluctuations**; despite synchronous reset dependence, individual distinct coordinates remain uncorrelated at equal time.

## Assumptions and scope
There are exactly \(N\ge2\) particles, each carrying an independent standard Brownian motion between common resetting events, with variance \(2Dt\) over a free interval of length \(t\). Each resetting event simultaneously puts **every** coordinate at the origin; the common resetting process has a constant rate \(r>0\), independent of all Brownian motions. Observations are taken from the unique stationary distribution, not from a fixed elapsed time after initialization. No individual resets, confinement, particle interaction between resets or non-Poisson renewal protocol is included.

A stationary snapshot admits the exact representation
\[
(X_1,\ldots,X_N)\stackrel{d}=S(Z_1,\ldots,Z_N),\quad
S=\sqrt{2DT},\quad T\sim\operatorname{Exp}(r),
\]
where the \(Z_i\) are independent standard normal variables, independent of \(T\). This common-age Gaussian-mixture representation is established in the cited literature; it is not claimed here as a new result.

## Proof
**1. Covariance reduction.** Write \(A_N=\max_i Z_i\), \(B_N=\min_i Z_i\), \(a_N=\mathbb E A_N=-\mathbb E B_N\), and \(g_N=\operatorname{Cov}(A_N,B_N)\). Let \(c=1-\pi/4>0\). Direct Gamma integration gives
\[
\mathbb E S^2=\frac{2D}{r},\qquad
(\mathbb E S)^2=\frac{2D}{r}\frac\pi4.
\]
By conditioning on \(S\),
\[
\boxed{\operatorname{Cov}(M_N,L_N)
=\frac{2D}{r}\bigl[g_N-c a_N^2\bigr]
=\frac{2D}{r}\left[\mathbb E(A_NB_N)+\frac\pi4a_N^2\right].}
\tag{1}
\]
The positive \(g_N\) reflects ordinary Gaussian extreme-order dependence, whereas the negative term arises from fluctuating common diffusion age.

**2. Exact first three population sizes.** Let \(\phi\) and \(\Phi\) be the standard Gaussian density and distribution function. Integration by parts in
\(a_N=N\int_{\mathbb R} x\phi(x)\Phi(x)^{N-1}\,dx\) gives
\[
a_N=N(N-1)\int_{\mathbb R}\phi(x)^2\Phi(x)^{N-2}\,dx.
\tag{2}
\]
Thus
\[
a_2=\frac1{\sqrt\pi},\qquad a_3=\frac3{2\sqrt\pi},\qquad
a_4=\frac3{2\sqrt\pi}\left(1+\frac2\pi\arcsin\frac13\right).
\tag{3}
\]
For the last identity, normalize \(\phi^2\) to the density of a \(N(0,1/2)\) variable \(G\). Then
\(\mathbb E\Phi(G)^2=\frac14+\frac1{2\pi}\arcsin(1/3)\), by the bivariate Gaussian orthant formula, since the two differences of independent standard normals with \(G\) have correlation \(1/3\).

For \(N\ge2\), the joint density of \((B_N,A_N)\), for \(x<y\), is
\[
f_{B_N,A_N}(x,y)=N(N-1)\phi(x)\phi(y)
[\Phi(y)-\Phi(x)]^{N-2}.
\tag{4}
\]
For \(N=2\), \(A_2B_2=Z_1Z_2\) and \(\mathbb E A_2B_2=0\). For \(N=3\), use \(x\phi(x)=-\phi'(x)\) and Fubini in (4) to obtain
\[
\mathbb E(A_3B_3)=-6\int_{\mathbb R}\phi(y)^3\,dy=-\frac{\sqrt3}{\pi}.
\]
For \(N=4\), the corresponding inner integral is
\(\int_{-\infty}^y x\phi(x)[\Phi(y)-\Phi(x)]\,dx
=-\int_{-\infty}^y\phi(x)^2\,dx\), hence
\[
\mathbb E(A_4B_4)=-24\int\phi(y)^2
\left(\int_{-\infty}^y\phi(x)^2\,dx\right)dy
=-12\left(\int\phi^2\right)^2=-\frac3\pi.
\]
Substitution in (1) yields the stated exact covariances. The \(N=3\) expression is positive since \(9\pi>16\sqrt3\) (e.g. use \(\pi>25/8\) and \(\sqrt3<7/4\)). For \(N=4\), the inequality \(\arcsin(1/3)<\pi/8\) implies
\(\frac9{16}(1+\frac2\pi\arcsin(1/3))^2<225/256<3/\pi\), hence strict negativity.

**3. An all-population Gaussian extreme-covariance bound.** We establish the auxiliary inequality
\[
\boxed{0\le g_N\le\frac1N\qquad\text{for all integers }N\ge2.}
\tag{5}
\]
Let \(Z\) and \(Z'\) be independent standard Gaussian vectors, and put
\(Y_\rho=\rho Z+\sqrt{1-\rho^2}Z'\) for \(0\le\rho\le1\).
Gaussian interpolation (first for smooth max/min approximations and then by dominated convergence, using their bounded almost-everywhere gradients) gives
\[
g_N=\int_0^1\sum_{i=1}^N
\Pr\{i=\arg\max_j Z_j\ \text{and}\ i=\arg\min_j(Y_\rho)_j\}\,d\rho.
\tag{6}
\]
This proves nonnegativity. For any fixed \(\rho\in[0,1]\), the bivariate standard Gaussian pair \((U,V)\) of correlation \(\rho\) obeys
\[\Pr(U\le x,V\ge y)\le\Phi(x)\Phi(-y),\tag{7}\]
by positive Gaussian association (the two threshold events have opposite monotonicity). Conditional on the \(i\)-th correlated pair, the probability in (6) is at most
\[\mathbb E\left[\Phi(Z_i)^{N-1}\Phi(-(Y_\rho)_i)^{N-1}\right]\le
\mathbb E\Phi(Z_i)^{N-1}\,\mathbb E\Phi(-(Y_\rho)_i)^{N-1}=N^{-2}.\]
The second inequality uses the same opposite-monotonicity Gaussian covariance inequality; each marginal expectation equals \(1/N\) by the probability-integral transform. Summing over the \(N\) choices of index and integrating proves (5).

**4. Strict negativity for every larger population.** The Gaussian maximum means \(a_N\) are nondecreasing in \(N\). Equation (3) shows \(a_4>20/(11\sqrt{22/7})>1\) (use \(\pi<22/7\) and \(\arcsin(1/3)>1/3\)). Also \(c=1-\pi/4>1/5\), using \(\pi<16/5\). For each \(N\ge5\), therefore,
\[
g_N\le\frac1N\le\frac15<c a_4^2\le c a_N^2.
\]
Equation (1) now proves strict negativity for all \(N\ge5\), completing the sharp finite-population classification.

**5. Large-population behavior.** Standard Gaussian tail bounds show
\(a_N/\sqrt{2\log N}\to1\). The Gaussian Poincaré inequality yields
\(\operatorname{Var}(A_N)\le1\) because the maximum map is 1-Lipschitz. Combining this with (5) and (1) gives the covariance asymptotic. Moreover, symmetry and the same scale-mixture calculation give
\[
\operatorname{Var}(M_N)=\operatorname{Var}(L_N)
=\frac{2D}{r}\left[\operatorname{Var}(A_N)+c a_N^2\right].
\]
The \(O(1)\) Gaussian-extreme variance and \(O(1/N)\) Gaussian max-min covariance are negligible against \(c a_N^2\sim2c\log N\); their covariance/variance ratio therefore tends to \(-1\), as claimed.

## Verification
The included standard-library script `verify.py` reconstructs the Gaussian extreme means and max-min products through independent deterministic one- and two-dimensional quadrature, checks the exact formulas for \(N=2,3,4\), and tests the resulting signs and the Gaussian-covariance bound for \(2\le N\le8\). Run `python3 verify.py` alongside this file. These finite computations are diagnostic and do **not** replace the analytic all-\(N\) bound (5), the exact integral evaluations or the limit argument.

## Relationship to prior work
Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563) derive this model's stationary common-reset Gaussian mixture, one-sided ordered-position distributions, and adjacent-particle spacings. Their 2023 follow-up arXiv:2307.15351 develops a general conditionally i.i.d. framework and its marginal extreme laws. De Mauro and collaborators (arXiv:2509.06658) extend the framework to general renewal-time distributions and treat marginal extreme and gap statistics. The new claim here is **not** the Gaussian mixture, a marginal maximum distribution, or an adjacent gap: it is the *sign and asymptotic strength of the covariance of the two opposite extremes at the same observation time*, with a sharp four-particle boundary. None of the inspected source sections provided this finite-population sign classification or its uniform Gaussian bound. General joint-density formulas make this covariance computable in principle but do not themselves settle its sign for all particle numbers.

## Limitations
The theorem is specific to one-dimensional independent Brownian diffusions coupled only through simultaneous Poisson resets. It does not prove the same four-particle boundary for non-Poisson resetting ages, inhomogeneous diffusivities, confining forces, different endpoint observables or spatially interacting particles. The result is a statement about stationary spatial covariance, not a dynamical phase transition. The general Gaussian interpolation and orthant identities used in its proof are classical. Independent publication-priority verification has not been performed.

## References
1. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, first posted 2022-11-01; *Phys. Rev. Lett.* **130**, 207101 (2023). https://arxiv.org/abs/2211.00563
2. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351 (2023). https://arxiv.org/abs/2307.15351
3. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025). https://arxiv.org/abs/2509.06658
4. Classical tools used: Gaussian association, Gaussian covariance interpolation, the bivariate normal orthant formula, and the Gaussian Poincaré inequality.
