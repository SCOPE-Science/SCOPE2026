# Transmission zero forcing of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge 2\), partite sets \(V_1,\ldots,V_r\), part sizes \(n_i=|V_i|\), and total order \(N=\sum_i n_i\). Fix transmission proportion and threshold \(0<\alpha,\beta\le 1\), in the convention of Berliner et al.: an initially filled vertex has weight \(1\); a filled vertex that has exactly one unfilled neighbor may transmit once, sending \(\alpha\) times its current weight to that neighbor; a vertex is filled once its accumulated weight is at least \(\beta\).

If every part is a singleton, then \(G=K_N\) and
\[
Z_{\alpha,\beta}(G)=
\begin{cases}
N-1,&\beta\le (N-1)\alpha,\\
N,&\beta>(N-1)\alpha.
\end{cases}
\]

Assume now that at least one part has size at least \(2\). Define
\[
\Delta=N-\min_i n_i,
\qquad
\tau_\alpha(s)=\min\!\left\{(s-1)\alpha,\,(N-s-1)\alpha+(s-1)\alpha^2\right\},
\]
and
\[
T_\alpha(G)=\max_{i:n_i\ge2}\tau_\alpha(n_i).
\]
Then
\[
Z_{\alpha,\beta}(G)=
\begin{cases}
N-2,&\beta\le T_\alpha(G),\\
N-1,&T_\alpha(G)<\beta\le\Delta\alpha,\\
N,&\beta>\Delta\alpha.
\end{cases}
\]
This specializes exactly to the published formulas for complete graphs, stars, and complete bipartite graphs.

## Assumptions and scope
Graphs are finite, simple, and undirected. The statement uses the synchronous transmission-zero-forcing rule of Berliner et al., with each filled vertex permitted to transmit at most once. The result covers arbitrary complete multipartite part sizes, including singleton parts. The complete-graph case is separated because no part has size at least \(2\).

## Proof
First suppose that \(G\) is not complete. Its ordinary zero forcing number is \(N-2\). Indeed, if at least three vertices are initially unfilled and a filled vertex in a part \(V_i\) can force, then exactly one unfilled vertex lies outside \(V_i\). After that force, at least two unfilled vertices remain, all in \(V_i\); every filled vertex outside \(V_i\) then has at least two unfilled neighbors and every filled vertex inside \(V_i\) has none, so the process stalls. Conversely, leave one vertex unfilled in a non-singleton part and one vertex unfilled in a different part. A filled vertex in the first part forces the second unfilled vertex, after which that newly filled vertex forces the first. Since every transmission forcing set contains an ordinary zero forcing set, \(Z_{\alpha,\beta}(G)\ge N-2\).

Consider an initial set of size \(N-2\), leaving \(x\in V_i\) and \(y\in V_j\) unfilled with \(i\ne j\). In the first round, the \(n_j-1\) initially filled vertices of \(V_j\) all transmit to \(x\), while the \(n_i-1\) initially filled vertices of \(V_i\) all transmit to \(y\). Thus
\[
w_1(x)=(n_j-1)\alpha,
\qquad
w_1(y)=(n_i-1)\alpha.
\]
If neither reaches \(\beta\), the process stops. Suppose \(x\) fills first while \(y\) does not. At the next round, the vertices of \(V_i\) have already transmitted; the vertices outside \(V_i\cup V_j\) are unused and each contributes \(\alpha\) to \(y\); and the newly filled vertex \(x\) contributes \(\alpha w_1(x)=(n_j-1)\alpha^2\). Together with the weight already on \(y\),
\[
w_2(y)=(N-n_j-1)\alpha+(n_j-1)\alpha^2.
\]
Therefore this orientation of the two-step process succeeds exactly when
\[
\beta\le\tau_\alpha(n_j).
\]
The symmetric orientation is governed by \(\tau_\alpha(n_i)\). If both vertices fill in the first round, then at least one of \(n_i,n_j\) is at most \(N/2\); for such a part the second expression in \(\tau_\alpha\) is at least the first, so first-round success is also captured by the same criterion. Hence some size-\(N-2\) initial set is transmission forcing if and only if \(\beta\le T_\alpha(G)\).

If \(\beta>T_\alpha(G)\), size \(N-2\) is impossible. A size-\(N-1\) set leaves one vertex \(x\in V_i\) unfilled. Every initially filled vertex outside \(V_i\) then has \(x\) as its unique unfilled neighbor, so \(x\) receives exactly \((N-n_i)\alpha\) in the first round. Such a set succeeds for some \(i\) if and only if
\[
\beta\le\max_i(N-n_i)\alpha=\Delta\alpha.
\]
If \(\beta>\Delta\alpha\), no size-\(N-1\) set succeeds, whereas all \(N\) vertices initially filled trivially succeed. This proves the three cases. The complete-graph formula follows by the same one-unfilled-vertex calculation, giving threshold \((N-1)\alpha\).

## Verification
The standalone verifier `verify_transmission_multipartite.py` implements the transmission process directly with exact rational arithmetic. It exhaustively enumerates every initial subset for every complete-multipartite isomorphism type of order at most \(8\), for all \((\alpha,\beta)\) pairs from \(\{1/4,1/3,1/2,2/3,3/4,1\}^2\). It checks \(58\) multipartite types and \(2088\) parameter cases with no discrepancy. It also checks \(1332\) parameter specializations against the published star and complete-bipartite formulas. These finite computations are stress tests; the theorem itself is proved above for all admissible parameters and all finite complete multipartite graphs.

## Relationship to prior work
Berliner, Bozeman, Collins, Flagg, Furst, and Hunnell introduced transmission zero forcing in 2026. Their Section 4.1 gives exact formulas for complete graphs, stars, and complete bipartite graphs, while their general extremal theorem characterizes the case in which the transmission zero forcing number equals the order using maximum degree. The arbitrary complete multipartite formula above is not a restatement of those cases: it identifies exactly when the ordinary zero forcing minimum \(N-2\) survives transmission, through the part-size functional \(T_\alpha(G)\), and then resolves the entire intermediate regime. For \(G=K_{m,n}\) with \(2\le m\le n\), the formula reduces algebraically to their Proposition 4.1.3; for a star it reduces to their Proposition 4.1.2.

## Limitations
The result is specific to complete multipartite graphs and the stated synchronous one-transmission-per-filled-vertex model. It does not classify propagation time, optimal initial sets beyond their cardinality, or variants in which vertices may transmit more than once. The literature search found no covering arbitrary-multipartite theorem, but search non-detection is not a proof that no unindexed or later source exists.

## References
1. Adam H. Berliner, Chassidy Bozeman, Karen L. Collins, Mary Flagg, Veronika Furst, and Mark Hunnell, *Transmission Zero Forcing*, arXiv:2606.22246, first public version 2026-06-20. https://arxiv.org/abs/2606.22246
