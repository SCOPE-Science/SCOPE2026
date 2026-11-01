# A quenched law of the iterated logarithm for cardinality-grouped bootstrap walks

## Finding

Consider the independently resampled, cardinality-grouped inclusion-induced bootstrap transformation defined below. For almost every realization of its Bernoulli environment, the predictable cross-variation of the two resulting simple random walks obeys the **sharp classical law of the iterated logarithm**:

\[
\limsup_{N\to\infty}\frac{\sum_{j=1}^{N}\xi_j\eta_j}{\sqrt{2N\log\log N}}=1,
\qquad
\liminf_{N\to\infty}\frac{\sum_{j=1}^{N}\xi_j\eta_j}{\sqrt{2N\log\log N}}=-1
\]
almost surely under the walk law, for almost every fixed environment. In particular the normalized pair of walks converges **quenched** in the Skorokhod space \(D([0,1],\mathbb R^2)\) to a standard planar Brownian motion with independent components. This upgrades the annealed result of Hamza and Tournier, Corollary 9, for the same elliptic independent-time one-factor Markov model.

## Assumptions and scope

Fix \(0<\epsilon<1/2\). For all integers \(n\ge1\) and \(0\le k\le n\), let \(\beta_{n,k}\) be mutually independent Bernoulli random variables with deterministic success probabilities \(p_{n,k}\in[\epsilon,1-\epsilon]\). Their joint law is denoted \(\mathsf Q\). Let \(\xi_1,\xi_2,\ldots\) be independent fair signs, independent of the entire environment, and let \(\mathsf P\) denote their law. Put

\[
S_n=\sum_{j=1}^n\mathbf 1_{\{\xi_j=-1\}},\quad
\zeta_0=1,\quad
\zeta_n=(-1)^{\sum_{k=0}^{S_n}\binom{S_n}{k}\beta_{n,k}}\quad(n\ge1),
\]
where the exponent is understood modulo two. Define \(\eta_j=\zeta_{j-1}\xi_j\), \(X_N=\sum_{j=1}^{N}\xi_j\), and \(Y_N=\sum_{j=1}^{N}\eta_j\). For every fixed environment, \((\eta_j)\) is itself a sequence of independent fair signs under \(\mathsf P\), because \(\zeta_{j-1}\) is a predictable sign. The construction is exactly the inclusion-induced, cardinality-grouped one-factor Markov transformation: its original subset coefficients satisfy \(\beta_{n,K}=\beta_{n,|K|}\).

All claims are for **every** deterministic triangular parameter array satisfying the one uniform ellipticity bound, with \(\mathsf Q\)-almost-every environment followed by \(\mathsf P\)-almost-sure statements. No corresponding claim is made for coefficients dependent across time or with ellipticity tending to zero.

## Proof

**1. Conditional row means and variance.** Condition on the entire sign trajectory \(\xi\), and write \(w(s)\) for the number of ones in the binary expansion of the nonnegative integer \(s\). By Lucas's parity criterion, exactly \(2^{w(s)}\) coefficients among \(\binom{s}{0},\ldots,\binom{s}{s}\) are odd. Since the Bernoulli rows are independent across \(n\), the variables \(\zeta_n\), \(n\ge1\), are independent under \(\mathsf Q(\cdot\mid\xi)\). Their conditional means are

\[
m_n(\xi)=\mathbb E_{\mathsf Q}[\zeta_n\mid\xi]
=\prod_{0\le k\le S_n:\ \binom{S_n}{k}\ {\rm odd}}(1-2p_{n,k}),
\qquad |m_n(\xi)|\le q^{2^{w(S_n)}},\quad q=1-2\epsilon<1.
\]
Their conditional variances are \(1-m_n(\xi)^2\). The convention \(0^r=0\) for \(r>0\) applies if \(q=0\).

**2. The conditional drift has subpolynomial total size.** The count \(S_n\) is nondecreasing, increases by one with probability \(1/2\) at each step, and visits each integer \(s\ge0\) for a geometric number \(H_s\) of consecutive times. The \(H_s\) are independent with \(\mathbb P(H_s>h)=2^{-h}\) for integer \(h\ge0\). Borel--Cantelli implies

\[
\max_{0\le s\le N}H_s=O(\log(N+2))\quad\mathsf P\text{-almost surely}.
\]
For \(N\) large put \(L_N=\lceil\log_2(N+1)\rceil\) and \(K_N=\lceil2\log_2\log(N+3)\rceil\). The number of integers in \([0,N]\) with at most \(K_N\) binary ones satisfies

\[
\#\{0\le s\le N:w(s)\le K_N\}
\le\sum_{j=0}^{K_N}\binom{L_N}{j}
\le(L_N+1)^{K_N+1}
=\exp\bigl(O((\log\log N)^2)\bigr)=N^{o(1)}.
\]
Consequently the number of times \(n\le N\) at which \(w(S_n)\le K_N\) is \(N^{o(1)}\), almost surely. On all remaining times, the first step gives \(|m_n|\le q^{2^{K_N+1}}\le\exp(-c_\epsilon(\log N)^2)\), with a positive constant \(c_\epsilon\). Therefore

