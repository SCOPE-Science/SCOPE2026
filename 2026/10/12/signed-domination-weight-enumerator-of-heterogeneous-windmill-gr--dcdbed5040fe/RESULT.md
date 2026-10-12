# Signed-domination weight enumerator of heterogeneous windmill graphs
## Finding
For every integer \(r\ge2\) and positive integers \(m_1,\ldots,m_r\), let
\[
W(m_1,\ldots,m_r)=K_1\vee(K_{m_1}\cup\cdots\cup K_{m_r})
\]
have universal center \(c\) and pairwise disjoint clique blades \(B_1,\ldots,B_r\), where \(|B_i|=m_i\). A signed dominating function is a map \(f:V(W)\to\{-1,1\}\) such that the sum of its labels on every closed neighborhood is at least \(1\). Put \(e=f(c)\) and \(S_i=\sum_{v\in B_i}f(v)\).

Then \(f\) is signed dominating if and only if
\[
e+S_i\ge1\qquad(1\le i\le r).
\]
In particular, the center inequality is redundant once the blade inequalities hold.

Define
\[
P_m(x)=\sum_{k=\lceil m/2\rceil}^m\binom{m}{k}x^{2k-m},
\qquad
Q_m(x)=\sum_{k=\lceil(m+2)/2\rceil}^m\binom{m}{k}x^{2k-m},
\]
where an empty sum is zero. The complete weight enumerator is
\[
F_W(x)=\sum_{f\text{ signed dominating}}x^{\sum_{v\in V(W)}f(v)}
=x\prod_{i=1}^rP_{m_i}(x)+x^{-1}\prod_{i=1}^rQ_{m_i}(x).
\]
Although the second displayed expression uses \(x^{-1}\), every exponent that survives is nonnegative for \(r\ge2\).

Let \(o=|\{i:m_i\text{ is odd}\}|\). Then
\[
\gamma_s(W)=1+o,
\]
and every minimum signed dominating function has center label \(+1\) and exactly \(\lceil m_i/2\rceil\) vertices labeled \(+1\) in blade \(B_i\). Hence the number of minimum functions is
\[
N_{\min}(W)=\prod_{i=1}^r\binom{m_i}{\lceil m_i/2\rceil}.
\]
For a friendship graph, where every \(m_i=2\), this specializes to \(\gamma_s=1\) and exactly \(2^r\) minimum functions.

## Assumptions and scope
The graph is finite, simple, and undirected. The theorem assumes \(r\ge2\) and \(m_i\ge1\) for every blade. The signed-domination convention is the standard closed-neighborhood convention: every closed-neighborhood sum is at least \(1\). The claim concerns the original windmill graph itself, not its Mycielski graph, and it does not concern signed total domination or signed Roman domination.

The heterogeneous family allows unequal blade sizes. Equal blade sizes give the usual generalized windmills, and \(m_i=2\) for all \(i\) gives the friendship graphs.

## Proof
Every vertex \(v\in B_i\) is adjacent to the center and to every other vertex of its own blade, and to no vertex of any other blade. Therefore
\[
N[v]=\{c\}\cup B_i,
\qquad
\sum_{u\in N[v]}f(u)=e+S_i.
\]
Thus every blade vertex satisfies the signed-domination condition exactly when \(e+S_i\ge1\). The center has closed neighborhood all of \(V(W)\), so its condition is
\[
e+\sum_{i=1}^rS_i\ge1.
\]
This condition follows from the blade inequalities. If \(e=1\), then every \(S_i\ge0\), hence the center sum is at least \(1\). If \(e=-1\), then every \(S_i\ge2\), hence the center sum is at least \(-1+2r\ge3\). This proves the structural criterion.

Suppose first that \(e=1\). If blade \(B_i\) has exactly \(k\) vertices labeled \(+1\), then \(S_i=2k-m_i\). Feasibility is \(S_i\ge0\), equivalently \(k\ge\lceil m_i/2\rceil\). The contribution of that blade to the weight enumerator is therefore \(P_{m_i}(x)\), and the center contributes \(x\).

If \(e=-1\), feasibility is \(S_i\ge2\), equivalently \(k\ge\lceil(m_i+2)/2\rceil\). The blade contribution is \(Q_{m_i}(x)\), and the center contributes \(x^{-1}\). Independence of the label choices on distinct blades gives the product formula for \(F_W(x)\).

