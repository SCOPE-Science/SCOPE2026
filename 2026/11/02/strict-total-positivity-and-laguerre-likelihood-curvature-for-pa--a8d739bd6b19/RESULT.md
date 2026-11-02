# Strict total positivity and Laguerre likelihood curvature for partially informed matching

## Finding

Fix an integer \(n\ge 2\). In the partially informed matching model, each of \(n\) distinguishable objects is independently assigned to its correct position with probability \(\theta\in[0,1]\). All unassigned objects are then uniformly permuted over the remaining positions. Write \(K\) for the *total* number of correctly positioned objects and \(p_{n,k}(\theta)=\Pr_\theta(K=k)\). The possible counts are
\[
\mathcal S_n=\{0,1,\ldots,n-2,n\}.
\]

**Theorem (strict likelihood geometry).** For every \(1\le r\le n\), every \(k_1<\cdots<k_r\) in \(\mathcal S_n\), and every \(0<\theta_1<\cdots<\theta_r<1\),
\[
\det\big[p_{n,k_i}(\theta_j)\big]_{i,j=1}^{r}>0.
\]
Thus the entire probability kernel is strictly totally positive of every order, on its actual support. Moreover, for every \(k\in\mathcal S_n\), \(\log p_{n,k}(\theta)\) is strictly concave on \((0,1)\). More precisely, if \(z_{k,1},\ldots,z_{k,k}>0\) are the distinct positive roots of the generalized Laguerre polynomial \(L_k^{(n-k)}\), then
\[
p_{n,k}(\theta)=\frac{D_{n-k}}{k!(n-k)!}(1-\theta)^{n-k}
\prod_{j=1}^k\big(1+(z_{k,j}-1)\theta\big),
\]
where \(D_m\) is the number of derangements of \(m\) elements, \(D_0=1\), and the empty product is one. Consequently,
\[
\frac{d^2}{d\theta^2}\log p_{n,k}(\theta)
=-\frac{n-k}{(1-\theta)^2}
-\sum_{j=1}^k\frac{(z_{k,j}-1)^2}{[1+(z_{k,j}-1)\theta]^2}<0.
\]
For every nonempty independent sample of these counts at a fixed \(n\), the likelihood in the common \(\theta\) has a unique maximizer on \([0,1]\); its log is strictly concave wherever finite in \((0,1)\).

## Assumptions and scope

The initial recognition indicators are independent with one common success probability. Conditional on the recognized set, the remaining assignment is one uniformly random permutation; no replacement or additional matching stage occurs. Counts are observed in the full permutation and include recognized and accidentally correct placements. The size \(n\) is fixed and at least two. A count of \(n-1\) matches is impossible, so it is excluded from claims of positivity and likelihood derivatives. The determinants require strictly interior, strictly ordered parameter values. Independent repetitions, when used for the maximum-likelihood corollary, have the same \(n\) and \(\theta\).

## Proof

**1. Exact conditional kernel.** Let \(L\sim\operatorname{Bin}(n,\theta)\) be the number of pre-recognized positions. Conditional on \(L=\ell\), the remaining \(n-\ell\) positions undergo a uniform permutation. To obtain \(K=k\), choose exactly \(k-\ell\) additional fixed positions and derange the other \(n-k\) positions. Therefore, for \(0\le\ell\le k\),
\[
\Pr(K=k\mid L=\ell)
=\frac{\binom{n-\ell}{k-\ell}D_{n-k}}{(n-\ell)!}
=c_{n,k}(k)_\ell,
\quad c_{n,k}=\frac{D_{n-k}}{k!(n-k)!},
\]
where \((k)_\ell=k(k-1)\cdots(k-\ell+1)\), with \((k)_0=1\) and \((k)_\ell=0\) for \(\ell>k\). The only zero \(c_{n,k}\) among \(0\le k\le n\) is \(k=n-1\), since \(D_1=0\) and all other derangement numbers in this range are positive. Marginalizing over \(L\) yields
\[
p_{n,k}(\theta)=c_{n,k}\sum_{\ell=0}^{n}(k)_\ell
\binom n\ell\theta^\ell(1-\theta)^{n-\ell}.
\tag{1}
\]
This representation identifies the latent-size conditional law as a factorial size-bias transform of the classical fixed-point distribution.