\[
\sum_{n=1}^{N}|m_n(\xi)|\le N^{o(1)}
+N\exp(-c_\epsilon(\log N)^2)=N^{o(1)}
\quad\mathsf P\text{-almost surely}.
\]
In particular the conditional total variance satisfies

\[
V_N(\xi):=\sum_{n=1}^{N}(1-m_n(\xi)^2)=N-N^{o(1)}\sim N.
\]
Here \(N^{o(1)}\) means a bound smaller than \(N^\delta\) eventually for every fixed \(\delta>0\), with path-dependent constants; it is not an assertion of a particular finite-sample constant.

**3. Conditional law of the iterated logarithm.** For every trajectory satisfying Step 2, the variables \(\zeta_n-m_n(\xi)\) are independent, centered and bounded by two under \(\mathsf Q(\cdot\mid\xi)\). Their variance sum is asymptotic to \(N\). Kolmogorov's non-identically distributed law of the iterated logarithm applies because the uniform bound two is \(o(\sqrt{V_N/\log\log V_N})\). It gives upper and lower limits \(+1\) and \(-1\), respectively, with denominator \(\sqrt{2N\log\log N}\). The total drift is \(N^{o(1)}=o(\sqrt{N\log\log N})\), so the same limits hold for \(\sum_{n=1}^N\zeta_n\). By Fubini's theorem this joint almost-sure conclusion is, equivalently, a \(\mathsf P\)-almost-sure conclusion for \(\mathsf Q\)-almost every fixed environment. The extra deterministic \(\zeta_0=1\) has no effect, and \(\sum_{j=1}^N\xi_j\eta_j=\sum_{n=0}^{N-1}\zeta_n\), proving the displayed law.

**4. Quenched functional central limit theorem.** Fix any environment in the full-measure set of Step 3. Under \(\mathsf P\), the pair \((X_N,Y_N)\) is a two-dimensional martingale with increments \((\xi_j,\zeta_{j-1}\xi_j)\) and bounded jumps. Its predictable quadratic-covariation matrix at time \(N\) is

\[
\langle(X,Y)\rangle_N
=\begin{pmatrix}N&\sum_{n=0}^{N-1}\zeta_n\\
\sum_{n=0}^{N-1}\zeta_n&N\end{pmatrix}.
\]
The iterated-logarithm bound makes its off-diagonal entry \(o(N)\) almost surely. The same holds uniformly after rescaling on \([0,1]\): the partial sums have vanishing maximal rescaled size, by the pointwise convergence and the bounded increments. The diagonal entries converge to elapsed time, and the Lindeberg condition follows from bounded jumps. The martingale functional central limit theorem therefore gives two independent standard Brownian components.

## Verification

The included standalone script `checker.py` uses only the Python standard library. It enumerates the inclusion-induced subset sign product and its cardinality-folded parity expression for all sign words and row-bit choices through depth six; checks Lucas parity counts through \(s=1024\); enumerates exact rational conditional means through \(s=10\); checks exact two-row independence for small counts; and verifies combinatorial bounds for sparse binary-digit sets. Running `python3 checker.py` produced `PASS: 12002 exact assertions`. The infinite law of the iterated logarithm and the functional limit are proved analytically above, not inferred from those finite assertions.

## Relationship to prior work

Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, October 1, 2026), Corollary 9, prove **annealed** Brownian convergence under the same independent-time one-factor Markov assumptions. Their adjoining remark explicitly identifies the corresponding quenched question as unresolved and more difficult. Their Propositions 7 and 8 establish expectation and annealed second-moment conditions, rather than almost-sure conditional bracket control. The present argument obtains the latter with a sharp two-sided iterated-logarithm envelope.

The broad independent-subset environment theorem in Section 3 of that paper does not subsume this result: within each time level, coefficients of all subsets of the same cardinality are identified here, violating the independent-subset hypothesis. The totally-unordered model of Section 5 is a different basis and does not establish the inclusion-induced one-factor case. Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (arXiv:2010.16000; Electronic Journal of Probability, 2022), give a deterministic characterization of Brownian limits but do not verify its hypotheses for these random cardinality-grouped environments. The exact weak-limit criterion from that work is used here after establishing stronger pathwise control.

## Limitations

The conclusion is almost sure in the random environment, not uniform over individual environments; some deterministic environments can exhibit non-Gaussian limits. The theorem requires mutual independence across all time/cardinality coefficients and a uniform ellipticity bound. It does not resolve the time-constant cardinality-grouped model of Corollary 12 of Hamza and Tournier, nor establish a finite-sample normal-approximation rate. The use of the non-identically distributed Kolmogorov iterated-logarithm theorem and the martingale functional central limit theorem is classical; historical priority of this particular combination in the one-factor random bootstrap setting has not been independently certified.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first public October 1, 2026), especially Section 4.2, Corollary 9 and its remark. https://arxiv.org/html/2610.01658v1
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000 (2020); *Electronic Journal of Probability* 27, article 92 (2022), especially Theorem 6. https://arxiv.org/abs/2010.16000
3. *Law of the iterated logarithm*, Encyclopedia of Mathematics, statement of Kolmogorov's independent non-identically distributed bounded-increment version. https://encyclopediaofmath.org/wiki/Law_of_the_iterated_logarithm
