# Sharp shortest-path covers in the sixth, seventh and eighth Fibonacci cubes

## Finding
Let \(\Gamma_n\) be the Fibonacci cube: its vertices are the length-\(n\) binary strings with no adjacent ones, and two vertices are adjacent when they differ in one bit. Let \(c_{\mathrm{geo}}(G)\) be the least number of (not necessarily disjoint) shortest paths whose union of edge sets contains all edges of \(G\). Let \(\operatorname{gp}_{\mathrm e}(G)\) be the largest cardinality of an edge set containing no three edges from a common shortest path. Write \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

**Theorem (finite, exact).** For every \(n\in\{6,7,8\}\),
\[
c_{\mathrm{geo}}(\Gamma_n)=F_n,\qquad \operatorname{gp}_{\mathrm e}(\Gamma_n)=2F_n.
\]
In order, the pairs of exact values are \((8,16)\), \((13,26)\), and \((21,42)\). In particular, these are three successive instances beyond the range \(n\le5\) proved for the edge-general-position conjecture of Klavžar and Tan (2023). This theorem does **not** settle that conjecture in unbounded dimension.

## Assumptions and scope
Graphs are finite, simple and undirected. A shortest path has distinct vertices and the minimum possible number of edges between its endpoints. Paths in a covering family may share vertices or edges. The claim applies **only** to \(n=6,7,8\). Its finite certificates use the labeled coordinate order shown in `geodesics.json`, which is bundled with this statement.

## Proof
**Isometry and a lower bound.** Every length-\(n\) binary word in \(\Gamma_n\) represents an independent set of the path on \(n\) positions. From a word \(u\) to a word \(v\), first remove the 1-bits of \(u\) absent from \(v\), then add the 1-bits of \(v\) absent from \(u\). All intermediate sets are independent. This gives a path of length exactly the Hamming distance \(d_H(u,v)\); since any cube edge changes only one bit, no shorter path is possible. Therefore every shortest path changes each coordinate at most once.

The edges changing the first coordinate form a set of size \(F_n\): each is uniquely encoded by a valid length-\(n-2\) Fibonacci string in the remaining coordinates after fixing the second coordinate to zero. Any shortest path contains at most one such edge. Hence every edge-covering collection of shortest paths has size at least \(F_n\):
\[c_{\mathrm{geo}}(\Gamma_n)\ge F_n.\]

**Matching finite upper bounds.** The complete explicit witnesses are the JSON arrays in `geodesics.json`, with \(8\), \(13\), and \(21\) listed paths for \(n=6,7,8\), respectively. The independent, standard-library verifier `verify.py` constructs the complete vertex and edge sets, checks every successive pair in every listed path is a genuine edge, computes shortest-path distances by breadth-first search for the actual graph, and checks that the union of listed path edges is **exactly** its full edge set. Its validated counts are:

| Dimension | Vertices | Edges | Listed shortest paths | Covered edges |
| --- | ---: | ---: | ---: | ---: |
| 6 | 21 | 38 | 8 | 38 |
| 7 | 34 | 71 | 13 | 71 |
| 8 | 55 | 130 | 21 | 130 |

These checks constitute an exhaustive finite certificate of the asserted cover existence: every required vertex, adjacency, shortest-path length, and edge of the specified finite graphs is explicitly checked. Together with the lower bound, they prove \(c_{\mathrm{geo}}(\Gamma_n)=F_n\) on the stated set of dimensions. No optimization solver's success claim is needed to validate the witnesses.

**Edge general position.** The union \(X\) of the first-coordinate and last-coordinate edge classes is edge general position, since a shortest path changes any given coordinate at most once. Each class has \(F_n\) edges and they are disjoint for \(n\ge2\), so \(|X|=2F_n\). Conversely, if \(S\) is an edge-general-position set, then for every shortest path \(P\) of the finite certificates, \(|S\cap E(P)|\le2\). Because the listed paths cover every edge, \(|S|\le\sum_P |S\cap E(P)|\le2F_n\). Combining both inequalities proves the second equality.

## Verification
From this directory run `python3 verify.py`; the script has no nonstandard dependencies. It reads the included `geodesics.json` and prints `VERIFICATION_OK` only after exact edge-coverage, shortest-path, and extreme-coordinate checks for each of the three dimensions. The recorded run produced `n=6 vertices=21 edges=38 geodesics=8 union_edges=38 extreme_coordinate_edges=8`, `n=7 vertices=34 edges=71 geodesics=13 union_edges=71 extreme_coordinate_edges=13`, `n=8 vertices=55 edges=130 geodesics=21 union_edges=130 extreme_coordinate_edges=21`, followed by `VERIFICATION_OK`. Unlike a bounded experiment testing an infinite conjecture, these witnesses and checks exhaust the **entire finite domain of the theorem**.

## Relationship to prior work
Klavžar and Tan (arXiv:2304.10114, first posted 20 April 2023; journal DOI below) gave the \(2F_n\) lower bound for all \(n\), established the edge-general-position equality through dimension five, and explicitly posed its extension as Conjecture 4.5. They also used edge covering by geodesics as an upper-bound method in a different partial cube (their Figure 3). The new statement supplies matching geodesic covers for the first three subsequent dimensions, making the upper bound exact there and also determining the corresponding minimum *edge-geodesic cover* numbers. The later Tian–Klavžar–Tan article concerns graphs with extremal edge-general-position values and block graphs, not the present Fibonacci-cube cases. No claim is made about arbitrary dimensions or about uniqueness of these covers.

## Limitations
The theorem is finite and covers only three new dimensions. The existence witnesses were located computationally, but every witness is explicit and its validity is independently replayable using only finite graph definitions. The verifier does not establish a uniform construction for all larger \(n\), and these data must not be extrapolated to a proof of the original unbounded conjecture. Literature indexing is incomplete; undiscovered prior small-dimensional calculations remain a priority risk.

## References
1. S. Klavžar and E. Tan, *Edge General Position Sets in Fibonacci and Lucas Cubes*, first public arXiv version 20 April 2023, arXiv:2304.10114, https://arxiv.org/abs/2304.10114; *Bull. Malays. Math. Sci. Soc.* 46, article 120 (2023), https://doi.org/10.1007/s40840-023-01517-y. Sections 2–4, especially Proposition 4.1, Theorem 4.3, Proposition 4.4, and Conjecture 4.5.
2. J. Tian, S. Klavžar and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, *Graphs and Combinatorics* 40, article 40 (2024), https://doi.org/10.1007/s00373-024-02770-z. Introduction and Section 3 (different families and extremal parameters).
