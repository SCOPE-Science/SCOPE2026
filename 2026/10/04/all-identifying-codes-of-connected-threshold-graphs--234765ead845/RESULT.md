# All identifying codes of connected threshold graphs
## Finding
Let \(G\) be a finite connected threshold graph with canonical creation string
\[
0^{a_1}1^{b_1}0^{a_2}1^{b_2}\cdots 0^{a_k}1^{b_k},
\]
where all block sizes are positive and the final block is a \(1\)-block. A later \(1\)-vertex is adjacent to every earlier vertex, while a later \(0\)-vertex is adjacent to no earlier vertex.

The graph admits an identifying code if and only if
\[
a_1\ge 2\qquad\text{and}\qquad b_1=b_2=\cdots=b_k=1.
\]
Assume these conditions, write \(Z_i\) for the \(i\)-th \(0\)-block, put \(|Z_i|=a_i\), write \(d_i\) for the unique vertex of the \(i\)-th \(1\)-block, and let \(N=|V(G)|=k+\sum_i a_i\). Define
\[
E=\bigl(\{1\}\text{ if }a_1\ge3\bigr)\cup\{i:2\le i\le k,\ a_i\ge2\}.
\]
For a code candidate \(C\), let \(R(C)=\{i:|Z_i\setminus C|=1\}\). Then \(C\) is identifying exactly when:

1. every \(0\)-block omits at most one vertex and \(R(C)\subseteq E\); and
2. if \(R(C)=\{r_1<\cdots<r_t\}\ne\varnothing\), then \(C\cap\{d_{r_s},\ldots,d_{r_{s+1}-1}\}\ne\varnothing\) for \(1\le s<t\), and \(C\cap\{d_{r_t},\ldots,d_k\}\ne\varnothing\).

