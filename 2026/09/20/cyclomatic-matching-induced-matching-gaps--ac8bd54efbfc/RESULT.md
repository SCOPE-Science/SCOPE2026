# Cyclomatic bounds and sharp matching-induced-matching gaps

**Same-model review: passed. Independent audit: not yet performed.**

## Definitions

For a finite simple graph `G`, let `nu(G)` denote its matching number and let `nu_s(G)` denote its induced (strong) matching number. Let
\[
c(G)=|E(G)|-|V(G)|+\kappa(G)
\]
be its cyclomatic number, where `kappa(G)` is the number of connected components.

## The cyclomatic bound

### Theorem 1
For every finite simple graph `G`,
\[
\boxed{\nu_s(G)\ge \left\lceil\frac{\nu(G)-c(G)}2\right\rceil.}
\]
Equivalently,
\[
\nu(G)-\nu_s(G)\le
\left\lfloor\frac{\nu(G)+c(G)}2\right\rfloor.
\]

### Proof
Fix a maximum matching `M` of `G`, with `|M|=q=nu(G)`. Form the conflict graph `C_M` whose vertices are the edges of `M`, with two vertices adjacent exactly when an edge of `G` joins an endpoint of one matching edge to an endpoint of the other. Independent sets in `C_M` are precisely induced submatchings of `M`. Hence
\[
\nu_s(G)\ge \alpha(C_M).
\]

Delete from `G` all vertices not saturated by `M`, contract every edge of `M`, and simplify loops and parallel edges. The resulting simple graph is exactly `C_M`. Deletions, contractions of non-loop edges, and deletion of parallel copies do not increase cyclomatic number, so
\[
c(C_M)\le c(G).
\]

We use the following elementary lemma. If a graph `H` has `q` vertices and cyclomatic number `r`, then
\[
\alpha(H)\ge \left\lceil\frac{q-r}{2}\right\rceil.
\]
Indeed, choose a spanning forest `F` of `H`. Exactly `r` edges of `H` lie outside `F`. Choose one endpoint from each such edge and let `S` be the set of chosen vertices. Then `|S|<=r` and `H-S` is a forest. Every forest on `N` vertices has an independent set of size at least `ceil(N/2)`, whence
\[
\alpha(H)\ge \alpha(H-S)
\ge \left\lceil\frac{q-|S|}{2}\right\rceil
\ge \left\lceil\frac{q-r}{2}\right\rceil.
\]
Applying this to `C_M` gives
\[
\nu_s(G)\ge\alpha(C_M)
\ge \left\lceil\frac{q-c(C_M)}2\right\rceil
\ge \left\lceil\frac{\nu(G)-c(G)}2\right\rceil.
\]

## Sharp fixed-order consequence for trees

### Corollary 2
For every tree `T` of order `n`,
\[
\boxed{\nu(T)-\nu_s(T)\le \left\lfloor\frac n4\right\rfloor.}
\]
The bound is sharp for every `n>=1`. Thus
\[
\max_{|V(T)|=n}\bigl(\nu(T)-\nu_s(T)\bigr)
=\left\lfloor\frac n4\right\rfloor.
\]

### Proof
A tree has `c(T)=0`, so Theorem 1 gives
\[
\nu_s(T)\ge\left\lceil\frac{\nu(T)}2\right\rceil.
\]
Therefore
\[
\nu(T)-\nu_s(T)
\le\left\lfloor\frac{\nu(T)}2\right\rfloor
\le\left\lfloor\frac n4\right\rfloor.
\]

To show sharpness, use the following whiskering identity. For a graph `H` on `k` vertices, let `W(H)` be obtained by attaching one new leaf to every vertex of `H`. Then
\[
\nu(W(H))=k,\qquad \nu_s(W(H))=\alpha(H).
\]
The first equality follows from the perfect matching of whisker edges. For the second, any induced matching edge lying inside `H` can be replaced by the whisker edge at either endpoint without creating a conflict; after all such replacements, an induced matching consists only of whisker edges, whose base vertices form an independent set in `H`. Conversely every independent set of `H` gives an induced matching of its whisker edges.

If `n=2k`, take `W(P_k)`. Then
\[
\nu=k,\qquad \nu_s=\alpha(P_k)=\left\lceil\frac k2\right\rceil,
\]
so the gap is `floor(k/2)=floor(n/4)`.

If `n=2k+1`, start from `W(P_k)` and attach one additional leaf to an endpoint of the base path. The matching number remains `k`. The new leaf is a pendant twin of the old whisker at that base vertex, so any induced matching using the new leaf edge can replace it by the old whisker edge; hence `nu_s` remains `ceil(k/2)`. The gap is again `floor(n/4)`. The cases `n=1,2,3` are immediate.

## Sharp fixed-order consequence for connected unicyclic graphs

### Corollary 3
Let `G` be a connected unicyclic graph of order `n`. Then
\[
\nu_s(G)\ge \left\lfloor\frac{\nu(G)}2\right\rfloor.
\]
Moreover,
\[
\boxed{
\max\bigl\{\nu(G)-\nu_s(G):G\text{ connected unicyclic},\ |V(G)|=n\bigr\}
=
\begin{cases}
0,&n=3,\\
\left\lfloor\dfrac{n+2}{4}\right\rfloor,&n\ge4.
\end{cases}}
\]

