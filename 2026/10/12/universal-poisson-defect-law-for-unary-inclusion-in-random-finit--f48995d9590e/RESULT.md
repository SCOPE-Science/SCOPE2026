# Universal Poisson defect law for unary inclusion in random finite teams

## Finding

**Theorem (exact law and universal Poisson criterion).** For each integer \(n\ge1\), independently retain each ordered pair in \([n]^2\) with probability \(p_n\in[0,1]\). Let \(T_n\) be the resulting team on variables \(x,y\), put \(q_n=1-p_n\), and define
\[
W_n=\big|\pi_x(T_n)\setminus\pi_y(T_n)\big|,\qquad
\lambda_n=nq_n^n(1-q_n^{n-1}).
\]
For every integer \(0\le k\le n\), its falling factorial moments are exactly
\[
\mathbb E[(W_n)_{\underline k}]
=(n)_{\underline k}q_n^{nk}(1-q_n^{n-k})^k.
\tag{1}
\]
In particular, the entire finite distribution is given by
\[
\mathbb E[z^{W_n}]
=\sum_{k=0}^{n}\binom nk q_n^{nk}
(1-q_n^{n-k})^k(z-1)^k,
\tag{2}
\]
and the probability that the team satisfies the unary inclusion atom \(x\subseteq y\) is equation (2) at \(z=0\). For every sequence of probabilities \((p_n)\), without any regularity assumption, the following implications hold:

- If \(\lambda_n\to\lambda\in[0,\infty)\), then \(W_n\) converges in distribution to \(\mathrm{Poisson}(\lambda)\) and \(\Pr(T_n\models x\subseteq y)\to e^{-\lambda}\).
- If \(\lambda_n\to\infty\), then \(\Pr(T_n\models x\subseteq y)\to0\).

Moreover, when \(n\ge2\) the defect indicators are pairwise negatively correlated, and \(\mathrm{Var}(W_n)\le\lambda_n\). The result identifies two critical windows:
\[
\begin{array}{ll}
 n^2p_n\to a\in[0,\infty)&\Longrightarrow\Pr(T_n\models x\subseteq y)\to e^{-a},\\[2pt]
 np_n-\log n\to t\in\mathbb R&\Longrightarrow\Pr(T_n\models x\subseteq y)\to\exp(-e^{-t}).
\end{array}
\tag{3}
\]
Outside them, \(n^2p_n\to0\) implies satisfaction tends to \(1\); \(n^2p_n\to\infty\) together with \(np_n-\log n\to-\infty\) implies satisfaction tends to \(0\); and \(np_n-\log n\to\infty\) implies satisfaction tends to \(1\). The two windows have different mechanisms but one common obstruction count.

## Assumptions and scope

A team is a set, not a multiset, of assignments; no probabilistic independence between rows or between projections is assumed beyond independence of the original \(n^2\) pair-inclusion trials. Diagonal pairs are permitted. Empty teams satisfy the inclusion atom. For \(p_n=0\) or \(p_n=1\), and also for \(n=1\), there are no defects. The notation \((u)_{\underline k}=u(u-1)\cdots(u-k+1)\) includes \((u)_{\underline0}=1\). The conventions \(0^0=1\) in finite empty products and in expressions arising at endpoints ensure all displayed finite sums remain well defined. Limit assertions concern \(n\to\infty\); no fixed-probability asymptotics are substituted for moving probability sequences.

## Proof

**Exact finite law.** Write \(B_i\) for the event that row \(i\) is nonempty while column \(i\) is empty, so \(W_n=\sum_{i=1}^n\mathbf1_{B_i}\). Fix a subset \(S\subseteq[n]\) with \(|S|=k\). On \(\bigcap_{i\in S}B_i\), all \(nk\) entries in the columns indexed by \(S\) are forced absent. This event has probability \(q_n^{nk}\). Each of the \(k\) selected rows must contain a present entry among the other \(n-k\) columns. The corresponding sets of Bernoulli trials are disjoint across rows, and their probability contribution is \((1-q_n^{n-k})^k\). Thus
\[
\Pr\Big(\bigcap_{i\in S}B_i\Big)
=q_n^{nk}(1-q_n^{n-k})^k.
\tag{4}
\]
Summing over ordered \(k\)-tuples of distinct indices proves (1). Expanding \(z^{W_n}=\prod_{i=1}^n[1+(z-1)\mathbf1_{B_i}]\) and applying (4) proves (2). Taking \(k=1\) in (1) gives \(\lambda_n=\mathbb EW_n\), since \(B_i\) has no allowed diagonal edge.

**Variance bound.** For distinct \(i,j\), equation (4) yields
\[
\Pr(B_i\cap B_j)=q_n^{2n}(1-q_n^{n-2})^2
\le q_n^{2n}(1-q_n^{n-1})^2=\Pr(B_i)\Pr(B_j).
\]
Summing covariances shows \(\operatorname{Var}(W_n)\le\sum_i\operatorname{Var}(\mathbf1_{B_i})\le\lambda_n\), including endpoints by continuity. Hence, if \(\lambda_n\to\infty\), Chebyshev's inequality gives
\(\Pr(W_n=0)\le\operatorname{Var}(W_n)/\lambda_n^2\le1/\lambda_n\to0\).

