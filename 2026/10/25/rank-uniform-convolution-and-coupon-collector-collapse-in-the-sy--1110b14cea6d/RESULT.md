# Rank-uniform convolution and coupon-collector collapse in the symmetric inverse monoid

## Finding

For an integer \(n\ge1\), let \(\mathcal I_n\) be the symmetric inverse monoid of all partial bijections of \([n]=\{1,\ldots,n\}\), including the empty map. For \(0\le a\le n\), let \(\mu_a\) denote the uniform probability measure on partial bijections of rank \(n-a\). Products are compositions applied from right to left.

**Complete convolution theorem.** For every integer \(k\ge1\), all integers \(0\le a_1,\ldots,a_k\le n\), and independent \(F_i\sim\mu_{a_i}\), the product \(H=F_k\circ\cdots\circ F_1\) has the same distribution as the restriction of an independent uniform permutation \(\Pi\in S_n\) to \([n]\setminus U\), where \(U=A_1\cup\cdots\cup A_k\) and the \(A_i\) are independent uniform subsets of respective sizes \(a_i\). Consequently, \(\mu_{a_1}*\cdots*\mu_{a_k}\) is unchanged by any permutation of the factors; the linear span of the \(n+1\) rank-uniform measures is a commutative convolution subalgebra of the semigroup algebra.

For \(s\in\{0,\ldots,n\}\), define
\[
p_s(a_1,\ldots,a_k)=\sum_{j=0}^{s}(-1)^j\binom{s}{j}\prod_{i=1}^{k}\frac{\binom{s-j}{a_i}}{\binom{n}{a_i}},
\]
with \(\binom{b}{a}=0\) for \(a>b\). For every specific partial bijection \(h\) of rank \(n-s\), its **exact probability**, and the rank distribution, are
\[
\Pr(H=h)=\frac{s!}{n!}\,p_s(a_1,\ldots,a_k),\qquad
\Pr(\operatorname{rank}H=n-s)=\binom ns p_s(a_1,\ldots,a_k).
\]
Thus products conditioned on their rank are uniform over the entire corresponding rank stratum. These equations cover all endpoints, including empty maps and full permutations.

**Spectral and absorption theorem.** Let \(a\in\{0,\ldots,n\}\) be fixed, and let \(R_t\) be the rank of the product of \(t\) independent \(\mu_a\)-distributed maps, with \(R_0=n\). For \(0\le j\le n\), the falling factorial \((r)_j=r(r-1)\cdots(r-j+1)\) is an eigenfunction of the rank transition kernel, with eigenvalue
\[
\lambda_j=\frac{\binom{n-j}{a}}{\binom na}
=\frac{(n-a)_j}{(n)_j},
\]
interpreting the second fraction only where its denominator is nonzero. These eigenfunctions diagonalize the entire \((n+1)\)-state rank chain. Moreover,
\[
\mathbb E[(R_t)_j]=(n)_j\lambda_j^t,\qquad
\Pr(R_t=0)=\sum_{j=0}^n(-1)^j\binom nj\lambda_j^t.
\]
For \(a\ge1\), let \(T_{n,a}=\min\{t\ge0:R_t=0\}\). Fix any positive integer \(a\) as \(n\to\infty\). For every real \(c\), with \(t_n(c)=\lfloor(n/a)(\log n+c)\rfloor\),
\[
R_{t_n(c)}\ \Longrightarrow\ \operatorname{Poisson}(e^{-c}),\qquad
\Pr(T_{n,a}\le t_n(c))\longrightarrow \exp(-e^{-c}).
\]
For \(a=1\), writing \(\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\}\) for a Stirling number of the second kind, the exact remaining-rank and absorption laws are
\[
\Pr(R_t=n-s)=\frac{(n)_s}{n^t}\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\},\quad
\Pr(T_{n,1}\le t)=\frac{n!}{n^t}\left\{\begin{smallmatrix}t\\n\end{smallmatrix}\right\},\quad
\mathbb ET_{n,1}=n\sum_{j=1}^n\frac1j.
\]
The last coupon-collector formulas and limiting Gumbel distribution are classical as probability statements. The claim of contribution is the full **semigroup-valued rank-uniform product law and its exact spectral reduction**, not priority for coupon collection itself.

## Assumptions and scope

