# Conditional triad fluctuations and a Krawtchouk projection for fair tournaments

## Finding

Let \(T\) be a uniform random tournament on \(n\ge3\) labelled vertices, obtained by orienting all pairs independently and fairly. Write \(S_v\) for the outdegree (number of wins) of vertex \(v\), and \(C\) for the number of directed cyclic triples. Put \(N=n-1\). Then for each vertex and every integer \(0\le k\le N\),

\[
\mathbb E[C\mid S_v=k]=\tfrac14\binom N3+\tfrac12 k(N-k),\qquad
\operatorname{Var}(C\mid S_v=k)=\tfrac3{16}\binom N3+\tfrac14 k(N-k).
\]

Here and throughout \(\binom a3=0\) when \(a<3\). Thus these are exact conditional first and second moments, for every finite order, not asymptotic approximations.

For any real function \(f:\{0,\ldots,N\}\to\mathbb R\), define the additive score statistic \(A_f=\sum_v f(S_v)\), and let \(X\sim\operatorname{Bin}(N,1/2)\). Then the entire cross-covariance functional is

\[
\boxed{\operatorname{Cov}(C,A_f)=-\frac n8\,\mathbb E\left[\left((2X-N)^2-N\right)f(X)\right].}
\]

Equivalently, with the binary Krawtchouk polynomial \(K_2(k)=\tfrac12((N-2k)^2-N)\), the functional is \(-n\mathbb E[K_2(X)f(X)]/4\): **only the degree-two Krawtchouk component of an arbitrary additive score statistic can correlate with the cyclic-triple count**.

