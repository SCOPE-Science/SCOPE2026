# A reconfiguration singularity for minimum robust backbones of crown graphs

## Finding

Fix integers \(n\ge3\) and \(2\le k\le n-1\). Put \(H_n=K_{n,n}-M_n\), with left vertices \(A_i\) and right vertices \(B_i\), adjacent when their indices differ. A *\(k\)-robust dominating backbone* is a set \(S\subseteq V(H_n)\) that dominates \(H_n\) and whose induced subgraph has vertex connectivity at least \(k\). Count backbones according to the numbers selected on the left and right.

Write \(S=A_I\cup B_J\), \(a=|I|\), \(b=|J|\), and \(t=|I\cap J|\). Then a backbone exists **if and only if**

\[
 (a\ge k+1\ \text{and}\ b\ge k+1)\quad\text{or}\quad(\min(a,b)=k\ \text{and}\ t=0).
\]

Define \(F_{n,r}(z)=\sum_{j=r}^n\binom nj z^j\) and \(H_{n,k}(z)=\sum_{j=k}^{n-k}\binom{n-k}j z^j\), with empty sums equal to zero. The complete bivariate counting polynomial is

\[
 P_{n,k}(x,y)=F_{n,k+1}(x)F_{n,k+1}(y)
 +\binom nk\bigl(x^kH_{n,k}(y)+y^kH_{n,k}(x)\bigr)
 -\binom nk\binom{n-k}k x^ky^k.
\]

The minimum cardinality is \(2k\) when \(n\ge2k\), and \(2k+2\) when \(n<2k\). The respective numbers of minimum sets are \(\binom nk\binom{n-k}k\) and \(\binom n{k+1}^2\).

Let \(\mathcal R_{n,k}\) be the graph of minimum backbones, with an edge when exactly one chosen vertex is removed and another, previously absent, is chosen, while retaining a minimum backbone (*token jumping*). Then:

\[
 \begin{array}{ll}
 n<2k:&\mathcal R_{n,k}\cong J(n,k+1)\square J(n,k+1),\\
 n=2k:&\mathcal R_{n,k}\text{ consists of }\binom{2k}k\text{ isolated vertices},\\
 n>2k:&\mathcal R_{n,k}\text{ is connected and }2k(n-2k)\text{-regular}.
 \end{array}
\]

Here \(J(n,r)\) is the Johnson graph whose vertices are the \(r\)-subsets of \([n]\), adjacent when one element is replaced. In particular, the minimum-backbone solution space has a connectivity singularity at \(n=2k\).

## Assumptions and scope

All graphs are finite, undirected, and simple. For \(k\ge1\), an induced graph is \(k\)-vertex-connected when it has more than \(k\) vertices and remains connected after deletion of fewer than \(k\) vertices. Domination is ordinary closed-neighborhood domination in the full crown graph, and the reconfiguration operation is one token jump with **fixed minimum size**; it is not token sliding, addition/removal, or a reconfiguration permitting non-minimum intermediate sets. The theorem concerns \(n\ge3\) and \(2\le k\le n-1\).

## Proof

**Connectivity lemma.** For \(a,b\ge2\), the induced graph on \(A_I\cup B_J\) is \(K_{a,b}\) minus \(t\) independent edges. It is connected except when \(a=b=t=2\), in which case it is two disjoint edges. To prove this, two vertices in the same part have a common neighbor unless their opposite part consists of the two respective deleted partners. If the opposite part has two vertices and both are separately forbidden, a third vertex in the other part or an additional available opposite-side vertex gives a connecting route; the only obstruction is precisely two matched pairs with no others. Equivalently, any such graph with at least five vertices and at least two in each part is connected.

Assume \(a\le b\). If \(t=0\), the graph is complete bipartite, with vertex connectivity \(a\). For \(t>0\), some right vertex has degree \(a-1\), so connectivity is at most \(a-1\). When \(a=2\), connectedness (excluding the stated exception) proves the reverse bound of one. When \(a\ge3\), deleting at most \(a-2\) vertices leaves at least two vertices in each part and at least \(b+2\ge5\) overall; the surviving edges still form a complete bipartite graph minus a matching, which is connected by the previous observation. Thus

\[
 \kappa(H_n[A_I\cup B_J])=\begin{cases}
 \min(a,b),&t=0,\\
 \min(a,b)-1,&t>0,
 \end{cases}
\]

for \(a,b\ge2\), apart from the disconnected \(a=b=t=2\) exception.

**Domination and admissibility.** Any selected set with at least two vertices in each bipartition class dominates: each vertex not selected sees at least one of the two or more selected vertices opposite it, because at most its index partner is nonadjacent. Conversely, a connected dominating set has at least two selected vertices in each class. Indeed, if one class has no selected vertices, then a selected set has no edges and cannot both be connected and dominate; if a class contains the unique vertex \(A_i\), then either \(B_i\) is unselected and undominated, or \(B_i\) is selected and isolated from \(A_i\) in the induced graph (even if further right vertices are selected). Symmetry covers the other side. For \(k\ge2\), the connectivity formula above is equivalent to the claimed two cases. The exceptional two-edge graph is excluded automatically.

