# Sharp exponential loss of long-block fidelity in a two-pattern surrogate of irrational rotation

## Finding

Fix any irrational number \(0<\alpha<1/2\). The stationary ordinal-pattern process of the irrational rotation \(x\mapsto x+\alpha\pmod 1\) has zero entropy, while its exact two-pattern first-order transition walk is a primitive, exponentially mixing Markov chain of strictly positive entropy \(h_\alpha\). The two processes have identical one- and two-pattern laws, yet their length-\(n\) laws \(P_n\) and \(Q_n\) satisfy

\[
\lim_{n\to\infty}-\frac1n\log\bigl(1-\lVert P_n-Q_n\rVert_{\mathrm{TV}}\bigr)=h_\alpha>0.
\]

More precisely, for positive finite constants \(c_\alpha,C_\alpha\) and every sufficiently large \(n\),

\[
c_\alpha e^{-nh_\alpha}\le1-\lVert P_n-Q_n\rVert_{\mathrm{TV}}\le C_\alpha(n+1)e^{-nh_\alpha}.
\]

There is also an exact finite-length relative-entropy identity

\[
D(P_n\Vert Q_n)=H_{\mathrm b}(\alpha)+(n-1)h_\alpha-H(P_n),
\quad
\lim_{n\to\infty}\frac{D(P_n\Vert Q_n)}n=h_\alpha,
\]

where \(H\) is Shannon entropy with natural logarithms and \(H_{\mathrm b}\) is binary entropy. Thus exact adjacent-pair matching and an arbitrarily long stationary training sequence do not prevent exponentially severe long-block mismatch in a simple, deterministic quasiperiodic signal.

## Assumptions and scope

Let \(\mathbb T=\mathbb R/\mathbb Z\), represented by \([0,1)\), with normalized Lebesgue probability \(m\). Choose \(x_0\) with law \(m\), and set \(x_t=\{x_0+t\alpha\}\) for every nonnegative integer \(t\). Define the delay-one order-two ordinal symbol \(Z_t=U\) if \(x_t<x_{t+1}\), and \(Z_t=D\) otherwise. Because \(\alpha\) is irrational, ties never occur. The exact coding is

\[
Z_t=D\quad\Longleftrightarrow\quad x_t\in[1-\alpha,1),
\]

which fixes the boundary convention and makes no difference to the probability laws. Let \(P_n\) be the law of \((Z_0,\ldots,Z_{n-1})\). Let \(Q_n\) be the law on \(\{U,D\}^n\) of the stationary order-one Markov chain whose initial probabilities and transition probabilities are obtained exactly from \(P_1\) and \(P_2\). At order two and delay one, the overlap-compatibility state consists of just the immediately preceding ordinal symbol; any two consecutive binary ordinal comparisons are logically realizable. Hence this is exactly the corresponding compatibility-conditioned pattern-network walk, not an unconstrained replacement of a longer-state algorithm.

Put

\[
a=\frac{1-2\alpha}{1-\alpha},\qquad b=\frac\alpha{1-\alpha},\qquad
h_\alpha=-(1-2\alpha)\log a-\alpha\log b=(1-\alpha)H_{\mathrm b}(b).
\]

Here \(a,b\in(0,1)\) and \(a+b=1\); all exponential-rate assertions refer to fixed \(\alpha\) and \(n\to\infty\). Total variation is normalized by \(\lVert P-Q\rVert_{\mathrm{TV}}=\frac12\sum_w|P(w)-Q(w)|\). No assertion is made for a rational rotation, for an arbitrary observable or for ordinal orders above two.

## Proof

**1. Exact transition walk.** The event \(D\) has length \(\alpha\). Since \(\alpha<1/2\), two successive decreases are impossible. The exact adjacent-pair probabilities, in \((U,D)\) order, are \(1-2\alpha,\alpha,\alpha,0\). Thus the stationary law and transition matrix are

