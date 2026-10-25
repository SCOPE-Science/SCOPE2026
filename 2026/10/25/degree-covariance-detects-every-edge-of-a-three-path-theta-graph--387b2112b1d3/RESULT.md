# Degree covariance detects every edge of a three-path theta graph

## Finding

Let \(G=\Theta(a,b,c)\) consist of two distinct poles joined by three internally vertex-disjoint paths, with integer edge lengths \(a,b,c\ge2\). Choose a spanning tree \(T\) uniformly from all spanning trees of \(G\). Write \(D_v=\deg_T(v)\) for each labeled vertex and \(\Sigma_{uv}=\operatorname{Cov}(D_u,D_v)\).

For **every pair of distinct vertices** \(u,v\),
\[
\boxed{\quad uv\in E(G)\quad\Longleftrightarrow\quad\Sigma_{uv}\ge0.\quad}
\]
More precisely, all nonedges have strictly negative covariance, every edge has nonnegative covariance, and all edges have strictly positive covariance except the following sharp zero cases: all six edges of \(\Theta(2,2,2)=K_{2,3}\), and the unique edge joining the two internal vertices on the length-three path of \(\Theta(2,2,3)\). Thus the off-diagonal covariance matrix alone reconstructs the entire labeled host graph within this family, including the exceptional cases.

For exact values, set \(W=ab+ac+bc\). If an edge lies on a path of length \(r\), and the other two paths have lengths \(s,t\), then for its endpoints \(u,v\):

* If at least one endpoint is a pole,
\[
\boxed{\displaystyle \Sigma_{uv}=\frac{(s+t)W-4(s^2+st+t^2)}{W^2}
=\frac{(r-4)(s+t)^2+st(s+t+4)}{W^2}.}
\]
* If both endpoints are internal vertices,
\[
\boxed{\displaystyle \Sigma_{uv}=\frac{(s+t)(W-4(s+t))}{W^2}
=\frac{(s+t)((r-4)(s+t)+st)}{W^2}.}
\]

## Assumptions and scope

The graph is finite, simple, unweighted, and labeled. Each of the three paths has at least two edges; hence the poles are not adjacent and all internal vertices have host degree two. Spanning trees are equally likely, not sampled using independently retained edges or random minimum weights. All covariance statements are **finite exact identities**, not limiting approximations. The reconstruction rule uses exact population covariances; finite-sample estimated covariances require separate error control.

## Proof

**1. Uniform deletion representation.** The graph has \(a+b+c\) edges and \(a+b+c-1\) vertices. Each spanning tree therefore deletes exactly two edges. The deleted edges must lie on distinct paths: removing two from one path disconnects the segment between them. Conversely, deleting one edge from each of two different paths leaves the third path intact and all vertices connected, producing a tree. Consequently there are exactly
\[
W=ab+ac+bc
\]
spanning trees, indexed bijectively by unordered pairs of edges in distinct paths.

**2. Deletion covariance kernel.** For a path of length \(r\), put \(h=s+t\) where \(s,t\) are the other lengths, and set \(p_r=h/W\). Let \(I_e\) indicate deletion of edge \(e\). Every edge on the \(r\)-path has deletion probability \(p_r\). Distinct edges on the same path cannot both be deleted, while an edge on the \(r\)-path and an edge on the \(s\)-path are deleted together with probability \(1/W\). Hence
\[
\operatorname{Cov}(I_e,I_f)=
\begin{cases}
 p_r(1-p_r),&e=f\text{ on path }r,\\
 -p_r^2,&e\ne f\text{ on the same path }r,\\
 -t^2/W^2,&e\text{ on path }r,\ f\text{ on path }s,\text{ with third path length }t.
\end{cases}
\]
For the final case, the identity \(W-(s+t)(r+t)=-t^2\) is used. In particular **every pair of distinct edge-deletion indicators has strictly negative covariance**.

**3. Vertex degrees and nonedges.** For any vertex \(v\),
\[
D_v=\deg_G(v)-\sum_{e\ni v}I_e.
\]
Thus \(\Sigma_{uv}\) is the sum of the above deletion covariances over an edge incident to \(u\) and an edge incident to \(v\). If \(u,v\) are nonadjacent, their incident edge sets are disjoint. Every term is then strictly negative, proving \(\Sigma_{uv}<0\).

