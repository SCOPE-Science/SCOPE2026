# Indegree balancing increases fixed-point fluctuations of random mappings in convex order

## Finding

For an integer \(n\ge2\), let \(d=(d_1,\ldots,d_n)\) be a vector of nonnegative integers with \(\sum_i d_i=n\). Choose uniformly a function \(f:[n]\to[n]\) with exactly \(d_i\) preimages of label \(i\), and write \(F_d=|\{i:f(i)=i\}|\). If \(d\) majorizes \(e\) (that is, \(d\) is at least as concentrated as \(e\)), then

\[
F_d\le_{\mathrm{cx}}F_e.
\]

This means that \(\mathbb E\phi(F_d)\le\mathbb E\phi(F_e)\) for every convex real function \(\phi\); the means are both exactly \(1\). The inequality is strict for every strictly convex \(\phi\) unless \(d\) and \(e\) are permutations of each other. In particular, among all indegree profiles, the deterministic one-loop count of the constant map is least variable and the fixed-point count of a uniform random permutation is most variable, in convex order.

The theorem has an exact *transfer identity*. For a balancing move replacing two degrees \(A,B\), with \(A\ge B+2\), by \(A-1,B+1\), let \(Z\) count fixed positions outside these two labels, conditional on the two corresponding input positions being assigned one of those two labels. Its conditional distribution is the same before and after the move. For every function \(\phi\) on \(\{0,\ldots,n\}\),

\[
\mathbb E\phi(F_{\mathrm{balanced}})-\mathbb E\phi(F_{\mathrm{original}})
=\frac{A-B-1}{n(n-1)}\,
\mathbb E[\phi(Z)+\phi(Z+2)-2\phi(Z+1)].
\]

Consequently the full distribution, not merely its variance, responds monotonically to redistribution of indegrees.

The exact probability-generating function is

\[
\mathbb E[(1+t)^{F_d}]=\sum_{k=0}^{n}\frac{e_k(d)}{(n)_k}t^k,
\]

where \(e_k\) is the elementary symmetric function of degree \(k\) and \((n)_k=n(n-1)\cdots(n-k+1)\), with \((n)_0=1\). In particular, letting \(C(d)=\sum_i\binom{d_i}{2}\),

\[
\mathbb EF_d=1,\qquad \operatorname{Var}(F_d)
=1-\frac{2C(d)}{n(n-1)}.
\]

**A second-order dependence law.** Now take \(f\) uniformly from *all* \(n^n\) mappings, let \(D_i\) be its indegrees and \(F\) its fixed-point count, and set \(X_r=|\{i:D_i=r\}|\). For every integrable function \(H\) of the entire degree vector, \(\operatorname{Cov}(F,H(D_1,\ldots,D_n))=0\), although \(F\) is not independent of that vector. Set \(b_m(r)=\Pr(\operatorname{Bin}(m,1/n)=r)\), equal to zero outside the binomial range. For every \(0\le r\le n\),

\[
\operatorname{Cov}(F(F-1),X_r)
=\frac{n-1}{n^2}\{-b_{n-2}(r)+2b_{n-2}(r-1)-b_{n-2}(r-2)\}.
\]

For \(n\ge4\) this covariance is strictly positive at \(r=1,2\) and strictly negative at \(r=0,3,\ldots,n\). At \(n=3,r=2\) it equals zero, while at \(n=2,r=2\) it is negative. The profile shows precisely how the degree vector, despite having zero covariance with the untransformed loop count, detects *paired* self-loops.

## Assumptions and scope

There is no asymptotic hypothesis and no randomness in \(d\) in the convex-order statement: \(n\) is any integer at least \(2\), every coordinate of \(d\) is a nonnegative integer, and its total is \(n\). Conditional maps are uniformly chosen among the \(n!/\prod_i d_i!\) maps with that indegree sequence. Majorization refers to vectors sorted in nonincreasing order, and convex order to expectations of arbitrary real convex functions evaluated on the finite support. Strict convexity means a strictly positive discrete second difference at every interior integer.

The unconditional mixed-covariance statement instead uses \(n\) independent uniformly chosen images in \([n]\); no fixed degree sequence is imposed in this part. The zero-covariance statement holds for arbitrary real degree statistics, which are automatically integrable on the finite sample space. Conditional and unconditional assertions are distinguished throughout.

