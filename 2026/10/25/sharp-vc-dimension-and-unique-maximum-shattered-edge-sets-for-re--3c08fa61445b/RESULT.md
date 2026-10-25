# Sharp VC dimension and unique maximum shattered edge sets for regular tournaments

## Finding
For every integer \(m\ge 1\), let \(V\) be a labeled set of size \(2m+1\), and let \(\mathcal R_m\) be the Boolean concept class indexed by all **regular tournaments** on \(V\). The query domain is \(E(K_{2m+1})\); each query asks for the direction of one fixed unordered vertex pair, encoded using one arbitrarily fixed reference direction. A set \(S\) of edge queries is *shattered* if every orientation of all edges in \(S\) extends to a regular tournament.

The exact Vapnik–Chervonenkis dimension is
\[
\operatorname{VCdim}(\mathcal R_m)=m^2.
\]
Moreover, **every shattered set of cardinality \(m^2\)** is, up to relabeling, precisely
\[
S=E(K_A)\mathbin{\dot\cup}E(K_B),\qquad |A|=m,\quad |B|=m+1,\quad A\mathbin{\dot\cup}B=V.
\]
Thus the maximum shattered support is unique up to vertex permutation; on fixed labeled vertices there are exactly \(\binom{2m+1}{m}\) distinct maximum supports.

A general result used in the proof may be of independent interest: if \(G\) is any finite loopless undirected graph in which all degrees are even, then an edge set \(S\subseteq E(G)\) is shattered by the class of Eulerian orientations of \(G\) if and only if
\[
2|S\cap\delta_G(U)|\le |\delta_G(U)|\quad\text{for every }U\subseteq V(G).
\]
Here \(\delta_G(U)\) denotes the edge cut between \(U\) and its complement, and Eulerian means equal in- and outdegree at each vertex. The empty graph and disconnected even-degree graphs are included.

## Assumptions and scope
The graph \(K_{2m+1}\) is simple and the vertices are labeled. The hypotheses are **all** regular tournaments, not a single fixed tournament. Every unordered vertex pair is a separate Boolean query. In the general cut lemma, parallel edges may be allowed if distinguished as separate queries, but loops are excluded. There is no assertion about Littlestone dimension or about nonregular tournament classes.

## Proof
**Lemma (prescribed-outdegree orientation).** For a finite loopless undirected graph \(H=(V,F)\) and integers \(b_v\), there is an orientation of \(F\) with outdegree \(b_v\) at each vertex if and only if
\[
\sum_{v\in V}b_v=|F|,\qquad \sum_{v\in U}b_v\ge |E_H(U)|\quad\text{for every }U\subseteq V.
\]
Here \(E_H(U)\) consists of edges whose two endpoints lie in \(U\). This is the standard prescribed-outdegree theorem. For completeness, make a unit-supply node for each edge, connect it to its two endpoint nodes, and give vertex \(v\) capacity \(b_v\) to the sink. Integral max flow assigns each edge to one endpoint (its tail). The displayed inequalities are exactly the max-flow/min-cut or capacitated Hall conditions. Equality of the total capacities forces all edge supply to be routed. This also proves the lemma for arbitrary integral degrees without an unstated connectivity assumption.

**Cut-shattering criterion.** Let \(G\) have even degrees, and let \(S\) be fixed. Choose an arbitrary direction for every edge of \(S\). To finish an Eulerian orientation, the remaining graph \(H=G-S\) must have outdegrees
\[
b_v=\frac{\deg_G(v)}2-d_S^+(v).
\]
The sum of these demands equals \(|E(H)|\), since \(\sum_vd_S^+(v)=|S|\) and \(\sum_v\deg_G(v)/2=|E(G)|\). For each vertex subset \(U\), direct counting gives
\[
\sum_{v\in U}b_v-|E_H(U)|
=\frac{|\delta_G(U)|}{2}-d_S^+(U,V\setminus U),
\]
where the last term counts the selected edges leaving \(U\). Consequently the fixed orientation extends if and only if all its directed-cut counts satisfy the corresponding inequalities. **All** orientations of \(S\) extend if and only if \(|S\cap\delta_G(U)|\le |\delta_G(U)|/2\) for each cut: necessity follows by orienting every selected crossing edge outward, and sufficiency follows from the displayed identity and the prescribed-outdegree lemma. This proves the criterion with full quantifiers.

