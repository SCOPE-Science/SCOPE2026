# Connected forcing enumerators of unequal clique windmills

## Finding

Let \(r\ge 2\), let \(m_1,\ldots,m_r\ge 2\) be integers, and let
\[
G=K_1\vee(K_{m_1}\sqcup\cdots\sqcup K_{m_r}).
\]
Its universal vertex is the **hub**; its \(r\) cliques of non-hub vertices are the **blades**, with sizes \(m_i\). For every integer \(k\ge1\), initially color a nonempty vertex set \(S\) black. A black vertex with between one and \(k\) white neighbors can simultaneously color all those neighbors black. Call \(S\) *connected \(k\)-forcing* when \(G[S]\) is connected and this rule eventually colors every vertex black. Write
\[
F_{G,k}(z)=\sum_{\substack{S\subseteq V(G)\\ S\text{ connected }k\text{-forcing}}}z^{|S|}.
\]
Define \(M=\sum_{i=1}^r m_i\) and
\[
B_i(z)=\sum_{s=\max\{1,m_i-k\}}^{m_i}\binom{m_i}{s}z^s.
\]
Then the **complete connected forcing-set polynomial** for every blade-size profile is
\[
\boxed{F_{G,k}(z)=
z\!\sum_{\substack{J\subseteq\{1,\ldots,r\}\\ \sum_{j\in J}m_j\le k}}
\ \prod_{i\notin J}B_i(z)
+\sum_{h=1}^{r}\mathbf{1}_{\{M-m_h\le k\}}
\sum_{s=\max\{1,m_h-k+1\}}^{m_h}\binom{m_h}{s}z^s.}
\]
An empty product is \(1\). Every coefficient counts distinct labeled vertex subsets, not forcing sequences.

For the uniform case \(m_1=\cdots=m_r=m\ge2\), let \(B(z)=(1+z)^m-1\) and \(q=\min\{r,\lfloor k/m\rfloor\}\). The polynomial simplifies to
\[
F_{G,k}(z)=
\begin{cases}
z\Big(\displaystyle\sum_{s=m-k}^{m}\binom ms z^s\Big)^r,&1\le k<m,\\[2mm]
z\displaystyle\sum_{j=0}^{q}\binom rj B(z)^{r-j}
+r\,\mathbf1_{\{k\ge(r-1)m\}}B(z),&k\ge m.
\end{cases}
\]
Consequently, denoting its least positive exponent by \(c_k\) and that coefficient by \(a_k\),
\[
\boxed{(c_k,a_k)=
\begin{cases}
\big(1+r(m-k),\binom mk^r\big),&1\le k<m,\\
\big(1+r-\lfloor k/m\rfloor,\binom r{\lfloor k/m\rfloor}m^{r-\lfloor k/m\rfloor}\big),&m\le k<(r-1)m,\\
(1,rm),&(r-1)m\le k<rm,\\
(1,rm+1),&k\ge rm.
\end{cases}}
\]
The second range is empty when \(r=2\). At \(k=(r-1)m\), the connected forcing number drops from \(3\) to \(1\), and the optimum changes from hub-containing sets to individual peripheral vertices. At \(k=rm\), the hub itself becomes an additional singleton solution. These jumps and all counts hold for every \(r,m\ge2\).

## Assumptions and scope

All graphs are finite, simple and undirected. The joined cliques are disjoint before adjoining the hub. The integer \(k\) is positive and is not required to be smaller than the maximum degree. Every connected starting set is nonempty. A vertex with zero white neighbors changes nothing; only nonzero forcing steps matter. As usual for monotone graph forcing, simultaneous application of every available legal step and any sufficient sequence give the same eventual colored closure: adding black vertices cannot invalidate a subsequent force by making its white-neighbor count larger.

## Proof

**Hub initially black.** For blade \(i\), put \(s_i=|S\cap V(K_{m_i})|\) and \(w_i=m_i-s_i\). A black peripheral vertex in a nonempty blade sees exactly \(w_i\) white neighbors in its own blade (the hub is already black). It can therefore color the whole blade when \(w_i\le k\). If \(s_i>0\) but \(w_i>k\), no black vertex in that blade can force; the hub also has at least \(w_i>k\) white neighbors and cannot force. No vertex outside that blade, apart from the hub, is adjacent to its white vertices. Thus the process cannot finish. Therefore each initially occupied blade requires \(s_i\ge\max\{1,m_i-k\}\).

Let \(J\) be the set of initially empty blades. Initially and until the hub forces them, no peripheral vertex from another blade can force a vertex of an empty blade. Their total white mass is \(\sum_{j\in J}m_j\). If it exceeds \(k\), the hub always has more than \(k\) white neighbors, so the process cannot finish. Conversely, when that mass is at most \(k\) and every occupied blade satisfies its local threshold, one can first force all occupied blades via a selected peripheral vertex in each, then the hub forces every remaining vertex in the empty blades. Hence the two conditions are both necessary and sufficient. For a fixed empty-blade set \(J\), the generating polynomial for the hub and the other blades is \(z\prod_{i\notin J}B_i(z)\). Summation gives the first displayed term, without overlaps because \(J\) is uniquely determined by \(S\).