Hence the identifying-code polynomial \(I_G(x)=\sum_C x^{|C|}\), summed over all identifying codes, is
\[
\begin{aligned}
I_G(x)=&\;x^{N-k}(1+x)^k\\
&+\sum_{\varnothing\ne R=\{r_1<\cdots<r_t\}\subseteq E}
\left(\prod_{s=1}^t a_{r_s}\right)x^{N-k-t}(1+x)^{r_1-1}\\
&\quad\cdot\left(\prod_{s=1}^{t-1}\bigl((1+x)^{r_{s+1}-r_s}-1\bigr)\right)
\bigl((1+x)^{k-r_t+1}-1\bigr).
\end{aligned}
\]
In particular,
\[
\gamma_{\mathrm{ID}}(G)=N-k=\sum_{i=1}^k a_i.
\]
The number of minimum identifying codes is
\[
1+\sum_{\varnothing\ne R=\{r_1<\cdots<r_t\}\subseteq E}
\left(\prod_{s=1}^t a_{r_s}\right)
\left(\prod_{s=1}^{t-1}(r_{s+1}-r_s)\right)(k-r_t+1).
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. An identifying code is a vertex set \(C\) such that every closed-neighborhood trace \(N[v]\cap C\) is nonempty and all these traces are pairwise distinct. The theorem is stated for the canonical alternating block representation of a connected threshold graph; it includes the one-block stars but does not claim results for arbitrary split graphs.

## Proof
For \(z\in Z_i\),
\[
N[z]=\{z\}\cup\{d_i,d_{i+1},\ldots,d_k\},
\]
while
\[
N[d_i]=\{d_1,\ldots,d_k\}\cup Z_1\cup\cdots\cup Z_i.
\]
If some \(1\)-block has size at least two, its vertices have equal closed neighborhoods, so no identifying code exists. If every \(1\)-block is a singleton but \(a_1=1\), the first \(0\)-vertex and \(d_1\) have equal closed neighborhoods. Conversely, if all \(1\)-blocks are singletons and \(a_1\ge2\), the whole vertex set is already separating, so the graph is identifiable.

Assume now that the graph is identifiable. Two vertices inside one \(Z_i\) have the same open neighborhood, so at most one of them can be omitted from an identifying code. For \(i\ge2\), omitting the unique vertex of a singleton \(Z_i\) would make \(d_{i-1}\) and \(d_i\) have the same code trace; hence such an omission is impossible. If \(a_1=2\), omitting one vertex of \(Z_1\) makes the remaining selected vertex of \(Z_1\) and \(d_1\) have the same trace, so block \(1\) is omittable only when \(a_1\ge3\). These are exactly the restrictions \(R(C)\subseteq E\).

Let omitted vertices lie in blocks \(r_1<\cdots<r_t\). Two omitted \(0\)-vertices from blocks \(r_s<r_{s+1}\) have traces that differ exactly when at least one selected \(d_j\) has \(r_s\le j<r_{s+1}\). The last omitted \(0\)-vertex is dominated exactly when at least one selected \(d_j\) has \(r_t\le j\le k\). Thus the stated interval-hitting conditions are necessary.

They are also sufficient. Distinct selected \(0\)-vertices are separated by their own membership in the code. An omitted \(0\)-vertex is separated from every selected \(0\)-vertex for the same reason, and omitted \(0\)-vertices in different blocks are separated by the required selected \(d_j\). Consecutive \(d_{i-1},d_i\) are separated by a selected vertex from \(Z_i\): every \(Z_i\) with \(i\ge2\) contains a selected vertex under the eligibility conditions, so all \(d_i\) are pairwise separated. Finally every \(d_i\) sees a selected vertex in \(Z_1\), while a \(0\)-vertex outside \(Z_1\) sees no vertex of \(Z_1\); the only possible \(Z_1\)-versus-\(d_i\) collision was the excluded case \(a_1=2\) with one omitted \(Z_1\)-vertex. Hence all traces are nonempty and pairwise distinct.

For fixed nonempty \(R=\{r_1<\cdots<r_t\}\), there are \(\prod_s a_{r_s}\) choices of the omitted \(0\)-vertices. The vertices \(d_1,\ldots,d_{r_1-1}\) are unrestricted, while the selected \(d\)-set must hit each of the disjoint intervals
\[
[r_1,r_2-1],\ldots,[r_{t-1},r_t-1],[r_t,k].
\]
Their ordinary generating functions are respectively \((1+x)^{r_1-1}\) and \((1+x)^\ell-1\) for an interval of length \(\ell\). Multiplying these factors and the forced selected \(0\)-vertices gives the displayed polynomial. The empty omission set contributes \(x^{N-k}(1+x)^k\).

For a nonempty omission set of size \(t\), the \(t\) disjoint required intervals force at least \(t\) selected \(d\)-vertices, so every code has size at least \(N-k\). Taking all \(0\)-vertices and no \(d\)-vertices attains this bound. Minimum codes arise by choosing exactly one \(d\)-vertex in each required interval and none before \(r_1\), which gives the final counting formula.

## Verification
The accompanying checker independently constructs every canonical connected threshold graph of orders \(2\) through \(10\), enumerates every vertex subset, tests the identifying-code definition directly from closed neighborhoods, and compares the resulting coefficient vector with the theorem. It checks \(511\) creation strings and \(349524\) subsets in total. This finite experiment corroborates the formulas and boundary cases but is not used as an infinite proof.

## Relationship to prior work
Identifying codes are a standard separating-dominating notion. Foucaud's 2015 restricted-class complexity paper shows that Minimum Identifying Code remains hard on split graphs, the broader class containing threshold graphs. Argiroffo, Bianchi, and Wagler subsequently studied exact identifying-code polyhedra and minimum values for several structured split-graph families, illustrating the value of exact subclass structure. The statement above is different: it gives an existence criterion, a complete classification of all identifying codes, and the full cardinality generating polynomial for every connected threshold graph.

No threshold-graph theorem matching this statement was found in the semantic database searches or web searches recorded in the review. The closest published split-graph papers concern hardness or other structured subclasses rather than the canonical threshold-block family. This negative search is not itself a novelty proof; residual indexing risk is retained below.

## Limitations
The result is restricted to connected threshold graphs and ordinary closed-neighborhood identifying codes. It does not cover locating-dominating sets, open identifying codes, disconnected threshold graphs, or arbitrary split graphs. The literature comparison is limited by indexing and by the fact that not every relevant split-graph article exposed full searchable text. The exact polynomial is proved structurally; the finite exhaustive checker only tests small orders.

## References
F. Foucaud, “Decision and approximation complexity for identifying codes and locating-dominating sets in restricted graph classes,” Journal of Discrete Algorithms 31 (2015), 48–68, DOI: 10.1016/j.jda.2014.08.004.

G. Argiroffo, S. Bianchi, and A. Wagler, “Progress on the description of identifying code polyhedra for some families of split graphs,” Discrete Optimization 22 (2016), 225–240, DOI: 10.1016/j.disopt.2016.06.002.

F. Foucaud and G. Perarnau, “Bounds for Identifying Codes in Terms of Degree Parameters,” Electronic Journal of Combinatorics 19(1) (2012), P32, DOI: 10.37236/2036.
