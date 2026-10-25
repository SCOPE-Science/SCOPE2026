# Bias-sensitive Lyndon subsequence growth and a sharp uniform-source optimizer

## Finding
Let \(\Sigma\) be a totally ordered finite alphabet of \(q\ge2\) symbols. Let \(\mathbf p=(p_a)_{a\in\Sigma}\) satisfy \(p_a>0\) and \(\sum_a p_a=1\). The letters of \(W_n\) are independent and have distribution \(\mathbf p\). A Lyndon word is a nonempty primitive word that is strictly lexicographically smaller than each nontrivial cyclic rotation. Let \(L_n\) count **distinct Lyndon strings** occurring as scattered subsequences of \(W_n\), regardless of their positional multiplicity.

Write \(\mu\) for the ordinary number-theoretic Möbius function and define
\[
g_a(z)=\frac{p_a z}{1-(1-p_a)z},\qquad S_d(z)=\sum_{a\in\Sigma}g_a(z)^d \quad(d\ge1).
\]
Then the exact ordinary generating function of the expectations is
\[
\boxed{\sum_{n\ge0}\mathbb E[L_n]z^n=-\frac1{1-z}\sum_{d\ge1}\frac{\mu(d)}d\log(1-S_d(z)).}
\]
The identity holds as a formal power series and analytically near the origin.

