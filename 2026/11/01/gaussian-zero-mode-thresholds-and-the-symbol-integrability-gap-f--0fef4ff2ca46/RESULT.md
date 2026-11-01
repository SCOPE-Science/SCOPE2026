# Gaussian zero-mode thresholds and the symbol-integrability gap for polynomial Airy equations

## Finding
For integers \(m,n\ge1\) and \(c\in\mathbb C\setminus\{0\}\), consider the entire differential equation
\[
z^m f(z)+c f^{(n)}(z)=0.
\]
Let \(E_{m,n,c}\) be its solutions in the Gaussian Bargmann–Fock space, and let \(W_{m,n,c}\subset E_{m,n,c}\) consist of the solutions for which multiplication by \(z^m+c\overline z^{\,n}\) is Gaussian-square-integrable. Both are vector spaces, and their dimensions are completely determined:
\[
\dim E_{m,n,c}=\begin{cases}n,&m<n,\\ n,&m=n,\ |c|>1,\\ n,&m=n\ge3,\ |c|=1,\\0,&\text{otherwise},\end{cases}
\quad
\dim W_{m,n,c}=\begin{cases}n,&m<n\ \text{or}\ (m=n,\ |c|>1),\\0,&\text{otherwise}.\end{cases}
\]
At the balanced critical point \(m=n\ge3\) and \(|c|=1\), exactly \(n\) independent Fock zero modes appear, but **all fail the additional harmonic-symbol Gaussian-integrability condition**. The two classifications are one result: the second pinpoints the otherwise hidden boundary-domain obstruction of the first.

## Assumptions and scope
Use normalized area measure \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\). The Gaussian Fock space \(\mathcal F^2\) consists of entire \(f(z)=\sum_{k\ge0}a_kz^k\) with
\[
\|f\|_{\mathcal F^2}^2=\int_{\mathbb C}|f|^2d\mu=\sum_{k\ge0}k!|a_k|^2<\infty.
\]
The coefficient \(c\) is nonzero and may have any complex phase. We define
\[
E_{m,n,c}=\{f\in\mathcal F^2:z^m f+c f^{(n)}\equiv0\},\qquad
W_{m,n,c}=\{f\in E_{m,n,c}:(z^m+c\overline z^{\,n})f\in L^2(d\mu)\}.
\]
The condition for \(W\) is multiplication by the *full symbol* before projection, not merely existence of a projected or distributional action. No assertion about alternate extensions of unbounded operators is made.

## Proof
**Coefficient ladders and entire solutions.** Put \(s=m+n\). Comparing the coefficient of \(z^k\) for \(0\le k<m\) shows \(a_n=\cdots=a_{n+m-1}=0\). For every \(N\ge0\), the coefficient of \(z^{N+m}\) gives
\[
a_{N+s}=-c^{-1}\frac{(N+m)!}{(N+s)!}\,a_N.
\tag{1}
\]
Therefore each solution is uniquely specified by its arbitrary \(n\) initial values \(a_0,\ldots,a_{n-1}\). For each seed \(0\le j<n\), only indices \(N=j+s\ell\), \(\ell\ge0\), can be nonzero. The recurrence ratio for ordinary Taylor coefficients is \(O(N^{-n})\), hence all \(n\) seed series converge everywhere; these account for all entire solutions.

**Fock membership.** Fix a nonzero seed, put \(N=j+s\ell\), and let \(q_{j,\ell}=N!|a_N|^2\). Formula (1) yields exactly
\[
\frac{q_{j,\ell+1}}{q_{j,\ell}}=
|c|^{-2}\frac{(N+m)!^2}{N!(N+m+n)!}
=|c|^{-2}\frac{\prod_{r=1}^{m}(N+r)}{\prod_{r=m+1}^{m+n}(N+r)}.
\tag{2}
\]
If \(m<n\), the ratio tends to zero; every seed is in Fock space and has all polynomial Gaussian moments. If \(m>n\), it tends to infinity; no nonzero seed belongs to Fock space. If \(m=n=p\), the ratio tends to \(|c|^{-2}\), so convergence holds for \(|c|>1\) and fails for \(|c|<1\). At \(|c|=1\), put \(N=j+2p\ell\) in (2). Then
\[
\frac{q_{j,\ell+1}}{q_{j,\ell}}
=\prod_{r=1}^{p}\frac{N+r}{N+p+r}
=1-\frac{p}{2\ell}+O(\ell^{-2}),
\qquad q_{j,\ell}\asymp (1+\ell)^{-p/2}.
\tag{3}
\]
Indeed, logarithms of successive ratios differ from \(-p/(2\ell)\) by a summable \(O(\ell^{-2})\); exponentiating the summed logarithms gives the two-sided asymptotic. The Fock series converges precisely when \(p>2\). Distinct seeds are supported on disjoint Taylor indices and are orthogonal in Fock space; thus \(E\) has exactly the advertised dimensions.

**Symbol-integrability for strict regimes.** In both \(m<n\) and \(m=n,|c|>1\), the seed factorial energies from (2) decrease eventually at a geometric rate or faster. For every fixed integer \(h\ge0\), \(\sum_N(N+h)!|a_N|^2<\infty\). In particular, both \(z^m f\) and \(\overline z^{\,n}f\) lie in \(L^2(d\mu)\), so all \(n\) Fock solutions lie in \(W\).

