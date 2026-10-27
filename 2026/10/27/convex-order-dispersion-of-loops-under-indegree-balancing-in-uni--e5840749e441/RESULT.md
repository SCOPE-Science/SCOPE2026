# Convex-order dispersion of loops under indegree balancing in uniform random mappings

## Finding
Let \(n\ge2\), and let \(\mathbf d=(d_1,\ldots,d_n)\) be nonnegative integers with \(\sum_i d_i=n\). Draw uniformly a function \(f:[n]\to[n]\) with exactly \(d_i\) preimages of vertex \(i\), and write \(F_{\mathbf d}=|\{i:f(i)=i\}|\) for its number of fixed points (loops in its functional digraph).

If \(d_u=A\ge B+2=d_v+2\), replace these entries by \(A-1,B+1\), obtaining \(\mathbf d'\). Put \(\delta=A-B-1>0\), and let \(\mathbf c\) be the remaining \(n-2\) entries. There is an explicitly constructed nonnegative integer random variable \(H_{\mathbf c}\) (defined below) such that **for every function** \(\phi:\{0,\ldots,n\}\to\mathbb R\),
\[
\mathbb E\phi(F_{\mathbf d'})-\mathbb E\phi(F_{\mathbf d})
=\frac{\delta}{n(n-1)}\mathbb E[\phi(H_{\mathbf c}+2)-2\phi(H_{\mathbf c}+1)+\phi(H_{\mathbf c})].
\]
In particular \(F_{\mathbf d}\le_{\mathrm{cx}}F_{\mathbf d'}\), with **strict inequality for every strictly convex test function**, because \(\delta>0\). Thus if \(\mathbf d\) majorizes \(\mathbf e\) (both vectors nonnegative integral with sum \(n\)), then \(F_{\mathbf d}\le_{\mathrm{cx}} F_{\mathbf e}\); the inequalities are strict for strictly convex tests unless the vectors are permutations of one another.

Among all fixed-indegree profiles, the one-image mapping \((n,0,\ldots,0)\) minimizes fixed-point dispersion and the uniform random permutation profile \((1,\ldots,1)\) maximizes it in convex order. All profiles satisfy
\[
\mathbb E F_{\mathbf d}=1,\qquad
\operatorname{Var}(F_{\mathbf d})=\frac{n^2-\sum_i d_i^2}{n(n-1)}.
\]
A unit balancing transfer increases the variance by exactly \(2\delta/[n(n-1)]\).

## Assumptions and scope
This is a **uniform mapping conditional on its entire target-indegree vector**, not a random permutation of a multiset measured against a reference word containing repeated symbols. Every allowable map has probability \((\prod_i d_i!)/n!\). The vector \(\mathbf d\) may contain zeros; only \(n\ge2\) is required for the transfer law. Majorization means that, after decreasing rearrangement, every initial partial sum of \(\mathbf d\) is at least that of \(\mathbf e\), with equal total sums. Convex order means expectation inequalities for all convex real functions on the finite integer support, with equal means.

To define \(H_{\mathbf c}\), write the positive entries of \(\mathbf c\) as \(c_1,\ldots,c_s\). Since \(A+B\ge2\), one has \(\sum_j c_j\le n-2\), so choose pairwise disjoint fixed subsets \(B_j\subseteq[n-2]\) with \(|B_j|=c_j\). Sample an ordered injection \((U_1,\ldots,U_s)\) uniformly among injections from \([s]\) into \([n-2]\), and set \(H_{\mathbf c}=\sum_j\mathbf1_{\{U_j\in B_j\}}\). If \(s=0\), set \(H_{\mathbf c}=0\). Its distribution does not depend on the placement of the disjoint sets.

## Proof
For \(0\le r\le n\), write \((n)_r=n(n-1)\cdots(n-r+1)\), with \((n)_0=1\), and write \(e_r(\mathbf d)\) for the elementary symmetric polynomial of degree \(r\), with \(e_0=1\). For distinct vertices \(i_1,\ldots,i_r\), conditioning on indegrees gives
\[
\Pr\{f(i_1)=i_1,\ldots,f(i_r)=i_r\mid\mathbf d\}
=\frac{d_{i_1}\cdots d_{i_r}}{(n)_r}.
\]
This follows by exposing \(r\) positions of a uniformly random ordering of the multiset of target labels: each required distinct label removes one copy from the appropriate multiplicity. Summing over ordered tuples yields \(\mathbb E(F_{\mathbf d})_r=r!e_r(\mathbf d)/(n)_r\), and the finite binomial expansion gives
\[
P_{\mathbf d}(z):=\mathbb E z^{F_{\mathbf d}}
=\sum_{r=0}^{n}\frac{e_r(\mathbf d)}{(n)_r}(z-1)^r.
\]
The same exposure applied to the random injection defining \(H_{\mathbf c}\) shows
\[
Q_{\mathbf c}(z):=\mathbb E z^{H_{\mathbf c}}
=\sum_{r=0}^{n-2}\frac{e_r(\mathbf c)}{(n-2)_r}(z-1)^r.
\]
For the balancing move, elementary-symmetric generating polynomials satisfy the **exact factorization**
\[
\prod_i(1+d_i't)-\prod_i(1+d_it)
=\bigl[(1+(A-1)t)(1+(B+1)t)-(1+At)(1+Bt)\bigr]\prod_{i\notin\{u,v\}}(1+d_it)
=\delta t^2\prod_{i\notin\{u,v\}}(1+d_it).
\]
Substituting the resulting coefficient identity \(e_{r+2}(\mathbf d')-e_{r+2}(\mathbf d)=\delta e_r(\mathbf c)\) into the formula for \(P\), and using \((n)_{r+2}=n(n-1)(n-2)_r\), yields
\[
P_{\mathbf d'}(z)-P_{\mathbf d}(z)
=\frac{\delta}{n(n-1)}(z-1)^2Q_{\mathbf c}(z).
\]
Equating coefficients of \(z^j\), multiplying by \(\phi(j)\), and summing proves the stated second-difference identity. Its right side is nonnegative for convex \(\phi\), and is positive for every strictly convex \(\phi\): the auxiliary law is a probability distribution and the discrete second difference of a strictly convex function is positive at every integer in its support.

The classical integer majorization criterion states that \(\mathbf e\) can be obtained, up to permutation, from \(\mathbf d\) by successive unit transfers from a coordinate at least two larger than another. Repeated application of the displayed identity proves the convex-order statement, and a nontrivial chain contains a strictly positive step. Permuting \(\mathbf d\) does not change \(P_{\mathbf d}\) because it contains only symmetric polynomials. Finally, \(e_1(\mathbf d)=n\) gives \(\mathbb EF=1\); \(2e_2(\mathbf d)=n^2-\sum_i d_i^2\) gives the stated variance. The one-mass and all-one vectors are respectively maximal and minimal in the majorization preorder, yielding the sharp sandwich.

## Verification
Run `python verify_balancing.py` using Python 3 and the standard library. The program enumerates ordered injections directly for every integer partition of \(n\) through \(n=8\), independently computes probability generating functions from exact falling-factorial moments, and checks all allowable single-unit degree-balancing transfers, the exact second-difference coefficients, every integer-threshold convex-call inequality, and variance increments. It passed 4,372 exact assertion units. This finite testing is supplementary: the argument above proves the theorem for all \(n\ge2\), all permitted vectors, all transfers and all convex tests.

## Relationship to prior work
Hansen and Jaworski's 2006 preprint develops the prescribed/exchangeable-in-degree random-mapping framework and analyzes cyclic vertices, components and component size, not the stated convex-order comparison of loop counts. Leckey and Wormald subsequently studied six-length under prescribed indegrees rather than this loop-count distribution. Classical fixed-point factorial-moment counting motivates the proof but does not by itself state the second-difference transfer kernel or the full convex-order law.

Stark's 2026 study of fixed points of multiset permutations uses a **different fixed-point statistic**, comparing a permuted multiset with its sorted repeated-symbol reference word; its mean is \(\sum_i d_i^2/n\). Here every source position has its own unique target label, giving mean exactly one. The two models must not be identified. No independent claim of priority or audit is made.

## Limitations
This is an exact finite result for mappings conditioned on a deterministic indegree vector; it does not assert stochastic ordering, because every profile has the same mean and nonidentical laws cannot be stochastically ordered. The proof gives only a sufficient order condition through majorization; it does **not** characterize all pairs of profiles that happen to be convex-order comparable. Published priority remains subject to independent literature assessment, especially general classical matching and permutation-order results. No asymptotic Poisson approximation or extension to random directed graphs with general outdegree is claimed.

## References
- J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529v1, publicly posted 2006-03-22, https://arxiv.org/pdf/math/0603529.
- K. Leckey and N. Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence*, arXiv:1803.02667, 2018, https://arxiv.org/abs/1803.02667.
- D. Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710, 2026, https://arxiv.org/html/2608.00710 (different matching statistic).
