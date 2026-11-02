# The square-root overlap transition for missed super-coupons

## Finding

Suppose a round draws a uniformly random \(r\)-element subset of \([n]\), independently of other rounds, and declares all its \(s\)-subsets collected. For an \(s\)-subset \(A\), let \(U_A(k)\) be the indicator that \(A\) has never been collected after \(k\) rounds. Throughout the finite theorem, \(1\le s\le r<n\), \(k\ge1\), and \(A,B\) are \(s\)-subsets with intersection size \(j\).

Put
\[
 a=\frac{(r)_s}{(n)_s},\qquad
 b_j=\begin{cases}\displaystyle\frac{(r)_{2s-j}}{(n)_{2s-j}},&2s-j\le r,\\0,&2s-j>r.\end{cases}
\]
Here \((v)_t=v(v-1)\cdots(v-t+1)\) for \(0\le t\le v\). Then
\[
 \operatorname{Cov}(U_A(k),U_B(k))
 =(1-2a+b_j)^k-(1-a)^{2k},
 \quad
 \operatorname{sgn}\operatorname{Cov}(U_A(k),U_B(k))
 =\operatorname{sgn}(b_j-a^2).
\]
The sign is independent of the positive round count. As feasible overlap \(j\) increases from \(\max(0,2s-n)\) to \(s\), there is a **single sign transition**: an initial segment is strictly negative, at most one overlap value has zero covariance, and the final segment is strictly positive. In particular, two distinct *overlapping* targets can be negatively correlated.

The sharp dense-draw boundary \(r=n-1\) has the simple identity
\[
 \operatorname{Cov}(U_A(k),U_B(k))
 =\left(\frac{j}{n}\right)^k-\left(\frac{s^2}{n^2}\right)^k.
\]
Thus the sign switches exactly when overlap \(j\) crosses the expected intersection \(s^2/n\) of two independent uniform \(s\)-sets. For example, at \(n=20\), \(s=6\), \(r=19\), overlap \(j=1\) gives strictly negative covariance, while \(j=2\) gives strictly positive covariance at every \(k\ge1\).

More generally, suppose \(r=r_n\), \(s=s_n\) satisfy \(r_n/n\to\rho\in(0,1)\), \(s_n/\sqrt n\to c>0\); fix a nonnegative integer overlap \(j\). If \(k_n\) is any positive integer sequence with \(k_n a_n\to\lambda\in(0,\infty)\), then
\[
 \boxed{\quad\frac{b_{n,j}}{a_n^2}\longrightarrow
 R_j(c,\rho)=\rho^{-j}\exp\!\left(-\frac{1-\rho}{\rho}c^2\right),\quad}
\]
\[
 \boxed{\quad\frac{\operatorname{Cov}(U_A(k_n),U_B(k_n))}{a_n}
 \longrightarrow\lambda e^{-2\lambda}\bigl(R_j(c,\rho)-1\bigr).\quad}
\]
For any fixed \(j\ge1\), the eventual covariance is positive if
\[
 c^2<\frac{j\rho\log(1/\rho)}{1-\rho},
\]
and negative if the inequality is reversed. At equality, this leading-order limit alone does not determine the finite-size sign. Hence the square-root target-size scale has a nontrivial, tunable *overlap-dependent sign transition* despite temporal independence of drawing rounds.

**Global sign census.** Select two \(s_n\)-subsets independently and uniformly, and let \(J_n\) be their overlap. Then \(J_n\Rightarrow\operatorname{Poisson}(c^2)\). If
\[
 \tau(c,\rho)=\frac{c^2(1-\rho)}{\rho\log(1/\rho)}
\]
is not an integer, the fraction of ordered pairs of distinct target sets having *positive* covariance converges to
\[
 \boxed{\quad\mathbb P\{\operatorname{Poisson}(c^2)>\tau(c,\rho)\}.\quad}
\]
The complementary fraction has negative covariance; there are no zero-covariance overlaps for all sufficiently large \(n\) within every bounded overlap range. A concrete consequence is that at \(\rho=1/2\) and \(c=1\), the asymptotic positive fraction is \(1-2/e\), while the negative fraction is \(2/e\). **Even among pairs that overlap**, the limiting fraction with negative covariance is \(1/(e-1)\), which exceeds one half. This quantifies how often overlap fails to produce positive association, rather than merely exhibiting exceptional pairs.

