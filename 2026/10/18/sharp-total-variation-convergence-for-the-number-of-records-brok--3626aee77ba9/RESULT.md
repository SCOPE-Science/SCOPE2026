# Sharp total-variation convergence for the number of records broken by an observation

## Finding

Let \(X_0,X_1,\ldots\) be independent identically distributed random variables with a continuous distribution. A *current record* at time \(n-1\) is an index \(i\in\{0,\ldots,n-1\}\) such that \(X_i> X_j\) for every \(i<j<n\). Let \(B_n\) count these records destroyed when \(X_n\) arrives, with \(n\ge1\). Let \(G\) be geometric on \(\{0,1,\ldots\}\) with \(\Pr(G=k)=2^{-k-1}\). Let
\[
K_n=\sum_{j=1}^n I_j,\qquad I_j\text{ independent},\quad \Pr(I_j=1)=1/j,
\]
with \(G\) independent of \(K_n\); write \(a_{n,k}=\Pr(K_n=k)\) and set \(a_{n,k}=0\) off its support.

**Exact finite-horizon identity.** For every integer \(n\ge1\), the probability-generating function is
\[
\mathbb E[z^{B_n}]=\frac{1}{2-z}+\frac{1-z}{(n+1)(2-z)}\prod_{j=1}^n\left(1+\frac{z-1}{j}\right).
\]
In particular, the signed law difference is exactly
\[
\Pr(G=k)-\Pr(B_n=k)=\frac{\Pr(K_n+G=k)-a_{n,k}}{n+1},\qquad k\ge0.
\]
The two probability mass functions of \(B_n\) and \(G\) have a **single sign crossing** (zero entries permitted). Their total-variation and Kolmogorov distances coincide and admit the finite formula
\[
\boxed{\ d_{\rm TV}(B_n,G)=d_{\rm K}(B_n,G)
=\frac{1}{n+1}\max_{k\in\mathbb Z}\sum_{r=0}^{\infty}2^{-r-1}a_{n,k-r}.\ }
\]
The sum is finite for every \(k\). Finally, the sharp asymptotic constant is
\[
\boxed{\ \lim_{n\to\infty}n\sqrt{\log n}\,d_{\rm TV}(B_n,G)=\frac1{\sqrt{2\pi}}.\ }
\]
Consequently, the geometric approximation error decays at the precise order \(1/(n\sqrt{\log n})\), not merely at order \(1/n\). The mean satisfies \(\mathbb E B_n=n/(n+1)\).

## Assumptions and scope

Only independence, identical distribution, and continuity of the observation law are assumed. Continuity removes ties, and the probability integral transform reduces the entire problem to i.i.d. uniform observations. The model uses the deterministic time coordinate and a scalar observed value: it is different from randomly sampled bivariate Pareto records. The distances above are between probability laws on the nonnegative integers, with \(d_{\rm TV}(P,Q)=\frac12\sum_k|P\{k\}-Q\{k\}|\) and \(d_{\rm K}(P,Q)=\sup_k|P(( -\infty,k])-Q(( -\infty,k])|\). The logarithm is natural.

## Proof

