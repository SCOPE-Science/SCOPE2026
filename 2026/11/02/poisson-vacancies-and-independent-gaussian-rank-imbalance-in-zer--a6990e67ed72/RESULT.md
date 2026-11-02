# Poisson vacancies and independent Gaussian rank imbalance in zero products of rook monoids

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid of all partial injections of \([n]\), including the empty map \(0\). Select \(\alpha_n\) and \(\beta_n\) independently and uniformly from \(\mathcal I_n\), conditional on \(\beta_n\circ\alpha_n=0\). Put
\[
I_n=|\operatorname{dom}\alpha_n|,\qquad J_n=|\operatorname{dom}\beta_n|,\qquad S_n=n-I_n-J_n,
\qquad H_n=(I_n-J_n)/\sqrt n.
\]
Then \(S_n\) is nonnegative and, as \(n\to\infty\),
\[
(S_n,H_n)\ \Longrightarrow\ (P,G),
\qquad P\sim\operatorname{Poisson}(1),\quad G\sim N(0,1/2),
\qquad P\text{ and }G\text{ independent}.
\]
In particular, \(S_n\to\operatorname{Poisson}(1)\) in total variation and \((I_n/n,J_n/n)\to(1/2,1/2)\) in probability. Exactly, for integers \(i,j\ge0\) with \(i+j\le n\), the number of ordered zero-product pairs with these ranks is
\[
Z_{n;i,j}=\frac{n!}{(n-i-j)!}\binom ni\binom nj.
\]
This rank-refined count is a proof device. The resulting **unrefined total** \(Z_n=n!\sum_{s=0}^n\binom{2n}{n-s}/s!\) is already represented by OEIS A082545 and is not asserted to be new. The assessed claim is the joint conditional limit and asymptotic independence.

## Assumptions and scope
Here \(n\) ranges over positive integers, maps are unweighted and uniformly distributed, and \(\operatorname{rank}\gamma\) means the cardinality of the domain (equivalently, image) of a partial injection \(\gamma\). Composition \(\beta\circ\alpha\) acts first by \(\alpha\). The condition \(\beta\circ\alpha=0\) is equivalent to \(\operatorname{im}\alpha\cap\operatorname{dom}\beta=\varnothing\). It entails \(I_n+J_n\le n\). The Gaussian is real and centered with variance \(1/2\); convergence of the pair is weak on \(\mathbb Z_{\ge0}\times\mathbb R\) with the discrete topology in the first coordinate.

## Proof
**1. Exact rank-refined enumeration.** Fix ranks \(i,j\) and require the image of \(\alpha\) to be disjoint from the domain of \(\beta\). Choose the domain and image of \(\alpha\), and then a bijection between them, in \(\binom ni^2 i!\) ways. Independently choose the domain of \(\beta\) from the \(n-i\) points outside that image, choose its image from all \(n\) points, and choose the bijection, in \(\binom{n-i}j\binom nj j!\) ways. Multiplying and cancelling factorials gives precisely
\[
\binom ni^2 i!\binom{n-i}j\binom nj j!=\frac{n!}{(n-i-j)!}\binom ni\binom nj.
\]
Set \(s=n-i-j\). Vandermonde's identity, applied to \(\sum_i\binom ni\binom n{n-s-i}=\binom{2n}{n-s}\), gives
\[
Z_n=n!\sum_{s=0}^n \frac{\binom{2n}{n-s}}{s!}.
\]
Thus the conditional vacancy law and the conditional first-rank law are, exactly,
\[
\Pr(S_n=s\mid\beta\circ\alpha=0)
=\frac{\binom{2n}{n-s}/s!}{\sum_{t=0}^n\binom{2n}{n-t}/t!},
\]
\[
\Pr(I_n=i\mid S_n=s,\beta\circ\alpha=0)
=\frac{\binom ni\binom n{n-s-i}}{\binom{2n}{n-s}}.
\]
In the second display, out-of-range binomial coefficients are zero. The second distribution is hypergeometric with population \(2n\), \(n\) marked positions and draw size \(n-s\).

**2. Poisson limit.** Divide numerator and denominator of the vacancy law by \(\binom{2n}n\). For each fixed \(s\ge0\), the ratio \(r_{n,s}=\binom{2n}{n-s}/\binom{2n}n\) tends to \(1\). As \(0\le r_{n,s}\le1\) for every \(n,s\), and \(\sum_{s\ge0}1/s!=e\), dominated convergence on the counting measure gives convergence of the normalizing denominator to \(e\). Thus the vacancy mass function converges pointwise to \(e^{-1}/s!\). Since it is a probability mass function and the limiting probabilities sum to one, the convergence is in total variation (or directly by the same summable domination). This also recovers the previously tabulated unrefined asymptotic \(Z_n\sim e n!\binom{2n}n\), without claiming priority for it.

