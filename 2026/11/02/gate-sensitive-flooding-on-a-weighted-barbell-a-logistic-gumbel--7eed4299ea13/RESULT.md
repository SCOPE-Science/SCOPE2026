# Gate-sensitive flooding on a weighted barbell: a logistic–Gumbel limit

## Finding

Let \(\mathcal B_n\) be two disjoint complete graphs on \(n\ge2\) vertices joined by exactly one bridge between designated gate vertices. Every intra-clique edge has an independent exponential passage time of rate \(1/n\); the bridge has independent exponential passage time of fixed rate \(\beta>0\). From a source vertex, passage follows the minimum-total-weight path; its flooding time \(T_n\) is the maximum passage time to any vertex.

**Source away from the gate.** For any nongate source, as \(n\to\infty\),
\[
T_n-3\log n\ \xrightarrow{d}\ W_\beta:=G_0+L+E_\beta+G_1+G_2,
\]
where the \(G_i\) are independent standard Gumbel variables with distribution function \(\exp(-e^{-x})\), \(L=\log(U/(1-U))\) with \(U\sim\operatorname{Uniform}(0,1)\), and \(E_\beta\sim\operatorname{Exp}(\beta)\); all five variables are independent. For \(-1<s<\min\{1,\beta\}\),
\[
\mathbb E[e^{sW_\beta}]
=\frac{\beta}{\beta-s}\,\Gamma(1-s)^4\Gamma(1+s).
\]
In particular,
\[
\mathbb E T_n=3\log n+3\gamma+\beta^{-1}+o(1),\qquad
\operatorname{Var}(T_n)\longrightarrow\frac{5\pi^2}{6}+\beta^{-2},
\]
where \(\gamma\) is Euler's constant.

**Source at a gate.** For either gate source, independently sample four standard Gumbels \(G_1,G_2,G_3,G_4\) and \(E_\beta\). Then
\[
T_n-2\log n\ \xrightarrow{d}\
\max\{G_1+G_2,\ E_\beta+G_3+G_4\}.
\]
Consequently the leading expected flooding times are \(3\log n\) and \(2\log n\) respectively, and their ratio tends to \(3/2\). In particular, moving the source from an ordinary vertex to a gate saves \(\log n+O(1)\) expected time. This compares the two distinct source orbits of the barbell, not arbitrary changes to edge weights.

