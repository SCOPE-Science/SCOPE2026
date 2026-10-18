# Sharp endpoint analyticity on Boolean cubes: a two-term law and half-shell locking

## Finding

For the unnormalized graph Laplacian \(L_d=dI-A_d\) of the \(d\)-dimensional Boolean cube, \(d\ge 3\), let \(H_d(t)=\exp(-tL_d)\). Its time derivative has the following exact endpoint operator norm (a specialization of the standard binomial-deviation/resampling formula, included as a normalization identity rather than claimed as new):
\[
N_d(t):=\|\partial_tH_d(t)\|_{\ell^1\to\ell^1}=\|\partial_tH_d(t)\|_{\ell^\infty\to\ell^\infty}
=2d e^{-2t}\binom{d-1}{\lfloor dp(t)\rfloor}
 p(t)^{\lfloor dp(t)\rfloor}[1-p(t)]^{d-1-\lfloor dp(t)\rfloor},
\qquad p(t)=\frac{1-e^{-2t}}2,\quad t>0.
\]
Define \(M_d=\sup_{t>0}tN_d(t)\). Let \(t_*\) be the unique positive solution of \(1-e^{-4t_*}=2t_*\) (approximately \(0.398406065010010\)), and put
\[
c_*=\sqrt{\frac8\pi}\frac{t_*}{\sqrt{e^{4t_*}-1}}
=2\sqrt{\frac{t_*(1-2t_*)}{\pi}},\qquad
b_* =\frac{1+t_*}{12t_*}.
\]
The sharp maximized asymptotic is
\[
\boxed{M_d=c_*\sqrt d\left(1+\frac{b_*}{d}+O(d^{-2})\right)}\qquad(d\longrightarrow\infty).
\]
In addition, every choice of maximizing time \(t_d\) satisfies
\[
t_d=t_*+O(d^{-1}),\qquad
\left|\{dp(t_d)\}-\frac12\right|=O(d^{-1/2}),
\]
where \(\{\cdot\}\) denotes the fractional part. Thus optimization in continuous time asymptotically selects *half-integer Hamming shells*, eliminating the first-order lattice-phase oscillation present at a fixed time. The estimates hold for all integers \(d\ge3\) in the exact identity, and as \(d\to\infty\) in the asymptotics.

## Assumptions and scope

The graph has vertex set \(\{0,1\}^d\), and two vertices are adjacent precisely when they differ in one coordinate. The unnormalized Laplacian \(L_d=dI-A_d\) has eigenvalues \(2j\) for \(0\le j\le d\). The \(\ell^p\) norms use counting measure (the operator norms agree with those from normalized counting measure). In this manuscript \(d\) is an integer, \(d\ge3\), and time is continuous with \(t>0\). \(M_d\) is the *time-weighted, first-derivative endpoint norm*, not a spectral projection constant, an \(L^2\) norm, or the supremum of the unweighted derivative norm. No claim is made about other exponents or higher derivatives.

## Proof