In particular, letting \(M_k=\#\{v:S_v=k\}\) and \(p_k=2^{-N}\binom Nk\),

\[
\boxed{\operatorname{Cov}(C,M_k)=-\frac{n p_k}{8}\left((2k-N)^2-N\right).}
\]

The sign is positive strictly inside the interval \(|2k-N|<\sqrt N\), negative strictly outside it, and zero at equality. Such exact zero covariances occur if and only if \(N=t^2\) for an integer \(t\ge2\), then precisely at \(k=(t^2-t)/2\) and \(k=(t^2+t)/2\). Both strictly positive and strictly negative cases occur for every \(n\ge3\).

## Assumptions and scope

All \(\binom n2\) edge orientations are mutually independent fair Bernoulli choices; the claim is about *unconditional* tournaments and conditional moments given the score of just one specified vertex, not about a tournament drawn uniformly subject to its entire score sequence. A cyclic triple has all three directed edges consistently oriented around a cycle, in either direction. All functions on the finite score domain are admissible. The conditional distribution of the complete cyclic-triple count is **not** claimed to be binomial or to factor independently into two pieces; only the stated first two moments and covariances are asserted.

## Proof

**1. Conditioning on a full star.** Fix a vertex \(v\) and reveal all \(N\) incident edge directions. Suppose \(v\) beats exactly \(k\) other vertices; write \(W\) for the set it beats and \(L\) for the set beating it, of sizes \(k\) and \(N-k\). A triangle through \(v\) is cyclic if and only if its other two vertices belong to different groups and the edge joining them points in the unique direction completing a cycle. Consequently the number \(B\) of cyclic triangles through \(v\), conditional on the full star, is a sum of \(k(N-k)\) independent fair edge indicators, with mean \(k(N-k)/2\) and variance \(k(N-k)/4\).

The \(\binom N3\) triangles avoiding \(v\) are unaffected by the star. Each has cyclicity probability \(1/4\) and variance \(3/16\). The indicators of any two distinct such triangles are pairwise independent: if the triangles share no edge this is immediate; if they share exactly one edge, conditioning on its direction leaves each triangle cyclic with probability \(1/4\), independently using its own remaining edges. Each avoiding-\(v\) triangle indicator is also independent of each individual through-\(v\) triangle indicator, conditional on the star. Indeed their only possible common edge is one edge inside \(W\times L\); conditional on the direction of that edge, the avoiding-\(v\) triangle is cyclic with probability \(1/4\) in both directions. This proves zero cross-covariance between the through- and avoiding-\(v\) sums. Therefore the star-conditional mean and variance are exactly the first displayed formulas. As they depend only on \(k\), conditioning further only on \(S_v=k\) leaves both formulas unchanged by the laws of total expectation and total variance.

**2. Exact regression.** A given triple is cyclic with probability \(1/4\), giving \(\mathbb E C=\binom n3/4\). From step 1 and \(\binom n3=\binom N3+\binom N2\),

\[
\mathbb E[C\mid S_v=k]-\mathbb E C
=\frac12 k(N-k)-\frac14\binom N2
=-\frac18\left((2k-N)^2-N\right).
\]

Here \(S_v\sim\operatorname{Bin}(N,1/2)\). Multiply by \(f(k)\), average over this binomial law, and sum the resulting \(n\) identical covariance contributions. This gives the displayed general covariance identity and its specialization to \(M_k\) by choosing \(f(j)=\mathbf 1_{\{j=k\}}\).

**3. Orthogonal projection.** Let \(K_j(k)=[z^j](1-z)^k(1+z)^{N-k}\), for \(0\le j\le N\). Directly \(K_2(k)=((N-2k)^2-N)/2\). For independent formal variables \(z,w\) and \(X\sim\operatorname{Bin}(N,1/2)\),

\[
\mathbb E[(1-z)^X(1+z)^{N-X}(1-w)^X(1+w)^{N-X}]=(1+zw)^N.
\]

Comparing coefficients yields \(\mathbb E[K_j(X)K_\ell(X)]=\mathbf1_{\{j=\ell\}}\binom Nj\), establishing orthogonality and completeness on the \(N+1\)-point support. Hence the covariance functional vanishes on every Krawtchouk mode other than degree two, establishing the precise rank-one statement.

**4. Signs and arithmetic zero cases.** The probability \(p_k\) is positive. The sign of \(\operatorname{Cov}(C,M_k)\) is the opposite of \((2k-N)^2-N\). Its zeros require an integer square \(N=t^2\); since \(n\ge3\), \(N\ge2\) forces \(t\ge2\). Conversely the two integers \(k=(t^2\pm t)/2\) lie in \([0,t^2]\) because \(t^2\pm t\) is even. The extremes \(k=0,N\) give the negative case because \(N^2>N\), while choosing \(k\) nearest \(N/2\) gives \((2k-N)^2\le1<N\), hence the positive case. This exhausts all cases.

## Verification

Run the bundled standard-library checker with `python3 verification/check.py`. It exhaustively enumerates all \(2^{\binom n2}\) edge-orientation patterns for each \(n=3,4,5,6\); for every possible score \(k\) it checks the claimed conditional mean, conditional variance, and frequency-count covariance using exact rational arithmetic. These finite checks are independent consistency evidence, not an infinite proof; the preceding arguments prove the theorem for all \(n\ge3\).

## Relationship to prior work

The statistic \(C\) is the classical count of *circular triads* underlying Kendall–Smith measures of intransitivity in paired-comparison data. The deterministic tournament identity \(C=\binom n3-\sum_v\binom{S_v}{2}\) is classical and **not** a novelty claim. The fair-independent-edge model is a special Bradley–Terry random tournament. Aldous and Kolesnik (2018) and Kolesnik and Sanchez (2020) analyze random-tournament score sequences; Bucić et al. (2019) analyze tournament quasirandomness via local counting; Chatterjee and Bhattacharya (2026) study the distribution and asymptotic fluctuations of circular-triad counts in inhomogeneous random tournaments. The specific fully conditional finite-sample variance, all-additive-score Krawtchouk projection, and square-order zero-covariance classification were not located in the compared material. This is a bounded priority assessment, not proof of historical uniqueness.

## Limitations

The conclusions rely on independent symmetric pair outcomes; they need not hold for heterogeneous Bradley–Terry parameters, correlated outcomes, or score-sequence-conditioned random tournaments. Pairwise independence of triangle indicators does not mean their joint independence. There is no assertion about the joint distribution of the \(M_k\), joint normality, or the entire conditional law of \(C\). Early literature on circular triads may implicitly cover portions of the formulas; in particular, full text of Kendall and Babington Smith (1940) was unavailable for a decisive priority check. The supplied finite enumeration does not replace the all-order proof, and an independent audit has not been performed.

## References

1. D. J. Aldous and B. Kolesnik, *To stay discovered: On tournament mean score sequences and the Bradley–Terry model*, arXiv:1811.06662v1, first posted 2018-11-16, https://arxiv.org/pdf/1811.06662v1.
2. B. Kolesnik and M. Sanchez, *The Geometry of Random Tournaments*, arXiv:2009.09322v1, https://arxiv.org/pdf/2009.09322v1.
3. M. Bucić, E. Long, A. Shapira, and B. Sudakov, *Tournament quasirandomness from local counting*, arXiv:1910.09936v1, https://arxiv.org/pdf/1910.09936v1.
4. S. Chatterjee and B. B. Bhattacharya, *Transitivity in Inhomogeneous Random Tournaments*, arXiv:2606.02340v1, https://arxiv.org/pdf/2606.02340v1.
5. M. G. Kendall and B. Babington Smith, *On the Method of Paired Comparisons*, Biometrika **31** (1940), 324–345, doi:10.1093/biomet/31.3-4.324 (historical priority risk: full text not inspected).