## Assumptions and scope

Each of the \(k\) rounds draws afresh, uniformly over all \(\binom nr\) distinct \(r\)-subsets. A target becomes permanently collected on its first inclusion in a round. The two targets \(A,B\) are deterministic; feasible intersections satisfy \(\max(0,2s-n)\le j\le s\). The case \(j=s\) is \(A=B\) and is included to describe the whole covariance-sign geometry. The asymptotic statement uses **fixed** \(j\), \(\rho\) and \(c\), and the time scale \(k_n a_n\to\lambda>0\). It makes no assertion about joint dependence for a growing number of target sets or Gumbel cover-time asymptotics.

## Proof

**1. Exact joint law.** A fixed target is collected in one round with probability \(a\). Both targets are collected in the same round precisely when their union, of size \(2s-j\), is a subset of the drawn block; this has probability \(b_j\). Consequently, in one round the chance that neither is collected equals \(1-2a+b_j\). Independence across rounds yields
\[
 \mathbb P(U_A(k)=1)=(1-a)^k,
 \qquad
 \mathbb P(U_A(k)=U_B(k)=1)=(1-2a+b_j)^k.
\]
Subtracting the product of the marginals proves the covariance expression. Since \((1-a)^2=1-2a+a^2\) and positive integer powers preserve the order of nonnegative bases, its sign equals the sign of \(b_j-a^2\).

**2. One sign transition.** The union of two targets shrinks as \(j\) grows. The sequence \(b_j\) is nondecreasing in \(j\), and strictly increasing after its first positive term, because if \(L=2s-j\le r\),
\[
 \frac{b_{j+1}}{b_j}=\frac{n-L+1}{r-L+1}>1.
\]
At the largest intersection \(j=s\), \(b_s=a>a^2\), since \(0<a<1\).

At the smallest feasible intersection \(j_0=\max(0,2s-n)\), the covariance is negative. If \(j_0>0\), the union is all \(n\) points, so \(b_{j_0}=0\) because \(r<n\). If \(j_0=0\) and \(r<2s\), again \(b_0=0\). Otherwise \(2s\le r<n\) and
\[
 \frac{b_0}{a}=
 \prod_{i=0}^{s-1}\frac{r-s-i}{n-s-i}
 <\prod_{i=0}^{s-1}\frac{r-i}{n-i}=a.
\]
Every factor inequality is strict because \(r<n\). Thus \(b_0<a^2\). Monotonicity proves a single ordered negative/zero/positive transition, with at most one zero.

**3. The dense-draw identity.** For \(r=n-1\), each round omits exactly one uniformly random ground element. A target \(A\) remains unseen if and only if every omitted element belongs to \(A\), which occurs with probability \((s/n)^k\). Both \(A\) and \(B\) remain unseen exactly when every omission belongs to \(A\cap B\), with probability \((j/n)^k\). Subtracting the product of marginals proves the displayed formula and its sharp threshold \(j=s^2/n\).

**4. Critical square-root asymptotics.** Write \(\rho_n=r_n/n\). Uniformly for integer \(t=O(\sqrt n)\), the Taylor expansion of \(\log(1-x)\) gives
\[
 \log\frac{(r_n)_t}{(n)_t}
 =t\log\rho_n-
 \frac{t(t-1)}2\left(\frac1{r_n}-\frac1n\right)
 +O\!\left(\frac{t^3}{n^2}\right).
\]
The error is uniform because \(\rho_n\) stays bounded away from zero and one. Apply this at \(t=s_n\) and \(t=2s_n-j\); the latter is eventually at most \(r_n\). Subtracting twice the first expansion from the second gives
\[
 \log\frac{b_{n,j}}{a_n^2}
 =j\log\frac{n}{r_n}
 -\left(\frac1{r_n}-\frac1n\right)s_n^2+o(1)
 \longrightarrow j\log(1/\rho)-\frac{1-\rho}{\rho}c^2.
\]
Exponentiating gives \(R_j\). Since \(s_n\to\infty\) and \(\rho<1\), \(a_n\to0\), and \(b_{n,j}=a_n^2(R_j+o(1))\). Let \(\delta_n=b_{n,j}-a_n^2\) and \(h_n=(1-a_n)^2\). By the integral mean-value identity,
\[
 \frac{(h_n+\delta_n)^{k_n}-h_n^{k_n}}{a_n}
 =(k_n a_n)\frac{\delta_n}{a_n^2}
 \int_0^1(h_n+t\delta_n)^{k_n-1}\,dt.
\]
Here the integral converges to \(e^{-2\lambda}\) uniformly in \(t\in[0,1]\), because \(k_n a_n\to\lambda\) and \(\delta_n=O(a_n^2)\). The desired covariance limit follows. Its sign away from the critical equality follows from the already proved exact finite sign rule and \(b_{n,j}/a_n^2\to R_j\).