All sets are labeled; a partial bijection may have arbitrary domain and image, and composition is ordinary partial-function composition. The integers \(n\ge1\), \(k\ge1\), and deletion sizes \(0\le a_i\le n\) are arbitrary and fixed for the finite convolution identities. The homogeneous spectral statements cover every \(0\le a\le n\). The limit theorem assumes **fixed positive** \(a\) with \(n\ge a\) tending to infinity. Set \((r)_0=1\); binomial coefficients with lower argument larger than the upper argument are zero. The time-zero rank chain starts from the identity, not a uniform permutation; the distributional permutation coupling is asserted only for one or more random factors. No assertion is made about arbitrary non-rank-uniform measures.

## Proof

**Step 1: uniform permutation restriction.** Fix an integer \(a\in[0,n]\). Generate a uniform \(\pi\in S_n\), independently of a uniform \(a\)-subset \(D\subset[n]\). Define \(f=\pi|_{[n]\setminus D}\). Every rank-\(n-a\) partial bijection admits exactly \(a!\) extensions to a full permutation. Therefore \(f\sim\mu_a\), including \(a=0\) and \(a=n\).

**Step 2: pullback of deleted sets.** For independent pairs \((\pi_i,D_i)\), set \(P_0=\mathrm{id}\), \(P_i=\pi_i\circ\cdots\circ\pi_1\), and \(A_i=P_{i-1}^{-1}(D_i)\). Directly expanding the domain condition of a composition gives
\[
F_k\circ\cdots\circ F_1
=P_k\big|_{[n]\setminus(A_1\cup\cdots\cup A_k)}.
\]
Condition on all permutations \((\pi_1,\ldots,\pi_k)\). Since \(D_i\) are independent uniform \(a_i\)-subsets, so are their pullbacks \(A_i\), and their conditional joint law does not depend on the conditioned permutations. Hence the \(A_i\) are unconditionally independent of \(P_k\), which is itself a uniform permutation for \(k\ge1\). This proves the exact semigroup-valued coupling. The right-hand side is symmetric in deletion sizes, so the convolution of rank-uniform measures is commutative; it is closed because the conditional law at fixed rank is uniform (proved next).

**Step 3: inclusion-exclusion and individual fibers.** For a fixed \(s\)-subset \(S\), the event \(U=S\) is that every \(A_i\subset S\) but their union omits no element of \(S\). Inclusion-exclusion gives \(\Pr(U=S)=p_s(a_1,\ldots,a_k)\). By label symmetry, \(\Pr(|U|=s)=\binom ns p_s\). Fix a rank-\(n-s\) partial bijection \(h\). Its domain complement \(S\) is determined, and exactly \(s!\) permutations extend it. Thus \(\Pr(H=h)=p_s s!/n!\), proving all finite product formulas. In particular, rank-stratum measures span an \((n+1)\)-dimensional commutative convolution algebra; its identity as a vector-space subalgebra is \(\mu_0\), which is the normalized sum of all permutations, **not** the point-mass identity \(\delta_{\mathrm{id}}\) of the full monoid algebra.

**Step 4: hypergeometric rank chain and diagonalization.** Given \(R_t=r\), the next deleted \(a\)-subset hits exactly \(h\) of the \(r\) surviving points with probability
\[
\Pr(R_{t+1}=r-h\mid R_t=r)
=\frac{\binom rh\binom{n-r}{a-h}}{\binom na}.
\]
For an ordered \(j\)-tuple of distinct surviving points, the probability that the next uniformly deleted \(a\)-set misses all \(j\) points is \(\lambda_j=\binom{n-j}{a}/\binom na\). Summing indicators of such tuples yields
\(\mathbb E[(R_{t+1})_j\mid R_t=r]=\lambda_j(r)_j\).
The polynomials \((r)_j\), \(j=0,\ldots,n\), form a basis for real functions on the \(n+1\) possible ranks, since their evaluation matrix is lower triangular with nonzero diagonal \(j!\). Thus this gives a complete eigenbasis, including repeated or zero eigenvalues. Iteration gives the factorial moments. Applying inclusion-exclusion to the event that no labeled points survive gives \(\Pr(R_t=0)=\sum_j(-1)^j\binom nj\lambda_j^t\). For \(t=0\) use \(\lambda_j^0=1\), including eigenvalues zero.

