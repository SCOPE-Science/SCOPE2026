# The worst complete multipartite graph for edge-gradient fitting at fixed vertex and part counts

## Finding

Fix integers \(N\ge 2\) and \(2\le r\le N\). Among unweighted complete multipartite graphs with \(N\) vertices and exactly \(r\) nonempty parts, the unique part-size multiset maximizing the coordinatewise maximum-norm amplification of the Euclidean edge-gradient projection is
\[
\{a,b,\underbrace{1,\ldots,1}_{r-2}\},\qquad
a=\left\lfloor\frac{N-r+2}{2}\right\rfloor,\quad
b=\left\lceil\frac{N-r+2}{2}\right\rceil.
\]
The optimized value is
\[
\mathcal M_{N,r}=2+\frac{N-r+2}{N}
-\frac{2(N-1)}{N}\left(\frac1{N-a}+\frac1{N-b}\right)
=3-\frac{r+6}{N}+O_r(N^{-2})
\]
as \(N\to\infty\) at fixed \(r\). The exact formula holds also at the smallest admissible orders. Uniqueness is a statement about the graph up to part permutation, not the choice of the output edge realizing its norm.

## Assumptions and scope

Each edge has unit weight, and all part sizes are positive integers. With any orientation, use the real vertex-by-edge incidence matrix \(B\) and combinatorial Laplacian \(L=BB^\mathsf T\). The fitted edge flow is \(Pj=B^\mathsf T L^\dagger Bj\), with \(L^\dagger\) the Moore–Penrose inverse, and the amplification is \(\|P\|_{\infty\to\infty}\) for the unweighted maximum of the absolute edge coordinates. Changing orientation does not affect this norm. Both graph counts \(N,r\) are prescribed; there is no optimization over other linear projections or over edge conductances.

## Proof

The preceding complete-multipartite endpoint result [1, Finding and Proof §§1–4] gives the exact absolute row sum for an edge joining parts of sizes \(u,v\):
\[
2+f_N(u)+f_N(v),\qquad
f_N(s)=\frac{s}{N}-\frac{2(N-1)}{N(N-s)}.
\]
The reference gives absolute column sums for its cut projector, which is this same symmetric matrix. The induced maximum norm is the largest such row sum. Since every pair of distinct parts has edges between them, it suffices to optimize the score over all feasible pairs, accounting for which graphs can attain the optimal pair.

Put \(t=u+v\). Necessarily \(2\le t\le T=N-r+2\). At each fixed \(t\), the strictly concave function \(f_N\) has \(f_N''(s)=-4(N-1)/[N(N-s)^3]<0\). Thus the maximum pair score at sum \(t\) occurs only at the most balanced integer split up to order: if the larger entry exceeds the smaller by at least two, transferring one unit from the larger to the smaller increases the score strictly. Call this balanced score \(g_N(t)=f_N(\lfloor t/2\rfloor)+f_N(\lceil t/2\rceil)\).

For \(r=2\), the sum is forced to equal \(N\). For \(r\ge3\) and \(N\ge5\), the allowed successive increments \(g_N(t+1)-g_N(t)\), with \(t<T\), equal \(f_N(k+1)-f_N(k)\), where \(k=\lfloor t/2\rfloor\le (N-2)/2\). Their signs are the signs of
\[
(N-k)(N-k-1)-2(N-1)
\;\ge\;\frac{N(N+2)}4-2(N-1)=\frac{(N-2)(N-4)}4>0.
\]
Hence an optimal pair must use the full feasible sum \(T\), leaving \(r-2\) singleton parts. Conversely, the balanced pair of sum \(T\) and those singleton parts form an admissible graph and attain the bound. For \(r\ge3, N\le4\), each allowed \((N,r)\) has only one multiset, which agrees with the stated one. This proves uniqueness and the exact expression by substitution. Finally \(a,b=N/2+O_r(1)\), so the sum of reciprocals in the formula is \(4/N+O_r(N^{-2})\), giving the displayed expansion.

## Reproducibility and relationship to prior work

The finite-graph calculation [1] supplies the per-edge scores, both complementary norms, and a comparison of their norming edge orbits. Those are prior results, not asserted here as new. The extremal question here instead fixes the number of parts and asks which graph realizes the worst amplification among the possible part-size multisets. The optimization in the proof is discrete and includes uniqueness and all boundary orders. As a supplementary finite check, enumerate integer partitions of each \(N\le30\) into \(2\le r\le N\) positive parts, score each pair using the rational formula above, and compare the maximizing multisets. This was checked for all 435 such \((N,r)\) cases; finite enumeration is not the proof. A later companion [2] optimizes over all part counts at fixed vertex count; that does not classify the extremizers at an arbitrary prescribed part count.

## Limitations

The extremum is for canonical orthogonal gradient fitting on the indicated unweighted graph class, not the projection constant minimized over all projections. The result does not assert uniqueness of a norming edge, or guarantee historical priority beyond the sources compared.

## References

1. *Exact endpoint Hodge norms and an edge-orbit reversal for complete multipartite graphs*, Resultary, 18 October 2026, record `745e7b0c399e`, [Finding and proof](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-endpoint-hodge-norms-and-an-edge-orbit-reversal-for-comple--745e7b0c399e).
2. *Sharp endpoint norms of complete multipartite electrical gradient projections*, Resultary, 17 November 2026, record `0f6b407e194c`, [Finding and proof](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-sharp-endpoint-norms-of-complete-multipartite-electrical-gradien--0f6b407e194c).