### Proof
Here `c(G)=1`, so Theorem 1 gives
\[
\nu_s(G)\ge\left\lceil\frac{\nu(G)-1}{2}\right\rceil
=\left\lfloor\frac{\nu(G)}2\right\rfloor.
\]
Thus
\[
\nu(G)-\nu_s(G)
\le \left\lceil\frac{\nu(G)}2\right\rceil
\le \left\lfloor\frac{n+2}{4}\right\rfloor.
\]
For `n=3`, the only connected unicyclic graph is `C_3`, whose two matching parameters are both `1`.

For sharpness when `n=4`, use `C_4`; when `n=5`, use `C_4` with one pendant leaf. Both have gap `1`.

For even `n=2k>=6`, use `W(C_k)`. The whiskering identity gives
\[
\nu(W(C_k))=k,\qquad
\nu_s(W(C_k))=\alpha(C_k)=\left\lfloor\frac k2\right\rfloor,
\]
so the gap is `ceil(k/2)=floor((n+2)/4)`.

For odd `n=2k+1>=7`, add one extra leaf to a cycle vertex of `W(C_k)`. As in the tree construction, the matching number remains `k` and the induced matching number remains `floor(k/2)`. Hence the same bound is attained.

## Relation to prior literature

Induced matchings (also called strong matchings or 2-matchings) have a substantial algorithmic and structural literature. Fricke and Laskar (1992), Zito (1999, 2000), and Golumbic and Lewenstein (2000) developed exact algorithms for trees or broader graph classes. Cameron and Walker (2005) characterized graphs for which the matching number and induced matching number are equal. Kang, Kim, Kim, and Law (2017) studied the *number* of `r`-matchings in trees of fixed order and proved an extremal counting theorem for induced matchings. Choi, Furuya, Kim, and Park (2020) treated matching number and induced matching number together in Ramsey-type theorems. Work on unicyclic edge ideals also uses induced matching number as a structural invariant.

The checked sources and synonymous searches did not locate Theorem 1, the exact fixed-order tree gap `floor(n/4)`, or the exact connected-unicyclic gap above. The older tree papers that were available only through abstracts, bibliographic records, or secondary citations were not fully inspected, so originality is asserted only to the best of our knowledge.

## Verification

`artifacts/verify_matching_induced_gap.py` performs independent finite checks using NetworkX 3.x. It verifies the cyclomatic inequality on every nonempty connected graph in the NetworkX Graph Atlas, the sharp tree extremum on every nonisomorphic tree through order 14, and the sharp unicyclic extremum on every nonisomorphic connected unicyclic graph through order 11. The expected output is recorded in `artifacts/expected_output.txt`.

## Limitations

- Originality is to the best of our knowledge; an equivalent inequality may occur in older strong-matching literature under different notation or in algebraic work on edge ideals.
- The full texts of Fricke--Laskar (1992), Zito (1999), and Zito (2000) were not all inspected. Their accessible descriptions emphasize algorithms for maximum induced matching on trees rather than the parameter inequalities proved here, but they remain the most relevant residual coverage risk.
- The fixed-order results determine the maximum gap and provide sharp families; they do not classify every extremal tree or unicyclic graph.
- All graphs are finite and simple.

## References

1. G. Fricke and R. Laskar, *Strong matchings on trees*, Congressus Numerantium 89 (1992), 239--243.
2. M. Zito, *Induced matchings in regular graphs and trees*, Lecture Notes in Computer Science 1665 (1999), 89--101. https://doi.org/10.1007/3-540-46784-X_10
3. M. Zito, *Linear Time Maximum Induced Matching Algorithm for Trees*, Nordic Journal of Computing 7 (2000), 58--63. https://www.cs.helsinki.fi/njc/References/zito2000%3A58.html
4. M. C. Golumbic and M. Lewenstein, *New results on induced matchings*, Discrete Applied Mathematics 101 (2000), 157--165. https://doi.org/10.1016/S0166-218X(99)00194-8
5. K. Cameron and T. Walker, *The graphs with maximum induced matching and maximum matching the same size*, Discrete Mathematics 299 (2005), 49--55. https://doi.org/10.1016/j.disc.2004.07.022
6. D. Y. Kang, J. Kim, Y. Kim, and H.-F. Law, *On the Number of r-Matchings in a Tree*, Electronic Journal of Combinatorics 24 (2017), P1.24. https://doi.org/10.37236/6681
7. I. Choi, M. Furuya, R. Kim, and B. Park, *A Ramsey-type theorem for the matching number regarding connected graphs*, Discrete Mathematics 343 (2020), 111648. https://doi.org/10.1016/j.disc.2019.111648
8. A. Alilooee, S. Kara, and S. Selvaraja, *Regularity of Powers of Unicyclic Graphs*, Rocky Mountain Journal of Mathematics 49 (2019), 699--728. https://arxiv.org/abs/1702.00916
9. B. Brešar, J. Dravec, T. Hedžet, and A. Samadi, *Induced matching vs edge open packing: trees and product graphs*. https://arxiv.org/abs/2406.04020
