# Quantitative asymptotic independence of Quicksort cost and inversion fluctuations

## Finding

For a uniform random input permutation of size \(n\), write \(C_n\) for first-element-pivot Quicksort comparisons and \(I_n\) for input inversions. The centered Quicksort cost has an order-\(n\) nondegenerate limiting variable; normalized inversions have order-\(n^{3/2}\) Gaussian fluctuations. These two fluctuations are jointly asymptotically independent, with an explicit nonlinear finite-sample decorrelation bound. This is stronger than their exact finite-sample zero covariance.

Set \(H_n=\sum_{j=1}^{n}1/j\), \(m_n=2(n+1)H_n-4n\), and
\[
M_n=\frac{C_n-m_n}{n+1},\qquad Z_n=\frac{I_n-n(n-1)/4}{n^{3/2}}.
\]
There is an absolute constant \(A<\infty\) such that for every \(n>k\ge1\), and real functions \(f,g\) both bounded by one and with Lipschitz constant at most one,
\[
\big|\operatorname{Cov}(f(M_n),g(Z_n))\big|
\le A\left(\frac{1+\log k}{\sqrt k}+\frac{k}{\sqrt n}\right).
\tag{1}
\]
Consequently the left side is \(O(n^{-1/6}(\log n)^{2/3})\) uniformly over those test functions. Further, \(M_n\to M_\infty\) almost surely and in \(L^2\) for a nonconstant random variable, and
\[
(M_n,Z_n)\ \xrightarrow{\mathrm d}\ (M_\infty,G),\qquad
G\sim N(0,1/36),\qquad G\ \text{independent of }M_\infty.
\tag{2}
\]
For every \(n\ge2\), the conditional law of \(I_n\) given \(C_n\) is symmetric around \(n(n-1)/4\); thus \(\operatorname{Cov}(C_n,I_n)=0\) exactly. This does *not* mean finite-sample independence; at \(n=3\) the two statistics are dependent.

## Assumptions and scope

Let \(U_1,U_2,\ldots\) be independent uniform random variables on \((0,1)\), almost surely all different; let \(\pi_n\) be the permutation obtained by ranking the first \(n\) values. The algorithm always compares a subarray's *first* key to its other keys and recursively processes the smaller and larger subsequences without changing their original relative order. Equivalently, \(C_n\) is the total internal path length of the binary-search tree formed by inserting \(U_1,\ldots,U_n\) successively. The inversion count is \(I_n=\sum_{1\le i<j\le n}\mathbf1\{U_i>U_j\}\). All limits are as \(n\to\infty\), and all constants in (1) are universal.

## Proof

**1. Exact centering and symmetry.** Two values of ranks \(a<b\) are compared by this Quicksort variant exactly when the first-arriving key from the rank interval \(\{a,\ldots,b\}\) is one of its endpoints. Its probability is \(2/(b-a+1)\). Summing over pairs gives
\[
\mathbb EC_n=2\sum_{d=1}^{n-1}\frac{n-d}{d+1}=2(n+1)H_n-4n=m_n.
\]
The transformation \(U_i\mapsto1-U_i\) reflects every binary-search tree, so it leaves \(C_n\) invariant and changes \(I_n\) into \(\binom n2-I_n\). The two input samples have the same law; conditioning on any value of \(C_n\) proves the asserted conditional reflection. At \(n=3\), the event \(C_3=2\) forces \(I_3\in\{1,2\}\), whereas \(I_3=0\) is possible; hence independence is false.