**2. Positivity of all ordered minors.** Let \(B_{k\ell}=(k)_\ell=\ell!\binom{k}{\ell}\) and \(C_{\ell j}=\binom n\ell\theta_j^\ell(1-\theta_j)^{n-\ell}\). The rectangular kernel in (1) is the product of a positive diagonal matrix \(\operatorname{diag}(c_{n,k})\), a submatrix of \(B\), and \(C\).

The Pascal matrix \(\big[\binom{k}{\ell}\big]_{k,\ell=0}^n\) is totally nonnegative. For completeness, start with the identity matrix and, for each \(j=1,\ldots,n\), successively replace row \(i\) by row \(i\) plus row \(i-1\), for \(i=n,n-1,\ldots,j\). Pascal's recurrence shows that the final matrix is precisely the Pascal matrix. Each row-addition factor is a nonnegative unit lower-bidiagonal matrix, whose ordered minors are nonnegative; Cauchy–Binet preserves that property under products. Multiplying columns by the positive \(\ell!\) proves that \(B\) is totally nonnegative.

Put \(t_j=\theta_j/(1-\theta_j)\). Each ordered minor of \(C\) is a product of positive binomial and \((1-\theta_j)^n\) factors with a generalized Vandermonde determinant \(\det[t_j^{\ell_i}]\), which is strictly positive for strictly increasing nonnegative integer exponents \(\ell_i\) and \(0<t_1<\cdots<t_r\). One elementary verification: a nonzero polynomial with \(r\) nonzero monomials has at most \(r-1\) distinct positive zeros (induction using Rolle's theorem after dividing by the smallest power); hence this determinant never vanishes. Its sign is positive by taking separated values \(t_j=\varepsilon^{r-j}\) and letting \(\varepsilon\downarrow0\), for which the positive identity-permutation term dominates.

Cauchy–Binet now expresses each claimed minor as a sum of nonnegative terms. The term indexed by \(\ell=0,1,\ldots,r-1\) is strictly positive: \(\det[(k_i)_{j-1}]=\prod_{i<j}(k_j-k_i)>0\), and the corresponding generalized Vandermonde determinant for \(C\) is positive. Hence the whole minor is strictly positive. This argument works for every allowed order \(r\), including the largest possible \(r=n\).

**3. Laguerre factorization and exact negative curvature.** Define
\[
F_{n,k}(t)=\sum_{\ell=0}^{k}\binom n\ell(k)_\ell t^\ell.
\]
The standard coefficient definition of the generalized Laguerre polynomial gives
\[
L_k^{(n-k)}(x)=\sum_{j=0}^k\binom n{k-j}\frac{(-x)^j}{j!},
\qquad
F_{n,k}(t)=k!t^kL_k^{(n-k)}(-1/t).
\]
Every \(L_k^{(\alpha)}\) with \(\alpha\ge0\) has \(k\) distinct strictly positive zeros. This can be recovered without any numerical root calculation: the Rodrigues identity
\[
L_k^{(\alpha)}(x)=\frac{x^{-\alpha}e^x}{k!}
\frac{d^k}{dx^k}\big(e^{-x}x^{k+\alpha}\big)
\]
and \(k\) integrations by parts establish orthogonality against every polynomial of degree below \(k\) under the positive weight \(x^\alpha e^{-x}\) on \((0,\infty)\). If the degree-\(k\) polynomial had fewer than \(k\) distinct sign-changing zeros there, multiplying by the factors at those zeros would produce a polynomial of degree below \(k\) whose weighted product with \(L_k^{(\alpha)}\) has one nonzero sign, contradicting orthogonality. Hence all \(k\) roots lie in \((0,\infty)\), and they are simple.

Since \(F_{n,k}(0)=1\), its zero set gives \(F_{n,k}(t)=\prod_{j=1}^k(1+z_{k,j}t)\). Substituting \(t=\theta/(1-\theta)\) into (1) produces the claimed factorization. Each factor \(1+(z-1)\theta\) is strictly positive on \((0,1)\), so twice differentiating its logarithm gives the displayed curvature identity. If \(k<n\), the first term is strictly negative. If \(k=n\), then \(n\ge2\) and the \(n\) Laguerre roots are distinct, so at least one is different from one and a summand is strictly negative. Thus every allowed count has strictly negative log curvature.

**4. Maximum-likelihood consequence.** For independent observed counts \(k_1,\ldots,k_m\), \(m\ge1\), the log likelihood is a sum of the strictly concave log-probabilities above. Its derivative at zero is \(n\sum_i(k_i-1)\). If the sample mean is at most one, the unique maximum occurs at \(\theta=0\). If all counts equal \(n\), the unique maximum is at \(\theta=1\), since \(p_{n,n}(\theta)=\mathbb E[1/(n-L)!]\) strictly increases with \(\theta\). Otherwise, if the sample mean exceeds one and at least one count is below \(n\), the score starts positive and tends to minus infinity at one; strict concavity gives exactly one interior score zero and hence one maximum. These endpoint cases are already discussed in the motivating literature; the strengthened statement here is exact strict curvature for every datum and sample.

## Verification

A standalone standard-library Python script, `verify.py`, independently enumerates recognized subsets and residual permutations for \(2\le n\le6\), compares the resulting distributions with (1) at four rational parameter values, checks the Laguerre coefficient identity, evaluates exact rational second-log-derivative signs for \(2\le n\le10\), and verifies every selected ordered minor up to order four for \(2\le n\le7\) on a five-point rational parameter grid. The recorded run passed 2,563 exact assertions. These computations test finite instances only; the arbitrary-size and arbitrary-order statements follow from the algebraic argument above.

Reproduction: place the included `verify.py` beside this file and run `python3 verify.py` using Python 3. No external libraries, random seeds, downloaded tables or outside artifacts are needed.

## Relationship to prior work

O'Neill's *A generalised matching distribution for the problem of coincidences* first appeared on arXiv on 2021-12-23. The published open-access text supplies the two-stage model and finite matching-count mass function, discusses stochastic monotonicity and a monotone-likelihood-ratio property, and asserts likelihood unimodality and a unique maximum-likelihood estimate. It does not state all-order **strict** total positivity, identify the count-likelihood polynomial with generalized Laguerre zeros, or give the exact universal strict log-curvature formula. These are stronger shape results rather than a new model, mass function, likelihood-ratio monotonicity, or existence of a unique estimator.

Classical generalized Laguerre orthogonality and positive-root theorems, and classical total nonnegativity of Pascal matrices, are essential established ingredients. The contribution is the joint identification of their consequences for the full finite matching likelihood kernel. The existence of standard general tools creates a residual risk that an equivalent application has appeared in older statistical total-positivity literature. No definitive historical-priority or independent verification claim is made.

## Limitations

The result does not concern heterogeneous recognition probabilities, nonuniform completion permutations, or partial observations other than the total matching count. At \(n=1\) the likelihood is independent of \(\theta\), so strict concavity is false; at count \(k=n-1\) the likelihood is identically zero, so no logarithm exists. Strict determinant positivity is asserted only for distinct interior parameters, not boundary values. This result proves deterministic shape identities, not finite-sample confidence-interval coverage or comparative test power. It establishes no new property of the generalized Laguerre polynomials themselves.

## References

1. Ben O'Neill, *A generalised matching distribution for the problem of coincidences*, arXiv:2112.12442 (first public posting 2021-12-23); *Methodology and Computing in Applied Probability* 25, article 93 (2023), https://doi.org/10.1007/s11009-023-10067-6 . The complete accessible journal text, especially sections 1, 3, 5, 6, and the notes, was compared with this claim.
2. NIST Digital Library of Mathematical Functions, Chapter 18, especially §18.2(i),(vi) (orthogonality and positive simple zeros), https://dlmf.nist.gov/18.2 .
3. David Galvin and Adrian Pacurar, *Total non-negativity of some combinatorial matrices*, arXiv:1807.08658 (2018), especially the introduction's binomial-coefficient matrix and the general total-nonnegativity framework, https://arxiv.org/abs/1807.08658 .