\[
\pi=(1-\alpha,\alpha),\qquad M=\begin{pmatrix}a&b\\1&0\end{pmatrix}.
\]

The self-loop at \(U\), together with both directed edges between \(U\) and \(D\), makes \(M\) primitive; its eigenvalues are \(1\) and \(-b\). Its entropy rate is \(h_\alpha>0\), and its nontrivial temporal dependence decays geometrically at rate \(b\).

**2. Exact size of the true language.** For the first \(n\) comparisons, the coding may change only at the distinct circle points \(\{-j\alpha\}\), with \(j=0,1,\ldots,n\). Thus \(P_n\) has at most \(n+1\) words in its support \(S_n\). For every starting point the number of decreases in the first \(n\) steps is

\[
k_n=\sum_{t=0}^{n-1}\bigl(\lfloor x_0+(t+1)\alpha\rfloor-\lfloor x_0+t\alpha\rfloor\bigr)
=\lfloor x_0+n\alpha\rfloor-\lfloor x_0\rfloor.
\]

Consequently \(k_n/n\to\alpha\) for every orbit. A periodic or eventually periodic binary sequence has a rational limiting symbol frequency, whereas \(\alpha\) is irrational. By the elementary Morse–Hedlund word-complexity criterion, any non-eventually-periodic one-sided sequence contains at least \(n+1\) distinct words of length \(n\). Irrational-rotation unique ergodicity ensures every admissible finite word occurring along an orbit has positive measure; this also follows by taking a point in an interior cylinder arc and using density of rotations. It follows that \(|S_n|=n+1\) and every word in \(S_n\) has positive probability. In particular \(H(P_n)\le\log(n+1)\), so the source entropy rate is zero.

