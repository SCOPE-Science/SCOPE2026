# Exact b-forcing numbers for powers of paths and cycles
## Finding
Let \(b,k\ge 1\). For every path \(P_\ell\) with \(\ell\ge 2\),
\[
Z_b(P_\ell^k)=\max\{1,\min\{k,\ell-1\}-b+1\}.
\]
For every cycle \(C_n\) with \(n\ge 3\),
\[
Z_b(C_n^k)=\max\{1,\min\{2k,n-1\}-b+1\}.
\]
Equivalently, for either family,
\[
Z_b(G^k)=\max\{1,\delta(G^k)-b+1\}.
\]
Hence the standard minimum-degree lower bound for the generalized forcing process is attained throughout both graph-power families, for every forcing threshold and every power, including powers that have already become complete graphs.

## Assumptions and scope
Graphs are finite, simple, and undirected. The \(k\)-th power \(G^k\) joins two distinct vertices when their distance in \(G\) is at most \(k\). In the \(b\)-forcing process, initially some vertices are black and the rest are white; whenever a black vertex has at most \(b\) white neighbors and at least one white neighbor, all of those white neighbors may be turned black. The quantity \(Z_b(G)\) is the minimum size of an initial black set that eventually turns the entire graph black. This is the parameter denoted \(F_b(G)\) in the earlier \(k\)-forcing literature and \(Z_b(G)\) in the graph-powers paper.

The formulas cover all positive \(b\) and \(k\), not only the nonsaturated regimes. For paths, \(P_\ell^k=K_\ell\) when \(k\ge \ell-1\). For cycles, \(C_n^k=K_n\) when \(2k\ge n-1\).

## Proof
First note the universal lower bound
\[
Z_b(H)\ge \max\{1,\delta(H)-b+1\}
\]
for every nonempty graph \(H\). Indeed, consider a minimum initial black set \(B\). If \(B\neq V(H)\), then at the first force some black vertex \(u\) has at most \(b\) white neighbors. Thus at least \(d(u)-b\) neighbors of \(u\) were already black, and \(u\) itself was black. Therefore
\[
|B|\ge d(u)-b+1\ge \delta(H)-b+1.
\]
Also \(|B|\ge 1\).

For a path power,
\[
\delta(P_\ell^k)=\min\{k,\ell-1\}.
\]
If \(k\ge \ell-1\), then \(P_\ell^k=K_\ell\). In a complete graph with \(s\) initial black vertices, every \(b\)lack vertex has exactly \(\ell-s\) white neighbors, so forcing starts exactly when \(\ell-s\le b\). Hence
\[
Z_b(K_\ell)=\max\{1,\ell-b\},
\]
which is the claimed formula.

Now assume \(k\le \ell-2\), and put
\[
s=\max\{1,k-b+1\}.
\]
Color the consecutive vertices \(v_1,\ldots,v_s\) black. If \(b<k\), then \(v_1\) has exactly \(k-s+1=b\) white neighbors, so it forces all of them and makes \(v_1,\ldots,v_{k+1}\) black. If \(b\ge k\), then \(s=1\) and \(v_1\) has \(k\le b\) white neighbors, with the same result. Once \(v_1,\ldots,v_{k+1}\) are black, for each \(i=2,3,\ldots,\ell-k\), the vertex \(v_i\) has exactly one white neighbor \(v_{i+k}\) at the relevant stage, and forces it. Thus the entire path power becomes black from \(s\) initial vertices. The lower bound gives equality.

For a cycle power,
\[
\delta(C_n^k)=\min\{2k,n-1\}.
\]
If \(2k\ge n-1\), then \(C_n^k=K_n\), and the complete-graph argument gives
\[
Z_b(C_n^k)=\max\{1,n-b\}.
\]

Assume now \(2k<n-1\), and put
\[
s=\max\{1,2k-b+1\}.
\]
Color a cyclically consecutive block of \(s\) vertices black. If \(b\le k\), then \(s\ge k+1\); choose the \((k+1)\)-st vertex of the block. Every other vertex of the black block lies in its radius-\(k\) neighborhood, so it has exactly
\[
2k-(s-1)=b
\]
white neighbors and forces all of them. If \(b\ge k\), choose an endpoint of the black block. When \(b\le2k\) it again has exactly \(b\) white neighbors, and when \(b>2k\) it has all \(2k\) of its neighbors white and still may force them. In either case one force produces a cyclically consecutive black block of length \(2k+1\).

Suppose a cyclically consecutive black block has length at least \(2k+1\) but does not yet cover the cycle. Let \(x\) be the black vertex located \(k-1\) positions before the right endpoint of the block. Its radius-\(k\) neighborhood has exactly one vertex outside the block, namely the next vertex after the right endpoint. Thus \(x\) has exactly one white neighbor and forces it. Repeating grows the block one vertex at a time until all of \(C_n^k\) is black. This proves the matching upper bound and completes the proof.

## Verification
The proof is analytic for all stated parameters. A standalone verifier independently constructs graph powers, simulates the \(b\)-forcing closure, exhaustively searches all initial subsets in increasing cardinality, and compares the exact optimum with the two formulas. It checks path orders \(2\) through \(9\), cycle orders \(3\) through \(9\), powers \(1\) through \(7\), and forcing thresholds through two above the minimum degree, including saturated complete-graph cases.

The recorded verifier output is:

`ALL CHECKS PASSED; exhaustive_profiles=589; subset_prefixes_checked=21493; path_orders=2..9; cycle_orders=3..9; powers=1..7`

These finite checks corroborate the proof; they are not used to infer the infinite statement.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker introduce the notation \(Z_b\) for the generalized forcing rule in their study of graph powers and prove monotonicity of \(Z_b(G^k)\) with the power. In the same paper they determine the ordinary zero forcing values \(Z(P_\ell^k)=k\) in the nonsaturated path regime and \(Z(C_n^k)=2k\) in the nonsaturated cycle regime. The present result keeps the generalized forcing threshold \(b\) throughout and gives the exact value for every \(b\), every power, and every order.

Amos, Caro, Davila, and Pepper introduced the same process under the notation \(F_b\) and established general bounds, including the minimum-degree lower bound used above. Their general result supplies the lower bound but not the family-specific constructions that make it exact for all powers of paths and cycles.

Targeted searches using both \(b\)-forcing and \(k\)-forcing terminology, the symbols \(Z_b\) and \(F_b\), and path-power/cycle-power aliases found no statement covering these all-parameter formulas. Related work on skew zero forcing, ordinary zero forcing of graph powers, and \(k\)-forcing of Cartesian products concerns different propagation rules or different graph operations.

## Limitations
The theorem is specific to path powers and cycle powers; it does not assert that the minimum-degree lower bound is sharp for arbitrary graph powers. The construction exploits one-dimensional consecutive neighborhoods. No claim is made about positive-semidefinite, skew, signed, or other forcing variants. A residual bibliographic risk remains because generalized forcing terminology varies across the literature and an older poorly indexed special-case calculation could use different notation.

## References
1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1, first public 2026-10-02.
2. D. Amos, Y. Caro, R. Davila, R. Pepper, *Upper bounds on the k-forcing number of a graph*, arXiv:1401.6206v1, first public 2014-01-23.