**4. Covariance at an edge.** If an edge joins two internal vertices on the \(r\)-path, their incident edge sets share one edge, with two other distinct edges on that same path. Therefore
\[
\Sigma_{uv}=p_r(1-p_r)-3p_r^2=p_r(1-4p_r),
\]
which is the second displayed formula. If the edge joins a pole to the first internal vertex of the \(r\)-path, the pair shares one edge; it also has one further same-path pair and two pairs involving each of the two other paths. Consequently
\[
\begin{aligned}
\Sigma_{uv}&=p_r(1-p_r)-p_r^2-2\frac{s^2+t^2}{W^2}\\
&=\frac{(s+t)W-4(s^2+st+t^2)}{W^2},
\end{aligned}
\]
which is the first displayed formula. The other pole is symmetric.

**5. Sharp signs and equality.** For a pole-to-internal edge, the numerator is
\[
(r-4)(s+t)^2+st(s+t+4).
\]
It increases strictly with \(r\). At \(r=2\), putting \(s=2+x\), \(t=2+y\) with integers \(x,y\ge0\), it becomes
\[
x^2y+xy^2+8xy+4x+4y\ge0,
\]
with equality exactly when \(x=y=0\). Hence zero pole-to-internal covariance occurs exactly for \(\Theta(2,2,2)\). For an internal-to-internal edge, \(r\ge3\). Its sign is that of
\[
(r-4)(s+t)+st.
\]
This is strictly positive if \(r\ge4\). If \(r=3\), it equals \((s-1)(t-1)-1\), nonnegative for \(s,t\ge2\), and zero exactly at \(s=t=2\). Combining this with strict negativity at nonedges proves both the sign test and its complete equality classification. \(\square\)

## Verification

The standalone pure-Python checker `verify.py` reconstructs the graph, independently enumerates each pair of removed edges, checks graph connectivity to count actual spanning trees, and calculates exact rational degree covariances from direct spanning-tree enumeration. For all \(216\) ordered length triples \((a,b,c)\in\{2,3,4,5,6,7\}^3\), the checker compares every covariance entry against an independently implemented deletion-kernel calculation, compares all adjacent entries against both local closed forms, checks every nonedge's strict sign, checks every edge's nonnegative sign and its exceptional zeros, and checks covariance row sums. It passed \(35{,}865\) exact assertions. Execute `python verify.py` with Python 3. No external packages are required. These finite checks test the derivation but do not replace the all-parameter proof.

## Relationship to prior work

Cherkashin, Petrov and Prozorov (2022) classify connected graphs whose spanning-tree vertex-degree enumerator is real stable; their classification includes the fact that \(\Theta(2,2,2)\) is stable while longer three-path theta graphs containing an induced cycle of length at least five are not. Their result does not state the present signed vertex-covariance classification.

Fita Sanmartín, Schnörr and Hamprecht (2024) give a general reduced-Laplacian inverse formula for covariance of weighted spanning-tree degrees on arbitrary graphs. Their formula provides broad **computational coverage of individual covariance entries**, including this family in principle. The present claim is narrower in graph class but stronger in its **uniform all-length sign theorem**, sharp zero classification, and reconstruction of labeled adjacency by a sign threshold; those consequences require additional global algebraic inequalities not given by the general matrix formula. Rapoport (2025) further develops general joint degree laws through fermionic methods; the inspected text does not identify this theta-graph sign structure.

## Limitations

The theorem is not an originality claim for general spanning-tree covariance formulas or for the stability classification. It assumes uniformly distributed unweighted spanning trees and three internally disjoint paths of length at least two. It does not claim covariance-sign recovery on arbitrary connected graphs: even wheel graphs have different adjacent-degree sign behavior. Exact reconstruction from empirically estimated covariance is not guaranteed without accuracy bounds, especially where true adjacent covariance is zero. Historical priority for a possible earlier equivalent theta-graph specialization has not been independently resolved.

## References

1. D. Cherkashin, F. Petrov, P. Prozorov, *On stability of spanning tree degree enumerators*, arXiv:2209.04413 (first posted 2022-09-09), https://arxiv.org/abs/2209.04413.
2. E. Fita Sanmartín, C. Schnörr, F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472 (first posted 2024-09-20), https://arxiv.org/html/2409.13472v1.
3. A. Rapoport, *Correlations in Uniform Spanning Trees: a Fermionic Approach*, Journal of Statistical Physics **192** (2025), article 145, https://doi.org/10.1007/s10955-025-03510-0.
