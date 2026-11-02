# A smooth non-Gaussian residual covariance with exact Haar dyadic residues for random bootstrap walks

## Finding
For two simple symmetric random walks coupled by independent, uniformly random Boolean recycling maps at every depth, their unscaled *quenched endpoint covariance* has a nondegenerate almost-sure limit over the random environment, although their diffusive functional limit has independent coordinates. The centered limiting covariance \(Z\) has the exact characteristic function
\[
\widehat\mu_Z(t)=\prod_{j=1}^{\infty}\left[\cos\left(\frac{t}{2^j}\right)\right]^{2^j}.
\]
It has variance \(1\), fourth cumulant \(-2/7\), fourth moment \(19/7\), an everywhere real-analytic density, and a **uniform law modulo \(2\)**. More precisely, even the depth-\(L\) truncation is exactly uniformly distributed among its \(2^L\) equally spaced residues modulo \(2\), for every integer \(L\ge1\). Its law is the unique centered, square-integrable fixed point of
\[
Z\ \stackrel{d}{=}\ \frac{\varepsilon_1+\varepsilon_2+Z_1+Z_2}{2},
\]
with independent fair signs \(\varepsilon_1,\varepsilon_2\) and independent copies \(Z_1,Z_2\) of \(Z\), all independent. These results concern a specific uniformly random recycling law, not general random environments.

## Assumptions and scope
Let \(\xi_1,\xi_2,\ldots\) be independent signs, each \(\pm1\) with probability \(1/2\). Independently, for every integer \(j\ge1\), sample a function \(\phi_j:\{-1,1\}^j\to\{-1,1\}\) uniformly from the \(2^{2^j}\) sign-valued functions, independently over \(j\). Thus all \(2^j\) function values at depth \(j\) are independent fair signs. We distinguish averaging over the walk signs, written \(\mathbb E_\xi[\cdot\mid\phi]\), from averaging over the random functions, written \(\mathbb E_\phi\).

Define, for integers \(N\ge1\),
\[
X_N=\sum_{k=1}^{N}\xi_k,\qquad
Y_N=\xi_1+\sum_{k=2}^{N}\xi_k\phi_{k-1}(\xi_1,\ldots,\xi_{k-1}),\qquad
C_N(\phi)=\operatorname{Cov}_\xi(X_N,Y_N\mid\phi).
\]
Set \(U_j=2^{-j}\sum_{a\in\{-1,1\}^j}\phi_j(a)\) and \(Z_L=\sum_{j=1}^L U_j\). Our centered residual is \(Z=\sum_{j=1}^\infty U_j\), so the endpoint covariance limit is \(C_\infty=1+Z\). All limits below are with respect to the law of the random functions, unless otherwise specified.

## Proof
**1. Exact endpoint covariance.** Both walks are martingales for each frozen environment. Cross-increments at distinct times have mean zero by conditioning on the later independent sign. Their simultaneous increment product equals \(1\) at time one and \(\phi_{k-1}(\xi_1,\ldots,\xi_{k-1})\) at time \(k\ge2\). Therefore, for every environment and all \(N\ge1\),
\[
C_N=1+\sum_{j=1}^{N-1}U_j.
\]
Since the environment functions are independent and uniform, the \(U_j\) are independent and centered, with \(\operatorname{Var}_\phi(U_j)=2^{-j}\). Consequently the Kolmogorov convergence criterion and orthogonality give almost-sure and \(L^2\) convergence, with the **exact error**
\[
\mathbb E_\phi[(C_\infty-C_N)^2]=\sum_{j=N}^{\infty}2^{-j}=2^{1-N}.
\]
In particular, \(C_N/N\to0\) almost surely, whereas \(C_N\) itself does not converge to a deterministic number.

**2. Law, non-Gaussianity, and recursion.** At level \(j\), the variable \(U_j\) is the sum of \(2^j\) independent Rademacher signs, each weighted by \(2^{-j}\). Independence gives
\[
\mathbb E_\phi e^{it Z_L}=\prod_{j=1}^{L}\cos(t/2^j)^{2^j}.
\]
The infinite product converges for every real \(t\), yielding the displayed characteristic function. The variance is \(\sum_{j\ge1}2^{-j}=1\). A sign has fourth cumulant \(-2\), so cumulant additivity gives
\[
\kappa_4(Z)=-2\sum_{j=1}^{\infty}2^{-3j}=-\frac27,
\qquad \mathbb E_\phi Z^4=3+\kappa_4(Z)=\frac{19}{7}.
\]
The fourth cumulant is nonzero, so the residual is non-Gaussian. Separating the two signs in the first layer and partitioning all subsequent level signs into two equal, independent groups gives the distributional fixed-point equation. On centered square-integrable laws, the associated mapping is a contraction in quadratic Wasserstein distance with factor \(1/\sqrt2\): couple two input laws optimally, use two independent copies of the centered coupling, and divide their sum by two. This proves uniqueness in that class.

