# Spatial Poisson errors and the sharp exact-ordering transition for exponential races

## Finding

Let independent exponential clocks be ordered by decreasing rates as specified below. When successive rates are separated by factors of order \(n^{-1}\), their random ordering has an asymptotically complete description: all errors are disjoint neighboring transpositions, and their locations converge to an inhomogeneous Poisson point process.

**Theorem.** Let \(a:[0,1]\to[0,\infty)\) be continuous. For each integer \(n\ge2\), take arbitrary positive rates \(\lambda_{n,1},\ldots,\lambda_{n,n}\), and suppose
\[
\max_{1\le i<n}\left|n\frac{\lambda_{n,i+1}}{\lambda_{n,i}}-a(i/n)\right|\longrightarrow0.
\]
Independently sample \(T_{n,i}\sim\operatorname{Exp}(\lambda_{n,i})\), where the argument is the *rate*. Let \(\sigma_n\) be the unique permutation with
\[
T_{n,\sigma_n(1)}<\cdots<T_{n,\sigma_n(n)}.
\]
Writing \(A_{n,i}=\mathbf1_{\{T_{n,i+1}<T_{n,i}\}}\), the random point measure
\[
\Xi_n=\sum_{i=1}^{n-1}A_{n,i}\,\delta_{i/n}
\]
converges in law on \([0,1]\) to a Poisson point process of intensity \(a(t)\,dt\). With probability \(1-O(n^{-1})\), the permutation \(\sigma_n\) is *exactly* the permutation obtained from \((1,2,\ldots,n)\) by simultaneously swapping each pair \((i,i+1)\) for which \(A_{n,i}=1\); those pairs are then disjoint.

Consequently, with \(\Lambda=\int_0^1 a(t)\,dt\), its full inversion count \(I_n\) converges to \(\operatorname{Poisson}(\Lambda)\), and
\[
\Pr(\sigma_n=\mathrm{id})\longrightarrow e^{-\Lambda},
\qquad
\Pr(\sigma_n\text{ even})-\Pr(\sigma_n\text{ odd})\longrightarrow e^{-2\Lambda}.
\]

For the geometric-rate subfamily \(\lambda_{n,i}=\lambda_{n,1}r_n^{i-1}\), where \(0<r_n<1\), the *exact finite-size* perfect-ranking probability is
\[
\Pr(\sigma_n=\mathrm{id})=
\frac{(1-r_n)^{n-1}}{\prod_{k=2}^{n}(1-r_n^k)}.
\]
For every sequence \(r_n\to0\), its limit is \(1\), \(e^{-c}\), or \(0\) according as \(nr_n\to0\), \(nr_n\to c\in(0,\infty)\), or \(nr_n\to\infty\). In particular, when \(-\log r_n-\log n\to x\in\mathbb R\), the perfect-ranking probability converges to the Gumbel profile \(\exp(-e^{-x})\).

## Assumptions and scope

All clocks are independent and have continuous exponential laws. The \(\lambda_{n,i}\) need not have an explicit formula, are positive, and depend on \(n\). Rate ratios are defined between *consecutive labels*, not consecutive random order statistics. No equal-clock ties occur. Continuity and boundedness of \(a\) give uniform control of all neighboring ratios; they do not require \(a\) to be everywhere positive. The first claim is a point-process limit under the displayed uniform hypothesis. The geometric-rate classification additionally allows \(nr_n\) to diverge but requires \(r_n\to0\).

The inversion count \(I_n\) is the number of label pairs \((i,j)\) with \(1\le i<j\le n\) for which \(T_{n,j}<T_{n,i}\). Parity refers to this inversion count. The point-process law is convergence of finite measures on compact \([0,1]\), equivalently convergence of their Laplace functionals against nonnegative continuous test functions.

## Proof

