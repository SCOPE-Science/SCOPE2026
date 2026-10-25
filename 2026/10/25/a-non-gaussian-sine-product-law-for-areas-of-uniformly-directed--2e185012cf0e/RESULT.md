# A non-Gaussian sine-product law for areas of uniformly directed planar zonogons

## Finding
Let \(n\ge2\), and let \(\Theta_1,\ldots,\Theta_n\) be independent uniform variables on \([0,\pi)\). Put \(u_j=(\cos\Theta_j,\sin\Theta_j)\), define the planar zonogon \(Z_n=\sum_{j=1}^n[-u_j,u_j]\) (Minkowski sum), and write \(A_n=\operatorname{Area}(Z_n)\). Its exact mean and variance are
\[
\mathbb EA_n=\frac4\pi n(n-1),\qquad
\operatorname{Var}(A_n)=16\binom n2\left(\frac12-\frac4{\pi^2}\right).
\]
In particular, despite the independence of the generating directions, the fluctuations are **not** asymptotically Gaussian. Let \(E_1,E_2,\ldots\) be independent mean-one exponential random variables. Then
\[
\frac{A_n-\mathbb EA_n}{n}\ \xrightarrow{\mathrm d}\ L
=-\frac8\pi\sum_{m=1}^{\infty}\frac{E_m-1}{4m^2-1}.
\]
The series converges almost surely and in \(L^2\). Writing \(T=4/\pi-L\), its law has the exact Laplace transform
\[
\mathbb E e^{-sT}=\frac{\sqrt{1-8s/\pi}}{\sin\left(\frac\pi2\sqrt{1-8s/\pi}\right)}\qquad(s\ge0),
\]
where the quotient is interpreted continuously at \(s=\pi/8\) and via hyperbolic sine when \(s>\pi/8\). Furthermore,
\[
\operatorname{ess\,sup}L=\frac4\pi,\quad
\operatorname{Var}(L)=4-\frac{32}{\pi^2},\quad
\Pr\left\{L<\frac4\pi-x\right\}\sim\frac{16}{3\pi}e^{-3\pi x/8}\quad(x\to\infty).
\]
Thus a bounded-above, non-Gaussian limiting distribution replaces the usual central-limit behavior for this fixed-length, isotropic geometric model.

## Assumptions and scope
All generating segments have deterministic Euclidean half-length one. Directions are independent and uniform modulo \(\pi\), with no random lengths. Area is Euclidean area, unnormalized. The limit is for integer \(n\to\infty\); the final tail limit is for \(x\to\infty\) **after** the distributional limit has been taken. The result does not address random lengths, directional anisotropy, higher-dimensional volumes, or simultaneous large-deviation regimes in \(n\) and \(x\).

## Proof
**1. Area and its finite moments.** Every pair of generating segments contributes four times the absolute determinant to the zonotope area, giving
\[
A_n=4\sum_{1\le i<j\le n}|\sin(\Theta_i-\Theta_j)|.
\]
For an independent uniform angular difference modulo \(\pi\), the sine absolute value has mean \(2/\pi\) and second moment \(1/2\). Covariances for disjoint index pairs vanish by independence. For distinct pairs sharing one index, condition on the shared angle: the conditional mean of each remaining factor is the same constant \(2/\pi\), so those covariances also vanish. Counting the \(\binom n2\) summands proves both finite-moment formulas.

**2. Exact centered Fourier identity.** The absolutely and uniformly convergent series
\[
|\sin t|=\frac2\pi-\frac4\pi\sum_{m=1}^{\infty}\frac{\cos(2mt)}{4m^2-1}
\]
has summable absolute coefficients. Let \(S_{m,n}=\sum_{j=1}^ne^{2im\Theta_j}\). The identity \(\sum_{i<j}\cos(2m(\Theta_i-\Theta_j))=(|S_{m,n}|^2-n)/2\) gives, for every realization,
\[
\frac{A_n-\mathbb EA_n}{n}=-\frac8\pi\sum_{m=1}^{\infty}\frac{|S_{m,n}|^2/n-1}{4m^2-1}.
\]
This series is absolutely convergent for each fixed \(n\) because \(|S_{m,n}|\le n\), and its tail is also uniformly controlled in \(L^2\) in \(n\) by the orthogonality shown below.

**3. Limit and tail control.** For any fixed positive integer \(M\), apply the multivariate real central limit theorem to the bounded vectors \((e^{2i\Theta_j},\ldots,e^{2iM\Theta_j})\). Their distinct Fourier coordinates are orthogonal and each has real/imaginary variance \(1/2\). Consequently the coordinates \((S_{m,n}/\sqrt n)_{1\le m\le M}\) converge jointly to independent standard complex Gaussians, so \((|S_{m,n}|^2/n)_{1\le m\le M}\) converge jointly to independent \(\operatorname{Exp}(1)\) variables.

For \(m\ne \ell\), character orthogonality on the independent angular torus gives
\[
\operatorname{Cov}(|S_{m,n}|^2-n,|S_{\ell,n}|^2-n)=0,
\qquad
\mathbb E(|S_{m,n}|^2-n)^2=n(n-1).
\]
Indeed, write \(|S_{m,n}|^2-n=\sum_{i\ne j}e^{2im(\Theta_i-\Theta_j)}\), and integrate the product. A nonzero expectation requires cancellation of every angular frequency; this is possible only for a matching pair of opposite directed edges **in the same Fourier mode**, yielding exactly \(n(n-1)\) matches. Thus the squared \(L^2\) norm of the omitted modes \(m>M\) after division by \(n\) equals
\[
\frac{64}{\pi^2}\frac{n-1}{n}\sum_{m>M}\frac1{(4m^2-1)^2},
\]
which tends uniformly to zero as \(M\to\infty\). The same estimate applies to the independent exponential limit series, proving the distributional limit by finite truncation followed by \(L^2\) approximation. It also proves \(\operatorname{Var}(L)=\lim_{n\to\infty}\operatorname{Var}(A_n/n)=4-32/\pi^2\).

