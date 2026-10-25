# One-crossing reinforced occupancy covariance, exact zeros, and noncommuting critical fractions

## Finding

For integers \(m\ge3\), \(n\ge2\), and a real concentration \(\alpha>0\), draw a probability vector \(P\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\), and then sample \(n\) categorical observations independently conditional on \(P\). Equivalently, sample sequentially from a symmetric reinforced Pólya urn. Let \(N_i\) be the number of occurrences of color \(i\), let \(Z=\#\{i:N_i=0\}\), and let \(X_r=\#\{i:N_i=r\}\) for \(1\le r\le n\).

Define rising factorials \((a)^{\overline j}=\prod_{h=0}^{j-1}(a+h)\) (with the empty product equal to one), and put
\[
 u=\frac{((m-1)\alpha)^{\overline n}}{(m\alpha)^{\overline n}},\quad
 v_r=\binom nr\frac{(\alpha)^{\overline r}((m-1)\alpha)^{\overline{n-r}}}{(m\alpha)^{\overline n}},\quad
 w_r=\binom nr\frac{(\alpha)^{\overline r}((m-2)\alpha)^{\overline{n-r}}}{(m\alpha)^{\overline n}}.
\]
These are respectively \(\Pr(N_1=0)\), \(\Pr(N_1=r)\), and \(\Pr(N_1=0,N_2=r)\). The exact finite-sample covariance is
\[
 \boxed{\operatorname{Cov}(Z,X_r)=m(m-1)w_r-m^2u v_r.}\tag{1}
\]
It is **strictly negative at \(r=1\), strictly positive at \(r=n\), and changes sign exactly once from negative to positive when zero entries are omitted**. At most one integer frequency can have zero covariance.

More explicitly, define
\[
 R_{m,n,\alpha}(r)=
 \frac{(m\alpha)^{\overline n}((m-2)\alpha)^{\overline{n-r}}}
 {((m-1)\alpha)^{\overline n}((m-1)\alpha)^{\overline{n-r}}}.
\tag{2}
\]
Then \(R_{m,n,\alpha}(r)\) increases strictly in \(r\) and
\[
 \operatorname{sgn}\operatorname{Cov}(Z,X_r)
 =\operatorname{sgn}\!\left(R_{m,n,\alpha}(r)-\frac{m}{m-1}\right).
\tag{3}
\]
In particular, **strict nonzero covariance is not universal**: at the natural uniform-weak-composition point \(\alpha=1\),
\[
 \boxed{\operatorname{sgn}\operatorname{Cov}(Z,X_r)
 =\operatorname{sgn}\big(m(r-1)-2(n-1)\big).}\tag{4}
\]
Thus a zero occurs *if and only if* \(m(r-1)=2(n-1)\). For example, \(m=3,n=4,r=3\) gives exactly zero.

For fixed \(m\ge3\) and fixed \(\alpha>0\), the crossing concentrates at a deterministic fraction. Let \(r_n\) be the smallest \(r\) with nonnegative covariance, and define
\[
 B_{m,\alpha}=\frac{\Gamma((m-1)\alpha)^2}
 {\Gamma((m-2)\alpha)\Gamma(m\alpha)}.
\]
Then
\[
 \boxed{\lim_{n\to\infty}\frac{r_n}{n}
 =\theta(m,\alpha)
 :=1-\left(\frac{m-1}{m}B_{m,\alpha}\right)^{1/\alpha}.}\tag{5}
\]
In particular, \(\theta(m,1)=2/m\). The large-sample and weak-reinforcement limits do **not** commute:
\[
 \boxed{\lim_{\alpha\to\infty}\theta(m,\alpha)
 =1-\frac{(m-1)^{2(m-1)}}{(m-2)^{m-2}m^m},}\tag{6}
\]
whereas first letting \(\alpha\to\infty\) for fixed \(n\), and *then* letting \(n\to\infty\), yields the independent-uniform occupancy threshold
\[
 \boxed{\theta_{\rm iid}(m)=1-
 \frac{\log(m/(m-1))}{\log((m-1)/(m-2))}.}\tag{7}
\]
For \(m=3\), these fractions are respectively \(11/27\) and \(1-\log(3/2)/\log2\), which differ.

## Assumptions and scope

There are exactly \(m\) labeled colors, exactly \(n\) draws, and one common symmetric Dirichlet concentration \(\alpha>0\). The colors are exchangeable but, after integrating over \(P\), the draws are generally dependent. An equivalent integer-parameter model starts with \(\alpha\) balls of each color and adds one copy of the observed color after each draw; positive noninteger \(\alpha\) is interpreted through the Dirichlet mixture. The limit \(n\to\infty\) in (5) fixes \(m\) and \(\alpha\); the limit in (6) subsequently changes \(\alpha\). Equation (7) reverses these limit operations. There is no asserted rate of convergence, stochastic domination, or sign claim for nonsymmetric Dirichlet priors.

## Proof

**1. Exact mixed moments.** The Dirichlet mixture has probability mass
\[
 \Pr(N_1=k_1,\ldots,N_m=k_m)=
 \frac{n!}{\prod_i k_i!}
 \frac{\prod_i(\alpha)^{\overline{k_i}}}{(m\alpha)^{\overline n}},
 \qquad \sum_i k_i=n.
\tag{8}
\]
Beta-binomial marginals and the two-coordinate marginal obtained by summing (8) give precisely \(u,v_r,w_r\). With indicator variables \(I_i=\mathbf1_{\{N_i=0\}}\), \(J_{i,r}=\mathbf1_{\{N_i=r\}}\), we have \(I_iJ_{i,r}=0\) because \(r\ge1\). Therefore
\[
 \mathbb EZ=mu,\quad\mathbb EX_r=mv_r,\quad
 \mathbb E[ZX_r]=m(m-1)w_r,
\]
which establishes (1). Dividing \(w_r\) by \(uv_r\), using positivity and (2), yields \(w_r/(uv_r)=R_{m,n,\alpha}(r)\) and (3).

**2. Single crossing and endpoints.** Write \(k=n-r\), \(a=(m-2)\alpha\), \(b=(m-1)\alpha\). Because \(a<b\), the sequence \((a)^{\overline k}/(b)^{\overline k}\) is strictly decreasing in \(k\), hence (2) strictly increases in \(r\). At \(n=1\), \(R_{m,1,\alpha}(1)=m/(m-1)\). Holding \(r=1\) and increasing \(n\), direct cancellation gives
\[
 \frac{R_{m,n+1,\alpha}(1)}{R_{m,n,\alpha}(1)}
 =1-\frac{\alpha(\alpha+1)}
 {((m-1)\alpha+n)((m-1)\alpha+n-1)}<1.
\tag{9}
\]
Thus \(R_{m,n,\alpha}(1)<m/(m-1)\) for \(n\ge2\). At \(r=n\),
\[
 R_{m,n,\alpha}(n)=\prod_{j=0}^{n-1}
 \frac{m\alpha+j}{(m-1)\alpha+j}>\frac{m}{m-1}
 \qquad(n\ge2).
\]
Strict monotonicity and (3) give the claimed sign order and at most one zero.

**3. A natural zero-covariance locus.** At \(\alpha=1\), (8) is constant on all weak compositions of \(n\) into \(m\) parts. Cancellation of binomial coefficients gives
\[
 u=\frac{m-1}{n+m-1},\qquad
 \frac{w_r}{v_r}=\frac{m-2}{n-r+m-2}.
\]
Consequently the sign of (1) equals the sign of
\[
 (m-2)(n+m-1)-m(n-r+m-2)
 =m(r-1)-2(n-1).
\]
All other factors are strictly positive, so equality occurs exactly on the stated integer locus, not merely asymptotically.

**4. Fixed-concentration critical fraction.** The gamma-ratio identity \((a)^{\overline k}=\Gamma(a+k)/\Gamma(a)\) and \(\Gamma(t+c)/\Gamma(t+d)\sim t^{c-d}\) give, whenever \(r/n\to x\in[0,1)\),
\[
 R_{m,n,\alpha}(r)\longrightarrow
 \frac{B_{m,\alpha}}{(1-x)^\alpha}.
\tag{10}
\]
Strict log-convexity of \(\Gamma\) gives \(0<B_{m,\alpha}<1\). Thus the right side of (10), increasing continuously in \(x\), crosses \(m/(m-1)>1\) at the unique \(x=\theta(m,\alpha)\in(0,1)\). For arbitrary \(\varepsilon>0\) sufficiently small, take integer \(r\) on either side of \((\theta\pm\varepsilon)n\); (3) and (10) establish opposite strict signs for all sufficiently large \(n\). This sandwiches the first nonnegative crossing \(r_n/n\) and proves (5). Evaluation of the gamma recurrence at \(\alpha=1\) gives \(B_{m,1}=(m-2)/(m-1)\), hence \(\theta(m,1)=2/m\).

**5. Two orders of limit.** Stirling's formula at fixed \(m\) gives
\[
 \lim_{\alpha\to\infty}B_{m,\alpha}^{1/\alpha}
 =\frac{(m-1)^{2(m-1)}}{(m-2)^{m-2}m^m};
\]
the extra factor \(((m-1)/m)^{1/\alpha}\) tends to one. This proves (6). If instead \(\alpha\to\infty\) with \(m,n\) fixed, the Dirichlet mixture converges to fixed uniform color probabilities, and the covariance formula (1) converges to that of independent categorical draws. Directly in (2), its ratio tends to
\[
 \left(\frac{m}{m-1}\right)^n
 \left(\frac{m-2}{m-1}\right)^{n-r}.
\]
The sign comparison (3) then has its crossing at
\[
 \frac rn\longrightarrow
 1-\frac{\log(m/(m-1))}{\log((m-1)/(m-2))}
\]
as \(n\to\infty\), giving (7). The two expressions already differ for \(m=3\): equality would imply \(\log(3/2)/\log2=16/27\), hence \(3^{27}=2^{43}\), contrary to unique prime factorization. Thus the two limiting procedures are not interchangeable. This completes the proof.

## Verification

An independent-of-the-formula finite check enumerates every weak composition of \(n\) into \(m\) parts, assigns its exact Dirichlet-multinomial rational weight using (8), and calculates \(\mathbb E[ZX_r]-\mathbb EZ\,\mathbb EX_r\) without using (1). The accompanying standalone standard-library script compares this calculation to (1) for \(m\in\{3,4,5\}\), \(2\le n\le8\), and \(\alpha\in\{1/2,1,3/2,2\}\), checking all frequency thresholds. There are 420 exact rational \((m,n,r,\alpha)\) cases. It also verifies monotone sign ordering, endpoint signs and the \(\alpha=1\) zero criterion. It checks elementary numerical consistency of (5), but no infinite theorem is inferred from numerical calculations; the proof above supplies all infinite claims.

## Relationship to prior work

Huillet and Martínez [1], especially Proposition 5 and Section 3, already give general joint factorial moments for positive occupancy-frequency counts and the symmetric Dirichlet sampling law. Such results permit algebraic recovery of raw covariances and should not be mistaken for novel ingredients here. The present claim focuses on the *dependence classification*: a global one-crossing sign order for empty-versus-exact-size counts, the sharp zero-covariance diophantine locus for \(\alpha=1\), a gamma-function critical fraction, and two provably different limit-order critical fractions. These classifications are not asserted in the inspected material [1].

Dello Schiavo and Quattrocchi [2] formulate the Dirichlet-multinomial law in a wider polychromatic sampling setting (Example 5.54 and related Dirichlet moment results); that framework supplies model motivation, not the particular sign and limit-order conclusions. A published analysis [3] of ordinary **independent uniform occupancy** proves a strict one-sign-switch result for occupied-richness versus positive frequency counts with *no possible zero covariance*. Because \(Z=m-K\), its covariance signs are reversed relative to (1), but its iid premise cannot yield finite-\(\alpha\) exact zeros or (5)–(6). The iid threshold matches (7), as expected. The model's relevance to zero-inflated categorical counts is also described in [4].

## Limitations

The raw moments and the Dirichlet-multinomial law are classical. The contribution is the explicit structural sign/equality/asymptotic classification, not rediscovery of the distribution or the general factorial-moment formula. Earlier treatments of conditioned negative-binomial urns may contain algebraically equivalent sign conditions under different notation; exhaustive historical priority has not been established. The constant-\(\alpha\) large-sample fraction describes a growing sample from one fixed random environment; it does not directly describe the joint regime \(\alpha\) increasing with \(n\). The theorem treats only covariance, not association in stochastic order.

## References

1. T. Huillet and S. Martínez, “Occupancy distributions arising in sampling from Gibbs-Poisson abundance models,” arXiv:1307.3000 (2013), particularly Proposition 5 and Section 3, https://arxiv.org/abs/1307.3000.
2. L. Dello Schiavo and F. Quattrocchi, “Multivariate Dirichlet Moments and a Polychromatic Ewens Sampling Formula,” arXiv:2309.11292, first publicly submitted 2023-09-20; revised presentation “Polychromatic Partitions, Kingman Theory, and Ewens Sampling Formula,” especially Example 5.54, https://arxiv.org/abs/2309.11292.
3. “A one-switch covariance law for occupancy richness and frequency counts,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
4. “Bayesian analysis of zero-inflated compositional count data,” arXiv:2302.12283 (2023), https://arxiv.org/abs/2302.12283.