**Hub initially white.** Connectivity of the nonempty black set forces all initially selected vertices to lie in a single blade \(h\). Write \(s=|S|\). Every initially selected vertex in that blade has exactly \(m_h-s+1\) white neighbors: its unselected blade-mates and the white hub. Thus a first force is possible if and only if \(m_h-s+1\le k\). That force colors the whole blade and the hub. All other blades are still entirely white; only the hub can act on them, and it can complete the process precisely when \(M-m_h\le k\). If this final inequality fails, no forces from black peripheral vertices can reach the other blades. These two inequalities yield the second displayed term. Distinct blade indices \(h\) produce disjoint configurations.

**Uniform case and minimum coefficients.** If \(k<m\), every empty blade has size \(m>k\), and a hub-free set cannot reach \((r-1)m\) remaining vertices. Therefore all blades must be occupied, each with \(m-k\) or more seeds. This gives the first uniform polynomial and its least term \(z^{1+r(m-k)}\binom mk^r\).

If \(k\ge m\), each occupied blade needs only one seed; exactly \(j\le\lfloor k/m\rfloor\) blades may be empty, contributing \(z\binom rj B(z)^{r-j}\). A hub-free connected set works exactly when \(k\ge(r-1)m\); then any nonempty subset of its single blade works, contributing \(rB(z)\). Before that threshold the largest allowable \(j\) minimizes the hub-containing set size; there are \(\binom rq m^{r-q}\) choices of minimum sets. From the threshold onward every peripheral singleton works, and at \(k=rm\) the hub singleton works too. Immediately below \(k=(r-1)m\), the minimum size is three: for \(r=2\) the range \(k<m\) gives three, and for \(r\ge3\) the range \(m\le k<(r-1)m\) has \(\lfloor k/m\rfloor=r-2\). This completes every boundary case.

## Verification

The accompanying self-contained \(\texttt{verify.py}\) constructs the original adjacency lists and tests connectedness and monotone forcing closure on every subset; it independently computes the classification and polynomial convolution. Execution with the Python standard library confirmed all \(671\) admissible parameter tuples drawn from \(r\in\{2,3,4\}\), \(m_i\in\{2,3,4\}\), total blade order at most \(11\), and \(1\le k\le M+1\). There were \(1{,}458{,}592\) subset-level predicate comparisons; polynomial coefficients also agreed. The verifier can be run using \(\texttt{python verify.py}\) from the extracted package. Finite tests are auxiliary to the general proof.

## Relationship to prior work

Premodkmuar, Dominic and Chacko (2020), Proposition 7, establish only the **minimum connected \(k\)-forcing cardinality** of friendship graphs, the \(m=2\) subfamily, with a parity-dependent formula. The present general formula specializes to their scalar value, which is not claimed as new. It additionally counts every connected forcing set of every cardinality, all minimum-set multiplicities, and every heterogeneous clique bouquet. Their inspected Proposition 7 and related sections contain neither this polynomial nor the heterogeneous classification.

Their 2019 work concerns scalar \(k\)-forcing numbers of other graphs and splitting graphs; its inspected material does not enumerate connected starting sets in clique bouquets. Amos, Caro, Davila and Pepper (2014) provide general \(k\)-forcing bounds, not a distribution for these graphs.

Indexed results on unrestricted zero-forcing polynomials of friendship graphs concern \(k=1\) without the initial-connectivity restriction. An indexed result on all \(k\)-forcing sets of complete multipartite graphs concerns a different graph family: in the present bouquet, peripheral vertices from different blades are nonadjacent, whereas a multipartite graph joins different parts. Neither result implies the stated heterogeneous connected polynomial. Other indexed windmill enumerators concern dissociation or general-position sets with different predicates.

## Limitations

The result is limited to clique bouquets with one common hub, blades of order at least two, and the specified \(k\)-forcing rule. It does not classify connected forcing sets of arbitrary block graphs, nor optimize forcing propagation time. No external independent proof audit has been performed. The inspected literature and indexed searches do not prove universal publication priority; unindexed or differently described equivalent work could exist.

## References

1. K. P. Premodkmuar, C. Dominic, B. Chacko, “Connected k-forcing sets of graphs and splitting graphs,” *Journal of Mathematics and Computer Science* **10** (2020), 656–680, Proposition 7; DOI: https://doi.org/10.28919/jmcs/4446 (published online 2020-03-06). Full text: https://scik.org/index.php/jmcs/article/download/4446/2155.
2. K. P. Premodkmuar, C. Dominic, B. Chacko, “K-Forcing Number of Some Graphs and Their Splitting Graphs,” *International Journal of Scientific Research in Mathematical and Statistical Sciences* **6** (2019), 121–127; DOI: https://doi.org/10.26438/ijsrmss/v6i3.121127.
3. D. Amos, Y. Caro, R. Davila, R. Pepper, “Upper bounds on the k-forcing number of a graph,” arXiv:1401.6206 (2014), https://arxiv.org/abs/1401.6206.