**1. Exact pair comparisons and exclusion of long inversions.** Put
\[
r_{n,i}=\lambda_{n,i+1}/\lambda_{n,i},\qquad
R_n=\max_{i<n}r_{n,i}.
\]
The hypothesis gives \(R_n\le C/n\) for all sufficiently large \(n\) and some constant \(C\). Independence and the exponential race identity give, for \(i<j\),
\[
\Pr(T_{n,j}<T_{n,i})=
\frac{\lambda_{n,j}}{\lambda_{n,i}+\lambda_{n,j}}
\le\frac{\lambda_{n,j}}{\lambda_{n,i}}
=\prod_{h=i}^{j-1}r_{n,h}\le R_n^{j-i}.
\]
Therefore, for \(R_n<1\),
\[
\Pr\left(\exists\,i<j-1:T_{n,j}<T_{n,i}\right)
\le\sum_{d=2}^{n-1}(n-d)R_n^d
\le\frac{nR_n^2}{1-R_n}=O(n^{-1}).
\]
On the complementary event every inversion joins consecutive labels. Two consecutive adjacent inversions would imply a distance-two inversion by transitivity, so the inverted neighboring pairs are disjoint. Inversion sets uniquely determine permutations, hence \(\sigma_n\) consists exactly of the asserted disjoint neighboring swaps.

**2. Joint bounds for neighboring inversion indicators.** For \(1\le i<n\), the exponential two-clock formula yields
\[
p_{n,i}:=\Pr(A_{n,i}=1)=\frac{r_{n,i}}{1+r_{n,i}},
\qquad \max_i p_{n,i}=O(n^{-1}).
\]
The events \(A_{n,i}\) and \(A_{n,j}\) are independent whenever \(|i-j|\ge2\), because they then use disjoint clock pairs. For any consecutive run \(A_{n,u}=\cdots=A_{n,u+\ell-1}=1\), the order is
\(T_{n,u+\ell}<\cdots<T_{n,u}\). The exponential-race ordering formula gives the exact probability
\[
\prod_{j=1}^{\ell}
\frac{\lambda_{n,u+j}}{\sum_{h=0}^{j}\lambda_{n,u+h}}
\le\prod_{j=1}^{\ell}r_{n,u+j-1}\le R_n^{\ell}.
\]
Every finite subset of indicator indices decomposes into disjoint consecutive runs, whose underlying clock sets are disjoint. Thus for every subset \(S\subseteq\{1,\ldots,n-1\}\),
\[
\Pr(A_{n,i}=1\text{ for all }i\in S)\le R_n^{|S|}.
\]
For sets containing no neighboring indices, this probability is exactly \(\prod_{i\in S}p_{n,i}\).

**3. Spatial Poisson convergence.** Fix any nonnegative continuous \(f:[0,1]\to\mathbb R\) and let \(b_{n,i}=1-e^{-f(i/n)}\). By the product expansion,
\[
\mathbb E\,e^{-\int f\,d\Xi_n}
=\sum_{k=0}^{n-1}(-1)^k
\sum_{\substack{S\subseteq\{1,\ldots,n-1\}\\|S|=k}}
\left(\prod_{i\in S}b_{n,i}\right)
\Pr(A_{n,i}=1\text{ for all }i\in S).
\]
For every fixed \(k\), at most \(O_k(n^{k-1})\) of the size-\(k\) subsets contain neighboring indices. Each corresponding term has absolute value at most \(R_n^k=O(n^{-k})\), so their total is \(O_k(n^{-1})\). On the remaining subsets the probabilities factor into \(p_{n,i}\). The uniform hypothesis, Riemann sums, and \(p_{n,i}-r_{n,i}=O(n^{-2})\) imply
\[
\sum_{i=1}^{n-1}b_{n,i}p_{n,i}
\longrightarrow L_f:=\int_0^1a(t)(1-e^{-f(t)})\,dt.
\]
Expansion of the corresponding elementary symmetric sum shows that the size-\(k\) contribution tends to \(L_f^k/k!\). Moreover each complete size-\(k\) contribution is at most \(\binom nk R_n^k\le C^k/k!\) in absolute value, so the exponential series dominates uniformly. Taking the limit of the entire expansion gives
\[
\lim_{n\to\infty}\mathbb E\,e^{-\int f\,d\Xi_n}
=\sum_{k=0}^\infty\frac{(-L_f)^k}{k!}
=\exp\!\left[-\int_0^1a(t)(1-e^{-f(t)})\,dt\right],
\]
which is precisely the Laplace functional of the stated Poisson point process. This proves the first assertion and, with Step 1, the full-permutation description.

**4. Inversion count, parity, and perfect recovery.** Step 1 implies that with probability \(1-O(n^{-1})\), the inversion count equals \(\Xi_n([0,1])\). The latter converges to a Poisson random variable with mean \(\Lambda\). The same bound transfers both the zero-inversion probability and the expectation of the bounded parity sign \((-1)^{I_n}\), whose Poisson expectation is \(e^{-2\Lambda}\).