**Exact finite reduction.** Set \(q_{n,k}=k(n-k)/n\) for \(1\le k<n\). Let \(X_k\) be independent exponentials of rates \(q_{n,k}\), let \(J\) be independent uniform on \(\{2,\ldots,n\}\), and let \(F'_n\) be an independent copy of \(F_n=\sum_{k=1}^{n-1}X_k\). Define \(H_n=\sum_{k=1}^{J-1}X_k\). For a nongate root,
\[
T_n\ \overset d=\ \max\{F_n,\ H_n+E_\beta+F'_n\}.
\]
For a gate root, set \(H_n=0\) in this formula, keeping \(F_n,F'_n,E_\beta\) independent. The dependence between \(F_n\) and \(H_n\) in the nongate representation is essential.

## Assumptions and scope

All edges are undirected; edge weights are mutually independent, with the stated continuous exponential distributions. The graph consists of exactly two equal-size cliques and exactly one bridge. A flooding time is the maximum of shortest-path distances, equivalently the completion time of a permanent susceptible–infected process with independent exponential edge transmissions. The bridge rate \(\beta\) is a positive constant, independent of \(n\). The source is either a specified gate vertex or a specified nongate vertex. The theorem concerns \(n\to\infty\), with the exact finite representation valid for every integer \(n\ge2\).

## Proof

**1. Exact bridge decomposition.** In either clique, when \(k\) vertices have been reached, there are \(k(n-k)\) boundary edges of rate \(1/n\). Exponential memorylessness implies that the next discovery wait has rate \(q_{n,k}=k(n-k)/n\), independent of which vertex is next. Symmetry makes successive newly discovered labels a uniform permutation, independent of all waiting times. If the source is nongate, the designated gate therefore appears at a rank \(J\) uniform on \(\{2,\dots,n\}\), independent of \((X_k)\). The gate is reached at time \(H_n\), and its own clique is complete at \(F_n\). The bridge has one independent passage time \(E_\beta\), after which the other clique starts a fresh and independent complete-graph growth process with completion time \(F'_n\). Because every path between cliques uses the sole bridge, the exact displayed maximum follows. If the source is a gate, the left gate time is zero. These arguments also establish the finite Laplace transforms
\[
\mathbb E[e^{-zF_n}]=\prod_{k=1}^{n-1}\frac{q_{n,k}}{q_{n,k}+z},\qquad
\mathbb E[e^{-zH_n}]=\frac1{n-1}\sum_{j=2}^n\prod_{k=1}^{j-1}\frac{q_{n,k}}{q_{n,k}+z},\quad z\ge0.
\]

**2. Two independent Gumbels in a clique flood.** Write \(X_k=Y_k(1/k+1/(n-k))\), for independent unit-exponential \(Y_k\), using \(1/q_{n,k}=1/k+1/(n-k)\). The sum \(\sum_{k=1}^{n-1}Y_k/k-\log n\) converges to a standard Gumbel (indeed its uncentered sum has the law of the maximum of \(n-1\) independent unit exponentials). The reversed sum \(\sum_{k=1}^{n-1}Y_k/(n-k)-\log n\) does likewise. Their limiting Gumbels are independent: truncate the centered random fluctuations to \(k\le K\) and \(n-k\le K\), whose underlying exponential variables are disjoint for \(n>2K\); the centered omitted fluctuations have variance bounded by \(2\sum_{k>K}k^{-2}\), uniformly in \(n\), and their deterministic means converge to the required logarithmic centering. Letting \(K\to\infty\) yields
\[
F_n-2\log n\xrightarrow{d}G_1+G_2.
\]
Also \(\mathbb E F_n=2H_{n-1}^{(1)}\), where \(H_m^{(1)}=\sum_{k=1}^m1/k\), and
\(\operatorname{Var}(F_n)=2H_{n-1}^{(2)}+4H_{n-1}^{(1)}/n\), establishing uniformly bounded centered moments.

**3. Hitting a prescribed nongate-source gate.** The independent rank \(J\) satisfies \(J/n\Rightarrow U\), uniform on \((0,1)\). For ranks \(J/n\in[\varepsilon,1-\varepsilon]\), the first part of \(H_n\) obeys
\[
\sum_{k=1}^{J-1}\frac{Y_k}{k}-\log J\xrightarrow{d}G_0,
\]
where the limiting \(G_0\) is independent of \(U\), while the second part concentrates about
\[
\sum_{k=1}^{J-1}\frac1{n-k}
=\log\frac{n}{n-J}+o(1).
\]
The variance of this second part is bounded by \(n/(\varepsilon n)^2=O_\varepsilon(n^{-1})\). The independent rank can be restricted to the displayed compact fraction interval at probability cost at most \(2\varepsilon+o(1)\). Letting \(\varepsilon\downarrow0\) proves
\[
H_n-\log n\xrightarrow{d}G_0+\log\frac{U}{1-U}.
\]
The limit is a convolution of an independent standard Gumbel and standard logistic law. The exact mean is
\[
\mathbb E H_n
=\sum_{k=1}^{n-1}\Pr(J>k)\,q_{n,k}^{-1}
=\frac{n}{n-1}H_{n-1}^{(1)}.
\]

**4. The nongate flood is asymptotically governed by the second clique.** With \(S_n=H_n+E_\beta+F'_n\), steps 2–3 show \(S_n-3\log n\) converges to the stated sum, while \(F_n-2\log n\) is tight. Hence \(F_n-S_n=-\log n+O_{\mathbb P}(1)\), and the correction \((F_n-S_n)_+\) vanishes in probability. For moment convergence, the displayed finite Laplace products and a rank-mixture estimate give uniformly bounded exponential moments of \(H_n-\log n\) for exponents in a sufficiently small interval about zero; likewise for \(F_n-2\log n\) and \(F'_n-2\log n\). More explicitly, for \( |s|<1/4\), the logarithm of the conditional exponential moment of \(H_n\) differs from \(s\sum_{k<J}q_{n,k}^{-1}\) by at most \(C_s\sum_{k=1}^{n-1}q_{n,k}^{-2}\le C_s'\). The centered conditional bound is consequently \(C_s (J/n)^s((n-J+1)/n)^{-s}\), whose uniform-rank average is bounded for \( |s|<1\). The same product bound applies to the centered full-clique flood. The independent exponential bridge delay has finite exponential moments below \(\beta\). Hölder's inequality thus makes the centered difference \(F_n-S_n+\log n\) uniformly bounded in every fixed polynomial moment, and the positive correction vanishes in \(L^2\). Therefore the distribution, mean and variance of \(T_n-3\log n\) converge to those of \(W_\beta\). Standard Gumbel and logistic moment generating functions are \(\Gamma(1-s)\) and \(\Gamma(1-s)\Gamma(1+s)\); independence yields the displayed transform. Differentiating its logarithm at zero gives mean \(3\gamma+\beta^{-1}\) and variance \(5\pi^2/6+\beta^{-2}\).

**5. The gate-root limit.** If the source is a gate, exact bridge decomposition gives independent \(F_n,F'_n\) and \(E_\beta\). Applying step 2 twice and the continuous mapping theorem yields the stated centered maximum. Uniform exponential-moment bounds ensure convergence of expectations, so its leading expectation is \(2\log n+O(1)\). Compared with the nongate expectation, the difference is \(\log n+O(1)\) and their ratio tends to \(3/2\).

## Verification

The companion standard-library program `checker.py` computes the exact mean flooding time in two independently coded ways: a continuous-time infected-count Markov recursion distinguishing the bridge endpoint, and an independent uniform-infection-rank recursion conditioned on the gate's rank. These agree as rational numbers for all \(2\le n\le8\) at four rational bridge rates. It also checks the gate-root specialization, nonnegative exact-maximum corrections, and convergence of the explicitly derived centered Laplace/moment products for \(n\in\{100,1000,10000\}\) at two transform arguments. The program emits `CHECKS_PASS 96` using Python's standard library. The infinite-size conclusions are proved analytically above; finite computations are not treated as an infinite proof.

## Relationship to prior work

Van der Hofstad, Hooghiemstra and Van Mieghem give the known complete-graph exponential flooding birth-process transform and the two-Gumbel limit, which is explicitly used as an ingredient here. Leskelä and Ngo (first public preprint 2018) study first-passage flooding in sparse random graphs with boundary delays; Mountford and Saliba (first public preprint 2019) investigate flooding and diameter in configuration-model random graphs with general edge-weight tails. The latter's primary classification is MSC2020 \(60C05\), matching the probabilistic graph-flooding focus of this result. Their random sparse graph hypotheses do not include a deterministic growing-degree two-clique barbell with a single separating edge, and their results do not yield the displayed gate-versus-nongate fluctuation laws. The new assertion is the complete source-sensitive barbell law and its explicit logistic–Gumbel structure; neither classical clique flooding nor the generic Markov decomposition is presented as new.

## Limitations

The theorem requires two equal-size cliques, one bridge, intra-clique exponential passage rates \(1/n\), a fixed positive bridge rate and permanent transmissions. It does not cover growing numbers of bridges, nonexponential edges, unequal communities or arbitrary graph families. Its originality is not an independently certified historical priority statement.

## References

1. T. Mountford and J. Saliba, *Flooding and Diameter in General Weighted Random Graphs*, arXiv:1909.04563v1, publicly posted 2019-09-10, https://arxiv.org/abs/1909.04563 .
2. L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, arXiv:1806.09568v1, publicly posted 2018-06-25, https://arxiv.org/abs/1806.09568 .
3. R. van der Hofstad, G. Hooghiemstra and P. Van Mieghem, *The flooding time in random graphs*, preprint dated 2001-12-19, subsequently *Extremes* 5 (2002), 111–129, https://www.nas.ewi.tudelft.nl/people/Piet/papers/flooding.pdf .
4. J. Duda and T. G. Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks*, arXiv:2408.08244v1, publicly posted 2024-08-15, https://arxiv.org/abs/2408.08244 . This paper treats a different quantum-walk observable on the same graph family.