**Critical symbol-integrability obstruction.** It remains to take \(m=n=p\ge3\) and \(|c|=1\). For a nonzero seed at \(j\), set \(N=j+2p\ell\). The angular Fourier component of \((z^p+c\overline z^{\,p})f\) at angular frequency \(N+p\) is
\[
a_Nr^{N+p}\left(1-\frac{(N+p)!}{(N+2p)!}r^{2p}\right)e^{i(N+p)\theta}.
\tag{4}
\]
Different pairs \((j,\ell)\) yield different frequencies \(j+p+2p\ell\), and these are disjoint from the finitely many possible negative initial frequencies. By the Gaussian radial moment identity \(\int_{\mathbb C}|z|^{2k}d\mu=k!\), the exact squared \(L^2(d\mu)\) norm of (4) is
\[
q_{j,\ell}\frac{(N+p)!}{N!}\left[
\frac{(N+p)!(N+3p)!}{((N+2p)!)^2}-1\right].
\tag{5}
\]
The bracket equals
\[
\prod_{r=1}^p\frac{N+2p+r}{N+p+r}-1
=\frac{p^2}{N}+O(N^{-2})
\]
as \(N\to\infty\). Combining this with (3) and \((N+p)!/N!\asymp N^p\), every squared Fourier-component norm in (5) is asymptotically a positive constant times \(\ell^{p/2-1}\). Its sum over \(\ell\) diverges. Orthogonality of the angular components rules out any cancellation between different seeds. Hence no nonzero critical Fock solution lies in \(W\), proving its classification.

## Verification
The companion `CHECK.py` uses exact rational factorial ratios to check the recurrence identity, the angular-component norm identity (5), and positivity of its bracket over a range of distinct orders and degrees. It also checks convergence of the scaled critical factorial energies numerically for orders on both sides of the threshold. The critical asymptotic comparison and infinite divergence are proved above; finite tests are not substituted for that proof. All calculations can be independently reproduced using only the Python standard library with `python CHECK.py`.

## Relationship to prior work
Liu, Qin and Huang (arXiv:2610.30209v1, first made public 21 October 2026) study finite zero products of harmonic-symbol Fock Toeplitz operators. Their Theorem 1.2 establishes factor cancellation for a finite exponential-type harmonic class, and Remark 4.2 explicitly observes that individual Toeplitz factors may have kernels. Neither statement determines Gaussian norms of zero modes for \(z^m+cD^n\), nor their symbol-integrability distinction. The present result treats those two spaces, not the earlier product question.

Hai and Putinar (arXiv:1803.04890), especially their maximal-operator domain definition and Section 6, examine complex-symmetric differential operators and certain point spectra in Fock space. That maximal differential domain only asks that the differential expression itself belongs to Fock space; in the critical case here this expression is zero even while the original harmonic symbol times the function is not Gaussian-square-integrable. Their inspected results concern operator symmetry and different spectral coefficient hypotheses, not the two explicit dimension tables here.

Fischer, Burgarth and Lonigro (arXiv:2508.09044, Section 4 and Theorem 4.16) analyze pure higher-order squeezing operators on a finite-state core and compute deficiency spaces and self-adjoint extensions. Their symmetric \(p\)-th order setting overlaps one formal critical differential expression, but the deficiency-space calculations at nonreal spectral parameters and their self-adjoint domains do not state this classification of Gaussian entire zero solutions together with the multiplication-symbol integrability obstruction. Related literature on normal harmonic-symbol Fock Toeplitz operators (Sun, Du and Qi, 2020, DOI listed below) supplies projection/moment identities but studies normality rather than this dichotomy.

## Limitations
The theorem is restricted to nonzero \(c\), positive integer \(m,n\), the standard one-variable Gaussian Fock norm, and the explicitly stated extra \(L^2\) condition. The critical case does not assert that every closed extension or sesquilinear-form definition of Toeplitz quantization has zero kernel. The formula does not describe the entire spectrum, completeness of eigenfunctions, or higher-dimensional generalizations. Implicit coverage in the broad squeezing and Fock differential-operator literature remains an originality risk despite the inspected comparisons.

## References
- Y. Liu, J. Qin, and S. Huang, *Finite zero products of Toeplitz operators with harmonic symbols*, arXiv:2610.30209v1 (2026-10-21), https://arxiv.org/html/2610.30209v1.
- P. V. Hai and M. Putinar, *Complex symmetric differential operators on Fock space*, arXiv:1803.04890 (2018), https://arxiv.org/abs/1803.04890.
- F. Fischer, D. Burgarth, and D. Lonigro, *Self-adjoint realizations of higher-order squeezing operators*, arXiv:2508.09044 (2025), https://arxiv.org/pdf/2508.09044.
- Z.-L. Sun, W.-S. Du, and F. Qi, *Normal Toeplitz Operators on the Fock Spaces*, Symmetry 12 (2020), article 1615, https://doi.org/10.3390/sym12101615.
