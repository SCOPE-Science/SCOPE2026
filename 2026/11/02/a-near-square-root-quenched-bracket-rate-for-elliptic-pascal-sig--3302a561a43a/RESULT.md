# A near-square-root quenched bracket rate for elliptic Pascal-sign walks

## Finding
Fix \(0<\varepsilon<1/2\). Let \((\beta_k)_{k\geq0}\) be independent Bernoulli variables with arbitrary deterministic probabilities \(p_k\in[\varepsilon,1-\varepsilon]\). Define the random sign scenery
\[
f(s)=(-1)^{\sum_{k=0}^s\binom{s}{k}\beta_k},\qquad s\geq0.
\]
Binomial coefficients in the exponent are interpreted modulo two. Let \((\xi_j)_{j\geq1}\) be independent fair signs, independent of the scenery, and set \(S_n=\sum_{j=1}^n\mathbf1_{\{\xi_j=-1\}}\), \(\zeta_0=1\), and \(\zeta_n=f(S_n)\) for \(n\geq1\). Put \(X_n=\sum_{j=1}^n\xi_j\) and \(Y_n=\sum_{j=1}^n\zeta_{j-1}\xi_j\).

There is a deterministic finite constant \(C_\varepsilon\), depending only on \(\varepsilon\), such that for almost every fixed scenery, almost surely under the conditional driving-sign law,
\[
\max_{0\leq m\leq N}\left|\sum_{j=0}^{m-1}\zeta_j\right|
\leq \sqrt N\exp\left\{C_\varepsilon\bigl[\log\log(N+e^e)\bigr]^2\right\}
\quad\text{for all sufficiently large integers }N.\tag{1}
\]
The same bound, potentially with an enlarged deterministic \(C_\varepsilon\), holds for the spatial maxima \(\max_{m\leq N}|\sum_{s<m}f(s)|\) almost surely under the scenery law. Consequently, for every \(\delta>0\), the predictable cross-bracket of \((X,Y)\) is \(O(N^{1/2+\delta})\) almost surely under almost every quenched law, and its normalized value is \(O(N^{-1/2+\delta})\).

The polynomial exponent \(1/2\) is optimal uniformly over allowed probability profiles: with \(p_k=1/2\) throughout, the unnormalized bracket divided by \(\sqrt N\) converges under the joint (annealed) law to a nondegenerate centered normal law of variance \(3\). In particular, no bound \(O(N^\alpha)\) with a fixed \(\alpha<1/2\) can hold almost surely for all allowed profiles.

## Assumptions and scope
All indexing starts at zero for the scenery and at one for the independent driving increments. The \(p_k\) are deterministic but need not converge, be periodic, or be identically distributed. The environment is frozen in time: the same \(\beta_k\) is used for each \(n\). The statement holds for every fixed ellipticity constant \(\varepsilon\), without claiming uniform constants as \(\varepsilon\downarrow0\). The process \(S_n\) is a one-way count of negative increments, not a symmetric walk in its state index. An almost-sure assertion under the joint law is converted by disintegration into an assertion for almost every environment under the conditional law.

## Proof
**1. Binary submask decorrelation.** For a nonnegative integer \(s\), let \(D(s)\) be the set of integers whose binary one-bits are contained in the one-bits of \(s\). The elementary parity identity \((1+z)^{2^i}=1+z^{2^i}\) over \(\mathbb F_2\), multiplied over the one-bits of \(s\), shows that \(\binom{s}{k}\) is odd exactly for \(k\in D(s)\). Write \(h(s)\) for the number of one-bits of \(s\); then \(|D(s)|=2^{h(s)}\). For distinct \(s,t\),
\[
|D(s)\triangle D(t)|=2^{h(s)}+2^{h(t)}-2^{h(s\mathbin{\&}t)+1}
\geq2^{\max(h(s),h(t))-1}.\tag{2}
\]
Indeed, if \(h(s)\ne h(t)\), the smaller Boolean cube has at most half as many elements as the larger; if the bit-counts agree but the integers differ, their common cube has at most half the cardinality of either. Let \(\rho=1-2\varepsilon\in(0,1)\). Independence gives the exact identity
\[
\mathbb E_\beta[f(s)f(t)]
=\prod_{k\in D(s)\triangle D(t)}(1-2p_k),
\]
so for \(s<t\), the absolute covariance-free pair moment is at most \(g(t)=\rho^{2^{h(t)-1}}\). The factor for \(s=0\) is well defined because \(2^{h(0)-1}=1/2\); we may harmlessly set \(g(0)=1\).