## Proof

**Prescribed degree counts and factorial moments.** A uniformly chosen mapping with indegrees \(d\) is equivalent to a uniformly randomly permuted word containing exactly \(d_j\) copies of symbol \(j\). If \(S\subseteq[n]\) has \(k\) distinct labels, the probability that every \(i\in S\) is a fixed point is

\[
\Pr(f(i)=i\ \forall i\in S\mid d)=\frac{\prod_{i\in S}d_i}{(n)_k}.
\]

Expanding \(\prod_i(1+t\mathbf1_{\{f(i)=i\}})\) and summing over sets \(S\) yields the generating function. The coefficient of \(t\) is \(e_1(d)/n=1\). The second factorial moment is \(2e_2(d)/(n(n-1))\). Since \(2e_2(d)=n(n-1)-2C(d)\), and \(\operatorname{Var}(F_d)=\mathbb E(F_d)_2+\mathbb EF_d-(\mathbb EF_d)^2\), the variance formula follows.

**Two-coordinate convex-order transfer.** Fix distinct labels \(a,b\) carrying multiplicities \(A,B\) and write \(m=A+B\). First sample the uniformly random set \(S\) of the \(m\) positions assigned either \(a\) or \(b\); assign all other symbols to the complement uniformly, and then choose uniformly which \(A\) of the positions in \(S\) receive \(a\). This construction works equally for \((A,B)\) and \((A-1,B+1)\). The count \(T\) of fixed positions outside \(\{a,b\}\) depends only on the first two stages and is unaffected by the split of \(m\).

When \(S\) meets neither of the two designated positions, the number of fixed positions among them is zero for both splits. When \(S\) meets exactly one, exchangeability of the two positions in the first-stage experiment pairs the two cases, and the average success probability is \((A+B)/(2m)=1/2\) for *each* split; the paired conditional distribution of \(T\) is identical. In these cases expectations of arbitrary functions \(\phi(T+R)\), where \(R\in\{0,1\}\) counts matches at positions \(a,b\), are therefore unchanged.

If \(S\) contains *both* \(a\) and \(b\), conditional on \(T\) the probabilities of \(R=0\) and \(R=2\) are both \(AB/[m(m-1)]\), and the probability of \(R=1\) is the remainder. The move \((A,B)\mapsto(A-1,B+1)\) increases \(AB\) by \(A-B-1\). Thus the conditional expected change is

\[
\frac{A-B-1}{m(m-1)}[\phi(T)+\phi(T+2)-2\phi(T+1)].
\]

Both designated positions belong to \(S\) with probability \(m(m-1)/[n(n-1)]\); multiplying proves the exact transfer identity. For convex \(\phi\), its bracket is nonnegative; for strictly convex \(\phi\) it is strictly positive, since the event has positive probability and \(A-B-1\ge1\). Any integer majorization relation can be decomposed into such transfers and permutations of coordinates. Simultaneously permuting input and output labels does not change the fixed-point count, proving the asserted convex order and strictness. The extremal degree vectors are \((n,0,\ldots,0)\) and \((1,\ldots,1)\).

**Unconditional degree orthogonality.** Given the multinomial random degree vector \(D\), the map is uniform over all maps with those indegrees. The previously proved conditional mean identity yields \(\mathbb E[F\mid D]=1\), and hence \(\operatorname{Cov}(F,H(D))=0\) for every degree-measurable \(H\). However, the event \(F=n\) forces \(D_i=1\) for all \(i\), and its probability is \(n^{-n}>0\), whereas \(\Pr(D_i=1\ \forall i)=n!/n^n<1\); hence independence fails for every \(n\ge2\).

**Second-order profile.** The sum \(F(F-1)\) counts ordered pairs of distinct fixed points. Its mean is \((n-1)/n\). Conditional on two specified labels being fixed, the other \(n-2\) mapping values are independent uniform choices, so

\[
\mathbb E[X_r\mid\text{two prescribed fixed points}]
=2b_{n-2}(r-1)+(n-2)b_{n-2}(r).
\]

The unconditional mean is \(nb_n(r)\). Consequently

\[
\operatorname{Cov}(F(F-1),X_r)
=\frac{n-1}{n}[2b_{n-2}(r-1)+(n-2)b_{n-2}(r)-nb_n(r)].
\]

