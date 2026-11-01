# Isotropic Gaussian splitting of finite-time singular values in the twisted baker map

## Finding
Fix an integer \(M\ge2\). For the Saiki–Takahasi–Yorke twisted baker map \(F\) in dimension \(M\), start a point \(x\) from normalized Lebesgue measure. For each integer \(n\ge1\), write
\[
L_{j,n}(x)=\log\|D F^n(x)e_j\|,\qquad 1\le j\le M,
\]
where \(e_j\) is the standard basis and the derivative is evaluated away from the measure-zero union of branch boundaries. The entries \(L_{j,n}\) are the **labeled** logarithmic coordinate stretches; because the derivative is monomial, their unordered multiset is exactly the multiset of logarithms of its singular values.

There is an exact universal multivariate central limit theorem, for every fixed \(M\):
\[
\boxed{\frac1{\sqrt n}\left(L_{j,n}-\frac{n\log2}{M}\right)_{j=1}^M\ \Longrightarrow\ \mathcal N_M(0,\Sigma_M),\qquad
\Sigma_M=(\log2)^2\left(\frac{I_M}{M}-\frac{\mathbf1\mathbf1^{\mathsf T}}{M^2}\right).}
\]
All nonzero eigenvalues of \(\Sigma_M\) are equal to \((\log2)^2/M\), with multiplicity \(M-1\). Thus, although the expansion directions move around a deterministic cyclic permutation and have correlated finite-time histories, their centered asymptotic Gaussian fluctuations are isotropic on the sum-zero hyperplane. In contrast, singular-value logs listed in decreasing order converge to the *ordered* coordinates of this Gaussian, not to an ordinary nonsingular Gaussian vector.

Let \(\kappa_n=\|D F^n\|_2\,\|(D F^n)^{-1}\|_2\) be the Euclidean condition number, and let \(Z_1,\ldots,Z_M\) be independent standard Gaussians. Then
\[
\boxed{\frac{\log\kappa_n}{\sqrt n}\ \Longrightarrow\ \frac{\log2}{\sqrt M}\bigl(\max_j Z_j-\min_j Z_j\bigr).}
\]
This convergence also holds in expectation:
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E\log\kappa_n}{\sqrt n}=\frac{2\log2}{\sqrt M}\,\mu_M,\quad
\mu_M=M\int_{-\infty}^{\infty}z\,\phi(z)\Phi(z)^{M-1}\,dz>0,}
\]
where \(\phi\) and \(\Phi\) are the standard Gaussian density and distribution function. In particular, at \(M=2\), the constant is \(\log2\sqrt{2/\pi}\). Nevertheless, for Lebesgue-almost every starting point, **all** finite-time logarithmic singular growth rates converge to the same Lyapunov exponent \((\log2)/M\). The square-root-scale anisotropy does not contradict that common exponent.