**Counting and minima.** The case \(a,b\ge k+1\) contributes \(F_{n,k+1}(x)F_{n,k+1}(y)\). If the left class has exactly \(k\) selected indices, it must be disjoint from the right class: choose those indices in \(\binom nk\) ways, then choose \(b\ge k\) from the remaining \(n-k\) indices. The right-class-symmetric term is analogous. Configurations with both classes of size \(k\) are counted twice, and their \(\binom nk\binom{n-k}k\) instances must be subtracted once. This proves the polynomial. If \(n\ge2k\), a disjoint pair of \(k\)-subsets exists and yields minimum size \(2k\). If \(n<2k\), no disjoint \(k\)-subsets exist and the minimum is attained by precisely all choices \(a=b=k+1\), giving size \(2k+2\). These observations also give both optimizer counts.

**Minimum-set reconfiguration.** If \(n<2k\), all minimum sets choose independently \(k+1\) left indices and \(k+1\) right indices. Every such pair is feasible. A replacement between sides would produce side sizes \(k\) and \(k+2\); feasibility would then demand disjoint supports, impossible because their union would have \(2k+2>n\) indices. Therefore each allowed jump preserves both part sizes and changes one index in one coordinate, proving the Cartesian product of Johnson graphs, which is connected (including the one-vertex boundary).

If \(n\ge2k\), every minimum set consists of disjoint left and right \(k\)-subsets \(I,J\). Single replacements between sides would change a side to size \(k-1\), hence are forbidden. Replacing an index within a side is legal exactly when the new index lies in the remaining \(n-2k\) unoccupied positions. For \(n=2k\), no such position exists; every state is isolated, and there are \(\binom{2k}k\) states. For \(n>2k\), interpret \(I,J\) as two colors of indistinguishable tokens and the other indices as holes on a complete index set. A token and a hole may always exchange positions. One hole suffices to exchange any two occupied tokens at indices \(i,j\), by moving the token at \(i\) into the hole, the token at \(j\) into \(i\), and the temporarily moved token into \(j\); the hole returns to its original position. Hole locations can also be rearranged arbitrarily. Consequently all placements with the required numbers of tokens of both colors are connected. At every placement each of the \(2k\) selected tokens has \(n-2k\) legal destinations, so the graph is \(2k(n-2k)\)-regular. This completes the proof.

## Verification

The two supplied Python scripts in `checks/` reconstruct adjacency from the definition, test domination directly, compute induced vertex connectivity by enumerating vertex removals, and compare all bivariate coefficients for every selected subset when \(3\le n\le6\). They separately enumerate all minimum backbones and their legal token-jump moves to verify components and degrees. Run `python checks/crown_conn_check.py` and `python checks/crown_reconfig_check.py` from the extracted package root. Their recorded outputs are in `checks/output.txt`. Finite checks corroborate the proof but do not establish it for arbitrary \(n,k\).

## Relationship to prior work

Lokshtanov, Mouawad, Panolan and Siebertz (2019) analyze the complexity of connected-domination reconfiguration under a token-addition/removal rule. Bousquet, Mouawad, Nishimura and Siebertz (2022) survey token jumping and sliding models for dominating and connected dominating sets. Neither inspected work gives this fixed-size optimum-state graph for crown graphs, and the move rules in the 2019 paper differ from those used here.

The 2025 crown-graph paper *Binomial edge ideals of crown graphs* supplies a related induced-connectivity lemma (Lemma 3.1) and the minimum ordinary connected domination number of four (Lemma 5.1). Those graph properties are prior results, not newly claimed here. The present all-\(k\) selection counts and the transition between isolated and connected **minimum token-jumping reconfiguration graphs** require separate enumeration and a hole-exchange argument. They are not asserted in the inspected source. An undiscovered equivalent result in reconfiguration literature remains possible.

## Limitations

The theorem is restricted to crown graphs and to \(2\le k\le n-1\). Reconfiguration refers exclusively to minimum-cardinality feasible sets under single-vertex replacement; allowing intermediate supersets or token slides changes the problem. The connectivity guarantee for the selected backbone does not assert that domination survives deleting selected vertices. This work has not undergone independent scientific audit. Exhaustive computations cover only finite orders; no priority claim beyond the documented searches is made.

## References

1. D. Lokshtanov, A. E. Mouawad, F. Panolan, S. Siebertz, *On the Parameterized Complexity of Reconfiguration of Connected Dominating Sets*, arXiv:1910.00581v1 (2019-10-01), https://arxiv.org/abs/1910.00581.
2. N. Bousquet, A. E. Mouawad, N. Nishimura, S. Siebertz, *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, arXiv:2204.10526v1 (2022-04-22), https://arxiv.org/abs/2204.10526.
3. *Binomial edge ideals of crown graphs*, arXiv:2507.03889v2 (2025), https://arxiv.org/abs/2507.03889.
