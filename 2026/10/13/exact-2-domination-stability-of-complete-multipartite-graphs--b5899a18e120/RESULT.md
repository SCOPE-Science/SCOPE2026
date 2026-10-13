# Exact 2-domination stability of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph, with \(r\ge2\). A set \(D\subseteq V(G)\) is 2-dominating when every vertex outside \(D\) has at least two neighbors in \(D\). Write \(\gamma_2(G)\) for the minimum size of such a set, and
\[
\operatorname{st}_{\gamma_2}(G)=\min\{|X|:\gamma_2(G-X)\ne\gamma_2(G)\}.
\]

For two parts, write \(1\le a\le b\). Then
\[
\gamma_2(K_{a,b})=
\begin{cases}
2,&a=1,\ b\le2,\\
b,&a=1,\ b\ge3,\\
2,&a=2,\\
3,&a=3,\\
4,&a\ge4,
\end{cases}
\]
and
\[
\operatorname{st}_{\gamma_2}(K_{a,b})=
\begin{cases}
2,&(a,b)=(1,2),\\
3,&(a,b)=(2,2),\\
a-3,&a\ge4,\\
1,&\text{otherwise.}
\end{cases}
\]

For \(r\ge3\), put
\[
u=|\{i:n_i=1\}|,\qquad v=|\{i:n_i=2\}|,\qquad w=|\{i:n_i\ge3\}|,\qquad N=\sum_i n_i.
\]
Then
\[
\gamma_2(G)=
\begin{cases}
2,&v\ge1\text{ or }u\ge2,\\
3,&v=0\text{ and }u\le1.
\end{cases}
\]
If \(\gamma_2(G)=2\), then
\[
\operatorname{st}_{\gamma_2}(G)=
\begin{cases}
N-1,&w=0,\\
u+2v-1,&w\ge1.
\end{cases}
\]
If \(\gamma_2(G)=3\), let \(m=\min\{n_i:n_i\ge3\}\). Then
\[
\operatorname{st}_{\gamma_2}(G)=
\begin{cases}
1,&r=3\text{ and }u=1,\\
m-2,&\text{otherwise.}
\end{cases}
\]

## Assumptions and scope
Graphs are finite and simple. The original graph is connected because it has at least two nonempty partite classes. After deletion, empty partite classes are discarded; a one-part residual graph is edgeless, and the standard 2-domination definition still applies. Stability is vertex-deletion stability, not edge bondage and not 2-rainbow domination stability.

## Proof
For a vertex set \(D\), write \(d_i=|D\cap V_i|\) and \(d=|D|\). A vertex in \(V_i\setminus D\) is adjacent to exactly \(d-d_i\) vertices of \(D\). Hence
\[
D\text{ is 2-dominating}\quad\Longleftrightarrow\quad d-d_i\ge2\text{ for every }i\text{ with }d_i<n_i. \tag{1}
\]
This occupancy criterion is the only graph-specific ingredient.

Suppose first that \(r\ge3\). A 2-set can satisfy (1) only if every occupied part is completely selected. Thus a 2-dominating 2-set exists exactly when one part has size \(2\), or two parts are singletons. If neither occurs, choose one vertex from each of three distinct parts. Every incomplete occupied part then contributes one selected vertex and sees the other two selected vertices, while every unoccupied part sees all three. Thus \(\gamma_2(G)=3\).

Assume next that \(r\ge3\) and \(\gamma_2(G)=2\). If \(w=0\), every residual graph obtained by deleting at most \(N-2\) vertices has at least two vertices and all positive part sizes are \(1\) or \(2\). It therefore still has a 2-dominating 2-set: either a whole 2-part or two singleton parts. Deleting \(N-1\) vertices leaves one vertex, whose 2-domination number is \(1\). Hence the stability is \(N-1\).

Now let \(w\ge1\). To destroy every 2-dominating 2-set, all original 2-parts must cease to have size \(2\), and at most one singleton may survive. For each original singleton the choices cost \(0\) to keep it or \(1\) to delete it; for each original 2-part the choices cost \(1\) to turn it into a singleton or \(2\) to delete it. The cheapest way to leave no 2-part and at most one singleton costs exactly \(u+2v-1\): keep one old singleton when \(u>0\), or turn one old 2-part into the unique singleton when \(u=0\). Deletions in the large parts cannot reduce this necessary cost. Performing this cleanup while leaving every large part untouched produces a residual graph with 2-domination number at least \(3\). This proves \(\operatorname{st}_{\gamma_2}(G)=u+2v-1\).

