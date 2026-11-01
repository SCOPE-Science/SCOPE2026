# A generalized-roundness cliff and critical Hilbert-rank transition across three folded hypercubes

## Finding

Let \(F_n\) be the folded \(n\)-cube: the graph obtained from the \((n-1)\)-dimensional Boolean cube by adding the antipodal perfect matching, endowed with its unit-edge shortest-path metric \(d_n\). Let \(\wp_n\) denote its supremal \(p\)-negative-type exponent (equivalently, generalized roundness).

For \(n=6,7,8\), the exact exponents are characterized by the **unique positive roots** of the following equations:

\[
\begin{aligned}
F_6:\quad &2\,3^p-2^p-2=0, &\wp_6&\approx0.4821471851820996,\\
F_7:\quad &3\,3^p-3\,2^p-1=0, &\wp_7&\approx0.5165843743005904,\\
F_8:\quad &35\,4^p-56\,3^p+28\,2^p-8=0, &\wp_8&\approx0.1353727235567274.
\end{aligned}
\]

In particular, the exact ordering includes
\[
0<\wp_6<\tfrac12<\wp_7<1,\qquad 0<\wp_8<\tfrac14<\wp_6.
\]
Thus increasing from 64 to 128 vertices, and from diameter three to four, produces a sharp decrease in generalized roundness, reversing the preceding increase from 32 to 64 vertices.

For each of these three graphs, \((F_n,d_n)\) has **strict** \(p\)-negative type for \(0\le p<\wp_n\), has non-strict \(p\)-negative type at \(p=\wp_n\), and fails \(p\)-negative type for every \(p>\wp_n\). The nullities of the critical powered-distance quadratic forms on the real zero-sum subspaces are exactly \(15,35,1\), respectively. Accordingly, the least Euclidean dimensions of isometric embeddings of the endpoint snowflakes \((F_n,d_n^{\wp_n/2})\) are exactly \(16,28,126\). Below the respective endpoints these least dimensions are \(31,63,127\).

The critical equality spaces have a character-theoretic classification: for \(F_6\) and \(F_7\), they are the spans of Walsh characters of weights three and four on \(\mathbb F_2^5\) and \(\mathbb F_2^6\), respectively; for \(F_8\) the only critical equality direction is the parity character on \(\mathbb F_2^7\).

## Assumptions and scope

All graphs are finite, simple, unweighted and considered only with **vertex** shortest-path distances. The folded \(n\)-cube is defined unambiguously as
\[
F_n=\operatorname{Cay}\!\left(\mathbb F_2^{n-1},\{e_1,\ldots,e_{n-1},\mathbf1\}\right),\qquad n\in\{6,7,8\},
\]
where \(\mathbf1\) is the all-ones vector. This agrees with antipodal identification in the usual \(n\)-cube. Put \(d=n-1\) and \(h(x,y)=|x-y|\), the Hamming distance. Then
\[
d_n(x,y)=\min\{h(x,y),d+1-h(x,y)\}.
\]
For \(p>0\) the powered distance matrix \(D_p\) has entries \(d_n(x,y)^p\) and zero diagonal. At \(p=0\) its diagonal remains zero and all off-diagonal entries are one. The real zero-sum condition is \(\sum_x a_x=0\); \(p\)-negative type means \(\sum_{x,y}a_xa_y d_n(x,y)^p\le0\) for every such coefficient vector. The least Euclidean embedding dimension refers to an exact isometric embedding of distances \(d_n(x,y)^{p/2}\), not a distortion estimate.

## Proof

**1. Exact path metric.** The generating set consists of single-coordinate flips and the all-coordinate flip. Any word in these commuting involutions uses the all-coordinate flip either an even or an odd number of times, modulo cancellation. In the first case at least \(h(x,y)\) coordinate flips are necessary; in the second case at least \(d-h(x,y)\) coordinate flips plus one all-coordinate flip are necessary. Both bounds are realized, proving the metric formula.

