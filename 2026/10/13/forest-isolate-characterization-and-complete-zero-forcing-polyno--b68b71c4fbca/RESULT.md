# Forest-isolate characterization and complete zero-forcing polynomial of triangular graphs

## Finding

For each integer \(n\ge 3\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, with \(N=\binom n2\) vertices identified with the unordered pairs from \([n]\). For \(S\subseteq V(T_n)\), define the white-edge graph \(F_S=([n],E(K_n)\setminus S)\); isolated vertices are retained. Then

\[
 S\text{ is an ordinary zero-forcing set of }T_n
 \quad\Longleftrightarrow\quad
 F_S\text{ is a forest having at least one isolated vertex.}
\]

Consequently, the **complete** ordinary zero-forcing polynomial \(\mathcal Z(T_n;z)=\sum_{S\text{ zero-forcing}}z^{|S|}\) satisfies

\[
 \mathcal Z(T_n;z)=z^{\binom n2}H_n(z^{-1}),\qquad
 \sum_{n\ge1}H_n(y)\frac{u^n}{n!}
 =(e^u-1)\exp\!\left(
 \sum_{j\ge2}\frac{j^{j-2}}{j!}y^{j-1}u^j
 \right).
\]

Here \(H_n(y)\) counts labeled spanning forests of \(K_n\) having at least one isolated vertex, by number of edges. All coefficients are determined explicitly by the above exponential generating function, or by the finite recurrence in the proof. In particular, the minimum cardinality and number of minimum sets are

\[
 Z(T_n)=\binom n2-n+2,
 \qquad
 \#\{S\subseteq V(T_n): |S|=Z(T_n),\ S\text{ zero-forcing}\}
 =n(n-1)^{n-3}.
\]

The **maximum size of a non-zero-forcing set** is
\[
 \binom n2-\min\!\left\{3,\left\lceil\frac n2\right\rceil\right\}.
\]
Thus the number of cardinalities occupied by both forcing and nonforcing sets is
\[
 \max\!\left\{0,n-1-\min\!\left(3,\left\lceil\frac n2\right\rceil\right)\right\};
\]
in particular it equals \(n-4\) for every \(n\ge6\). The minimum-number formula itself is already known and is not claimed as new.

## Assumptions and scope

Graphs are finite, undirected, simple, and vertex-labeled. In the **ordinary** zero-forcing rule, a black vertex with exactly one white neighbor may color that neighbor black. A set is zero-forcing when some finite sequence of legal forces blackens every vertex. The triangular graph has as vertices the edges of \(K_n\); two vertices are adjacent exactly when their corresponding edges share an endpoint. White edges of \(F_S\) correspond to vertices initially left white in \(T_n\). A spanning forest on \([n]\) includes all \(n\) vertices, including isolated ones. The theorem applies for all \(n\ge3\), all \(S\subseteq E(K_n)\), and all cardinality coefficients; it concerns neither skew nor positive-semidefinite zero forcing.

## Proof

**Forcing moves in terms of white edges.** At any step let \(F\) consist of the still-white edges of \(K_n\). A black vertex of \(T_n\) corresponds to some edge \(uv\notin E(F)\). Its number of white neighbors is exactly \(d_F(u)+d_F(v)\), since a white edge cannot equal \(uv\). Therefore a force is possible only when \(d_F(u)=1\) and \(d_F(v)=0\), or vice versa. Its target is the unique white edge incident with the degree-one endpoint. In particular every force deletes a leaf edge of \(F\), using an isolated vertex of \(F\) as the other endpoint of the black forcing edge.

**Necessity.** If \(F_S\) has no isolated vertex, every initially black vertex has either zero or at least two white neighbors, so no first force is possible unless there are no white edges; the latter case does have isolated vertices. If \(F_S\) contains a cycle, assume for contradiction that the first edge of that cycle is ever forced. At that instant both endpoints of this cycle edge are still incident with at least two remaining white cycle edges, contradicting the leaf-edge condition. Thus a zero-forcing configuration has neither a cycle nor an absence of isolated vertices.

**Sufficiency.** Suppose \(F_S\) is a forest containing an isolated vertex \(w\). As long as any white edge remains, choose a leaf \(v\) of any nontrivial tree component; write its sole white edge as \(vt\). The edge \(vw\) of \(K_n\) is black because \(w\) is isolated, and its unique white neighbor in the line graph is \(vt\). Hence \(vw\) forces \(vt\). Deleting this edge preserves acyclicity and the isolated vertex \(w\). Induction on the number of white edges empties \(F_S\), proving the characterization for every initial set.

**Enumerator.** The exponential formula for labeled forests decomposes them into isolated vertices (EGF \(e^u\)) and tree components of orders \(j\ge2\). Cayley's formula gives exactly \(j^{j-2}\) labeled trees on \(j\) vertices, each with \(j-1\) edges. Requiring at least one isolated vertex replaces the isolated-vertex factor \(e^u\) by \(e^u-1\), yielding the stated EGF. The substitution \(z^N H_n(z^{-1})\) holds because each white forest with \(r\) edges uniquely corresponds to a black zero-forcing set of \(N-r\) vertices.

For a finite coefficient recurrence, set \(P_0(y)=1\), and for every integer \(m\ge1\), define
\[
 P_m(y)=\sum_{j=1}^{m}\binom{m-1}{j-1}t_j y^{j-1}P_{m-j}(y),
 \qquad t_1=1,\quad t_j=j^{j-2}\ (j\ge2).
\]
The component containing a distinguished vertex has \(j\) vertices, so \(P_m\) enumerates all spanning forests. Inclusion-exclusion over the vertices required to be isolated then gives
\[
 H_n(y)=\sum_{j=1}^{n}(-1)^{j-1}\binom nj P_{n-j}(y).
\]
This is a terminating exact integer recurrence for every coefficient, independent of formal infinite-series truncation.

**Extrema.** A forest on \(n\) vertices with at least one isolate has at most \(n-2\) edges. Equality means exactly one isolated vertex and a tree on the other \(n-1\) vertices. There are \(n\) choices of the isolated vertex and \((n-1)^{n-3}\) labeled trees, proving both minimum forcing cardinality and its exact coefficient. Conversely, a set is nonforcing precisely when its white-edge graph either has a cycle (requiring at least three edges) or has no isolated vertices (requiring at least \(\lceil n/2\rceil\) edges). Both thresholds are achieved in \(K_n\): by a triangle, and by a minimum edge cover, respectively. Thus the fewest edges in a nonforcing white graph are \(r_n=\min\{3,\lceil n/2\rceil\}\), and the most black vertices in a failed initial set are \(N-r_n\). Adding black vertices preserves forcing, while removing them preserves nonforcing; hence both kinds occur at every cardinality from \(N-n+2\) through \(N-r_n\) when this interval is nonempty, with the stated count.

## Verification

A self-contained exact checker (`verify.py`) constructs \(T_n\) from all edges of \(K_n\), enumerates every initial black/white assignment, runs the ordinary color-change rule without using the structural characterization, and separately tests the forest-and-isolate condition with disjoint sets. It also evaluates the separately derived Cayley component recurrence and inclusion-exclusion coefficient formula. All \(33864\) assignments across \(n=3,4,5,6\) agree with the theorem and with the recurrence. The coefficient lists by ascending number of white edges are, respectively,

\[
\begin{aligned}
H_3(y)&=1+3y,\\
H_4(y)&=1+6y+12y^2,\\
H_5(y)&=1+10y+45y^2+80y^3,\\
H_6(y)&=1+15y+105y^2+420y^3+750y^4.
\end{aligned}
\]

To reproduce: run `python3 verify.py` using Python 3 and only its standard library. Exhaustive finite checks support, but do not establish, the theorem for unbounded \(n\); the combinatorial arguments above are its proof.

## Relationship to prior work

The foundational paper, publicly available from 26 November 2007, introduced ordinary zero forcing and proved the relevant Hamiltonian-path scalar equality (Proposition 4.9), without classifying all initial forcing sets. Eroh, Kang, and Yi (first public version 25 July 2012, Proposition 3.5, citing the earlier work) explicitly state the **already known scalar** \(Z(L(K_n))=\binom n2-n+2\). Fallat and Soltani (2016, Theorem 3.4) prove a broader **scalar** formula for line graphs of graphs with Hamiltonian paths, which again implies this minimum number but not a count of each initial set. Fallat, Meagher, Soltani, and Yang (2015, Lemma 8.3) compute the **positive-semidefinite** forcing number of \(J(n,2)\), a different rule. Boyer and collaborators (2018) introduce the ordinary zero-forcing polynomial and evaluate several other graph families; the inspected full-text sections do not state the triangular-graph forest-isolate characterization or its evaluated polynomial.

The claimed contribution is the **all-set if-and-only-if classification**, its forest enumerator and minimum-set coefficient, and the exact range of failed-set cardinalities. None follows as an enumerative statement from the cited scalar formulas. A separately published equivalent characterization under edge-forcing or forest language cannot be categorically excluded by bibliographic searches.

## Limitations

This result is restricted to ordinary zero forcing on complete-graph line graphs. Neither positive nor skew zero forcing is enumerated. No formula for forcing time or optimal force chronology is claimed. The full 2008 foundational article was inspected in an openly hosted author copy; Proposition 4.9 computes the scalar using minimum-rank inequalities, not an all-set enumeration. Earlier or later equivalent work indexed under different terminology remains a literature risk. The theorem is proved mathematically and checked for small orders; no independent mathematical audit or external certification has been performed.

## References

1. AIM Minimum Rank–Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648 (first publicly available online 2007-11-26), Proposition 4.9. DOI: 10.1016/j.laa.2007.10.009. https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/published-version2.pdf
2. L. Eroh, C. X. Kang, E. Yi, “Metric Dimension and Zero Forcing Number of Two Families of Line Graphs,” arXiv:1207.6127 (first public version 2012-07-25), Proposition 3.5. https://arxiv.org/pdf/1207.6127
3. S. M. Fallat, A. Soltani, “Line graphs: their maximum nullities and zero forcing numbers,” *Czechoslovak Mathematical Journal* 66 (2016), 743–755, Theorem 3.4. DOI: 10.1007/s10587-016-0290-x. https://dml.cz/handle/10338.dmlcz/145869
4. S. M. Fallat, K. Meagher, A. Soltani, B. Yang, “Compressed Cliques Graphs, Clique Coverings and Positive Zero Forcing,” arXiv:1508.07357 (2015), Lemma 8.3. https://arxiv.org/pdf/1508.07357
5. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910 (2018), later *Discrete Applied Mathematics* 258 (2019), 35–48. https://arxiv.org/pdf/1801.08910
