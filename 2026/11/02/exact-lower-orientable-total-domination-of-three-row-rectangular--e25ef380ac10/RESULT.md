# Exact lower orientable total domination of three-row rectangular grids

## Finding
For every integer \(n\ge 2\), the lower orientable total domination number of the three-row rectangular grid is
\[
\operatorname{dom}_{t}(P_3\square P_n)=n+2.
\]
This determines the invariant for every circumference of the three-row path product, sharpening the previously available bounds \(n\le\operatorname{dom}_{t}(P_3\square P_n)\le n+2\) for \(n\ge3\).

## Assumptions and scope
All graphs are finite, simple, and undirected before orientation. Let \(G_n=P_3\square P_n\), with vertices \((r,j)\), row \(r\in\{1,2,3\}\) and column \(1\le j\le n\). Edges join vertices differing by one in exactly one coordinate. An orientation is *valid* if every vertex has positive indegree. A *directed total dominating set* \(S\) has an arc from some vertex of \(S\) to every vertex of the orientation, including vertices of \(S\). Its minimum cardinality is \(\gamma_t(D)\). The lower orientable total domination number is \(\operatorname{dom}_t(G)=\min_D\gamma_t(D)\), where \(D\) ranges over valid orientations of \(G\). The assertion covers \(n\ge2\); for \(n=1\), the graph is a path and has no valid orientation.

## Proof
**Orientation criterion.** A vertex subset \(S\subseteq V(G)\) is a directed total dominating set for some valid orientation if and only if (i) \(S\) dominates \(G\) in the ordinary, closed-neighborhood sense and (ii) every connected component of the induced graph \(G[S]\) contains a cycle.

For necessity, every vertex of \(G\setminus S\) has a neighbor in \(S\), and every vertex of \(S\) receives an arc from within \(S\). In each finite component of \(G[S]\), following incoming arcs backwards eventually yields a directed cycle, hence an undirected cycle. Conversely, choose a cycle in every component of \(G[S]\), orient it cyclically, and orient the edges of a forest rooted on that cycle away from the cycle, so that every selected vertex has an incoming selected neighbor. Direct all edges from \(S\) to its complement outward; this gives every unselected vertex an incoming selected neighbor by (i). The remaining edges may be oriented arbitrarily. Therefore, the resulting orientation is valid and \(S\) totally dominates it.

**Upper bound.** Select all \(n\) middle-row vertices and the two adjacent top-row vertices in columns one and two:
\[
S_0=\{(2,j):1\le j\le n\}\cup\{(1,1),(1,2)\}.
\]
Every unselected vertex has a selected middle-row neighbor in its own column. The induced selected graph is connected and contains the square on rows one and two and columns one and two. The orientation criterion thus gives \(\operatorname{dom}_t(G_n)\le n+2\).

**Lower bound.** Let \(S\) be any set meeting the orientation criterion. Write \(t_j=|S\cap(\{1,2,3\}\times\{j\})|\in\{0,1,2,3\}\). Let \(r\ge1\) be the number of maximal nonempty runs of consecutive columns having \(t_j>0\), let \(e=|\{j:t_j=0\}|\), and let \(b\in\{0,1,2\}\) count empty boundary columns among columns one and \(n\).

Every occupied run has at least one selected component, hence contains a cycle. In any grid cycle, the leftmost occupied column of the cycle must contain a vertical cycle edge: each of its vertices has at most one horizontal neighbor toward the remaining cycle, so the cycle could not pass through that column without a vertical edge. The same holds for the rightmost occupied column. These two columns are distinct because a single column induces a path. Consequently, every occupied run contains at least two distinct columns with \(t_j\ge2\), and its *surplus* \(\sum_{j\text{ in run}}(t_j-1)\) is at least two.

An interior block of empty columns has length at most two: otherwise the second empty column has no selected neighbor. A boundary block of empty columns has length at most one. Thus, with \(r-1\) interior gaps and \(b\) empty boundary columns,
\[
e\le 2(r-1)+b.\tag{1}
\]

We sharpen each run's surplus if it abuts an empty boundary column. If column one is empty, all three vertices of column two are selected, since each of the three vertices of column one can be dominated only from its matching row in column two. The resulting surplus of two in column two is accompanied by at least one other column with \(t_j\ge2\), owing to the cycle in that run, so this run has surplus at least three. The right boundary is symmetric. If *both* boundary columns are empty and the same occupied run is adjacent to both, the first and last occupied columns are distinct (the run contains a cycle); both are completely selected and contribute surplus at least four. Hence, in all cases, summing over the \(r\) occupied runs gives
\[
\sum_{j:t_j>0}(t_j-1)\ge 2r+b.\tag{2}
\]
There are \(n-e\) nonempty columns, and therefore (1) and (2) imply
\[
|S|=(n-e)+\sum_{j:t_j>0}(t_j-1)
\ge n-2(r-1)-b+2r+b=n+2.
\]
The orientation criterion and upper-bound construction finish the proof for every \(n\ge2\). \(\square\)

## Verification
The accompanying standalone C++17 file `verify.cpp` independently constructs each grid, exhaustively searches all vertex subsets of size at most \(n+2\), and tests closed-neighborhood domination plus existence of a cycle in each selected component, for every \(2\le n\le9\). For \(n=2,3\), it additionally enumerates all orientations with positive indegree, computes the best directed total dominating set, and compares the minima obtained by the two independent formulations. It verifies the explicit upper-bound witness for each tested width. The executable prints `VERIFY_OK`. These computations do not replace the all-width proof above.

## Relationship to prior work
Anderson, Dravec, Johnston, and Kuenzel (2023, arXiv:2311.16307v1), Section 4, establish \(\operatorname{dom}_t(P_m\square P_n)\ge mn/3\) for \(3\le m\le n\), and \(\operatorname{dom}_t(P_m\square P_n)\le m(n+2)/3\) when \(3\mid m\). At width three these are precisely \(n\) and \(n+2\), without equality. Their preliminary cycle requirement for selected components is used here and is not asserted to be new. Goto and Kobayashi (2021, arXiv:2109.14108v1) determine ordinary connected domination in rectangular grids, a distinct invariant without the required selected-component cycles. The present contribution is the matching all-width lower bound for lower *orientable total* domination, including its boundary-column accounting argument.

## Limitations
The formula concerns rectangular \(P_3\square P_n\) only; it does not determine the upper orientable total domination number, wider grids, or cylinders. The result relies on the precise definition of a valid orientation (strictly positive indegree at every vertex), not arbitrary orientations. Independent mathematical audit and publication-priority certification have not been performed. Searches cannot rule out unindexed equivalent results.

## References
1. S. E. Anderson, T. Dravec, D. Johnston, and K. Kuenzel, *Orientable total domination in graphs*, arXiv:2311.16307v1, initially public 2023-11-27, Section 4. https://arxiv.org/html/2311.16307v1
2. M. Goto and K. M. Kobayashi, *Connected domination in grid graphs*, arXiv:2109.14108v1, initially public 2021-09-29, Section 1. https://arxiv.org/html/2109.14108v1