**Step 5: fixed-batch critical window.** Fix integer \(a\ge1\) and \(j\ge0\). For large \(n\),
\[
\lambda_j=\prod_{u=0}^{j-1}\frac{n-a-u}{n-u}
=1-\frac{aj}{n}+O_{a,j}(n^{-2}).
\]
Taking \(t=t_n(c)\) gives \((n)_j\lambda_j^t\to e^{-cj}\). These are exactly the factorial moments of \(\operatorname{Poisson}(e^{-c})\). The first moments ensure tightness, and the Poisson distribution is moment-determinate, so convergence of all factorial moments implies convergence in distribution. Since ranks are nonnegative integers, the probability of zero converges as well. Finally \(\{T_{n,a}\le t\}=\{R_t=0\}\) because ranks never increase. This proves both critical-window assertions. This is a limit for a fixed batch size; growing deletion sizes require separate analysis.

**Step 6: singleton deletion.** For \(a=1\), each \(A_i\) is a uniformly sampled singleton: \(U\) is the set of observed labels among \(t\) independent draws. The number of words of length \(t\) that use exactly a prescribed \(s\)-element label set is \(s!\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\}\). The exact Stirling formulas follow. The waiting time to see a new label when \(j\) distinct labels have been seen is geometric with success probability \((n-j)/n\); summing its mean over \(j=0,\ldots,n-1\) gives \(n\sum_{j=1}^n1/j\).

## Verification

An independent exact-arithmetic verifier (`verify.py`) enumerates partial bijections as partial-function value vectors and actually composes them. It verifies the individual-product probabilities against the inclusion-exclusion formula for 21 small deletion profiles; separately verifies all rank-transition eigenfunction identities in 3,024 finite parameter instances, and checks Stirling and hitting-time equalities through \(n=7\). It prints `VERIFY_OK_ROOK_MONOID_BATCH_COUPON_CONVOLUTION`. Exact finite enumeration corroborates but does not establish the universal and asymptotic claims; those are established by the six arguments above.

## Relationship to prior work

André–Fernandes–Mitchell establish the rank strata and study maximal two-generated subsemigroups of the same symmetric inverse monoid; their Theorems 1.1–1.2, Lemmas 3.1–3.4, and examples are not probability laws for independent rank-uniform products. Malandro gives a general Fourier algorithm for convolution on inverse semigroups, including the rook monoid (Theorem 2.11 and Section 5), but not the explicit rank-dependent convolution constants and coupon-set coupling displayed here. Ivanov–Kerov study a **different** partial-permutation semigroup: pairs consisting of a subset and a permutation of that same subset, with support-union multiplication (Section 2), not arbitrary partial bijections under partial-map composition. Structured coupon collection and its asymptotics are studied separately by Falgas-Ravry–Larsson–Markström and many earlier authors; the occupancy/Gumbel consequences are credited as classical. The distinctive statement here is the distributional identification of products *as labeled partial bijections*, the commutative rank-uniform convolution algebra, and its explicit full-rank spectral diagonalization. The absence of an accessible equivalent statement is not proof of historical uniqueness.

## Limitations

The results require independent factors uniform **within** specified rank strata and labeled finite ground sets. They do not classify arbitrary convolution laws, nonuniform deletions, generating sets, conjugacy classes, or random walks from an arbitrary initial partial bijection. The Gumbel statement fixes positive deletion size before letting ground-set size diverge. Possible implicit coverage through general rook-monoid representation theory or older inverse-semigroup probability literature remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. J. M. André, V. H. Fernandes, J. D. Mitchell, “Largest 2-generated subsemigroups of the symmetric inverse semigroup,” *Proceedings of the Edinburgh Mathematical Society* 50 (2007), 551–561. DOI: 10.1017/S0013091505001598; journal site records online publication 8 January 2008.
2. M. E. Malandro, “Fourier inversion for finite inverse semigroups,” arXiv:1212.6462 (28 December 2012), especially Theorem 2.11 and Section 5.1.
3. V. Ivanov and S. Kerov, “The algebra of conjugacy classes in symmetric groups, and partial permutations,” arXiv:math/0302203 (18 February 2003), especially Section 2 (different semigroup).
4. V. Falgas-Ravry, J. Larsson, and K. Markström, “Speed and concentration of the covering time for structured coupon collectors,” *Advances in Applied Probability* 52 (2020), 433–462. DOI: 10.1017/apr.2020.5.