**1. Exact heat-kernel norm.** In time \(t\), every coordinate flips independently with probability \(p=p(t)=(1-e^{-2t})/2\); set \(q=1-p\). The heat-kernel entry between vertices at Hamming distance \(j\) is \(p^j q^{d-j}\). Since \(p'(t)=e^{-2t}\), differentiation gives
\[
\frac{d}{dt}(p^j q^{d-j})
=\frac{e^{-2t}}{pq}(j-dp)p^j q^{d-j}.
\]
Every matrix row is a translate of every other row, and the kernel is symmetric, so the \(\ell^1\) and \(\ell^\infty\) operator norms both equal the row's total absolute mass. If \(X\sim\operatorname{Bin}(d,p)\), this mass is
\[
N_d(t)=\frac{e^{-2t}}{pq}\,\mathbb E|X-dp|.
\]
For \(k=\lfloor dp\rfloor\), the binomial identity
\[
(j-dp)\binom djp^jq^{d-j}
=dpq\left[\binom{d-1}{j-1}p^{j-1}q^{d-j}
-\binom{d-1}{j}p^jq^{d-1-j}\right]
\]
telescopes on either side of \(dp\) and yields the classical De Moivre identity
\[
\mathbb E|X-dp|=2dpq\binom{d-1}{k}p^kq^{d-1-k}.
\]
At integer \(dp\), the adjacent binomial masses coincide, so the formula is continuous through the apparent floor-function jumps. Substitution proves the exact norm. The pointwise sharp \(\ell^\infty\) data are the signs of any derivative-kernel row (arbitrary values at its zeros); for \(\ell^1\), a unit point mass is an extremizing vector.

**2. Uniform local expansion.** Fix a compact interval \(J\subset(0,\infty)\), write \(a=\{dp(t)\}\) and \(p=p(t)\), \(q=1-p\). Uniformly for \(t\in J\) and \(a\in[0,1]\), Stirling's formula with a bounded shift gives
\[
\binom{d-1}{\lfloor dp\rfloor}p^{\lfloor dp\rfloor}q^{d-1-\lfloor dp\rfloor}
=\frac{1}{\sqrt{2\pi dpq}}
\left[1+\frac{1}{d}\left(\frac1{12}+\frac{6a(1-a)-1}{12pq}\right)+O_J(d^{-2})\right].
\]
For completeness, set \(n=d-1\) and \(k=np+z\), where \(z=p-a\) is bounded. The standard \(n\)-based logarithmic expansion of this binomial mass has relative first coefficient
\[
-\frac{z^2+(q-p)z}{2pq}+\frac{1-p^{-1}-q^{-1}}{12}.
\]
Changing the normalization from \(n^{-1/2}\) to \(d^{-1/2}\) adds \(1/2\), and simplification gives exactly the displayed coefficient; the gamma-function remainder is uniform because \(p\), \(q\) stay bounded away from zero and \(z\) stays bounded. This binomial mean-absolute-deviation correction is classical; the new use here concerns its *time optimization*. It follows that
\[
\frac{tN_d(t)}{\sqrt d}=g(t)\left[1+\frac{B(t,a)}d+O_J(d^{-2})\right],
\]
where
\[
g(t)=\sqrt{\frac8\pi}\frac{t}{\sqrt{e^{4t}-1}},\qquad
B(t,a)=\frac1{12}+\frac{6a(1-a)-1}{12p(t)q(t)}.
\]
This expansion remains uniform even when \(dp(t)\) crosses an integer, since both end values \(a=0\) and \(a=1\) yield the same coefficient.

**3. Localization and unique continuum optimum.** Cauchy–Schwarz applied to the binomial deviation gives \(\mathbb E|X-dp|\le\sqrt{dpq}\); hence
\[
0\le\frac{tN_d(t)}{\sqrt d}\le \frac{2t}{\sqrt{e^{4t}-1}}.
\]
The right side tends to zero at both \(t\downarrow0\) and \(t\to\infty\); a competing value near the positive maximizer of \(g\) stays bounded away from zero. Consequently all maximizing times eventually lie in a common compact subset of \((0,\infty)\). The logarithmic derivative
\[
\frac{g'(t)}{g(t)}=\frac1t-\frac{2e^{4t}}{e^{4t}-1}
\]
has exactly one zero in \((0,\infty)\), since \((1-e^{-4t})/(2t)\) decreases strictly from \(2\) to \(0\); the critical point is \(t_*\), and \(g''(t_*)<0\). Compact uniform convergence gives \(t_d\to t_*\). At this point \(p(t_*)q(t_*)=t_*/2\).

**4. Half-shell optimization and the second term.** The correction satisfies
\[
B(t,a)\le B_{\max}(t):=\frac1{12}+\frac1{24p(t)q(t)},\qquad
B_{\max}(t)-B(t,a)=\frac{(a-1/2)^2}{2p(t)q(t)}.
\]
For each sufficiently large \(d\), choose \(\tilde p_d=(m+1/2)/d\), with \(m\) the integer nearest to \(dp(t_*)-1/2\), and set \(\tilde t_d=-\tfrac12\log(1-2\tilde p_d)\). Then \(\tilde t_d=t_*+O(d^{-1})\) and \(\{d\tilde p_d\}=1/2\), whence
\[
\frac{M_d}{\sqrt d}\ge c_*\left(1+\frac{B_{\max}(t_*)}{d}\right)+O(d^{-2}).
\]
For the upper bound, the nondegenerate maximum gives \(g(t)\le c_*-C(t-t_*)^2\) near \(t_*\), while \(B_{\max}(t)=B_{\max}(t_*)+O(|t-t_*|)\). Completing the square in the uniform expansion proves
\[
\frac{M_d}{\sqrt d}\le c_*\left(1+\frac{B_{\max}(t_*)}{d}\right)+O(d^{-2}).
\]
The same comparison quantitatively locates all maximizing times. Write \(\delta_d=t_d-t_*\). Near \(t_*\), strict concavity gives \(g(t_d)\le c_*-\kappa\delta_d^2\), while smoothness gives \(B_{\max}(t_d)=B_{\max}(t_*)+O(|\delta_d|)\). Combining the preceding half-shell lower bound with the upper envelope at the actual maximizer yields
\[
\kappa\delta_d^2\le C\left(\frac{|\delta_d|}{d}+\frac1{d^2}\right),
\]
for constants independent of \(d\). Solving this quadratic inequality establishes \(\delta_d=O(d^{-1})\). Inserting this back into the full expansion and comparing with the half-shell witness gives
\[
0\le B_{\max}(t_d)-B(t_d,\{dp(t_d)\})=O(d^{-1}).
\]
Because \(p(t_d)q(t_d)\) stays bounded away from zero, the displayed identity for the deficit implies
\[
\left|\{dp(t_d)\}-\frac12\right|=O(d^{-1/2}).
\]
This proves both the time localization and the half-shell locking without assuming that a derivative of the floor-function expression exists at a shell transition. Finally
\[
B_{\max}(t_*)=\frac1{12}+\frac1{12t_*}=b_*;
\]
the asserted sharp coefficient follows. (At a shell boundary, the equal adjacent formulas give the same value, and the half-shell competitor strictly improves the leading correction for large \(d\), so a maximizer is interior.)

## Verification

The included `verify_hypercube.py` checks the exact binomial identity in rational arithmetic, independently differentiates finite heat kernels, verifies the formula at shell transitions, checks the uniform Stirling approximation numerically, and evaluates the asymptotic constants at half-shell competitor times. It runs with the Python standard library. There are 475 deterministic finite and asymptotic-consistency assertions; none is used as an infinite proof. The analytic justification is given above.

## Relationship to prior work

De Moivre's exact formula is historical. Berend–Kontorovich (2013) provide sharp estimates of binomial mean absolute deviation; Frame's first oscillatory correction (1945) is presented and placed into an all-orders expansion by Elezović (2026). These prior results cover the binomial identity and *fixed-parameter expansion*, not the sharp time optimization on the graph heat semigroup. Zhang (2022) treats Boolean heat-semigroup smoothing in a different range and norm setting. The low-dimensional graphs \(Q_1\) and \(Q_2\) are complete multipartite, whereas \(Q_d\) for \(d\ge3\) is not. This is one reason to state the structural contribution for \(d\ge3\). The exact finite-time derivative norm is also covered by more general weighted-Bernoulli resampling-derivative calculations. The claimed contribution here is **only** the fully optimized two-term endpoint law together with its half-Hamming-shell phase locking, not the exact finite-time identity, the known binomial formulas, or fixed-parameter central-limit estimates.

## Limitations

The spectral Laplacian convention is unnormalized; rescaling generator and time together does not change \(M_d\). The asymptotic statement applies to integer dimensions tending to infinity, not to a fixed finite dimension without an error bound. The constants concealed in the big-O notation are not explicit, and this analysis does not determine an exact closed form for \(M_d\) at each finite \(d\). The location of maximizing times may not be unique. Historical priority across all classical semigroup and probability literature has not been independently established.

## References

1. D. Berend and A. Kontorovich, *A sharp estimate of the binomial mean absolute deviation with applications*, Statistics & Probability Letters **83** (2013), 1254–1259, DOI: 10.1016/j.spl.2013.01.023. First online January 23, 2013.
2. N. Elezović, *Local binomial expansions with an Appell shift, and the mean absolute deviation of the binomial distribution*, arXiv:2607.18494 (2026), especially Sections 3–4 and references to Frame (1945).
3. H. Zhang, *Heat-smoothing for holomorphic subalgebras of free group von Neumann algebras*, arXiv:2205.12833 (2022), introductory discussion of Boolean cube heat semigroups.
4. J. S. Frame, *Mean deviation of the binomial distribution*, 1945; historical first-order correction identified in reference 2.
