# Exact zero-forcing polynomial of sunlet graphs via alternating-path obstruction

## Finding
For every integer \(n\ge3\), form the sunlet graph \(S_n=C_n\circ K_1\) with cycle vertices \(v_i\), leaves \(\ell_i\), and indices modulo \(n\). Its zero-forcing polynomial, counting all initially blue vertex sets by cardinality, is
\[
\boxed{\mathcal Z(S_n;z)=[u^n]\left(\frac{a u+2b u^2-3c u^3}{1-a u-b u^2+c u^3}-\frac{4z(1+z)u^2}{1-z(1+z)u^2}\right),}
\]
where \(a=z(z+2)\), \(b=2z(z+1)\), and \(c=z^2(1+z)^2\). Thus one fixed rational bivariate series gives every coefficient, for every order.

There is also an all-set characterization. Given initially blue set \(S\), define disjoint index sets \(B=\{i:\ell_i\in S\}\) and \(E=\{i:\ell_i\notin S,\ v_i\notin S\}\). Build \(H_S\) on \(B\cup E\), retaining the cyclic adjacency \(i\sim i+1\) exactly when one endpoint lies in \(B\) and the other in \(E\). Then
\[
\boxed{S\text{ is zero forcing}\quad\Longleftrightarrow\quad
\text{every component of }H_S\text{ containing an }E\text{-vertex has a degree-one }B\text{-vertex}.}
\]
Here degrees are within \(H_S\); isolated vertices in \(E\) fail the criterion. As a consequence, the known optimum \(Z(S_n)=\lceil n/2\rceil\) has the following exact number of attaining sets:
\[
\boxed{[z^{\lceil n/2\rceil}]\mathcal Z(S_n;z)=
\begin{cases}
4(2^{n/2-1}-1),&n\ge4\text{ even},\\
3n\,2^{(n-3)/2},&n\ge3\text{ odd}.
\end{cases}}
\]
Only the all-set characterization, complete polynomial, and minimum-set multiplicities are claimed as the present contribution; the minimum value itself was known.

## Assumptions and scope
Graphs are finite, simple, undirected. All initial subsets \(S\subseteq V(S_n)\) are counted with labeled cycle positions and labeled leaves. A blue vertex having exactly one white neighbor forces that neighbor blue; forces continue until no more are possible. The zero-forcing polynomial is \(\mathcal Z(S_n;z)=\sum_{S\text{ zero forcing}}z^{|S|}\). The ring of coefficients is \(\mathbb Z[z]\). All identities are for integers \(n\ge3\), including the triangle-based sunlet; no assertion is made for an undefined two-cycle.

## Proof
**Reduction to a static obstruction.** Whenever \(\ell_i\) is initially blue, it either has an already blue neighbor or immediately forces \(v_i\). Thus all centers indexed by \(B\) can first be regarded as blue. Every center with an initially white leaf cannot force a white *cycle* neighbor at any time: until its leaf becomes blue it has that leaf as a second white neighbor, and its leaf can be forced by the center only after *both* its cycle neighbors are blue. Hence only a center indexed by \(B\) can force another cycle vertex; an initially white center in \(E\), once forced, cannot propagate along the cycle. Initially blue centers with initially white leaves are inert for this purpose. Consequently center-forcing is exactly the deletion of vertices of \(E\) by adjacent vertices of \(B\) that currently have just one \(E\)-neighbor.

The graph \(H_S\) has maximum degree two. Every component is a path, an isolated vertex, or, only in a fully alternating even cycle, a cycle. In a component containing \(E\), a degree-one \(B\)-endpoint forces the adjacent \(E\)-vertex; successively deleting that \(E\)-vertex exposes another \(B\)-endpoint if an \(E\)-vertex remains. This removes every \(E\)-vertex of such a path. Conversely, any component containing \(E\) but lacking a degree-one \(B\)-vertex has no available first force within it and will never change, since forcing in another component cannot change its degrees. Once all centers are blue, each white leaf is forced by its center. This proves the boxed criterion.