**1. A random-length record-count representation.** By the probability integral transform suppose \(X_i\sim\operatorname{Uniform}(0,1)\). Reading the past backwards from time \(n-1\), let \(J_n\) be the number of consecutive past values smaller than \(X_n\), stopping at the first larger past value or at the beginning of the sample. Every destroyed current record is a reverse record among those \(J_n\) values, and there are no other destroyed records. Integration over \(X_n=u\) gives
\[
\Pr(J_n=j)=\int_0^1 u^j(1-u)\,du=\frac1{(j+1)(j+2)}\quad(0\le j<n),
\qquad \Pr(J_n=n)=\int_0^1u^n\,du=\frac1{n+1}.
\]
Conditional on \(J_n=j\), the relative order of the \(j\) stopped values is uniform. Successive relative ranks are mutually independent and uniform on \(\{1,\ldots,i\}\) at length \(i\): one can construct a uniform random permutation by independently inserting its entries at uniformly selected ranks. Therefore the reverse-record count has the law of \(K_j\), with polynomial
\[
A_j(z)=\mathbb E[z^{K_j}]=\prod_{i=1}^j\left(1+\frac{z-1}{i}\right),\quad A_0(z)=1.
\]
Writing \(F_n(z)=\mathbb E[z^{B_n}]\), the mixture becomes
\[
F_n(z)=\sum_{j=0}^{n-1}\frac{A_j(z)}{(j+1)(j+2)}+\frac{A_n(z)}{n+1}.
\]
For \(F_0(z)=1\), subtraction and \(A_n(z)-A_{n-1}(z)=(z-1)A_{n-1}(z)/n\) give
\[
F_n(z)-F_{n-1}(z)=\frac{z-1}{n(n+1)}A_{n-1}(z).
\]
The polynomial identity
\[
(2-z)F_n(z)=1+\frac{1-z}{n+1}A_n(z)
\]
holds at \(n=0\) and has exactly the preceding increments after division by \(2-z\); induction proves it for all \(n\ge0\). Rearrangement yields the displayed generating-function and signed-law identities. Although rationally displayed, \(F_n\) is a polynomial: \(A_n(2)=n+1\), so the apparent pole cancels. Differentiating at \(z=1\) gives the stated mean.

**2. A single crossing and exact distance.** For \(n\ge1\), \(A_n(z)=z\prod_{i=2}^n(z+i-1)/i\) has only nonpositive real zeros, so \(a_{n,k}>0\) on \(1\le k\le n\) and is log-concave. Let \(b_{n,k}=\Pr(K_n+G=k)\). For \(1\le k\le n\),
\[
\frac{b_{n,k}}{a_{n,k}}=\sum_{r=0}^{k-1}2^{-r-1}\frac{a_{n,k-r}}{a_{n,k}}.
\]
Log-concavity makes every ratio \(a_{n,k-r}/a_{n,k}\) nondecreasing in \(k\) when defined: it is a product of \(r\) successive nondecreasing ratios \(a_{n,j-1}/a_{n,j}\). Additional summands are nonnegative. The above ratio therefore increases with \(k\). At \(k=1\), it equals \(1/2<1\), whereas \(b_{n,k}>a_{n,k}=0\) for all \(k>n\). Thus \(b_{n,k}-a_{n,k}\) switches sign at most once, from negative to positive. By the exact signed-law identity, so does \(\Pr(G=k)-\Pr(B_n=k)\).

Since \(G\ge0\), the law of \(K_n+G\) stochastically dominates that of \(K_n\). With the single crossing, total variation equals the maximal CDF difference. For any integer \(k\), conditioning on \(G\) yields
\[
\Pr(K_n\le k)-\Pr(K_n+G\le k)
=\mathbb E\left[\sum_{r=0}^{G-1}a_{n,k-r}\right]
=\sum_{r=0}^{\infty}2^{-r-1}a_{n,k-r}.
\]
Dividing by \(n+1\) establishes the claimed exact formula and equality of both distances. This is an exact finite calculation using at most \(n\) nonzero coefficients for each \(k\); the global maximum need only consider \(1\le k\le n\), because the expression strictly decreases geometrically for \(k\ge n\).