**3. Exact dyadic Haar residues.** For each integer \(L\ge1\), the finite variable \(Z_L\) belongs to \(2^{1-L}\mathbb Z\). If \(k\in\{1,\ldots,2^L-1\}\), write \(k=2^{j-1}q\) with \(q\) odd and \(1\le j\le L\). The \(j\)-th factor of its characteristic function vanishes at \(t=\pi k\), because \(\cos(\pi q/2)=0\). Thus all nontrivial characters of the cyclic group of \(2^L\) residues modulo \(2\) have zero expectation. Fourier inversion on that finite group implies
\[
\Pr_\phi\bigl\{Z_L\bmod 2=r\,2^{1-L}\bigr\}=2^{-L},
\qquad r=0,1,\ldots,2^L-1.
\]
For each nonzero integer \(k\), the same vanishing persists for all sufficiently large \(L\); continuity of the characteristic function gives \(\mathbb E_\phi e^{i\pi kZ}=0\). Uniqueness of Fourier coefficients on the circle proves that \(Z\bmod2\) is uniform on \([0,2)\).

**4. Analyticity of the density.** Let \(c=-\log(\cos(1/2))>0\). For \(|t|\ge2\), choose \(j=\lceil\log_2|t|\rceil\). Then \(2^j\ge|t|\) and \(1/2<|t|/2^j\le1\), so one factor of the characteristic product bounds its absolute value by
\[
|\widehat\mu_Z(t)|\le\cos(1/2)^{2^j}\le e^{-c|t|}.
\]
All other factors have modulus at most one. Fourier inversion therefore produces a density extending holomorphically to the complex strip \(|\operatorname{Im}z|<c\). This proves the asserted everywhere real-analytic density. In particular the mod-\(2\) uniformity is an absolutely continuous—not merely atomic—phenomenon.

## Verification
Run `python3 verify.py` with the Python standard library. The checker directly enumerates the walk-path covariance over all environments through three steps, checks another \(200\) deterministic five-step environments, verifies finite-level moment and smoothing identities, tests exact binomial convolutions for the uniform residue law through six levels, and checks the Fourier-decay inequality numerically. The recorded run completed **917 assertions**. The infinite product, convergence, Haar law at all levels, uniqueness, and analyticity are proved above and do not rely on finite verification.

## Relationship to prior work
Hamza and Tournier (2026, arXiv:2610.01658v1) study random general bootstrap walks. Their independently uniform Boolean-map specialization is precisely the environment considered here. Their main conclusions concern convergence of diffusive rescalings to independent Brownian coordinates and related averaged covariation criteria (especially their Theorem 2 and Propositions 4, 14–15). Those statements do not identify the unscaled *environment-dependent* covariance limit, its law, its all-depth Haar residues, its smoothing fixed point, or its density regularity. Collevecchio, Hamza, Shi, and Williams (2022; arXiv:2010.16000v2) give the deterministic general-bootstrap representation and Brownian limit criteria, not an independently sampled uniform environment law. Standard independent-series and Fourier techniques are explicitly used rather than claimed as new; the contribution is their exact application to a canonical residual observable and its unexpected simultaneous non-Gaussian, analytic, and Haar-modulo-two structure.

## Limitations
The conclusions require independent, uniformly sampled complete Boolean maps at every depth. They do not extend as stated to biased, correlated, or cardinality-invariant recycling mechanisms. The two-copy smoothing relation is an identity in distribution, not a pathwise identity for one preselected environment. The result concerns endpoint quenched covariance, not a second-order functional limit for the full paired walks. Independent mathematical validation and exhaustive historical-priority certification have not been performed.

## References
- K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first submitted 2026-10-01, https://arxiv.org/html/2610.01658v1.
- A. Collevecchio, K. Hamza, M. Shi, and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000v2 (2021 preprint; published 2022), https://arxiv.org/pdf/2010.16000.