**Exact transfer enumeration.** Classify each index by three letters: \(B\) when its leaf is initially blue (its center is arbitrary), \(C\) when its center alone is blue, and \(E\) when both vertices are initially white. These letters have respective weights \(q=z+z^2\), \(z\), and \(1\). The edges of \(H_S\) connect precisely adjacent unlike letters \(B,E\). An alternating-run component containing \(E\) is permitted if and only if at least one endpoint is \(B\). Consider five scanning states \(\mathrm C,\mathrm{GB},\mathrm{GE},\mathrm{UE},\mathrm{UB}\). The \(\mathrm G\)-states describe a run whose starting endpoint is \(B\), and \(\mathrm U\)-states a run whose starting endpoint is \(E\). A run starting at \(E\) may end only at \(B\); a run starting at \(B\) may end at either letter. With rows and columns in the displayed state order, the weighted transition matrix is
\[
T(z)=\begin{pmatrix}
z&q&0&1&0\\
z&q&1&0&0\\
z&q&0&1&0\\
0&0&0&0&q\\
z&q&0&1&0
\end{pmatrix}.
\]
A cyclic word with at least one non-\(B E\) adjacency has a unique consistent state labeling, determined by the beginnings of its maximal alternating runs; such a word contributes to \(\operatorname{tr}(T(z)^n)\) precisely when all of its \(E\)-containing runs are allowed. A fully alternating even word, by contrast, is *not* zero forcing, but is counted twice by the trace, once with the fictitious \(\mathrm G\)-cycle and once with the fictitious \(\mathrm U\)-cycle. There are exactly two such words, each weighted \(q^{n/2}\). Therefore
\[
\mathcal Z(S_n;z)=\operatorname{tr}(T(z)^n)-\begin{cases}4q^{n/2},&n\text{ even},\\0,&n\text{ odd}.\end{cases}
\]
Direct determinant calculation gives
\[
\det(I-uT(z))=1-au-bu^2+cu^3.
\]
The formal identity \(\sum_{n\ge1}\operatorname{tr}(T^n)u^n=-u\frac{d}{du}\log\det(I-uT)\) yields the rational expression in the finding. The even-cycle correction is the coefficient of \(4q u^2/(1-q u^2)\).

**Leading nonzero coefficient.** Put \(z=t^2\), \(u=v/t\) in the rational expression, treated as formal series in \(t\) with coefficients in \(\mathbb Q[[v]]\). Its expansion begins
\[
\frac{4v^2}{1-2v^2}-\frac{4v^2}{1-v^2}
+t\frac{2v+v^3+2v^5}{(1-2v^2)^2}+O(t^2).
\]
No coefficient \([z^j]\mathcal Z(S_n;z)\) can occur with \(2j<n\). The constant term in \(t\) has only even powers of \(v\), so for odd \(n\) the bound increases to \(2j\ge n+1\). For \(n=2k\ge4\), extraction of \(v^{2k}\) from the constant term gives \(4(2^{k-1}-1)>0\). For \(n=2k+1\ge3\), extraction of \(v^{2k+1}\) from the coefficient of \(t\) gives \(3(2k+1)2^{k-1}>0\). Both the optimum and the multiplicity formulas follow.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It independently constructs the sunlet adjacency masks, simulates the forcing process, checks the static component criterion, constructs weighted closed walks in the five-state matrix, and computes the polynomial from the cubic recurrence. It exhausts all \(2^{2n}\) initial subsets for each \(3\le n\le10\), and compares exact coefficient tables. It also checks the leading coefficient through \(n=40\). On the actual included source the check completed with `VERIFY_OK graph_orders=3..10 exhaustive_initial_sets=1398080 static_and_matrix_and_recurrence=passed minimum_counts=3..40`. These computations corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
The ordinary zero-forcing rule and its linear-algebra motivation date to AIM Minimum Rank – Special Graphs Work Group (first publicly available online 26 November 2007). Row studied zero-forcing numbers for graphs with cut vertices and unicyclic graphs; existing sunlet minimum-number calculations are also reported in later work on connected forcing. Boyer et al. introduced the zero-forcing polynomial and evaluated it for cycles, wheels, and several other families. Those prior results establish the framework and previously known minima but do not supply the stated alternating-path all-set criterion, fixed rational sunlet enumerator, or the parity-dependent number of minimum sets in the inspected relevant sections. A differently named or separately published equivalent enumeration is not excluded by a literature search alone.

## Limitations
The theorem applies to one pendant leaf at every vertex of a simple cycle, not to variable numbers of leaves, arbitrary unicyclic graphs, or other forcing rules. The inaccessible complete text of Row's 2012 cutvertex article and potential enumerations indexed under non-sunlet terminology leave a residual priority risk; this does not alter the self-contained proof. Finite checks have been performed only through the stated bounds. No independent mathematical audit has been performed.

## References
1. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, available online 26 November 2007, DOI `10.1016/j.laa.2007.10.009`.
2. D. D. Row, *A technique for computing the zero forcing number of a graph with a cutvertex*, Linear Algebra and its Applications 436 (2012), 4423–4432, DOI `10.1016/j.laa.2011.05.012`.
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv `1801.08910v1` (26 January 2018); Discrete Applied Mathematics 258 (2019), 35–48.