**5. Global sign census.** For independent uniform \(s_n\)-subsets, \(J_n\) has the hypergeometric intersection distribution. For each fixed positive integer \(m\),
\[
 \mathbb E[(J_n)_m]=\frac{(s_n)_m^2}{(n)_m}\longrightarrow c^{2m}.
\]
These are the factorial moments of \(\operatorname{Poisson}(c^2)\); the first moment bounds guarantee tightness, and the Poisson law is moment-determinate, proving \(J_n\Rightarrow\operatorname{Poisson}(c^2)\). If \(\tau(c,\rho)\notin\mathbb Z\), each fixed integer \(j\) has a strict limiting sign determined by \(j>\tau(c,\rho)\). Tightness permits truncation to finitely many overlap values, establishing the limiting positive and negative fractions. Conditioning on \(A\ne B\) changes these fractions by at most \(1/\binom n{s_n}\to0\). In the stated numerical specialization, \(\tau(1,1/2)=1/\log2\in(1,2)\) and \(J_n\Rightarrow\operatorname{Poisson}(1)\). Thus positive overlaps are \(j\ge2\); negative overlaps are \(j=0,1\). The probability of negative covariance conditional on nonempty overlap is \(\mathbb P(J=1\mid J\ge1)=1/(e-1)\). This completes the proof.

## Verification

The standalone standard-library script `CHECK.py` enumerates every drawn block for \(3\le n\le9\), all admissible \(s,r\), every feasible intersection, and three positive round counts. Using exact rational arithmetic, it verifies the single- and double-target inclusion probabilities, covariance sign, monotonic overlap ordering and the dense-draw formula. It also checks an exact two-sign finite example, numerical convergence of the critical factorial-ratio logarithms, and the global Poisson sign census. Run `python3 CHECK.py`; the recorded replay result is supplied in `VERIFICATION.md`. These finite computations do not replace the unrestricted proof.

## Relationship to prior work

Athreya, Mukherjee and Mukherjee introduced and analyzed this generalized coupon-collection scheme. Their proof of Lemma 3.1 already identifies the per-round inclusion probability of a pair of targets through its union size. That elementary input, and the general coupon-collection construction, are prior work. Their stated asymptotic theorems concern fixed target and block sizes; the present claim is the **complete covariance-sign ordering** for arbitrary finite parameters together with the proportional-block, square-root-target-size transition, the time-scaled covariance limit, and the asymptotic global fraction of negatively associated pairs. It does not claim that the known joint-inclusion count is new. The earlier random covering-design literature emphasizes covering thresholds and Poisson approximations. An equivalent covariance phase description in broader sampling or covering-design literature cannot be excluded.

## Limitations

The result assumes independent uniform block draws and exactly two prescribed targets. There is no extension here to temporally dependent Johnson-graph sampling, more than two joint noncoverage events, or a uniform approximation through the critical equality \(R_j=1\). The \(r=n-1\) threshold is an elementary dual representation and is presented as an explanatory exact boundary, not as an independent new cover-time theorem. The more general square-root phase has not been independently validated, and historical priority remains open.

## References

1. S. Athreya, S. Mukherjee, and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145 (first posted 3 April 2023), especially Section 3 and Lemma 3.1. https://arxiv.org/abs/2304.01145
2. S. Athreya, S. Mukherjee, and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, Journal of Theoretical Probability 38, article 54 (2025), DOI:10.1007/s10959-025-01417-w. https://doi.org/10.1007/s10959-025-01417-w
3. A. P. Godbole and S. Janson, *Random covering designs*, Journal of Combinatorial Theory, Series A 75 (1996), 85–98, DOI:10.1006/jcta.1996.0065. https://doi.org/10.1006/jcta.1996.0065