## Assumptions and scope
Fix \(M\ge2\), and let
\[
X_M=[-1,1]\times[0,1]^{M-1},\qquad
F(x_1,\ldots,x_M)=\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
Take \(m_M\) to be normalized \(M\)-dimensional Lebesgue probability on \(X_M\). It is invariant under \(F\); more strongly, each specified \(n\)-word of left/right branches has measure \(2^{-n}\), so branch choices are independent fair binary symbols under \(m_M\). The last assertion and the invariant measure are established by the originating paper's basic-rectangle construction. Its exceptional branch-boundary preimages have zero \(m_M\)-measure; no claim is made about derivatives there.

All probabilistic limits are taken as \(n\to\infty\) with **fixed dimension** \(M\). The notation \(\mathcal N_M(0,\Sigma_M)\) permits a singular covariance: this Gaussian is supported on the \((M-1)\)-dimensional hyperplane of coordinate sum zero. All logarithms are natural, and the singular values and condition number use the Euclidean norm.

## Proof
**1. Exact derivative cocycle and the cyclic occupation identity.** The two branch derivatives are
\[
D_L=\operatorname{diag}(2,1,\ldots,1),\qquad
D_Re_j=\begin{cases}e_{j+1},&j<M,\\-2e_1,&j=M.\end{cases}
\]
Each is a signed monomial matrix. Let \(\varepsilon_t=0\) for a left visit, \(\varepsilon_t=1\) for a right visit, and put \(r_t=\sum_{s=1}^t\varepsilon_s\pmod M\), with \(r_0=0\). Define the coordinate label \(j(r)=1+((-r)\bmod M)\), taking residues in \(\{0,\ldots,M-1\}\). After \(t\) steps the permutation part of the derivative is a cyclic shift by \(r_t\). Both branches multiply exactly the coordinate that occupies the *new* first row by two: on a left step the first row stays put; on a right step the former last row moves to the first row and is multiplied by two. Thus, for every admissible finite itinerary,
\[
\boxed{\|D F^n(x)e_j\|=2^{N_j(n)},\qquad
N_j(n)=\sum_{t=1}^n\mathbf1_{\{j(r_t)=j\}},\quad\sum_jN_j(n)=n.}
\]
The full matrix is signed monomial, so its singular values are exactly these column norms, without extra diagonalization. Consequently \(L_{j,n}=(\log2)N_j(n)\), and
\[
\log\kappa_n=(\log2)(\max_jN_j(n)-\min_jN_j(n)).
\]

**2. Explicit Markov reduction.** The independent fair branch symbols imply that \(r_t\) is the irreducible, aperiodic Markov chain on \(\mathbb Z/M\mathbb Z\) with transition
\[
(Pg)(r)=\tfrac12g(r)+\tfrac12g(r+1).
\]
Its unique stationary distribution is uniform. Since \(r_0=0\), the chain is not initially stationary, but the finite-state ergodic theorem holds from this deterministic start. Therefore \(N_j(n)/n\to1/M\) almost surely, proving the equal almost-sure Lyapunov exponents.

**3. The exact fluctuation covariance.** Let \(a=(a_1,\ldots,a_M)\in\mathbb R^M\) and set
\[
f(r)=a_{j(r)}-\bar a,\qquad \bar a=M^{-1}\sum_ja_j.
\]
This has zero uniform mean. Choose a periodic function \(g\) on the residue group such that
\[
g(r)-g(r+1)=2f(r).
\]
It exists because \(\sum_r f(r)=0\); for example, fix \(g(0)=0\) and integrate these differences around the cycle. Then \((I-P)g=f\). Define the bounded martingale differences
\[
\xi_t=g(r_t)-(Pg)(r_{t-1}),\qquad t\ge1.
\]
Conditionally on \(r_{t-1}=r\), the value of \(\xi_t\) is \(+f(r)\) or \(-f(r)\), each with probability \(1/2\). In particular,
\[
\mathbb E(\xi_t\mid r_{t-1})=0,\qquad
\mathbb E(\xi_t^2\mid r_{t-1})=f(r_{t-1})^2.
\]
The Poisson/martingale identity yields
\[
\sum_{t=0}^{n-1}f(r_t)=g(r_0)-g(r_n)+\sum_{t=1}^n\xi_t.
\]
Replacing the sum from \(t=0\) to \(n-1\) by the sum from \(t=1\) to \(n\) changes it by a uniformly bounded term. The ergodic theorem gives
\[
\frac1n\sum_{t=1}^n\mathbb E(\xi_t^2\mid r_{t-1})\longrightarrow
\frac1M\sum_{r=0}^{M-1}f(r)^2=\frac1M\sum_{j=1}^M(a_j-\bar a)^2
\]
almost surely. Because the increments are bounded, the conditional Lindeberg condition is automatic. The bounded-increment martingale central limit theorem therefore gives a centered normal limit with precisely that variance for every \(a\). The Cramér–Wold device proves the vector central limit theorem with covariance \(I_M/M-\mathbf1\mathbf1^{\mathsf T}/M^2\) for \(N(n)\), and multiplication by \(\log2\) gives the displayed \(\Sigma_M\).

**4. Condition-number law and sharp mean coefficient.** Let \(Z_j\) be independent standard normal variables and \(\bar Z=M^{-1}\sum_jZ_j\). The vector \(((Z_j-\bar Z)/\sqrt M)_j\) has exactly the covariance from Step 3. Taking the continuous coordinate-range functional yields the weak limit of \(\log\kappa_n/\sqrt n\). To justify convergence of means, apply Step 3 to each coordinate indicator. The martingale sums have \(L^2\)-norm at most a constant times \(\sqrt n\), while the Poisson boundary terms remain uniformly bounded for fixed \(M\). Thus
\[
\sup_{n\ge1}\mathbb E\left[\frac{\|N(n)-(n/M)\mathbf1\|_2^2}{n}\right]<\infty.
\]
Since the range is at most twice the Euclidean norm of this centered vector, the normalized ranges are uniformly integrable. Symmetry gives \(\mathbb E(\max Z-\min Z)=2\mathbb E\max Z=2\mu_M\), and elementary Gaussian order statistics yield the displayed integral. At \(M=2\), \(\mu_2=1/\sqrt\pi\), giving the stated special constant.

## Verification
The standalone script `verify.py` (Python standard library only) independently composes the branch derivative matrices for all \(2\le M\le6\) and every binary word of length \(1\le n\le8\), checking the exact column-norm/occupation identity. It also checks the finite-state Poisson equation, Green–Kubo variance equality, and martingale conditional variance with exact rational arithmetic for \(2\le M\le17\), using basis, pair-difference and additional test observables. Finally, it checks distribution recurrences by two separate word-enumeration approaches. Execute `python verify.py` in a directory containing this document and `verify.py`.

The executed results were: `CHECK_OK derivative_words=2550 poisson_vectors=984 exact_moment_distributions=45`. These finite checks are consistency tests, not an infinite proof. The proof above establishes all fixed integer dimensions and all time horizons needed for the limit theorems.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the twisted baker map, established its invariant Lebesgue probability, fair Bernoulli symbolic coding, and mixing, and studied dense repelling periodic points with real or complex derivative eigenvalues and nonuniform *periodic-orbit* expansion. Those facts are premises, not new results here. In particular, their periodic-orbit conclusions and the known binomial-residue refinement do not provide the typical-trajectory multivariate **singular-value** fluctuation covariance or the sharp condition-number law. Standard finite-state martingale CLT and Gaussian order-statistic tools are used, but the cyclic derivative/occupation identification and the exact isotropic covariance calculation are the new joint conclusion assessed here.

The closest published comparison is *Exact real-spectrum residue law for the twisted baker map* (October 2026). It determines when the eigenvalues of derivatives at **periodic points** are real, including exact periodic word counts. That result does not control Lebesgue-typical derivative singular values, the centered covariance, the Gaussian fluctuations or the condition-number expectation.

## Limitations
The statement concerns normalized invariant Lebesgue measure only, fixed integer \(M\), and almost-everywhere derivatives for the specified piecewise map. No uniform limit in dimension, no claim for all invariant probabilities, and no conclusions about finite-time eigenvalues are asserted. Although the limiting covariance is proportional to the identity on the zero-sum hyperplane, the finite-time coordinates are not independent and the finite-time covariance is not generally identical to that of independent multinomial counts. Existing symbolic coding and standard finite-state martingale limit theory are prerequisites. Search of available primary literature and published research records does not prove absolute novelty; unindexed or equivalent formulations of the same derivative cocycle remain a priority risk. No independent external mathematical audit is claimed.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304v1, first public 9 February 2022; inspected full arXiv v3 text at https://arxiv.org/html/2202.04304v3, especially equations (1.1), (2.1), Lemma 2.4, property (P4), Theorems A–D and Section 3.3.
2. *Exact real-spectrum residue law for the twisted baker map*, publicly available research record, 11 October 2026, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b/RESULT.md.
3. D. Levin and Y. Peres, *Markov Chains and Mixing Times*, 2nd edition, AMS, 2017, background for finite-state Markov chains. The martingale covariance computation needed here is given explicitly above.