**4. Sine-product law.** Since \(\sum_{m\ge1}(4m^2-1)^{-1}=1/2\), the centered exponential series rewrites as
\[
T=\frac4\pi-L=\frac8\pi\sum_{m=1}^{\infty}\frac{E_m}{4m^2-1}.
\]
Monotone convergence of the partial sums and finite total mean ensure that this random sum is finite and strictly positive almost surely. Independence and dominated convergence give
\[
\mathbb Ee^{-sT}=\prod_{m=1}^{\infty}\left(1+\frac{8s/\pi}{4m^2-1}\right)^{-1}.
\]
Euler's sine product, \(\sin(\pi z)/(\pi z)=\prod_{m\ge1}(1-z^2/m^2)\), gives the displayed transform on putting \(z^2=(1-8s/\pi)/4\). The expression is real and positive for all \(s\ge0\); the branch for \(s>\pi/8\) uses \(\sin(iy)=i\sinh y\).

**5. Support and sharp negative tail.** The almost sure positivity of \(T\) shows \(L<4/\pi\). Conversely, for each \(\delta>0\), choose \(M\) with mean \(\mathbb E\sum_{m>M}(8/\pi)E_m/(4m^2-1)<\delta/4\). Markov's inequality ensures the remainder is \(<\delta/2\) with positive probability; independently, the finite first \(M\) exponential terms have a positive probability to sum below \(\delta/2\). Hence \(\Pr(T<\delta)>0\) and the upper essential support endpoint is exactly \(4/\pi\). As the variance is positive, a bounded-above law cannot be a Gaussian law.

For the tail, split \(T=w_1E_1+R\) with \(w_1=8/(3\pi)\) and independent \(R=\sum_{m\ge2}(8/\pi)E_m/(4m^2-1)\). Let \(\lambda=1/w_1=3\pi/8\). The remainder has an exponential moment at \(\lambda\), and the telescoping gamma-product calculation gives
\[
\mathbb Ee^{\lambda R}=\prod_{m=2}^{\infty}\frac{4m^2-1}{4m^2-4}=\frac{16}{3\pi}.
\]
Condition on \(R\):
\[
e^{\lambda x}\Pr(T>x)=\mathbb E\big[e^{\lambda R}\mathbf 1_{\{R\le x\}}\big]+e^{\lambda x}\Pr(R>x).
\]
Choose \(\lambda'>\lambda\) below the inverse scale of the second exponential summand (that inverse scale is \(15\pi/8\)); then \(\mathbb Ee^{\lambda'R}<\infty\) and the last term vanishes by exponential Markov's inequality. Monotone convergence gives the prefactor \(16/(3\pi)\), completing the tail proof.

## Verification
The standalone file `zonogon_repro.py` builds actual Minkowski sums by an independent convex-hull algorithm, checks area against the determinant formula, compares truncated Fourier formulas, tests finite mean/variance numerically, compares Euler's infinite product against its sine expression, and samples finite-dimensional Laplace transforms near the limit. Execute `python zonogon_repro.py` using only the Python standard library. These tests support but do not establish the universal statements; the proof above supplies their justification.

## Relationship to prior work
Paouris–Pivovarov–Zinn (2012, arXiv:1210.7012) establish a Gaussian theorem for random projections of high-dimensional cubes and describe nondegenerate random-zonotope \(U\)-statistic mechanisms. Schneider (2022, arXiv:2202.06774) establishes valuations, expectation identities, and a Gaussian limit under nondegeneracy hypotheses. The present unit-length isotropic model deliberately has constant first Hoeffding projection \(\mathbb E(|\sin(\Theta_1-\Theta_2)|\mid\Theta_1)=2/\pi\), eliminating the usual linear Gaussian fluctuation. What is obtained here is an explicit nonlinear angular Fourier limit, its sine-product transform, and a sharp tail prefactor. General degenerate \(U\)-statistic theory supplies broad background and is not claimed new; the stated model-specific formulas and geometric interpretation are the contribution.

## Limitations
Historical priority is assessed against the inspected primary literature and searchable mathematical records but not certified exhaustively. In particular, Vitale's earlier chapter on random shapes and degenerate symmetric statistics could contain relevant general results; its entire original chapter was not accessible for a complete implication comparison. Related small-ball literature was accessible principally through abstracts. No almost-sure limit of the centered sequence or full finite-\(n\) area distribution is asserted. All numerical reproducibility checks are finite and only corroborative.

## References
1. G. Paouris, P. Pivovarov and J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012, first publicly posted 25 October 2012. In particular, the section giving random-zonotope determinant volume and nondegenerate \(U\)-statistic comparison.
2. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774, first publicly posted 14 February 2022. In particular, the valuation-expectation and central-limit sections and their hypotheses.
3. R. A. Vitale, *Symmetric statistics and random shape*, conference chapter (1987), earlier general context for degenerate random-shape statistics; full material not accessed.
4. G. Paouris and P. Pivovarov, *Small-ball probabilities for the volume of random convex sets*, Discrete & Computational Geometry, DOI:10.1007/s00454-013-9492-2 (2013). Abstract-level context; full text not inspected.