**3. Sharp asymptotics.** Put \(\mu_n=H_n\) and \(v_n=H_n-H_n^{(2)}\), where \(H_n=\sum_{j=1}^n1/j\) and \(H_n^{(2)}=\sum_{j=1}^n1/j^2\). Then \(\mathbb EK_n=\mu_n\), \(\operatorname{Var}(K_n)=v_n\sim\log n\). A uniform lattice local central limit theorem applies:
\[
\sup_{k\in\mathbb Z}\left|\sqrt{v_n}\,a_{n,k}-\frac1{\sqrt{2\pi}}\exp\left(-\frac{(k-\mu_n)^2}{2v_n}\right)\right|\longrightarrow0.
\]
For completeness, Lyapunov's condition follows because the sum of third absolute centered moments of the independent Bernoulli terms is at most \(v_n\). The Fourier product satisfies
\[
|\mathbb E[e^{itK_n}]|\le\exp\{-2v_n\sin^2(t/2)\},\qquad |t|\le\pi,
\]
which gives the needed integrable Gaussian domination under Fourier inversion after scaling \(t\) by \(v_n^{-1/2}\). Consequently,
\[
\max_k a_{n,k}\sim\frac1{\sqrt{2\pi v_n}}.
\]
The geometric weights in the exact formula sum to one; hence its inner maximum is at most \(\max_k a_{n,k}\). Conversely, choose the nearest integer \(k_n\) to \(\mu_n\). For each fixed \(r\), the local theorem gives \(a_{n,k_n-r}\sim1/\sqrt{2\pi v_n}\). Keeping the first \(R\) terms in the exact expression produces a lower asymptotic factor \(1-2^{-(R+1)}\). Letting \(R\to\infty\) proves that the inner maximum is asymptotic to \(1/\sqrt{2\pi v_n}\). Since \(v_n\sim\log n\), the boxed sharp constant follows.

## Verification

The standard-library program `verify.py` independently constructs the reverse-record mixture using rational arithmetic, checks the polynomial identity and signed convolution through high degrees, and enumerates all distinct-rank observation orderings for \(1\le n\le7\). It also computes the exact finite-distance formula and numerical normalized distances for a sequence of increasing \(n\). The symbolic computations verify finitely many inputs only; the universal and asymptotic claims follow from the proofs above.

For example, \(n=2\) gives \(\Pr(B_2=0,1,2)=(1/2,1/3,1/6)\) and \(d_{\rm TV}(B_2,G)=1/8\). The count at \(n=1\) is Bernoulli with parameter \(1/2\) and its distance to \(G\) is \(1/4\).

## Relationship to prior work

Naiman and Torcaso (arXiv:2210.08426, posted 16 October 2022) established the geometric limiting law for exactly this deterministic-time, scalar-observation record-breaking statistic. Their main theorem is qualitative pointwise convergence; their displayed computations concern particular fixed counts. The exact finite-horizon generating-function identity, the one-crossing formula, and the sharp global total-variation rate above are additional statements and are not consequences of qualitative convergence alone.

Fill (arXiv:1901.08232) proved a geometric conditional limit and refined point-probability estimates for **i.i.d. bivariate random Pareto observations**. In that model, the arriving observation need not be a new Pareto record and the count is conditioned on record setting. The deterministic-time model here makes the new point current automatically and has a distinct finite law: its no-break probability is exactly \(1/2\) at every positive horizon. The related bivariate full-kill Stirling identity appearing in a published mathematical record concerns the bivariate model, not this total-variation formula. Classical independence of reverse-record indicators and the local central limit theorem are standard tools, not claimed as new.

## Limitations

No claim is made for observations with atoms or for heterogeneous, dependent, or vector-valued observations. The formula and asymptotic are distribution-free only within the specified i.i.d. continuous class. The history search and material inspected do not certify absolute novelty; differently indexed literature may contain an equivalent statement. The local-CLT proof applies to \(n\to\infty\); the exact formula handles each positive integer \(n\) separately. Independent mathematical review has not been performed.

## References

1. D. Q. Naiman and F. Torcaso, *A Geometric(1/2) Distribution Associated with Record Breaking*, arXiv:2210.08426v1 (first posted 2022-10-16), https://arxiv.org/abs/2210.08426 ; full open-access HTML at https://arxiv.org/html/2210.08426v1.
2. J. A. Fill, *Breaking Bivariate Records*, arXiv:1901.08232v1 (first posted 2019-01-24), https://arxiv.org/abs/1901.08232 ; published in *Combinatorics, Probability and Computing* 30 (2021), 105–123.