**2. Sparse low-bit-count integers.** For \(L\geq1\), put \(G_L=\sum_{t=0}^{2^L-1}g(t)\). Sorting integers by bit count gives
\[
G_L\leq1+\sum_{j=1}^L\binom Lj\rho^{2^{j-1}}.
\]
Split at \(J=\lceil2\log_2(L+2)\rceil\). The sum through \(J\) is at most \((J+1)(L+2)^J\), hence at most \(\exp\{C(\log(L+2))^2\}\). The remaining sum is bounded by \(2^L\exp\{-c(L+2)^2/2\}\), which is uniformly bounded for all sufficiently large \(L\), where \(c=-\log\rho>0\). Enlarge \(C\) for finitely many small \(L\). Thus
\[
G_L\leq \exp\{C_0(\log(L+2))^2\}.\tag{3}
\]

**3. Maximal spatial moment.** For an interval \(I\subseteq\{0,\ldots,2^L-1\}\) of length \(r\), the exact pair expansion and the bound from Step 1 give
\[
\mathbb E_\beta\left|\sum_{s\in I}f(s)\right|^2
\leq r+2r\sum_{t\in I}g(t).
\]
Take the aligned dyadic partition of \([0,2^L)\) at each scale \(r=2^j\). The sum of second moments of all blocks at that scale is at most \(2^L+2rG_L\). Every prefix is the union of at most one aligned block at each of the \(L+1\) scales. Cauchy--Schwarz, followed by summing over all blocks at all scales, yields
\[
\mathbb E_\beta\max_{0\leq m\leq2^L}\left|\sum_{s<m}f(s)\right|^2
\leq(L+1)\sum_{j=0}^L(2^L+2^{j+1}G_L)
\leq2^L\exp\{C_1(\log(L+2))^2\}.\tag{4}
\]
The change in constants depends only on \(\varepsilon\). Apply Markov's inequality to the event that the maximum exceeds \(2^{L/2}\exp\{C_2(\log(L+2))^2\}\). Choose fixed \(C_2>(C_1+1)/2\). Its probability is at most \(\exp\{-(2C_2-C_1)(\log(L+2))^2\}\), summable in \(L\). Borel--Cantelli, then interpolation between consecutive powers of two, proves the spatial part of (1) with an enlarged constant. This uses no assumption about cancellation of the expectations of the signs.

**4. Renewal occupation of a fixed scenery.** Fix an environment satisfying the spatial maximal bound. Since \(S_n\) increases by one with probability \(1/2\) and otherwise stays put, its completed holding lengths \(H_s\), indexed by \(s=0,1,\ldots\), are independent geometric variables on \(\{1,2,\ldots\}\), with \(\mathbb EH_s=2\), \(\operatorname{Var}(H_s)=2\), independent of the fixed scenery. Write
\[
W_m=\sum_{s=0}^{m-1}f(s)(H_s-2).
\]
For the conditional driving-sign law, \(W_m\) is a square-integrable martingale with \(\mathbb EW_m^2=2m\). Doob's maximal inequality gives \(\mathbb E\max_{m\leq2^L}|W_m|^2\leq8\cdot2^L\). Another dyadic Markov--Borel--Cantelli argument proves \(\max_{m\leq N}|W_m|\leq\sqrt N\exp\{C_3[\log\log(N+e^e)]^2\}\) eventually, for a deterministic \(C_3\). Geometric tails and Borel--Cantelli give \(\max_{s\leq N}H_s=O(\log(N+2))\) almost surely. At each completed holding time the signed occupation is \(\sum_{s<m}f(s)H_s=2\sum_{s<m}f(s)+W_m\); an incomplete holding interval contributes at most its full holding length. Since the number of visited sites by time \(N\) is at most \(N\), the spatial and martingale bounds combine to give (1). Replacing the first scenery value by the stipulated \(\zeta_0=1\) alters every prefix by at most two.