**2. Complete distance-power spectrum.** The Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), indexed by \(S\subseteq\{1,\ldots,d\}\), diagonalize every translation-invariant distance-power matrix. The character of weight \(k=|S|\) has eigenvalue
\[
\lambda_{d,k}(p)=\sum_{j=1}^{d}\min(j,d+1-j)^p
\sum_{i=\max(0,j-d+k)}^{\min(j,k)}(-1)^i\binom{k}{i}\binom{d-k}{j-i}.
\]
It occurs with multiplicity \(\binom dk\). The trivial character has a strictly positive row-sum eigenvalue. To abbreviate the nontrivial eigenvalues set \(X=2^p\) and \(Y=3^p\), so \(4^p=X^2\). Direct binomial expansion yields the complete table:

| Graph | Walsh weights \(k\) | Nontrivial eigenvalue |
|---|---|---|
| \(F_6\) | \(1,2\) | \(2-X-2Y\) |
| \(F_6\) | \(3,4\) | \(-2-X+2Y\) |
| \(F_6\) | \(5\) | \(-6+15X-10Y\) |
| \(F_7\) | \(1,2\) | \(3+X-5Y\) |
| \(F_7\) | \(3,4\) | \(-1-3X+3Y\) |
| \(F_7\) | \(5,6\) | \(-5+9X-5Y\) |
| \(F_8\) | \(1,2\) | \(4+4X-4Y-5X^2\) |
| \(F_8\) | \(3,4\) | \(3X^2-4X\) |
| \(F_8\) | \(5,6\) | \(-4+4X+4Y-5X^2\) |
| \(F_8\) | \(7\) | \(-8+28X-56Y+35X^2\) |

No eigenvalues are omitted: these weight classes partition all \(2^d-1\) nonconstant Walsh characters.

**3. Exact sign competition.** Throughout \(p\ge0\), \(1\le X\le Y\le X^2\), and \(Y\ge X^{3/2}\) because \(3^2>2^3\).

