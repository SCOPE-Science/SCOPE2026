# Closed-neighborhood balance collapses complete multipartite graphs to cliques
## Finding
Let \(k\ge2\) and let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\). Then \(G\) admits a closed neighborhood-balanced \(k\)-coloring if and only if
\[
n_1=\cdots=n_r=1
\quad\text{and}\quad
k\mid r.
\]
Equivalently, among connected complete multipartite graphs, the closed neighborhood-balanced \(k\)-colorable graphs are exactly the complete graphs \(K_r\) with \(k\mid r\).

When the colors are labeled by \([k]\), the number of such colorings is exactly
\[
\frac{r!}{((r/k)!)^k}.
\]
Thus every non-complete connected complete multipartite graph fails closed neighborhood balance for every \(k\ge2\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A closed neighborhood-balanced \(k\)-coloring uses exactly \(k\) colors and requires that, for every vertex, its closed neighborhood contain the same number of vertices of each color. The multipartite parts are nonempty, and \(r\ge2\) makes the graph connected.

## Proof
Write the partite sets as \(P_1,\ldots,P_r\), with \(|P_i|=n_i\), and let \(T_j\) be the total number of vertices of color \(j\). Vertices in one part have identical open neighborhoods. A standard necessary observation for closed neighborhood-balanced coloring therefore forces each \(P_i\) to be monochromatic.

Suppose \(P_i\) has color \(c_i\). For \(v\in P_i\),
\[
N[v]=\{v\}\cup\bigl(V(G)\setminus P_i\bigr).
\]
If the common number of vertices of each color in \(N[v]\) is \(q_i\), then
\[
q_i=\frac{|V(G)|-n_i+1}{k},
\]
and the balance equations are
\[
T_j=q_i\quad(j\ne c_i),
\qquad
T_{c_i}-n_i+1=q_i.
\]
Because exactly \(k\ge2\) colors are used and every part is monochromatic, there are two parts \(P_i,P_h\) with distinct colors.

First suppose \(k\ge3\). Choose a third color \(e\) different from both part colors. Since that color is used globally, the displayed equations give \(T_e=q_i=q_h\), hence \(n_i=n_h\). Looking at the color of \(P_h\), the equation for \(P_i\) gives \(T_{c_h}=q_i\), whereas the equation for \(P_h\) gives \(T_{c_h}=q_h+n_h-1\). Thus \(n_h=1\), and so \(n_i=1\).

If \(k=2\), call the two colors red and blue. For a red part \(P_i\) and a blue part \(P_h\), the same equations give
\[
T_R-T_B=n_i-1=1-n_h,
\]
so \(n_i+n_h=2\), and again both sizes are \(1\).

Now take any other part \(P_\ell\). If its color differs from that of a singleton part already found, repeat the preceding distinct-color argument to get \(n_\ell=1\). If it has the same color, compare the equations for the two same-colored parts using any other color: their \(q\)-values are equal, so their part sizes are equal, again giving \(n_\ell=1\). Hence every part is a singleton and \(G\cong K_r\).

For \(K_r\), every closed neighborhood is the whole vertex set. Balance is therefore equivalent to every color occurring exactly \(r/k\) times. This is possible exactly when \(k\mid r\), and the labeled colorings are the ordered equal-size partitions of \(r\) vertices into \(k\) color classes, counted by \(r!/((r/k)!)^k\).

## Verification
The accompanying `verify.py` independently constructs complete multipartite graphs, enumerates every surjective labeled coloring for all sorted part-size profiles with two through five parts, total order at most \(8\), and \(2\le k\le4\), and tests the closed-neighborhood balance condition directly. It compares the exhaustive count to the theorem and to the multinomial formula in the complete-graph cases.

Its replay is:

`ALL CHECKS PASSED; profiles=30; assignments=583627; valid_colorings=38; max_order=8; k_range=2..4`

The finite enumeration is a stress test only; the universal statement is proved above.

## Relationship to prior work
Almeida, Pawar, Gupta, and Singh introduced the \(k\)-color version of closed neighborhood-balanced coloring. Their paper proves that vertices with the same open neighborhood must receive the same color and states that \(K_n\) is closed neighborhood-balanced \(k\)-colorable exactly when \(k\mid n\). Targeted full-text inspection found no occurrence of “multipartite,” and the paper does not state the classification above.

The earlier two-color paper of Collins et al. explicitly observes that a complete bipartite graph \(K_{m,n}\) is closed neighborhood-balanced only for \(K_{1,1}\). It does not state a complete-multipartite classification. The present theorem simultaneously extends that obstruction from two parts to arbitrarily many parts and from two colors to every \(k\ge2\), and adds the exact labeled-coloring count.

Targeted database searches for the invariant together with complete-multipartite, complete-bipartite, and neighborhood-twin terminology located no statement implying the all-\(k\), all-multipartite theorem.

## Limitations
The result concerns complete multipartite graphs only. It does not characterize arbitrary graphs, and the proof relies essentially on the equal open neighborhoods within each part. The literature comparison cannot exclude an unindexed equivalent formulation, although the defining \(k\)-color generalization is recent and both the initiating full text and the earlier two-color full text were inspected for the closest family statements.

## References
1. M. Almeida, R. Pawar, S. Gupta, T. Singh, “Closed Neighborhood Balanced \(k\)-Coloring of Graphs,” arXiv:2510.16666v1, 18 October 2025.
2. K. L. Collins et al., “Closed Neighborhood Balanced Coloring of Graphs,” Graphs and Combinatorics 41 (2025), Article 88; arXiv:2412.02800.