**3. Gaussian imbalance conditional on each fixed vacancy count.** Fix \(s\ge0\). Under the displayed hypergeometric law, let \(T_n=I_n\). Its mean and variance are exactly
\[
\mathbb E(T_n\mid S_n=s)=\frac{n-s}{2},\qquad
\operatorname{Var}(T_n\mid S_n=s)=\frac{(n-s)(n+s)}{4(2n-1)}.
\]
For clarity one can derive the needed hypergeometric central limit theorem directly from Stirling's formula. Uniformly when \(i=(n-s)/2+u\sqrt n\), with \(u\) in a fixed compact interval and integral \(i\), the ratio
\[
\frac{\binom ni\binom n{n-s-i}}{\binom{2n}{n-s}}
=\frac{2}{\sqrt{\pi n}}\exp(-4u^2)(1+o(1)).
\]
(The leading coefficient integrates to one at lattice step \(1/\sqrt n\).) Expansion of \(\log\binom nk\) at \(k=n/2\) yields the quadratic \(-2(k-n/2)^2/n\) for each factor; the denominator is evaluated by Stirling at \(n-s\). The variance formula yields tightness of the normalized centered variable, so the local estimate and Riemann sums imply
\[
\frac{2T_n-(n-s)}{\sqrt n}\ \Longrightarrow\ N(0,1/2).
\]
Here \(2T_n-(n-s)=I_n-J_n\). There is no dependence on the fixed value of \(s\) in this Gaussian limit.

**4. Joint independence.** Let \(f\) be bounded and continuous on \(\mathbb Z_{\ge0}\times\mathbb R\). Conditional expectation gives
\[
\mathbb E[f(S_n,H_n)\mid\beta\circ\alpha=0]
=\sum_{s=0}^n p_{n,s}\,\mathbb E[f(s,H_n)\mid S_n=s,\beta\circ\alpha=0].
\]
For each fixed \(s\), the inner expectation converges to \(\mathbb E f(s,G)\) by Step 3, and \(p_{n,s}\to e^{-1}/s!\) by Step 2. The summable uniform bound \(p_{n,s}\le (1/s!)\) follows because the normalizer in Step 2 is at least \(1\). Dominated convergence over \(s\) proves that the sum tends to \(\sum_s (e^{-1}/s!)\mathbb E f(s,G)\), the product law. Finally \(I_n+J_n=n-S_n\) and \(I_n-J_n=O_{\Pr}(\sqrt n)\), giving both rank fractions \(1/2\).

## Verification
The accompanying `verify.py` constructs all partial injections explicitly for \(0\le n\le4\), tests whether each ordered composition is empty, records both ranks, and checks the counts against the closed formula for every admissible pair. It independently checks the OEIS total and rook-monoid cardinality. It then checks exact binomial-ratio probabilities and limiting numerical diagnostics through dimension \(70\). The executed output was `VERIFY_OK: direct pair products through n=4 and 70 exact-ratio cases`. Finite checks are consistency tests, not proof of the infinite limit.

## Relationship to prior work
The algebraic object is the standard symmetric inverse / rook monoid as described by Gusev and Volkov (first public preprint April 22, 2022), whose full text addresses finite identity bases for rook semirings, not conditioned zero-product rank fluctuations. Kinyon and Stanovský (first public preprint September 28, 2022, primary MSC 20M18) study universal-algebraic centrality and abelianness of inverse semigroups, rather than random zero-product counts. The **unrefined** zero-product total has the exact same numerical formula as OEIS A082545 (recorded 2003); the sequence and its published leading asymptotic are previous knowledge, not a finding here. The present result refines this total by the two ranks and proves a new candidate joint limiting law conditioned on a zero product. No earlier statement of the joint independence law was found in the inspected evidence. This is a best-knowledge originality assessment, not an assertion that no earlier probabilistic restatement exists.

## Limitations
The theorem concerns independent uniform *partial injections* conditioned on their product being empty. It does not describe arbitrary transformation monoids, products of more than two factors, or the unconditional joint ranks. Its Poisson–Gaussian limit is asymptotic; no global optimal rate is claimed. The total number of zero products, and its asymptotic leading constant, are **known** in OEIS A082545 as an integer-sequence identity. Other prior probabilistic formulations may exist outside inspected inverse-semigroup and combinatorial literature. This review is not independent mathematical validation.

## References
1. S. V. Gusev and M. V. Volkov, *Semiring identities of finite inverse semigroups*, arXiv:2204.10514v1 (April 22, 2022), https://arxiv.org/abs/2204.10514 ; full text https://arxiv.org/html/2204.10514v2 .
2. M. Kinyon and D. Stanovský, *Abelianness and centrality in inverse semigroups*, arXiv:2209.13805v1 (September 28, 2022), https://arxiv.org/abs/2209.13805 .
3. OEIS Foundation, A082545, https://oeis.org/A082545 (original sequence record May 11, 2003; known Laguerre identity and asymptotic).
