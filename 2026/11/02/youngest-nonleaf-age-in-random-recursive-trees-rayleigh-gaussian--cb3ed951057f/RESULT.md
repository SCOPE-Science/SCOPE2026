# Youngest nonleaf age in random recursive trees: Rayleigh–Gaussian separation and residual covariance

## Finding

For a uniformly random recursive tree on labels \(1,\ldots,n\), with \(n\ge3\), let \(L_n\) count leaves (vertices with no children), let \(M_n\) be the largest label of a vertex having at least one child, and let \(H_n=n-M_n\). Thus \(H_n\) measures the final run of leaves in **birth-label order**, not the height or depth of the tree. For \(1\le m\le n-1\), put \(a=n-m\). Then

\[
\Pr(H_n\ge m)=p_{n,m}:=\frac{a^m(a-1)!}{(n-1)!},
\qquad
\mathbb E[L_n\mid H_n\ge m]
=m+\frac a2\left(1-\frac1a\right)^m.
\]

Here and below the displayed conditional expectation is valid also for \(a=1\): the old root is certain to receive a child. In particular,

\[
\operatorname{Cov}(H_n,L_n)=
\frac12\sum_{m=1}^{n-1}p_{n,m}
\left[m-a\left\{1-\left(1-\frac1a\right)^m\right\}\right]>0.
\]

The summand vanishes for \(m=1\) and is strictly positive for \(m\ge2\). Moreover, writing \(R\) for a Rayleigh random variable with survival function \(\Pr(R>x)=e^{-x^2/2}\), and \(Z\) for a standard normal variable independent of \(R\),

\[
\left(\frac{H_n}{\sqrt n},\frac{L_n-n/2}{\sqrt{n/12}}\right)
\xrightarrow{d}(R,Z),
\qquad
\lim_{n\to\infty}\frac{\operatorname{Cov}(H_n,L_n)}{\sqrt n}
=\frac14\sqrt{\frac\pi2}.
\]

Thus the statistics separate on their principal fluctuation scales even though their unnormalized covariance grows at order \(\sqrt n\). For every fixed \(x\ge0\), with \(m_n=\lceil x\sqrt n\rceil\) (interpreting \(m_n=1\) when \(x=0\)), their lower-order conditional response satisfies

\[
\mathbb E[L_n\mid H_n\ge m_n]-\frac n2\longrightarrow\frac{x^2}{4}.
\]

## Assumptions and scope

A uniformly random recursive tree means a rooted labeled increasing tree on \(\{1,\ldots,n\}\), where vertex \(1\) is the root and each \(k\ge2\) independently selects a parent uniformly from \(\{1,\ldots,k-1\}\). Leaves are defined by **outdegree zero**; the root is not counted as a leaf for \(n\ge2\). Every result refers to this unweighted model, not to Cayley-uniform trees, preferential-attachment trees, or trees conditioned on degrees. There are exactly \((n-1)!\) equally likely trees. The exact identities hold for every integer \(n\ge3\), and every admissible integer \(m\).

## Proof

**1. Tail law.** Write \(P_k\) for the parent of vertex \(k\). The event \(H_n\ge m\) is precisely the event that none of the last \(m\) vertices ever receives a child. This is equivalent to \(P_k\le a=n-m\) for each \(a+1\le k\le n\). Independence of the parent choices gives

\[
\Pr(H_n\ge m)=\prod_{k=a+1}^n\frac{a}{k-1}
=\frac{a^m(a-1)!}{(n-1)!}.
\]

Conditioned on this event, the last \(m\) parent choices are independent and uniform on the first \(a\) labels; they are independent of the recursive tree induced on the first \(a\) vertices.

**2. Conditional regression.** The last \(m\) vertices are leaves on the event in question. An earlier leaf survives as a leaf precisely if none of the \(m\) new vertices selects it, an event of probability \((1-1/a)^m\). For \(a\ge2\), the elementary recursive-tree leaf recurrence gives \(\mathbb E L_a=a/2\). For \(a=1\), the unique old root is hit with probability one, so the same displayed formula holds with the zero factor. Consequently

\[
\mathbb E[L_n\mid H_n\ge m]
=m+\frac a2(1-1/a)^m.
\]

The usual recursion \(L_k=L_{k-1}+1-\mathbf1_{\{P_k\text{ is a leaf at time }k-1\}}\) gives \(\mathbb E L_n=n/2\) for all \(n\ge2\). Hence the excess mean is

\[
\Delta_{n,m}=\frac{m-a\{1-(1-1/a)^m\}}2.
\]

Bernoulli's strict inequality \(1-(1-u)^m<mu\), for \(0<u<1\) and \(m\ge2\), implies \(\Delta_{n,m}>0\) for \(a\ge2,m\ge2\); the \(a=1\) case gives \((m-1)/2>0\). For \(m=1\), \(\Delta_{n,1}=0\). As \(H_n=\sum_{m=1}^{n-1}\mathbf1_{\{H_n\ge m\}}\), linearity proves the exact strictly positive covariance formula.

**3. Rayleigh tail limit.** For \(m=\lceil x\sqrt n\rceil\), with fixed \(x>0\), expand the product from step 1:

\[
\log p_{n,m}=
\sum_{j=0}^{m-1}\log\left(1-\frac{j}{n-m+j}\right)
=-\frac{m(m-1)}{2n}+O\left(\frac{m^3}{n^2}\right)
\longrightarrow-\frac{x^2}{2}.
\]

The exact product is \(\prod_{j=0}^{m-1}(1+j/a)^{-1}\), which yields the same expansion and may be used in place of the displayed logarithmic form above. The limit is the Rayleigh survival law, including the boundary \(x=0\) by positivity of \(H_n\).

