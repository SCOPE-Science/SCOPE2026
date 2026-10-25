# Gaussian–Poisson decoupling for local chords and global crossings

## Finding
Let a chord diagram with \(n\ge2\) chords be a uniformly selected perfect matching of \(2n\) cyclically ordered, individually labeled endpoints. Write \(X_n\) for its number of pairs of crossing chords. A chord has *length* \(j\) if the shorter open circular arc between its endpoints contains exactly \(j\) endpoints; let \(L_{j,n}\) count such chords. Define
\[
\mu_n=\frac{n(n-1)}6,\qquad
\sigma_n^2=\frac{n(n-1)(n+3)}{45},\qquad
W_n=\frac{X_n-\mu_n}{\sigma_n}.
\]
The following three assertions form one local-deletion decoupling theorem.

**Exact factorial deletion.** For \(S_n=L_{0,n}\), every integer \(0\le k\le n\), and every bounded function \(h\) of a nonnegative integer,
\[
\mathbb E\big[(S_n)_{\underline{k}}h(X_n)\big]
=\frac{N_{n,k}}{(2n-1)(2n-3)\cdots(2n-2k+1)}\,\mathbb E[h(X_{n-k})],
\quad N_{n,k}=\frac{2n}{2n-k}\frac{(2n-k)!}{(2n-2k)!}.
\]
Here \((s)_{\underline k}=s(s-1)\cdots(s-k+1)\), with the empty product equal to one; the diagram with zero chords has \(X_0=0\).

**Uniform conditional normality.** For every fixed pair of nonnegative integers \(K,J\), uniformly over all choices of \(K\) pairwise endpoint-disjoint, *prescribed* chords of length at most \(J\),
\[
\sup_{x\in\mathbb R}\left|
\Pr\{W_n\le x\mid\text{all prescribed chords occur}\}-\Phi(x)
\right|=O_{K,J}(n^{-1/2})
\quad(n\longrightarrow\infty).
\]

**Joint limiting independence.** For each fixed integer \(J\ge0\),
\[
(W_n,L_{0,n},L_{1,n},\ldots,L_{J,n})
\ \xrightarrow{\ d\ }\ (Z,P_0,P_1,\ldots,P_J),
\]
where \(Z\) is standard normal and the \(P_j\) are independent Poisson random variables of mean one, **independent also of \(Z\)**.

## Assumptions and scope
Endpoints are distinct and have fixed cyclic order. Crossing is the alternating-endpoint relation; it is preserved when unmatched endpoints are deleted and the remainder is relabeled in circular order. For the length-count statements, take \(n\ge J+2\), so every length \(0\le j\le J\) has exactly \(2n\) distinct potential chords. The conditional estimate is for any fixed \(K,J\), with \(n\) large enough to allow all prescribed chords. All limits keep \(K\) and \(J\) fixed; no assertion of uniformity for growing \(J\) is made. The means and variances displayed above are classical, as is marginal asymptotic normality of \(X_n\).

## Proof
**1. Conditioning and deletion.** Fix \(K\) endpoint-disjoint chords \(F\). Each of the \((2n-2K-1)!!\) completions of \(F\) is equally likely, so after deleting their endpoints and cyclically relabeling, the remaining matching is uniform on \(2(n-K)\) endpoints. The crossing count of surviving chords is exactly distributed as \(X_{n-K}\). Every chord of length \(j\) crosses at most \(j\) others: a crossing partner must use one endpoint in its shorter open arc, and those \(j\) endpoints belong to distinct partners. Thus when every chord in \(F\) has length at most \(J\),
\[
X_n=X_{n-K}+R_F,\qquad 0\le R_F\le KJ,
\]
under a suitable conditional coupling. Crossings between marked chords may be counted twice in the sum of their degrees, which does not affect the upper bound. If all marked chords have length zero then \(R_F=0\) identically.

**2. Exact factorial identity.** On a cycle of \(2n\) endpoints, the number of ordered \(k\)-tuples of pairwise disjoint adjacent pairs is \(N_{n,k}\): the number of \(k\)-edge matchings in a cycle is \(\frac{2n}{2n-k}\binom{2n-k}{k}\), and ordering multiplies it by \(k!\). For any specified tuple, its inclusion probability is
\[
\frac{(2n-2k-1)!!}{(2n-1)!!}
=\left[(2n-1)(2n-3)\cdots(2n-2k+1)\right]^{-1}.
\]
The zero-length marked chords cannot cross anything, so the conditional crossing count has **exactly** the \(X_{n-k}\) distribution. Expand the falling factorial \((S_n)_{\underline{k}}\) as the sum over ordered distinct present adjacent pairs, discard incompatible tuples, and take conditional expectations. This proves the displayed identity, including \(k=0\) and \(k=n\).