Finally suppose \(r\ge3\) and \(\gamma_2(G)=3\). There are no 2-parts and at most one singleton. Deleting \(m-2\) vertices from a smallest large part creates a 2-part and lowers the 2-domination number to \(2\). With fewer than \(m-2\) deletions, no large part can fall below size \(3\). If there is no singleton, at least three parts therefore remain and (1) still gives value \(3\). If there is one singleton and \(r\ge4\), deleting it still leaves at least three large parts, again with value \(3\). The only cheaper transition is when \(r=3\) and the singleton is one entire part: deleting it costs \(1\), and the two remaining parts have size at least \(4\) whenever \(m>3\), so their 2-domination number is \(4\); when \(m=3\), the alternative deletion that creates a 2-part already costs \(1\). This proves the stated formula.

For \(r=2\), write the sizes as \(a\le b\). Criterion (1) gives the minimum directly. If \(a=1\), the larger part must be selected completely unless \(b\le2\); if \(a=2\), the smaller part itself is a 2-set; if \(a\ge3\), either one entire part is selected or both parts are incomplete, in which case at least two vertices must be selected from each shore. Hence the displayed formula for \(\gamma_2(K_{a,b})\). The stability cases follow by the same residual-size analysis: \(K_{1,2}\) needs two deletions before its value changes, \(K_{2,2}\) needs three, \(K_{2,b}\) with \(b\ge3\) changes after one deletion from the 2-part, \(K_{1,b}\) with \(b\ne2\) changes after one deletion, and for \(4\le a\le b\), exactly \(a-3\) deletions are needed to reduce one shore to size \(3\); fewer deletions leave both shores of size at least \(4\), so the value remains \(4\).

## Verification
The proof above is analytic and covers arbitrary part sizes. The accompanying `verify.py` independently enumerates part occupancies and every vertex-deletion profile for all complete multipartite profiles of order at most \(11\), then checks the closed formulas. It also checks every bipartite profile \(K_{a,b}\) with \(1\le a\le b\le20\). Its successful replay reports 183 multipartite profiles and 210 bipartite profiles. These finite checks corroborate boundary handling but are not used as an infinite proof.

## Relationship to prior work
Mehraban and Alikhani introduced \(\operatorname{st}_{\gamma_2}\) and computed it for several graph families. Their Proposition 2.7 includes complete and complete-bipartite graphs, but no general complete-multipartite classification. Under the definitions stated in that paper, its blanket value \(\operatorname{st}_{\gamma_2}(K_{m,n})=2\) for \(m,n\ge2\) does not agree with direct residual-size calculations: for example, deleting one vertex from the 2-vertex shore of \(K_{2,3}\) gives \(K_{1,3}\), changing \(\gamma_2\) from \(2\) to \(3\), while \(K_{2,2}\) requires three deletions before the value changes. The theorem above therefore supplies both a full multipartite classification and corrected bipartite boundary behavior.

Lu and Xu earlier obtained an exact formula for the general \(p\)-domination number of complete multipartite graphs. Their result covers the baseline values of \(\gamma_2\), but it does not study vertex-deletion stability. The present result uses the elementary occupancy form of the \(p=2\) condition to analyze every deletion profile.

## Limitations
The theorem is restricted to complete multipartite graphs and ordinary 2-domination. It does not address edge-deletion bondage, 2-rainbow domination, or stability of arbitrary graphs. Literature searches did not locate another exact complete-multipartite stability theorem, but poorly indexed equivalent work under different terminology remains a residual originality risk.

## References
1. M. Mehraban and S. Alikhani, “Stability of 2-Domination Number of a Graph,” arXiv:2507.18535v1, first public 2025-07-24; Mathematics Interdisciplinary Research 11 (2026), 113–124, DOI 10.22052/MIR.2025.257573.1540.
2. Y. Lu and J.-M. Xu, “The p-Domination Number of Complete Multipartite Graphs,” arXiv:1205.0102v1, first public 2012-05-01; Discrete Mathematics, Algorithms and Applications 6 (2014), 1450063, DOI 10.1142/S1793830914500633.