**Universal Poisson law.** If \(\lambda_n\to0\), Markov's inequality gives \(\Pr(W_n>0)\le\lambda_n\to0\). Suppose instead \(\lambda_n\to\lambda\in(0,\infty)\). Since \(q_n^n\ge\lambda_n/n\), necessarily \(q_n\to1\); equivalently \(p_n\to0\). For any fixed integer \(k\ge1\), and all sufficiently large \(n\), the ratio
\[
R_{n,k}=\frac{1-q_n^{n-k}}{1-q_n^{n-1}}
\]
converges to \(1\). Indeed, for \(k\ge2\) and \(0<p_n<1\),
\[
0\le1-R_{n,k}
=\frac{q_n^{n-k}(1-q_n^{k-1})}{1-q_n^{n-1}}
\le\frac{k-1}{n-1}q_n^{2-k}\longrightarrow0,
\tag{5}
\]
where \(1-q_n^{k-1}\le(k-1)p_n\) and \(1-q_n^{n-1}\ge(n-1)p_nq_n^{n-2}\); for \(k=1\) the ratio is exactly \(1\). Also \((n)_{\underline k}/n^k\to1\). Dividing (1) by \(\lambda_n^k\), we therefore obtain \(\mathbb E[(W_n)_{\underline k}]\to\lambda^k\) for every fixed \(k\). These are the factorial moments of a Poisson random variable; because its distribution is moment-determinate, the method of moments proves \(W_n\Rightarrow\mathrm{Poisson}(\lambda)\). Since the variables are nonnegative integer-valued, convergence in distribution implies convergence of their probabilities of being zero.

**Windows and phase boundaries.** If \(n^2p_n\to a<\infty\), then \(np_n\to0\), \(q_n^n\to1\), and
\[
\lambda_n=nq_n^n(1-q_n^{n-1})\sim n(n-1)p_n\to a
\]
when \(a>0\), while the same limit follows directly for \(a=0\). If \(np_n-\log n\to t\), then \(p_n\to0\), \(np_n^2\to0\), \(q_n^n=\exp(-np_n+o(1))\), and \(1-q_n^{n-1}\to1\), giving \(\lambda_n\to e^{-t}\). This proves (3).

For the intervening regime, write \(u_n=np_n\). Our assumptions force \(p_n\le\log n/n\) eventually and \(p_n\to0\). If \(u_n\le1\), then \(q_n^n\) is bounded below and \(1-q_n^{n-1}\ge c_1u_n\) for some absolute \(c_1>0\), whence \(\lambda_n\ge c_2n^2p_n\to\infty\). If \(u_n>1\), then \(1-q_n^{n-1}\ge c_3>0\), and
\[
\log(nq_n^n)=\log n+ n\log(1-p_n)=\log n-u_n+O(np_n^2)\to\infty,
\]
because \(np_n^2\le(\log n)^2/n\to0\). Thus \(\lambda_n\to\infty\) in either case. Finally \(\lambda_n\le n\exp(-np_n)\to0\) if \(np_n-\log n\to\infty\). This completes the proof.

## Verification

Run `python3 verify.py` using Python 3, with no third-party dependencies. It exhaustively visits all binary teams of orders \(1\) through \(4\), compares exact rational-valued coefficients of (2) against direct enumeration at probabilities \(0,1/3,1/2,2/3,1\), tests all factorial moments and the covariance inequality, and compares the support of the computed histograms. It processes \(66{,}066\) teams and validates \(20\) rational-probability instances; expected final line: `VERIFY_OK teams 66066 rational_parameter_cases 20 exact_probability_coefficients 70`. The infinite convergence proof is deductive, not inferred from these tests.

## Relationship to prior work

Hannula and Hella [1] define and study unary inclusion atoms \(x\subseteq y\), including the computational complexity of their maximal-subteam and model-checking problems. Hannula, Kontinen, and Link [2] study implication and axiomatization interactions involving inclusion dependencies and independence atoms. Neither inspected manuscript states a Bernoulli-team defect distribution or the universal parameter-dependent Poisson classification in equations (1)–(3). Classical degree-count and rare-event Poisson results for random graphs [3] show that some components of the asymptotic method belong to an established broader probabilistic tradition; this result's proposed contribution is the *combined exact defect law and its uniform classification of the two inclusion-reliability windows* for a single logical constraint.

## Limitations

The finite model samples a binary relation with independent entries, and does not address database generators with functional, cardinality, or key constraints, multiple interacting inclusion atoms, or multiset semantics. The model contains loops (diagonal entries). The originality comparison cannot rule out an equivalent result in older directed-random-graph literature stated solely in graph-theoretic terminology. Finite enumerations do not independently certify the limiting distributions. No independent mathematical or originality validation has been performed.

## References

1. M. Hannula and L. Hella, *Complexity Thresholds in Inclusion Logic*, arXiv:1903.10706v1 (first public 2019-03-26), https://arxiv.org/html/1903.10706v1.
2. M. Hannula, J. Kontinen, and S. Link, *On the Interaction of Functional and Inclusion Dependencies with Independence Atoms*, arXiv:2101.02466v1 (2021), https://arxiv.org/html/2101.02466v1.
3. W. Kordecki, *Poisson convergence of numbers of vertices of a given degree in random graphs*, Discussiones Mathematicae Graph Theory 16 (1996), 157–172, https://eudml.org/doc/270487. Its accessible summary describes random-graph degree counts, not the inclusion-specific exact law.