**2. The centered comparison-cost martingale.** Let \(\mathcal F_n\) record the relative order of the first \(n\) observations. The new observation is inserted uniformly into one of the \(n+1\) external gaps of the current search tree, conditionally on \(\mathcal F_n\). If \(D_{n+1}\) is the insertion depth, then \(C_{n+1}-C_n=D_{n+1}\). The sum of depths of the \(n+1\) external gaps equals \(C_n+2n\): it holds for the empty tree, and replacing a gap at depth \(d\) by an internal node and two deeper external gaps changes the external path total by \(d+2\) and the internal path total by \(d\). Consequently
\[
\mathbb E[D_{n+1}\mid\mathcal F_n]=\frac{C_n+2n}{n+1},\qquad
\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n.
\]
The second identity uses the displayed exact centering formula and denominators \(n+1,n+2\); thus \((M_n)\) is a martingale, with increment
\[
M_{n+1}-M_n=\frac{D_{n+1}-\mathbb E[D_{n+1}\mid\mathcal F_n]}{n+2}.
\tag{3}
\]

**3. Quantitative convergence.** Condition on the rank position of the newly inserted item among all \(n+1\) items. Its ancestors smaller than itself are precisely the *successive record maxima* of the previously inserted smaller keys, read in arrival order; its larger ancestors are the *successive record minima* among the larger keys. In a uniformly random ordering of \(r\) keys the record count is a sum of independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/r\). Each side therefore has mean at most \(H_n\) and variance at most \(H_n\); the two side orders are conditionally independent. Accordingly,
\[
\mathbb E D_{n+1}^{2}\le 4H_n^{2}+2H_n.
\]
By (3), the orthogonal martingale increments satisfy
\[
\mathbb E|M_{n+1}-M_n|^{2}\le \frac{4H_n^2+2H_n}{(n+2)^2}.
\]
Summability gives almost-sure and \(L^2\) convergence to \(M_\infty\), and for every \(n\ge k\ge1\),
\[
\mathbb E|M_n-M_k|\le
\left(\sum_{j=k}^{\infty}\frac{4H_j^2+2H_j}{(j+2)^2}\right)^{1/2}
\le A_0\frac{1+\log k}{\sqrt k}.
\tag{4}
\]
For \(n=3\), \(C_3=2\) with probability \(1/3\) and \(C_3=3\) otherwise. Hence \(\operatorname{Var}(M_3)=1/72\). Martingale orthogonality implies \(\operatorname{Var}(M_\infty)\ge1/72\), proving nondegeneracy.

**4. Independent-tail comparison.** Let \(I_{n,k}^{\mathrm{tail}}\) count inversions entirely among \(U_{k+1},\ldots,U_n\), and write
\[
T_{n,k}=\frac{I_{n,k}^{\mathrm{tail}}-\mathbb EI_{n,k}^{\mathrm{tail}}}{n^{3/2}}.
\]
Since the tail observations are independent of the first \(k\), \(T_{n,k}\) is independent of \(M_k\). All omitted inversion pairs meet at least one of the first \(k\) indices; their number is at most \(kn\). Their centered count is bounded in absolute value by \(kn\), so
\[
|Z_n-T_{n,k}|\le k/\sqrt n\quad\text{almost surely}.
\tag{5}
\]
For bounded-by-one 1-Lipschitz \(f,g\), replace \(f(M_n)\) by \(f(M_k)\) and \(g(Z_n)\) by \(g(T_{n,k})\) inside the covariance. Each replacement changes covariance by at most twice its \(L^1\) change, and the resulting covariance vanishes by tail independence. Equations (4) and (5) prove (1). Taking \(k=\lfloor n^{1/3}(\log n)^{2/3}\rfloor\) for sufficiently large \(n\) proves the indicated rate.

**5. Marginal central limit and joint independence.** Successive relative insertion ranks \(R_j\), \(j=1,\ldots,n\), are independent, each uniform on \(\{1,\ldots,j\}\). Therefore
\[
I_n=\sum_{j=1}^n(j-R_j),\quad
\mathbb EI_n=n(n-1)/4,\quad
\operatorname{Var}(I_n)=\frac{n(n-1)(2n+5)}{72}.
\]
All centered summands are bounded by \(n\), while their total standard deviation is of order \(n^{3/2}\). The triangular-array Lindeberg theorem yields \(Z_n\Rightarrow N(0,1/36)\). Since \(M_n\to M_\infty\) in \(L^2\), (1) gives factorization of expectations of products of bounded Lipschitz test functions; together with tightness this characterizes the independent-product joint limit (2).