Using the two-step binomial decomposition

\[
b_n(r)=(1-1/n)^2b_{n-2}(r)+2(1/n)(1-1/n)b_{n-2}(r-1)+(1/n)^2b_{n-2}(r-2)
\]

reduces this identity to the stated finite-difference formula.

For \(r=0\), only the negative first term survives. At \(r=1\), the difference equals \(2b_{n-2}(0)-b_{n-2}(1)>0\). For \(r=2\), divide by \(b_{n-2}(0)>0\): its sign agrees with \(n(n-3)/(2(n-1)^2)\), giving negative at \(n=2\), zero at \(n=3\), positive for \(n\ge4\). Finally, for every \(3\le r\le n\), the inequality \(2b_{n-2}(r-1)\le b_{n-2}(r-2)\) follows from

\[
\frac{b_{n-2}(r-1)}{b_{n-2}(r-2)}=\frac{n-r}{(r-1)(n-1)}<\frac12,
\]

with the boundary interpretation that the numerator is zero if \(r=n\). Therefore the covariance is strictly negative for these sizes. This completes all assertions.

## Verification

The standalone files `verify.py` and `convex.py` use only the Python standard library and exact integer/rational arithmetic. Run `python verify.py` to exhaustively enumerate every map for \(2\le n\le7\), verify the conditional first two factorial moments for every degree vector through \(n=6\), and verify the full quadratic covariance and sign spectrum through \(n=7\); exact formulas and signs are also tested through \(n=100\). Run `python convex.py` to check the entire convex-order relation for every integer-partition degree profile through \(n=10\) and every comparable pair. The unrestricted assertions above follow from the proof, not from extrapolating these finite checks.

## Relationship to prior work

Leckey and Wormald (2018) study the *same degree-conditioned uniform random mappings* and derive path-length distributions. Their Lemma 3.3 introduces the elementary-symmetric quantity \(k!e_k(d)/(n)_k\) in that setting. Thus the elementary-symmetric moment formula above is an immediate counting consequence of established methods and is **not claimed as a standalone novel contribution**. Hansen and Jaworski (2007) develop the exchangeable-indegree construction and analyze cyclic vertices, components, and component sizes. In their related 2008 *Local properties* paper they investigate predecessors, successors, heights, and local cycle lengths in the same model (primary MSC 60C05); no convex-order theorem for one-cycles or second-order self-loop/degree-profile covariance is given. Neither of these inspected sources states the degree-balancing comparison or the signed quadratic covariance profile of self-loops.

Stark (2026) examines fixed positions in random permutations of *multisets*, where each symbol originally occupies as many designated positions as its multiplicity. In that distinct statistic, the expected number of matches is \(\sum_i d_i^2/n\), unlike the present \(\mathbb EF_d=1\) with exactly one designated vertex for each symbol. Its Poisson approximation and variance results do not imply the convex-order result for self-maps.

The convex-order theorem and second-order profile are the substantive findings; unconditional mean invariance and elementary-symmetric identities serve as their established/proved prerequisites. Previously unlocated historical statements about the same specific diagonal matching statistic remain possible.

## Limitations

No claim of independent validation, journal priority, a multiset-permutation fixed-position theorem, or extension to mappings with nonuniform image probabilities is made. Exact computational tests stop at the finite ranges specified. The originality comparison is limited to identified literature and searched records; a mathematically equivalent unlocated earlier result remains a residual priority risk. The contrast between linear orthogonality and quadratic dependence is about covariance, not independence.

## References

1. K. Leckey and N. Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence*, arXiv:1803.02667v1, first posted 2018-03-07. In particular Section 2 and Lemma 3.3. https://arxiv.org/html/1803.02667v1
2. J. C. Hansen and J. Jaworski, *Random Mappings With Exchangeable In-Degrees*, Random Structures & Algorithms 33 (2008), 105–126, online 2007-09-04. DOI:10.1002/rsa.20187.
3. J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205. DOI:10.1239/aap/1208358892. Full publisher-hosted paper: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6993B104668C73703B9E57AF3DCC643E/S0001867800002433a.pdf/local-properties-of-random-mappings-with-exchangeable-in-degrees.pdf
4. D. Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710v1, posted 2026-08-01. https://arxiv.org/abs/2608.00710