For the minimum weight, the \(e=1\) branch has the smallest allowed blade sum \(0\) for even \(m_i\) and \(1\) for odd \(m_i\), so its minimum total weight is \(1+o\). If any \(m_i=1\), the \(e=-1\) branch is impossible. Otherwise its smallest blade sum is \(2\) for even \(m_i\) and \(3\) for odd \(m_i\), so its minimum is
\[
-1+2r+o=(1+o)+(2r-2)>1+o.
\]
Therefore every optimum lies in the \(e=1\) branch. In blade \(B_i\), equality forces exactly \(\lceil m_i/2\rceil\) positive labels, giving \(\binom{m_i}{\lceil m_i/2\rceil}\) choices. Multiplying over the independent blades proves the minimum-family count.

## Verification
The standalone script `verify_signed_windmill.py` constructs the graphs from their adjacency relation and independently tests the original closed-neighborhood definition against the structural criterion. It exhaustively enumerates all sign labelings for \(226\) parameter tuples with \(2\le r\le4\), \(1\le m_i\le4\), and graph order at most \(11\). It compares the full weight coefficient map, the minimum weight, and the number of minimum functions with the formulas above. It also checks the branch-minimum comparison on a larger bounded collection of parameter tuples.

The replay output is:

`VERIFY_OK tuples=226 labelings=188952 criterion_checks=188952 coefficient_checks=893 minimum_checks=102207 max_order=11`

These finite computations test boundary cases and the coefficient formula; the all-parameter result is proved by the neighborhood-sum argument above rather than inferred from enumeration.

## Relationship to prior work
Signed domination is an established majority-type graph invariant. Poghosyan and Zverovich give the standard definition and general bounds, and their first arXiv version is dated 2009-06-22 with MSC \(05C69\). Ghameshlou, Shaminezhad, Vatandoost, and Khodkar likewise use the same definition and explicitly note that exact signed domination numbers had already been determined for Dutch windmill graphs. Their paper defines a Dutch windmill as equal triangular blades sharing one universal center.

Sheikholeslami's 2007 paper studies forcing signed domination and includes Dutch windmills among the graph classes treated. Accordingly, the scalar friendship/Dutch-windmill specialization is not used as an originality claim here. The contribution assessed here is the all-weight enumerator and complete minimum-family classification for arbitrary unequal clique-blade sizes. Liang's complete-multipartite formulas do not imply this statement: a heterogeneous windmill is a one-vertex join of a disjoint union of cliques and, except for degenerate cases, is not complete multipartite; signed domination is determined by its actual closed neighborhoods.

Targeted searches for signed domination together with windmill, Dutch windmill, friendship graph, block graph, join, polynomial, enumerator, and heterogeneous clique blades found the homogeneous Dutch-windmill scalar/forcing literature but no source giving the displayed heterogeneous all-weight product formula. Published-record comparisons also located exact signed-domination results on complete multipartite graphs and other invariants on generalized windmills, neither of which implies the theorem.

## Limitations
The theorem does not cover the one-blade case \(r=1\), where the two center-sign branches can tie at minimum weight. It does not classify forcing subsets of minimum functions, nor does it address signed total, signed Roman, or edge-signed variants. The literature search cannot exclude an obscure or poorly indexed equivalent treatment. Direct inspection of the 2007 forcing paper was limited to its indexed abstract and accessible indexed text describing the Dutch-windmill section; a later full-text source independently states that exact signed-domination values for Dutch windmills were already known. No originality claim is made for that homogeneous scalar specialization.

## References
1. A. Poghosyan and V. Zverovich, *Discrepancy and Signed Domination in Graphs and Hypergraphs*, arXiv:0906.3993v1, first submitted 2009-06-22.
2. A. N. Ghameshlou, A. Shaminezhad, E. Vatandoost, and A. Khodkar, *Signed domination and Mycielski's structure in graphs*, RAIRO Operations Research 54 (2020), 1077–1086, doi:10.1051/ro/2019109.
3. S. M. Sheikholeslami, *Forcing signed domination numbers in graphs*, Matematički Vesnik 59 (2007), 171–179.
4. H. Liang, *Signed and Minus Domination in Complete Multipartite Graphs*, arXiv:1205.0343v1.