**3. Conditional normal approximation.** For \(m\ge2\), the classical crossing-number theorem, with the quantitative form proved by Paguyo, gives
\[
\sup_x\left|\Pr\left\{\frac{X_m-\mu_m}{\sigma_m}\le x\right\}-\Phi(x)\right|=O(m^{-1/2}).
\]
For fixed \(K,J\), the coupling in step 1 sandwiches every conditional distribution function between those of the recentered and rescaled \(X_{n-K}\), shifted by at most \(KJ/\sigma_n\). Direct substitution shows
\[
\frac{|\mu_n-\mu_{n-K}|+KJ}{\sigma_n}=O_{K,J}(n^{-1/2}),
\qquad \frac{\sigma_{n-K}}{\sigma_n}=1+O_K(n^{-1}).
\]
The standard normal cdf is Lipschitz; its change under these shifts and positive scale perturbations is bounded by a constant times their size (the derivative of \(\Phi(x/a)\) with respect to \(a\) is uniformly bounded near \(a=1\)). This proves the claimed uniform Kolmogorov estimate.

**4. Mixed factorial moments.** Fix \(J\) and a multiindex \(\mathbf r=(r_0,\ldots,r_J)\), with \(K=\sum_j r_j\). Expand \(\prod_j(L_{j,n})_{\underline{r_j}}\) into ordered arrays of prescribed chords. Each length class has \(2n\) candidates; at fixed \(K,J\), only \(O_{K,J}(n^{K-1})\) arrays repeat a chord or share an endpoint. Thus the number of compatible arrays is \((2n)^K[1+O_{K,J}(1/n)]\). By the first step, each compatible array occurs with probability \(\prod_{h=0}^{K-1}(2n-2h-1)^{-1}\), and by step 3 its conditional \(W_n\) converges uniformly to \(Z\). For any bounded continuous \(f\), therefore,
\[
\mathbb E\left[f(W_n)\prod_{j=0}^J(L_{j,n})_{\underline{r_j}}\right]
\longrightarrow \mathbb E[f(Z)].
\]
Taking \(f=1\) gives all mixed factorial moments of independent unit-mean Poisson variables. Bounded higher factorial moments ensure uniform integrability of every polynomial in the \(L_{j,n}\); bounded first moments give tightness of their vector, while \(W_n\) is tight by the preceding normal approximation. For any subsequential joint limit, the displayed mixed factorial moments factor for every bounded nonnegative continuous \(f\). The multivariate Poisson law is moment-determinate (its moment generating function is finite everywhere), so its \(f\)-weighted count law equals \(\mathbb E[f(Z)]\) times the product-Poisson law. Hence the joint limit is unique and factors, proving independence.

## Verification
The standalone `verify.py`, runnable with `python3 verify.py` and using only the Python standard library, exhaustively enumerates all \(146598\) perfect matchings on \(2n\) endpoints for \(2\le n\le7\). It checks the exact factorial deletion identity for all \(0\le k\le n\) via integer cross-multiplication of probability distributions. For every eligible anchored chord of lengths \(0,1,2,3\), it also checks that deleting that chord changes the crossing count by a nonnegative amount at most its length. The run completes with `VERIFY_OK total matchings 146598`. These finite checks are diagnostics; they are not the infinite-dimensional or asymptotic proof, which is given above.

## Relationship to prior work
Flajolet and Noy established crossing-number Gaussian asymptotics and classical moment formulas. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, Theorem 4.2, establishes the **mutual Poisson limiting independence of the fixed short-length counts alone**. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, Theorems 1.1 and 1.2, establishes quantitative **separate** Gaussian and Poisson marginal approximations. These marginal theorems do not, by themselves, determine the cross-statistic joint limit. The assertion here is a uniform conditional Gaussian law under specified local chords and consequently Gaussian independence from **all** fixed short-length Poisson counts, together with an exact factorial deletion transform for zero-length chords. Classical input results are not claimed as new.

## Limitations
Only fixed finite sets of chord lengths and fixed numbers of prescribed local chords are covered; no rate is proved for the full joint multivariate law or for increasing cutoff \(J\). The quantitative conditional normality relies on the previously published crossing-number normal approximation; it is not a new proof of that estimate. An earlier general joint generating-function or marked-matching theorem might imply the present joint limit and should be checked in an independent literature audit. In particular, the full Flajolet–Noy chapter could not be inspected in the available access context; only its bibliographic abstract and descriptions in later full texts were compared. No independent audit has been performed.

## References
1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first submitted 2 April 2021; Theorems 1.1 and 1.2, Lemma 2.2. https://arxiv.org/abs/2104.01134
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first submitted 7 January 2015; Theorem 4.2. https://arxiv.org/abs/1501.01489
3. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, in *Formal Power Series and Algebraic Combinatorics* (2000), pp. 191–201, DOI:10.1007/978-3-662-04166-6_17. Full-text priority comparison remains outstanding.