For geometric rates, sequentially choosing the earliest remaining exponential clock yields
\[
\Pr(\sigma_n=\mathrm{id})
=\prod_{i=1}^{n}\frac{\lambda_{n,i}}{\sum_{j=i}^{n}\lambda_{n,j}}
=\prod_{k=2}^{n}\frac{1-r_n}{1-r_n^k}.
\]
When \(nr_n\to c<\infty\), Step 3 applies with the constant profile \(a\equiv c\), including \(c=0\). If \(r_n\to0\) but \(nr_n\to\infty\), the \(\lfloor n/2\rfloor\) events \(A_{n,1},A_{n,3},A_{n,5},\ldots\) are independent and each has probability \(r_n/(1+r_n)\). Since a perfect ranking requires all of them to be zero,
\[
\Pr(\sigma_n=\mathrm{id})\le
(1+r_n)^{-\lfloor n/2\rfloor}\longrightarrow0.
\]
Finally \(-\log r_n-\log n\to x\) is equivalent to \(nr_n\to e^{-x}\), giving \(\exp(-e^{-x})\). All claimed cases follow. \(\square\)

## Verification

The standalone standard-library program `check.py` enumerates exact Plackett–Luce ordering probabilities using rational arithmetic for \(2\le n\le7\) under three rate-ratio families at each size. Its 340 assertions compare the full permutation probabilities with their exact normalization, the identity probability with both exponential-race product expressions, every pairwise inversion probability, every overlapping neighboring-pair probability, independence of nonoverlapping neighboring comparisons, and the nonadjacent-inversion union bound. Run it with `python check.py`; its expected output is `PASS: 340 independent exact-rational finite checks`.

Those checks concern finite identities only. The universal bounds, convergence of point processes, and limiting recovery profile are proved analytically in Steps 1–4, not inferred from finite enumeration.

## Relationship to prior work

Turvey's 2026 study of permutations generated by independent random variables determines the dimension of the space of attainable ranking laws and shows nontrivial Mallows measures cannot be represented for sufficiently many labels. The present result addresses a different question within that framework: the spatial distribution and full permutation structure of rare errors when independent variables are exponential with rapidly separated rates. Neither the dimension result nor the Mallows obstruction implies the stated Poisson process or recovery threshold.

Babson and collaborators' earlier study of random spanning trees develops the attainable-law and independent-ranking framework; its full text considers finite-dimensional constraints and applications to greedy spanning trees, not this growing-size rare-inversion limit. The Plackett–Luce exponential race and elementary Poisson approximation ideas are standard ingredients and are not claimed as new. The result isolates a model-specific asymptotic ranking law and exact finite-size recovery formula, rather than claiming a new general Poisson approximation principle.

## Limitations

The spatial theorem assumes independent **exponential** clocks with neighboring rate ratios uniformly of order \(n^{-1}\). The proof does not cover arbitrary independent continuous variables, correlated clocks, ties, or ratios appreciably larger than \(n^{-1}\) except for the scalar perfect-ranking classification in the geometric subfamily. The point-process statement gives weak convergence, not an optimal total-variation rate for the full permutation law. Secondary near-neighbor error regimes and rates below the first error scale are not classified. Priority uncertainty persists for possibly unindexed equivalent results on high-signal exponential races or rare inversions of random utility rankings.

## References

1. Luke Turvey, *Permutations from ranking independent random variables*, arXiv:2610.11895v1, first posted 2026-10-08. https://arxiv.org/html/2610.11895v1
2. Eric Babson, Moon Duchin, Annina Iseli, Pietro Poggi-Corradini, Dylan Thurston, and Jamie Tucker-Foltz, *Models of random spanning trees*, arXiv:2407.20226, first posted 2024-07-29; *Random Structures & Algorithms* 68 (2026), e70063. https://arxiv.org/abs/2407.20226
3. Harry Joe, *Inequalities for Random Utility Models, with Applications to Ranking and Subset Choice Data*, *Methodology and Computing in Applied Probability* 2 (2000), 359–372. https://doi.org/10.1023/A:1010058117460
4. John Guiver and Edward Snelson, *Bayesian inference for Plackett–Luce ranking models*, 2009. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/plackett.pdf
