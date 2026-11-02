# Strong chromatic index and strong cliques of uniform theta graphs

## Finding
For every pair of integers \(k\ge3\) and \(\ell\ge2\), let \(\Theta_{k,\ell}\) consist of \(k\) internally vertex-disjoint paths of length \(\ell\) between two distinct vertices. Then
\[
\chi'_s(\Theta_{k,\ell})=\begin{cases}
2k,&\ell=2,\\
k+2,&\ell=4,\\
k+1,&\ell=3\text{ or }\ell\ge5,
\end{cases}
\qquad
\omega_s(\Theta_{k,\ell})=\begin{cases}
2k,&\ell=2,\\
k+1,&\ell\ge3.
\end{cases}
\]
Here \(\chi'_s(G)\) is the strong chromatic index and \(\omega_s(G)\) the largest number of pairwise strongly conflicting edges. In particular, for \(\ell\ge3\), the strong chromatic index exceeds the strong clique number if and only if \(\ell=4\), in which case the gap is exactly one. The result is uniform in the number of branches and in their common length.

## Assumptions and scope
All graphs are finite and simple. The two terminals are distinct and nonadjacent when \(\ell\ge2\); the interiors of the \(k\) paths are mutually disjoint. Let \(e_{i,j}\), for \(1\le i\le k\) and \(1\le j\le\ell\), denote the edge at position \(j\) on branch \(i\), counted from the same terminal \(u\) toward the other terminal \(v\). Two distinct edges *conflict* if they share a vertex or some endpoint of one is adjacent to an endpoint of the other. A strong edge coloring assigns different colors to every pair of conflicting edges. Thus \(\chi'_s(G)=\chi(L(G)^2)\) and \(\omega_s(G)=\omega(L(G)^2)\).

The family with \(\ell=2\) is \(K_{2,k}\). The restriction \(k\ge3\) is substantive: for \(k=2\) the graph is a cycle of length \(2\ell\), with additional length-dependent coloring behavior.

## Proof
**1. Exact cross-branch conflicts.** Suppose \(\ell\ge3\) and \(i\ne h\). The only conflicting edge pairs between branches \(i\) and \(h\), written as their ordered position pairs, are
\[
(1,1),\ (1,2),\ (2,1),\ (\ell,\ell),\ (\ell,\ell-1),\ (\ell-1,\ell).
\]
Indeed, distinct branches meet only at their common terminals, and only edge endpoints at distance at most one from a common terminal can be adjacent across branches. In each cross-branch conflict bipartite graph the maximum degree is two and there is no \(K_{2,2}\): this also follows by checking the six displayed position pairs, with coincident middle positions handled when \(\ell=3\).

**2. Strong clique number.** For \(\ell=2\), every pair of the \(2k\) edges conflicts, giving \(\omega_s=2k\). For \(\ell\ge3\), the \(k\) edges \(e_{i,1}\) together with \(e_{1,2}\) form a strong clique of size \(k+1\). Conversely, a strong clique contained in a single branch has at most three edges, since edges separated by at least three positions do not conflict. If a strong clique meets two or more branches, and contains \(r_i\) edges in branch \(i\), the cross-branch conflict characterization yields \(r_i+r_h\le3\) whenever \(r_i,r_h>0\): a complete bipartite graph of conflicting pairs can have neither a \(K_{2,2}\) nor a vertex of degree above two. Thus at most one branch contributes two edges, and every other represented branch contributes one. With at most \(k\) represented branches, the clique has size at most \(k+1\). Therefore \(\omega_s=k+1\).

**3. Lower bounds for coloring.** Clique size supplies \(2k\) colors for \(\ell=2\) and \(k+1\) for \(\ell\ge3\). For \(\ell=4\), suppose a strong \((k+1)\)-coloring existed. The \(k\) edges \(e_{i,1}\) use distinct colors; every \(e_{i,2}\) conflicts with all of them, hence all \(e_{i,2}\) have the sole unused color \(a\). Similarly all \(e_{i,3}\) have the sole color \(b\) omitted by the \(k\) edges \(e_{i,4}\). Since \(e_{i,2}\) and \(e_{i,3}\) are adjacent, \(a\ne b\). It follows that \(b\) occurs on some \(e_{h,1}\). But \(e_{h,1}\) and \(e_{h,3}\) conflict along their branch and both have color \(b\), a contradiction. Thus \(\ell=4\) needs at least \(k+2\) colors.

**4. Explicit matching upper bounds.** The following prescriptions use exactly the stated numbers of colors. On branch \(i\), list the colors of its consecutive edges from \(u\) to \(v\), writing \(1\le i\le k\).

* For \(\ell=2\): use \((i,k+i)\).
* For \(\ell=3\): use \((i,k+1,1+(i\bmod k))\). The last-edge colors form a derangement of the first-edge colors.
* For \(\ell=4\): use \((i,k+1,k+2,i)\).
* For \(\ell=5\): use \((i,k+1,c_i,1,d_i)\), where \(c_i=3\) for \(i=2\) and \(c_i=2\) otherwise, and \(d_1=k+1\), \(d_i=i\) for \(i\ge2\). This uses only \(1,\dots,k+1\), even when \(k=3\).
* For \(\ell\ge6\): color the first and last edges on branch \(i\) with \(i\), and the second and penultimate edges with \(k+1\). Color the \(\ell-4\) interior edges at positions \(3,4,\dots,\ell-2\) by the periodic sequence \(1,2,3,1,2,3,\dots\), choosing one of its three cyclic phase shifts so that both its first and last colors differ from \(i\). Such a phase exists because only the two endpoint colors need be avoided, and they occupy at most two values of a three-color palette. Note that \(\ell\ge6\) separates the two occurrences of color \(k+1\) on each branch by at least three edge positions.

Each prescription is proper on the square of each path: no two edges at positions differing by at most two share a color. For distinct paths, the six conflict types in Step 1 all receive distinct colors: first-edge colors are distinct, last-edge colors are distinct, and the nearest internal edge to either terminal avoids all colors at that terminal. In the \(\ell=3\) case the derangement additionally resolves the same-branch conflict between first and last edges. Hence each prescription is a valid strong edge coloring. The lower and upper bounds agree and prove the formulas.

## Verification
Run the included standalone script with `python3 verify_theta.py`. It constructs graph adjacencies and the full edge-conflict graph from endpoint adjacency, checks the explicit colorings on 464 parameter pairs, independently decides exact minimum color counts on 30 small instances using a backtracking coloring solver, and computes exact maximum strong-clique sizes on 50 instances using a separate clique search. Its expected successful line is:

`VERIFY_OK constructive_graphs=464 exact_chromatic_instances=30 exact_clique_instances=50`

These finite tests corroborate the statement but do not prove its universal quantifiers. The proof is the structural argument and the explicit infinite colorings above.

## Relationship to prior work
Strong edge coloring is the coloring problem for squares of line graphs. Cames van Batenburg, de Joannis de Verclos, Kang and Pirot [1] study general minor-free bounds, including the \(3\Delta\) upper bound for \(K_4\)-minor-free multigraphs; the present series-parallel graphs satisfy much sharper exact values. DeOrsey and coauthors [2] study sparse strong edge coloring, including some three-branch theta cases in the proof of their sparse-graph theorem; their finite cases and sparse-graph bounds do not determine the uniform all-length formula or the strong-clique chromatic gap. Naprasit and Nakprasit [3] establish subdivision upper bounds of \(2\Delta\), which are not exact for these graphs with \(\ell\ge3\). A planar large-girth equality result [4] assumes \(\sigma(G)\ge\Delta(G)+2\), whereas \(\sigma(\Theta_{k,\ell})=k+1=\Delta+1\); it does not yield the classification here. These are comparisons of mathematical implications, not a claim of exhaustive priority verification.

## Limitations
The theorem concerns **uniform** path length and \(k\ge3\). It does not classify unequal branch lengths, strong list edge colorings, or the two-branch cycle family. Publication priority is provisional: publicly indexed searches are incomplete and the full text of the 2014 subdivision paper was not available for detailed inspection. No independent mathematical audit or external certification has been performed.

## References
[1] W. Cames van Batenburg, R. de Joannis de Verclos, R. J. Kang, F. Pirot, *Strong chromatic index and Hadwiger number*, arXiv:1905.06031, initially posted 2019-05-15; *Journal of Graph Theory* (2022).

[2] P. DeOrsey et al., *On the Strong Chromatic Index of Sparse Graphs*, arXiv:1508.03515, initially posted 2015-08-14; *Electronic Journal of Combinatorics* 25 (2018), P3.18.

[3] K. Naprasit and K. Nakprasit, *The strong chromatic index of graphs and subdivisions*, *Discrete Mathematics* 317 (2014), 75–78, DOI:10.1016/j.disc.2013.11.005.

[4] *On the precise value of the strong chromatic index of a planar graph with a large girth*, *Discrete Applied Mathematics* (2018), DOI:10.1016/j.dam.2018.03.075.