**3. Uniform exponential weight of true words under the walk.** For any \(w\in S_n\) put \(k=\#\{t:w_t=D\}\), \(f=\mathbf1_{w_0=D}\), and \(e=\mathbf1_{w_{n-1}=D}\). Since \(DD\) cannot occur, the numbers of \(U\to U\) and \(U\to D\) transitions are respectively \(n-1-2k+f+e\) and \(k-f\); each \(D\to U\) transition has probability one. Therefore the exact walk probability is

\[
Q_n(w)=\pi_{w_0}\,a^{n-1-2k+f+e}b^{k-f}.
\]

The telescoping identity implies \(|k-n\alpha|<1\). Writing \(\varepsilon=k-n\alpha\), direct subtraction gives

\[
\log Q_n(w)+nh_\alpha
=\log\pi_{w_0}+(-1-2\varepsilon+f+e)\log a+(\varepsilon-f)\log b.
\]

The right side has absolute value at most the finite, explicit constant

\[
K_\alpha=\max\{|\log\alpha|,|\log(1-\alpha)|\}+3|\log a|+2|\log b|.
\]

Hence, for all \(n\ge1\) and \(w\in S_n\),

\[
e^{-K_\alpha}e^{-nh_\alpha}\le Q_n(w)\le e^{K_\alpha}e^{-nh_\alpha}.
\]

**4. Sharp total-variation rate.** Since \(P_n\) is supported exactly on \(S_n\), the overlap identity is

\[
1-\lVert P_n-Q_n\rVert_{\mathrm{TV}}
=\sum_{w\in S_n}\min\{P_n(w),Q_n(w)\}.
\]

The preceding bound gives the upper bound \((n+1)e^{K_\alpha}e^{-nh_\alpha}\). Choose a word \(w_n\in S_n\) attaining maximal true mass. Necessarily \(P_n(w_n)\ge1/(n+1)\), whereas \(Q_n(w_n)\le e^{K_\alpha}e^{-nh_\alpha}\). Since \(h_\alpha>0\), for all sufficiently large \(n\), the latter is below the former. The overlap is then at least \(Q_n(w_n)\ge e^{-K_\alpha}e^{-nh_\alpha}\). Set \(c_\alpha=e^{-K_\alpha}\), \(C_\alpha=e^{K_\alpha}\) and take logarithms divided by \(n\). This proves the stated sharp limit.

**5. Exact relative entropy.** Because \(Q_n(w)=\pi_{w_0}\prod_{t=0}^{n-2}M_{w_t,w_{t+1}}\) for every true word and because the true process shares the same one- and two-symbol marginals, the \(P_n\)-cross entropy of \(Q_n\) equals \(H_{\mathrm b}(\alpha)+(n-1)h_\alpha\). Subtracting \(H(P_n)\) gives the identity. The bound \(0\le H(P_n)\le\log(n+1)\) proves the relative-entropy rate.

The two distributions agree at lengths one and two by construction. Nevertheless the law of the symbolic source has zero entropy and the walk has strictly positive entropy. This is a separation of dynamical statistics, not a claim about predictive or computational usefulness of the walk.

## Verification

Run `python3 CHECK.py` with Python's standard library. The program forms all \(n+1\) rotation-cut intervals for several explicit irrational choices and lengths through \(n=60\); it verifies the exact pair law, absence of successive decreases, word-count, transition-product formula, the weight bounds, and the finite-length relative-entropy identity. These are finite corroborations only; the arbitrary-irrational and all-length statements above follow from the proof.

## Relationship to prior work

Potratzki, de Jong, Small and Bröhl (2026) formalize compatibility-conditioned random walks on ordinal pattern transition networks and study their ergodicity-based fading memory and forecasting uses; their discussion explicitly leaves preservation of further source invariants open. This work analyzes the special order-two, delay-one case and derives an exact exponential failure of *long-block law fidelity*, without disputing that the network defines a valid symbolic computational reservoir. Unakafov and Keller (2014) investigate ordinal conditional entropy and the distinction between finite-order transitions and asymptotic metric entropy. Sakellariou, Stemler and Small (2019, 2021) construct Markov/entropy interpretations of ordinal networks; Hirata, Shiro and Amigó (2019) investigate finite-order-preserving ordinal surrogates. Those broad mechanisms are antecedents; the present quantified rotation-specific block total-variation and Kullback–Leibler law is not asserted to be a consequence stated in those publications. The 2019 Markov-modeling paper could not be reviewed in full and is a residual priority risk.

## Limitations

The theorem uses the ideal population transition probabilities, not finite-data estimators. It concerns an irrational rotation with the fractional-part observable, order-two consecutive comparisons, and a stationary first-order walk. The exponent depends on the fixed rotation rate; no bound uniform as \(\alpha\to0\) or \(\alpha\to1/2\) is claimed. Total variation compares joint block distributions, not a particular trained predictor's empirical success. Specialized earlier work on Sturmian Markov approximations or ordinal surrogates may contain closely related estimates; historical priority requires further external scrutiny. Independent scientific validation has not been performed.

## References

1. M. Potratzki, T. G. de Jong, M. Small, T. Bröhl, *Ordinal Pattern Transition Networks as a Symbolic Substrate for Reservoir Computing*, arXiv:2610.21973v1 (15 October 2026), https://arxiv.org/html/2610.21973v1.
2. A. M. Unakafov and K. Keller, *Conditional entropy of ordinal patterns*, arXiv:1407.5390 (2014), https://arxiv.org/abs/1407.5390.
3. K. Sakellariou, T. Stemler and M. Small, *Markov modeling via ordinal partitions: An alternative paradigm for network-based time-series analysis*, Physical Review E **100**, 062307 (2019), doi:10.1103/PhysRevE.100.062307.
4. K. Sakellariou, T. Stemler and M. Small, *Estimating topological entropy using ordinal partition networks*, Physical Review E **103**, 022214 (2021), doi:10.1103/PhysRevE.103.022214.
5. Y. Hirata, M. Shiro and J. M. Amigó, *Surrogate Data Preserving All the Properties of Ordinal Patterns up to a Certain Length*, Entropy **21**, 713 (2019), doi:10.3390/e21070713.