**Construction.** Partition \(V=A\mathbin{\dot\cup}B\), where \(|A|=m\), \(|B|=m+1\), and take all edges within each part, none between parts. For any \(U\subseteq V\), put \(a=|A\cap U|\), \(b=|B\cap U|\). Exact cut counting yields
\[
|\delta_{K_{2m+1}}(U)|-2|S\cap\delta_{K_{2m+1}}(U)|
=(a-b)(a-b+1)\ge0.
\]
The product is nonnegative because \(a-b\) is an integer. Thus every orientation of the \(m^2=\binom m2+\binom{m+1}2\) selected internal edges extends to a regular tournament. This proves the lower bound.

**Upper bound and rigidity.** Suppose \(S\) is shattered, and let \(F\) be the set of vertices of selected degree exactly \(m\). Applying the criterion to a singleton yields \(\deg_S(v)\le m\) for all \(v\). If two vertices \(u,v\in F\) were nonadjacent in \(S\), the two-vertex cut would contain \(2m\) selected edges while the full cut has \(2(2m-1)\) edges; this violates \(2|S\cap\delta|\le|\delta|\). Hence \(F\) induces a clique. Since each vertex in \(F\) has selected degree \(m\), we have \(|F|\le m+1\). Every vertex outside \(F\) has selected degree at most \(m-1\). Summing degrees gives
\[
2|S|\le |F|m+(2m+1-|F|)(m-1)
\le (m+1)m+m(m-1)=2m^2.
\]
Equality forces exactly \(m+1\) vertices in \(F\) and selected degree \(m-1\) on each of the remaining \(m\) vertices. Since \(F\) is a clique of size \(m+1\), every vertex of \(F\) uses its entire selected degree within \(F\); therefore no selected edge joins \(F\) to its complement. The remaining \(m\) vertices each have selected degree \(m-1\), so they induce \(K_m\). This proves both sharpness and uniqueness. Interchanging the two unequal part sizes cannot produce a different partition, giving exactly \(\binom{2m+1}{m}\) labeled maximum supports.

## Verification
The standard-library verifier `verify.py` tests the cut condition for the proposed extremal support at orders \(3,5,7,9,11\), exhausting all cuts at each order. At orders \(3\) and \(5\), it independently enumerates every regular tournament and every possible queried-edge support, and compares the direct shattering test with the cut criterion. It also verifies the maximum cardinality and the **entire** family of maximum supports. The expected output is in `verification_output.txt`. These finite checks corroborate the proof but are not substitutes for its all-\(m\) arguments.

## Relationship to prior work
Hakimi's classical theorem on prescribed degrees of orientations provides the general feasibility framework. Borbényi and Csikvári (first posted May 15, 2019) study the **numbers** of degree-constrained subgraphs and Eulerian orientations, particularly general lower bounds; Cai, Fu, and Shao (first posted April 4, 2019) classify weighted Eulerian-orientation **counting complexity**. Their inspected statements do not give the edge-query VC dimension or classify all maximum shattered supports. Recent literature on VC dimension **of individual tournaments** generally measures the neighborhoods of vertices within a fixed tournament; here the concept class varies across *all regular tournaments* and queries are ordered outcomes on individual vertex pairs. This is a different set system. The general feasibility theorem makes the cut criterion obtainable from classical tools, while the exact \(m^2\) extremum and equality classification require the separate extremal argument.

## Limitations
The claim is for odd-order regular tournaments only; even-order semiregular tournaments and additional model-theoretic query languages are not covered. Historical novelty is based on identified source comparisons, not exhaustive priority certification. The general cut lemma is a reformulation of prescribed-outdegree feasibility, not claimed as a newly invented orientation theorem. The proof and finite verifier do not determine adaptive/Littlestone dimension.

## References
- S. L. Hakimi, *On the degrees of the vertices of a directed graph*, Journal of the Franklin Institute 279 (1965), 290–308, DOI: 10.1016/0016-0032(65)90340-6. Accessible orientation-with-degree-bounds theorem summary: https://lemon.cs.elte.hu/egres/open/Orientation_with_degree_bounds .
- M. Borbényi and P. Csikvári, *Counting degree-constrained subgraphs and orientations*, first arXiv version May 15, 2019, https://arxiv.org/abs/1905.06215 .
- J.-Y. Cai, Z. Fu and S. Shao, *Beyond #CSP: A Dichotomy for Counting Weighted Eulerian Orientations with ARS*, first arXiv version April 4, 2019, https://arxiv.org/abs/1904.02362 .
- S. Raßmann and P. Schweitzer, *Isomorphism of tournaments with bounded VC dimension*, first arXiv version August 14, 2026, https://arxiv.org/html/2608.14486v1 (different neighborhood-based VC parameter).
