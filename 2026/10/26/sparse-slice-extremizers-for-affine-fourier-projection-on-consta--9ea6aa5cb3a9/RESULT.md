# Sparse-slice extremizers for affine Fourier projection on constant-weight layers

## Finding
Let \(n\ge2\), \(1\le k\le n-1\), and let \(X_{n,k}\) be the \(k\)-element subsets of \(\{1,\ldots,n\}\), with uniform probability measure. Let \(P_{n,k}\) be the \(L^2(X_{n,k})\)-orthogonal projection onto restrictions of affine coordinate functions, equivalently the sum of the degree-zero and degree-one Johnson spectral projectors. Its exact sharp endpoint norm is
\[
\Lambda_{n,k}:=\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}
=\sum_{j=\max(0,2k-n)}^k
\frac{\binom{k}{j}\binom{n-k}{k-j}}{\binom nk}
\left|1+\frac{n(n-1)}{k(n-k)}\left(j-\frac{k^2}{n}\right)\right|.
\]
The same formula gives the \(\ell^1\)-operator norm. The maximum is attained by a sign-valued function, and \(\Lambda_{n,k}=\Lambda_{n,n-k}\).

Write \(M_n=\max_{1\le k\le n-1}\Lambda_{n,k}\). Then the sharp cross-slice asymptotic and asymptotic location of *every* maximizing layer are
\[
\boxed{\lim_{n\to\infty}\frac{M_n}{\sqrt n}=\sqrt{\frac2e}},
\qquad
\boxed{\frac{\min\{k_n,n-k_n\}}{\sqrt n}\longrightarrow\frac1{\sqrt2}}
\]
for any choice \(k_n\in\operatorname*{argmax}_{1\le k\le n-1}\Lambda_{n,k}\). Thus worst-case amplification occurs on a sparse layer of order \(\sqrt n\), not on a fixed-density layer: whenever \(\min(k_n,n-k_n)/\sqrt n\to\infty\), the normalized amplification instead tends to \(\sqrt{2/\pi}<\sqrt{2/e}\).

## Assumptions and scope
The output space consists of the real or complex functions on the full finite slice; all norms use unweighted counting coordinates, while the orthogonal projector is defined using uniform *probability* measure. An affine coordinate function is \(S\mapsto a+\sum_{i\in S}b_i\); because \(\sum_i\mathbf1_{\{i\in S\}}=k\), this space has dimension exactly \(n\). The result concerns this canonical projector, not an optimal projector chosen among all maps onto the same subspace. The asymptotic maximization is over all admissible cardinalities at each \(n\).

## Proof
**Kernel and exact norm.** Write \(p=k/n\) and \(z_i(S)=\mathbf1_{\{i\in S\}}-p\). The centered feature vectors lie in the coordinate sum-zero space and have covariance matrix \(\lambda(I-\mathbf1\mathbf1^\mathsf T/n)\), with
\[\lambda=\frac{k(n-k)}{n(n-1)}.\]
Hence the reproducing kernel of the constant-plus-linear space is
\[
K(S,T)=1+\lambda^{-1}\sum_i z_i(S)z_i(T)
=1+\frac{n(n-1)}{k(n-k)}\left(|S\cap T|-\frac{k^2}n\right).
\]
The projection matrix with respect to coordinate counting is \(K(S,T)/\binom nk\). A uniform random \(T\) has intersection \(J=|S\cap T|\) with hypergeometric probabilities \(\binom{k}{j}\binom{n-k}{k-j}/\binom nk\). Each kernel row is a permutation of every other. Thus both endpoint operator norms are the displayed expectation of \(|K|\). For any fixed \(S\), choosing \(f(T)\) to equal the sign of \(K(S,T)\) realizes that row sum. Complementing all sets proves the symmetry.

**Three asymptotic regimes.** Put \(h=\min(k,n-k)\), and use complementation to assume \(1\le h\le n/2\). Let \(\mu=h^2/n\) and
\[\sigma^2=\operatorname{Var}(J)=\frac{h^2(n-h)^2}{n^2(n-1)}.\]
The exact identity
\[
K=1+\sqrt{n-1}\,\frac{J-\mu}{\sigma}
\]
implies \(\mathbb E K^2=n\), establishing uniform integrability of \(|K|/\sqrt n\) along any sequence of layers.

If \(h/\sqrt n\to0\), then \(\mathbb E|J-\mu|\le2\mu\) and
\[\Lambda_{n,h}\le1+\frac{2h(n-1)}{n-h}\le1+4h=o(\sqrt n).\]
If \(h/\sqrt n\to c\in(0,\infty)\), the factorial moments
\[\mathbb E(J)_{r}=\frac{(h)_{r}^2}{(n)_{r}}\longrightarrow c^{2r}\]
show that \(J\) converges to a Poisson random variable \(Z_{c^2}\) of mean \(c^2\). The exact kernel then yields, with uniform integrability,
\[
\frac{\Lambda_{n,h}}{\sqrt n}\longrightarrow
F(c):=\frac{\mathbb E|Z_{c^2}-c^2|}{c}.
\]
If \(h/\sqrt n\to\infty\), the hypergeometric central limit theorem gives \((J-\mu)/\sigma\Rightarrow N(0,1)\), hence \(\Lambda_{n,h}/\sqrt n\to\sqrt{2/\pi}\). Here is a direct verification of the applicable central limit theorem: \(\sigma\to\infty\) and \(\sigma=o(\mu),\ o(h-\mu),\ o(n-2h+\mu)\). The adjacent probability ratio is exactly
\[
\frac{\Pr(J=j+1)}{\Pr(J=j)}=
\frac{(h-j)^2}{(j+1)(n-2h+j+1)}.
\]
Taylor expansion of its logarithm about \(j=\mu\), summed over \(O(\sigma)\) consecutive indices, gives
\[\log\frac{\Pr(J=\lfloor\mu+s\sigma\rfloor)}{\Pr(J=\lfloor\mu\rfloor)}=-\frac{s^2}{2}+o(1)\]
uniformly for bounded real \(s\). Tightness follows from the exact variance, and the local ratio plus normalization gives the standard Gaussian weak limit.