## Verification

Run the included `verify.py` using Python 3 standard library. Exhaustive exact-rational comparisons cover all permutations of orders \(1\le n\le8\) (46,233 total), checking every conditional reflection class, comparison means, inversion means/variances and zero covariance; and all permutations of orders \(1\le n\le6\) (873 total) against every possible next insertion rank, checking external-gap depth and martingale conditional expectation. The program prints `VERIFY_OK`. These finite tests are independent consistency checks; the infinite claims follow from the proof above.

## Relationship to prior work

The Quicksort marginal comparison-cost limit, its search-tree representation and contraction treatment are classical. Neininger (2001) analyzes *comparison and key-exchange* counts jointly; an exchange count is not the number of inversions in the input. The full accessible author preprint was examined, particularly the Quicksort application, definitions, recursions and theorem. Brodal–Fagerberg–Moruz (2004) discuss how inversion-defined presortedness affects adaptive Quicksort behavior, not the joint fluctuations of the two variables here. Iliopoulos (2015) surveys Quicksort cost analysis; its references to inversions concern other sorting questions. Baxter–Zeilberger (2010) prove independent Gaussian limits for *inversions and major index*, a distinct pair. He–Peng–Xu (2018) study BST height under a prescribed inversion count, not the joint full internal path-length fluctuations; only the abstract was accessible, so that comparison remains a historical-priority risk. A previously established root-split-imbalance/path-length covariance is also distinct from input inversions. The exact symmetry/zero covariance and classical marginal limits are background, not the claimed contribution. The contribution is the quantitative nonlinear decoupling (1) and its independent non-Gaussian/Gaussian joint limit (2) for a concrete Quicksort rule.

## Limitations

The pivot rule and stable relative-order restriction matter. The exact finite covariance zero does not give finite independence, and the theorem does not claim a central limit for the Quicksort comparison cost itself. Rate (1) is a proved upper bound, not a claimed optimal one. The historical priority of the joint statement requires independent review: some older general permutation-statistic or recursive-algorithm results may imply it without naming inversions. A related 2012 Quicksort preprint was available at abstract level but not inspected in full because of a source-access restriction; it addresses residual cost errors rather than explicitly the inversion statistic. These uncertainties do not affect the self-contained proof.

## References

1. R. Neininger, *On a multivariate contraction method for random recursive structures with applications to Quicksort*, Random Structures & Algorithms **19** (2001), 498–524. DOI: https://doi.org/10.1002/rsa.10010 . Full author preprint: https://www.math.uni-frankfurt.de/~neiningr/multcont.pdf . First verified public journal release: 27 November 2001.
2. G. S. Brodal, R. Fagerberg and G. Moruz, *On the Adaptiveness of Quicksort*, BRICS Research Report RS-04-27 (December 2004). https://www.brics.dk/RS/04/27/BRICS-RS-04-27.pdf .
3. V. Iliopoulos, *The Quicksort Algorithm and Related Topics*, arXiv:1503.02504 (2015). https://arxiv.org/abs/1503.02504 .
4. A. Baxter and D. Zeilberger, *The Number of Inversions and the Major Index of Permutations are Asymptotically Joint-Independently Normal*, arXiv:1004.1160 (2010). https://arxiv.org/abs/1004.1160 .
5. M. He, R. Peng and Y. Xu, *Parameterizing the Hardness of Binary Search Tree Access Sequences by Inversion Counts*, ANALCO 2018, pp. 32–39. https://doi.org/10.1137/1.9781611975062.4 . Full text inaccessible in this review.
6. R. Neininger, *Refined Quicksort asymptotics*, arXiv:1207.4556 (2012). https://arxiv.org/abs/1207.4556 . Full text not accessed for this comparison.