**4. Gaussian leaf law and joint independence.** The distributional recursion for the leaf count has Eulerian-number coefficients: \(L_n-1\) has the distribution of the number of descents in a uniform permutation on \(n-1\) positions. To see this directly, if the current leaf count is \(\ell\), the next step leaves it unchanged with probability \(\ell/n\) and increases it by one with probability \(1-\ell/n\), precisely the Eulerian-number recursion. The descent-indicator sequence is bounded and 1-dependent with mean \(1/2\), nearest-neighbor covariance \(-1/12\), and variance \(n/12\) for \(L_n\). Dividing it into long blocks separated by one discarded indicator proves the standard central limit theorem, hence

\[
\frac{L_n-n/2}{\sqrt{n/12}}\xrightarrow{d}N(0,1).
\]

Fix \(x>0\) and let \(m=\lceil x\sqrt n\rceil\), \(a=n-m\). The event \(\{H_n\ge m\}\) depends solely on the parent choices after time \(a\), so it is independent of \(L_a\). By the leaf-count martingale decomposition, for \(m=O(\sqrt n)\),

\[
L_n-L_a-\frac m2=o_{\Pr}(\sqrt n).
\]

For clarity, each martingale difference has absolute value at most one, so the martingale part has variance at most \(m\). The predictable part is a sum of \(m\) terms \(1/2-L_{k-1}/(k-1)\). Since \(\operatorname{Var}(L_a)=a/12\), and each subsequent leaf increment is between zero and one, this sum is \(O_{\Pr}(m(\sqrt n+m)/a)=O_{\Pr}(1)\). Therefore the normalized leaf counts at times \(a\) and \(n\) differ by \(o_{\Pr}(1)\), uniformly on the event under consideration. Independently testing the tail event against each bounded continuous function of the normalized leaf count shows asymptotic factorization for every \(x>0\). These survival rectangles determine the joint weak limit, proving independence of \(R\) and \(Z\).

**5. Mixed covariance at the smaller scale.** When \(m=\lfloor x\sqrt n\rfloor\) for fixed positive \(x\), Taylor expansion gives

\[
\Delta_{n,m}=\frac{m(m-1)}{4(n-m)}+O\left(\frac{m^3}{(n-m)^2}\right)
\longrightarrow\frac{x^2}{4}.
\]

For \(m\le n/2\), the inequalities
\(0\le\Delta_{n,m}\le m(m-1)/(4(n-m))\) follow by the second-order binomial estimate. The tail probability obeys \(p_{n,m}\le\exp\{-m(m-1)/(2(n-1))\}\). For \(m>n/2\), \(\Delta_{n,m}\le m/2\), and this tail bound makes the summed contribution exponentially negligible. Therefore dominated Riemann-sum convergence applies to the exact covariance formula and gives

\[
\frac{\operatorname{Cov}(H_n,L_n)}{\sqrt n}
\longrightarrow\frac14\int_0^\infty x^2e^{-x^2/2}\,dx
=\frac14\sqrt{\frac\pi2}.
\]

The fixed-\(x\) conditional-response limit follows from the same expansion.

## Verification

Run the included deterministic standard-library script with `python3 verify.py`. It exhaustively enumerates all \((n-1)!\) uniform recursive trees for every \(3\le n\le9\), checking the exact tail law, conditional regression, strict covariance, Eulerian mean and variance, and the tail-sum formula. It also checks the asymptotic covariance constant numerically at three larger sizes. The included execution passed 178 exact or numerical assertions. Enumeration is an independent finite check, not the proof of the infinite statements.

## Relationship to prior work

The marginal Gaussian leaf law and the degree-count distribution of recursive trees are classical; in particular, Janson's 2004 first-public version (2005 journal issue) treats asymptotic degree counts and their evolution. Najock and Heyde (1982) analyze terminal-vertex counts, and Holmgren and Janson (2014) develop general fringe-tree limit theorems. The present result concerns an **age-indexed extremal statistic**, the last label with a child, and its exact conditional regression on the global leaf count. Those marginal theorems alone do not give the explicit tail, mixed covariance or joint independent Rayleigh–Gaussian limit. Eslava's accessible 2022 full work is about the *depths of high-degree vertices*, not the latest nonleaf in birth order. More general results could conceivably imply the joint statement; no unconditional historical priority claim is made.

## Limitations

The formulas require independent uniform parent choices, no degree conditioning, and \(n\ge3\). The Rayleigh and Gaussian variables are asymptotically independent only after the indicated normalizations; for each finite \(n\ge3\), the covariance is positive. Exact asymptotic correlation rates, other attachment rules, and multiple age-extreme statistics are not established here. Some older relevant sources were only accessible as abstracts, so equivalent earlier formulations cannot be excluded solely from title or search-result evidence.

## References

1. Svante Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* 26 (2005), 69–83; first online 2004-11-16. DOI: https://doi.org/10.1002/rsa.20046.
2. Dieter Najock and C. C. Heyde, “On the number of terminal vertices in certain random trees with an application to stemma construction in philology,” *Journal of Applied Probability* 19 (1982), 675–680. DOI: https://doi.org/10.2307/3213526.
3. Cecilia Holmgren and Svante Janson, “Limit Laws for Functions of Fringe Trees for Binary Search Trees and Random Recursive Trees,” first posted 2014-06-26. https://arxiv.org/abs/1406.6883.
4. Laura Eslava, “Depth of vertices with high degree in random recursive trees,” *ALEA* 19 (2022). DOI: https://doi.org/10.30757/ALEA.v19-33.
5. Bas Lodewijks, “On joint properties of vertices with a given degree or label in the random recursive tree,” first posted 2022-04. https://arxiv.org/abs/2204.09032.
