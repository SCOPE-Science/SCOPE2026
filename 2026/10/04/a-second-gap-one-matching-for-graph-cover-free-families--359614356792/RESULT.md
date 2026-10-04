# A second gap-one matching for graph cover-free families

## Finding
For the matching graph \(E_{14}\) consisting of seven disjoint edges, the graph cover-free-family number satisfies
\[
t(E_{14})=6=t_e(E_{14})+1.
\]
Thus \(m=7\) is a second explicit gap-one parameter for the matching family \(E_{2m}\), beyond the published case \(m=4\).

## Assumptions and scope
All set systems are finite. For a graph \(G\), a \(G\)-CFF is a family \((B_v)_{v\in V(G)}\) of subsets of a finite ground set such that, for every edge \(uv\), neither endpoint block contains the other and no block indexed by a third vertex is contained in \(B_u\cup B_v\). The number \(t(G)\) is the minimum ground-set size. The edge-only variant is denoted \(t_e(G)\). The graph \(E_{14}\) is the disjoint union of seven copies of \(K_2\).

## Proof
The general lower bound of Parida and Moura gives \(t(1,|V(G)|)\le t(G)\) for graphs without isolated vertices. Sperner's theorem gives
\[
\binom{5}{2}=10<14\le \binom{6}{3}=20,
\]
so \(t(1,14)=6\). Hence \(t(E_{14})\ge6\).

For the matching upper bound, take ground set \([6]\) and assign the endpoints of the seven matching edges the following pairs of triples:
\[
\begin{aligned}
&\{1,3,6\},\{3,4,6\};\qquad &&\{2,5,6\},\{3,5,6\};\\
&\{1,2,6\},\{2,4,6\}; &&\{1,5,6\},\{4,5,6\};\\
&\{1,3,5\},\{3,4,5\}; &&\{1,2,5\},\{2,4,5\};\\
&\{1,2,3\},\{2,3,4\}.&&
\end{aligned}
\]
All fourteen blocks are distinct triples, so the two blocks on each edge are incomparable. The complements in \([6]\) of the seven edge-unions are, respectively,
\[
\{2,5\},\{1,4\},\{3,5\},\{2,3\},\{2,6\},\{3,6\},\{5,6\}.
\]
For each edge, each of the other twelve displayed triples meets the corresponding two-point complement. Equivalently, no third block is contained in that edge's union. Thus the displayed set system is an \(E_{14}\)-CFF on six points, proving \(t(E_{14})\le6\). Therefore \(t(E_{14})=6\).

Parida and Moura also prove \(t_e(E_{2m})=t(1,m)\). Since
\[
\binom{4}{2}=6<7\le\binom{5}{2}=10,
\]
we have \(t_e(E_{14})=t(1,7)=5\). Hence \(t(E_{14})=t_e(E_{14})+1\).

## Verification
The standalone `verify.py` checks all fourteen blocks, all seven edge incomparability conditions, and all \(7\cdot12=84\) third-block exclusion tests directly from the displayed witness. It also recomputes the two Sperner thresholds from binomial coefficients. A successful run prints `ALL CHECKS PASSED` together with the checked counts. The finite checker verifies the explicit witness; the lower bound is the stated application of Sperner's theorem and the published general lower bound.

## Relationship to prior work
Parida and Moura introduce the graph cover-free-family parameter, specialize the edge-only value for matching graphs to \(t_e(E_{2m})=t(1,m)\), and prove the universal estimate \(t_e(G)\le t(G)\le t_e(G)+2\) for graphs without isolated vertices. For matchings they prove the gap-two value on infinite subfamilies and exhibit \(t(E_8)=5=t_e(E_8)+1\). They then ask which \(m\) satisfy gap one versus gap two, and specifically whether gap one occurs infinitely often. The value \(m=7\) above supplies a new explicit gap-one parameter but does not resolve infinitude.

The earlier hypergraph literature on disjoint edges determines the edge-only parameter used in the lower-level comparison; it does not impose the graph-Sperner condition needed for \(t(E_{14})\). Searches for the aliases `matching graph`, `disjoint union of seven edges`, \(E_{14}\), and graph cover-free families did not locate a published exact value for \(t(E_{14})\). A 2026 doctoral thesis with the same broad topic is publicly listed, but its full text was not surfaced in the checked sources, so this remains a residual literature risk.

## Limitations
The finding determines one finite parameter, \(m=7\). It does not classify all matching sizes, prove that infinitely many gap-one examples exist, or improve the asymptotic theory of cover-free families. The originality assessment is literature-dependent and remains subject to the residual risk that an unindexed or inaccessible source contains the same finite value.

## References
1. P. Parida and L. Moura, *Cover-free families on graphs*, arXiv:2605.12634, first public version 12 May 2026.
2. T. B. Idalino and L. Moura, *Cover-free families on hypergraphs and combinatorial group testing*, Journal of Combinatorial Optimization (2026), DOI 10.1007/s10878-026-01429-0.