For \(F_6\), the weight-one/two eigenvalue is negative. With \(t=\sqrt X\ge1\), the weight-five eigenvalue satisfies
\[
-6+15X-10Y\le-6+15t^2-10t^3\le-1,
\]
since the polynomial on the right is nonincreasing for \(t\ge1\). Thus the unique possible obstruction is \(g_6(p)=-2-2^p+2\,3^p\). It satisfies \(g_6(0)=-1\), \(g_6(1)=2\), and \(g_6'(p)>0\) for \(p\ge0\). Also \(g_6(1/2)>0\), because \(2\sqrt3>2+\sqrt2\), which follows on squaring from \(9>8\). Hence its unique zero obeys \(0<\wp_6<1/2\).

For \(F_7\), the weight-one/two eigenvalue is at most \(3-4X<0\). The weight-five/six eigenvalue satisfies
\[
-5+9X-5Y\le-5+9t^2-5t^3\le-\frac{17}{25},
\]
where the last polynomial has its maximum at \(t=6/5\). Thus only \(g_7(p)=-1-3\,2^p+3\,3^p\) can vanish first. It is strictly increasing, with \(g_7(0)=-1\) and \(g_7(1)=2\). Furthermore \(g_7(1/2)<0\), since \(3\sqrt3<1+3\sqrt2\), equivalent after squaring to \(16<18\). Therefore \(1/2<\wp_7<1\).

For \(F_8\), the weight-one/two eigenvalue is at most \(4-5X^2<0\). The weight-five/six eigenvalue is at most \(-4+4X-X^2=-(X-2)^2\), and is strictly negative for \(0\le p\le1/4\). The weight-three/four eigenvalue \(X(3X-4)\) is strictly negative throughout this interval because \(2^{1/4}<4/3\). Finally put
\[
g_8(p)=-8+28\,2^p-56\,3^p+35\,4^p.
\]
Here \(g_8(0)=-1\), and
\[
g_8'(p)=28(\log2)X-56(\log3)Y+70(\log4)X^2
\ge 28(\log2)X+(140\log2-56\log3)X^2>0,
\]
because \(Y\le X^2\) and \(2^{5/2}>3\). At \(p=1/4\), the certified rational bounds
\[
2^{1/4}>1189/1000,\quad 3^{1/4}<1317/1000,\quad 4^{1/4}>1414/1000
\]
follow by raising the rational endpoints to the fourth power, and give \(g_8(1/4)>103/100>0\). Consequently there is exactly one zero \(\wp_8\in(0,1/4)\), and every other nonconstant eigenvalue remains strictly negative up to this zero. Once the corresponding \(g_n\) becomes positive it remains positive, proving failure of \(p\)-negative type at **every** larger exponent, not only at the next sampled exponent.

**4. Equality directions and minimal dimensions.** The Walsh basis is orthogonal on the real zero-sum subspace. The strict signs established above show that below \(\wp_n\) its powered-distance form is negative definite. At the endpoint, exactly weights \(3,4\) vanish for \(F_6\) and \(F_7\), while exactly weight \(7\) vanishes for \(F_8\). Their multiplicities are \(\binom53+\binom54=15\), \(\binom63+\binom64=35\), and \(\binom77=1\). These character spans are precisely all equality directions. Schoenberg's centered Gram matrix \(-\frac12 JD_pJ\), with \(J=I-\frac1N\mathbf1\mathbf1^\mathsf T\), is positive semidefinite exactly in the negative-type range and has rank \(N-1\) minus the stated nullity. Its Gram realization and the rank lower bound give the claimed least isometric Euclidean embedding dimensions. This also proves the asserted exact equality/non-equality boundary.

## Verification

Run `python3 verification/check.py` in the directory containing this file. The standalone checker builds the Cayley adjacency lists, computes all-pairs shortest paths independently for 32, 64 and 128 vertices, checks the distance formula for every ordered vertex pair, and calculates all 18 distinct nontrivial weight classes by **two independent exact integer methods** (direct Walsh signed sums and binomial Krawtchouk expansion). It checks the precise endpoint nullities and embedding dimensions, the fourth-power rational inequalities used to locate the \(F_8\) root, and the rational stationary-polynomial bound for \(F_7\). Floating-point bisection is used only to display approximate roots. The all-real-exponent sign arguments and uniqueness are the analytic proof above, not deductions from the finite test output.

## Relationship to prior work

Sánchez (arXiv:1108.0451, first public version 2011-08-02) gives a general powered-distance-matrix criterion for supremal negative type and explicit complete-bipartite examples. Murugan (arXiv:1112.5657, first public version 2011-12-23) proves a determinant characterization for vertex-transitive metrics and analyzes Hamming-cube **subspaces with unchanged Hamming distance**. Those general criteria and the Walsh method motivate the present analysis, but neither inspected account determines the three **antipodally modified graph metrics**, their competing weight classes, or the critical ranks. Standard folded-cube references establish the graph construction but not the present quantitative snowflake profile. In particular, a quotient/antipodal-shortcut metric is not an ordinary metric subspace of the Hamming cube. Previous exact negative-type calculations for crown, wheel, split and clique-bouquet metrics involve different distance kernels and do not imply these results.

## Limitations

The explicit generalized-roundness and equality classifications are proved only for the folded \(6\)-, \(7\)- and \(8\)-cubes. No universal law in higher folded-cube dimensions, no metric-graph continuum version, and no assertion about a different edge-length normalization is made. Decimals are explanatory approximations; the exact definitions are the unique root conditions and inequalities. This is a proof and reproducibility package, not independent scientific validation.

## References

- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first public version 2011-08-02), https://arxiv.org/abs/1108.0451.
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first public version 2011-12-23), https://arxiv.org/abs/1112.5657.
- *Folded Cube Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/FoldedCubeGraph.html (graph definition and standard nomenclature).