**Sharp Poisson optimization.** For \(\theta>0\) and \(m=\lfloor\theta\rfloor\), the Poisson mass recursion gives
\[\mathbb E|Z_\theta-\theta|
=2\theta\Pr(Z_\theta=m)
=\frac{2e^{-\theta}\theta^{m+1}}{m!}.\]
Therefore for \(m\le c^2\le m+1\),
\[F(c)=\frac{2e^{-c^2}(c^2)^{m+1/2}}{m!}.\]
This has its unique maximum on that interval at \(c^2=m+1/2\). The corresponding peak height is
\[b_m=\frac{2e^{-(m+1/2)}(m+1/2)^{m+1/2}}{m!}.\]
These peak heights strictly decrease. Indeed with \(u=m+1/2\),
\[
\log\frac{b_m}{b_{m+1}}=
1-u\log(1+1/u)-\log\frac{u+1}{u+1/2}=:H(u).
\]
The midpoint inequality for the strictly convex function \(t\mapsto1/(u+t)\) gives
\[H'(u)=\frac1{u+1/2}-\log(1+1/u)<0,\]
while \(H(u)\to0\) as \(u\to\infty\); hence \(H(u)>0\). Thus \(F\) has a unique global maximizer \(c=1/\sqrt2\) and maximum \(b_0=\sqrt{2/e}\).

Finally choose \(h_n\) as the nearest integer to \(\sqrt{n/2}\) to obtain the lower bound on \(M_n/\sqrt n\). For any sequence of maximizing indices, pass to a subsequence along which \(h_n/\sqrt n\) tends to zero, a finite positive number, or infinity. The three regime results show that no subsequential limit exceeds \(\sqrt{2/e}\), since \(\pi>e\). Equality requires the unique Poisson maximizer. This proves both boxed conclusions.

## Verification
A standalone exact-rational checker is provided in `johnson_projection_check.py`. It constructs the full projection matrix from the kernel for every \(2\le n\le8\) and every \(1\le k<n\), checks symmetry, idempotence, trace/rank and all row absolute sums, and then checks the finite hypergeometric norm formula for all slices through \(n=120\). Further exact tests include the closed special case \(\Lambda_{n,2}=(3n-7)/(n-1)\), and sample maximizers. The checker is evidence for the formulas in finite cases, not a substitute for the infinite-dimensional asymptotic proof above.

## Relationship to prior work
Filmus (arXiv:1406.0142, first posted 1 June 2014) establishes the orthogonal Johnson-slice harmonic decomposition underlying the degree-zero/degree-one projector. The classical Johnson idempotents are expressed through Eberlein/Hahn polynomial data; these determine the spectral space but not the cross-cardinality endpoint maximization proved here. A published calculation of the *second* Johnson primitive projector supplies a sharp degree-two endpoint norm and its fixed-density Gaussian limit; it treats neither the low-pass degree-zero-plus-one operator nor the sparse-layer maximization. Elezović (arXiv:2608.06232) identifies hypergeometric mean absolute deviations with a boundary mass and studies fixed-proportion asymptotics, a directly relevant statistical input; the paper's full text was not accessible in the present comparison. The present claim concerns the sharp **joint limit** over varying cardinalities and the unique sparse maximizer. The Poisson identity is elementary and not claimed as new.

## Limitations
The asymptotic gives the leading optimal constant and maximizing density scale, not the exact finite-\(n\) optimizing cardinality, its second-order lattice displacement, or projection constants under nonuniform slice measures. An equivalent sparse optimization could occur in older Johnson-scheme, hypergeometric mean-deviation or approximation-theoretic literature not identified in the inspected record. The relevant 2026 mean-deviation paper was compared from its abstract and secondary exposition only, so its full coverage remains an explicit bibliographic risk; the scientific priority claim is provisional.

## References
1. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (v1: 1 June 2014; full-text HTML of v2 inspected), Electron. J. Combin. 23 (2016), P1.23.
2. M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra 17 (2008), 154–167, DOI 10.13001/1081-3810.1256 (abstract and publication metadata inspected).
3. *Exact endpoint norm of the second Johnson spherical projector* (2026), full published result inspected; it concerns the separate degree-two primitive idempotent.
4. N. Elezović, *The mean absolute deviation of the classical discrete distributions: collapse identities, complete asymptotic expansions, and enveloping series*, arXiv:2608.06232 (6 August 2026; abstract and secondary exposition inspected; full paper inaccessible).