**5. Predictable bracket and sharpness.** With the natural driving-sign filtration and fixed scenery,
\[
\mathbb E^\beta[(\Delta X_j,\Delta Y_j)(\Delta X_j,\Delta Y_j)^T\mid\mathcal F_{j-1}]
=\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
The bracket assertion follows directly from (1). For sharpness take \(p_k=1/2\). As \(s\) increases, the map from \((\beta_0,\ldots,\beta_s)\) to the signs \((f(0),\ldots,f(s))\) is invertible over \(\mathbb F_2\): its parity matrix is lower triangular, with diagonal entries \(\binom{s}{s}=1\). Therefore \((f(s))_{s\geq0}\) are i.i.d. fair signs under the environment law. Together with the independent geometric holding lengths, the completed site rewards \(f(s)H_s\) are i.i.d. mean-zero variables with variance \(\mathbb EH_s^2=6\); their mean holding time is two. The random-time-change central limit theorem for this elementary renewal-reward process gives
\[
\frac1{\sqrt N}\sum_{j=0}^{N-1}f(S_j)
\Longrightarrow\mathcal N(0,3)
\quad\text{under the joint law}.
\]
The first-value convention changes the left side by at most \(2/\sqrt N\). A universal almost-sure exponent strictly smaller than \(1/2\) would force convergence to zero in probability under the joint law, contradicting this nondegenerate limit. This proves the claimed optimality of the polynomial exponent.

## Verification
The accompanying `check.py` independently evaluates the Lucas parity relation, Boolean-submask symmetric differences, finite exact product moments for nonconstant Bernoulli parameters, the interval second-moment upper bound and the triangular invertibility of the fair-bit transform. Its output is supplied in `check_output.txt`; the calculations corroborate finite identities rather than establish an infinite theorem. All asymptotic and almost-sure conclusions follow from the analytical estimates in Steps 1--5.

## Relationship to prior work
Hamza and Tournier (2026), *Are random random walks normal?*, Section 4.3 and Corollary 12, formulate this frozen inclusion-induced one-factor setting and establish an annealed functional Brownian limit. The present claim is restricted to the nearly square-root *maximal quantitative bound*, its uniformity over arbitrary nonstationary elliptic parameter sequences, and optimality of its polynomial exponent. Qualitative quenched limits established for related environments are not claimed as new. Fair-environment Brownian-scale fluctuations, which have also been studied previously, serve solely as the sharpness boundary. The new proof's multiscale estimate for the whole collection of prefix sums is the key strengthening beyond a Cesàro strong law.

## Limitations
No exact iterated-logarithm constant or \(\sqrt{N\log\log N}\) upper bound is established for heterogeneous biased coefficients. The factor \(\exp\{C_\varepsilon(\log\log N)^2\}\) may not be sharp, and the constant deteriorates as ellipticity is lost. The result assumes independent coefficient bits, independent fair driving signs and static coefficients; it does not cover dependent coefficient environments or nonsymmetric walks. The lower bound establishes minimax polynomial optimality by a fair environment, not an individual-environment lower bound for every nonstationary probability sequence. Priority remains subject to independent literature review.

## References
1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first publicly submitted 2026-10-01), especially Section 4 and Corollary 12, https://arxiv.org/html/2610.01658v1.
2. A. Collevecchio, K. Hamza, Y. Shi and A. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000, https://arxiv.org/abs/2010.16000.
3. Classical ingredients: Lucas's binomial-parity identity, the dyadic maximal-block decomposition, Markov and Borel--Cantelli inequalities, Doob's martingale inequality, and the renewal-reward central limit theorem.