There is a unique \(r\in(0,1)\) for which \(S_1(r)=1\). As \(n\to\infty\) with the source distribution fixed,
\[
\boxed{\mathbb E[L_n]=\frac{r^{-n}}{(1-r)n}\left(1+O_{\mathbf p}(n^{-1})\right).}
\]
If \(D_n\) counts all distinct **nonempty** scattered subsequence strings of \(W_n\), then
\[
\boxed{\frac{\mathbb E[L_n]}{\mathbb E[D_n]}=\frac{rS_1'(r)}n\left(1+O_{\mathbf p}(n^{-1})\right).}
\]
For a fixed alphabet size \(q\), the exponential growth base \(\lambda(\mathbf p)=r^{-1}\) is strictly Schur-concave on the positive probability simplex: if \(\mathbf p\) majorizes \(\mathbf p'\) and is not a permutation of it, then \(\lambda(\mathbf p)<\lambda(\mathbf p')\). In particular,
\[
\boxed{\lambda(\mathbf p)\le 2-\frac1q,}
\]
with equality exactly for the uniform distribution. At uniformity,
\[
\mathbb E[L_n]\sim\frac{2q-1}{q-1}\frac{(2-1/q)^n}{n}.
\]
The last uniform specialization is a *new asymptotic interpretation of a previously published exact uniform expectation*, not a claim that the uniform expectation itself is new.

## Assumptions and scope
Every source letter has strictly positive probability, and there are at least two source symbols. The alphabet is totally ordered solely to choose canonical Lyndon representatives. The word \(W_0\) is empty, giving \(L_0=D_0=0\). A scattered subsequence has indices in strictly increasing order; two position selections with identical resulting strings contribute only one to \(L_n\). The formula does not count Lyndon *occurrences* or contiguous factors. The asymptotic error constants may depend on \(\mathbf p\), and no uniform statement as a source probability tends to zero is asserted. Majorization concerns distributions of the same fixed alphabet cardinality.

## Proof
**1. Greedy matching.** Fix a nonempty pattern \(u=u_1\cdots u_m\). Its first occurrence as a scattered subsequence ends when successive left-to-right greedy matches for \(u_1,\ldots,u_m\) finish. Independence of the source implies that the successive waiting times are independent geometric variables with success parameters \(p_{u_i}\), supported on positive integers. The probability generating function of their sum is \(\prod_{i=1}^{m}g_{u_i}(z)\). Summing the event that the sum is at most \(n\) over \(n\ge0\) gives
\[
\sum_{n\ge0}\Pr(u\preceq W_n)z^n=\frac{\prod_{i=1}^{m}g_{u_i}(z)}{1-z}.
\]
Linearity of expectation now reduces the problem to the multivariate weight enumerator of Lyndon words.

**2. Multivariate primitive-necklace identity.** Assign an indeterminate \(x_a\) to each symbol. For each \(m\ge1\), the sum of weights of all length-\(m\) words is \((\sum_a x_a)^m\). Every such word is a power of a unique primitive root. Möbius inversion on the repetition factor shows that the weight sum of primitive words of length \(m\) is
\[
\sum_{d\mid m}\mu(d)\left(\sum_a x_a^d\right)^{m/d}.
\]
Primitive words split into rotation orbits of size \(m\), all rotations having the same weight, with one Lyndon representative in each orbit. Thus the weight sum of length-\(m\) Lyndon words is exactly \(1/m\) times the displayed expression. Summing over \(m\) and reorganizing by \(d\mid m\) yields
\[
\sum_{u\text{ Lyndon}}\prod_{i=1}^{|u|}x_{u_i}
=-\sum_{d\ge1}\frac{\mu(d)}d\log\left(1-\sum_a x_a^d\right).
\]
Substituting \(x_a=g_a(z)\) and using Step 1 proves the exact generating function.

**3. Singular asymptotics.** For real \(z\in[0,1]\), \(S_1(z)\) strictly increases from \(0\) to \(q\), establishing unique \(r\in(0,1)\). At this point every \(g_a(r)\) lies strictly between zero and one, whence \(S_2(r)<S_1(r)=1\). The terms with \(d\ge2\) in the logarithmic identity form an analytic function in a disk of radius strictly greater than \(r\): choose a slightly larger radius so that \(\sum_a |g_a(z)|^2<1\), \(\max_a|g_a(z)|<1\), and the defining series converges uniformly. Furthermore each \(g_a(z)\) has strictly positive coefficients at every positive power (because \(0<p_a<1\)), so the strict triangle inequality gives \(|S_1(z)|<1\) for \(|z|=r\) with \(z\ne r\). The simple zero \(1-S_1(r)=0\), with \(S_1'(r)>0\), is therefore the unique dominant zero of \(1-S_1(z)\). By isolation of analytic zeros, a radius \(R>r\) can be chosen so that
\[
-\log(1-S_1(z))=-\log(1-z/r)+A(z),
\]
where \(A\) is analytic on \(|z|<R\). Shrink \(R\) below one if necessary. Consequently
\[
\sum_{n\ge0}\mathbb E[L_n]z^n
=-\frac{\log(1-z/r)}{1-z}+B(z),
\]
with \(B\) analytic on \(|z|<R\). The dominant coefficients are exactly
\[
[z^n]\left(-\frac{\log(1-z/r)}{1-z}\right)=\sum_{m=1}^{n}\frac{r^{-m}}m
=\frac{r^{-n}}{(1-r)n}(1+O(n^{-1})),
\]
while \([z^n]B(z)=O(R_0^{-n})\) for any \(r<R_0<R\). This proves the first asymptotic.

**4. Comparison with all distinct subsequences.** Summing the matching generating functions from Step 1 over *all* nonempty target strings gives
\[
\sum_{n\ge0}\mathbb E[D_n]z^n
=\frac{S_1(z)}{(1-z)(1-S_1(z))}.
\]
The same dominant-zero argument shows
\[
\mathbb E[D_n]\sim\frac{r^{-n}}{(1-r)rS_1'(r)}.
\]
Division by the result of Step 3 establishes the stated ratio.

**5. Majorization and the exact maximum.** For fixed \(z\in(0,1)\), the function \(f_z(t)=tz/(1-z+tz)\) satisfies
\[
f_z''(t)=-\frac{2z^2(1-z)}{(1-z+tz)^3}<0.
\]
Therefore \(\sum_a f_z(p_a)=S_1(z)\) is strictly Schur-concave. If \(\mathbf p\) majorizes \(\mathbf p'\), strictness away from permutations gives \(S_{1,\mathbf p}(z)<S_{1,\mathbf p'}(z)\); comparing their unique crossings of level one yields \(r(\mathbf p)>r(\mathbf p')\). The maximum occurs uniquely at uniform probabilities. In that case \(S_1(z)=qz/(q-(q-1)z)\), so \(r=q/(2q-1)\), and the claimed maximum base and prefactor follow.

## Verification
The standalone `verify.py` uses exact rational arithmetic and two logically different procedures: direct enumeration of all scattered subsequences of each source word, and a truncated coefficient computation from the Möbius–geometric series. It checks complete collections of source words for two binary and two ternary probability distributions, including biased distributions. The source-length ranges are 0–11, 0–10, 0–8 and 0–8, comprising 25,824 source-word cases in total. It also compares the asymptotic form with the previously known finite-length uniform formula at lengths 20, 40 and 80. Execute with `python3 verify.py`; Python's standard library suffices. These finite tests do not prove the asymptotics or the theorem; the argument above does.

## Relationship to prior work
Hirakawa, Nakashima, Inenaga and Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190v1 (first public 2021-06-02), Theorem 4, already provide the **exact uniform-alphabet expectation**. That theorem is expressly excluded from the originality claim. Indeed, putting all probabilities equal in Step 1 converts their finite binomial formula into the uniform specialization of our formal-series identity. The contribution here is the exact **arbitrary positive nonuniform source** identity, the sharp source-dependent asymptotic with an explicit universal logarithmic prefactor, the precise comparison with all distinct subsequences, and strict majorization of the exponential rate.

Biers-Ariel, Godbole and Kelley, arXiv:1704.08661 (first public 2017-04-27), study the mean count of **all** distinct subsequences under biased sources, not Lyndon-specific canonical primitive subsequences. Bannai, I, Kociumaka, Köppl and Puglisi, arXiv:2201.06773 (first public 2022-01-18), investigate algorithms for finding longest Lyndon subsequences rather than this random-source statistic. The classical multivariate Witt/necklace identity is used as a standard ingredient, not claimed as new. The specific conjunction of source bias, exact expected Lyndon counts, asymptotic prefactor, and majorization was not identified in the examined literature; equivalent unindexed coverage is a residual risk.

## Limitations
The original uniform finite-length mean is known, and this result must not be interpreted as rediscovering it. The argument gives expectations, not variance or concentration, and does not identify the typical sample-path Lyndon count. No uniform limit is claimed as a letter probability tends to zero or as the alphabet grows. The originality assessment relies on accessible primary literature and indexed comparisons rather than a proof of global uniqueness. Independent audit has not been performed.

## References
1. R. Hirakawa, Y. Nakashima, S. Inenaga, M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190v1, 2021-06-02. https://arxiv.org/abs/2106.01190
2. Y. Biers-Ariel, A. Godbole, E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661v1, 2017-04-27. https://arxiv.org/abs/1704.08661
3. H. Bannai, T. I, T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest (Common) Lyndon Subsequences*, arXiv:2201.06773v1, 2022-01-18. https://arxiv.org/abs/2201.06773
4. P. Moree, *The formal series Witt transform*, Discrete Mathematics 295 (2005), 143–160, DOI:10.1016/j.disc.2005.03.004; the classical primitive-necklace identity is background.
