# Zero forcing polynomial and minimum-set types of the Petersen graph
## Finding
Let \(P=P(5,2)\) be the Petersen graph in the standard generalized-Petersen labeling: outer vertices \(u_0,\ldots,u_4\) form a 5-cycle, inner vertices \(v_0,\ldots,v_4\) have edges \(v_i v_{i+2}\) with indices modulo \(5\), and \(u_i v_i\) is a spoke. For \(j\in\{0,\ldots,10}\), let \(z(P;j)\) be the number of zero forcing sets of cardinality \(j\), and let \(\mathcal Z(P;x)=\sum_j z(P;j)x^j\).

The exact polynomial is
\[
\mathcal Z(P;x)=132x^5+190x^6+120x^7+45x^8+10x^9+x^{10}.
\]
In particular, \(Z(P)=5\) and \(P\) has exactly \(132\) minimum zero forcing sets.

There is also a structural characterization of all minimum sets. For every \(S\subseteq V(P)\) with \(|S|=5\),
\[
S\text{ is zero forcing}
\quad\Longleftrightarrow\quad
P[S]\cong C_5,\ P_5,\text{ or }P_4\mathbin{\dot\cup}K_1.
\]
The three types contribute respectively \(12\), \(60\), and \(60\) minimum sets.

## Assumptions and scope
Graphs are finite, simple, and undirected. The zero forcing color-change rule is the standard rule: a blue vertex having exactly one white neighbor may force that neighbor blue. A set is zero forcing when repeated legal forces can color every vertex blue.

This is an exact theorem about the single canonical graph \(P=P(5,2)\), not an asymptotic or family statement. The known scalar value \(Z(P)=5\) is not claimed as new. The claimed contribution is the complete cardinality enumeration together with the induced-subgraph characterization and counts of all minimum sets.

## Proof
The graph has ten vertices, so the assertion admits an exhaustive finite proof without sampling. The accompanying checker constructs the standard \(P(5,2)\) adjacency relation directly, verifies that it is cubic with fifteen edges, and then examines every one of the \(2^{10}=1024\) vertex subsets.

For a set \(S\), its zero forcing closure is computed monotonically: at each round every white vertex that is the unique white neighbor of some blue vertex is added to the blue set. Because every update only decreases the white set, this reaches the standard zero forcing closure. The checker declares \(S\) zero forcing exactly when this closure is all ten vertices. Exact enumeration gives
\[
(z(P;0),\ldots,z(P;10))=(0,0,0,0,0,132,190,120,45,10,1),
\]
which proves the polynomial and \(Z(P)=5\).

For the structural statement, the checker additionally canonicalizes every five-vertex induced subgraph by direct isomorphism testing against the six types that actually occur. Among all \(252\) five-subsets the type census is
\[
12C_5,
\quad60P_5,
\quad60(P_4\mathbin{\dot\cup}K_1),
\quad60F,
\quad30(P_3\mathbin{\dot\cup}2K_1),
\quad30(2K_2\mathbin{\dot\cup}K_1),
\]
where \(F\) is the five-vertex tree with degree sequence \((3,2,1,1,1)\). Direct zero forcing closure on every member of this census shows that exactly the first three types force, giving \(12+60+60=132\) minimum sets. This finite classification simultaneously proves both directions of the stated induced-subgraph criterion.

Representative legal force sequences illustrate the three positive types. With indices modulo \(5\), the outer cycle \(\{u_0,u_1,u_2,u_3,u_4\}\) is a \(C_5\) minimum set and each \(u_i\) forces \(v_i\). The set \(\{u_0,u_1,u_2,u_3,v_0\}\), inducing \(P_5\), can force successively \(u_4,v_1,v_2,v_3,v_4\). The set \(\{u_0,u_1,u_2,u_3,v_4\}\), inducing \(P_4\mathbin{\dot\cup}K_1\), can force \(v_1,v_2,v_3,u_4,v_0\). These examples are illustrative; exhaustiveness comes from the complete 1024-subset certificate, not from symmetry assumptions.

## Verification
Run `python3 verify_petersen_zero_forcing.py`. The packaged script uses only the Python standard library and exhaustively checks all \(1024\) subsets, all \(252\) five-subsets, the six induced five-vertex types, the coefficient vector, and the equivalence between zero forcing and the three accepted minimum-set types.

Expected output:

`VERIFY_OK subsets=1024 zf_total=498 coefficients=5:132,6:190,7:120,8:45,9:10,10:1 min_types=C5:12,P5:60,P4+K1:60 nonforcing5=120`

## Relationship to prior work
The foundational zero forcing article introduced \(Z(G)\); its article header records online availability on 2007-11-26 and AMS classification beginning with 05C50. Hogben et al. explicitly record the Petersen graph as a matching graph and state the previously known value \(Z(P)=5\), using it to conclude minimum propagation time one. Thus the scalar minimum is prior work.

Boyer et al. introduced the zero forcing polynomial and characterize general extremal coefficients, but an inspection of the full text finds no occurrence of “Petersen.” Their general theory can account for some high-degree coefficients once the Petersen graph is supplied, but it does not provide the three lower nonzero coefficients \(132,190,120\) or the minimum-set type classification stated here.

Rashidi, Shajareh Poursalavati, and Tavakkoli study generalized Petersen graphs \(P(n,k)\), but their stated exact \(k=2\) result is \(Z(P(n,2))=6\) for \(n\ge10\); it does not cover \(P(5,2)\) or enumerate all zero forcing sets. Searches under the aliases “Petersen graph,” “generalized Petersen \(P(5,2)\),” “zero forcing polynomial,” “minimum zero forcing sets,” and the exact coefficient string found no stronger inspected source containing the complete statement.

## Limitations
This result is finite and graph-specific; it does not imply a formula for \(P(n,k)\) beyond \(P(5,2)\). Exhaustive verification is a complete proof for this ten-vertex graph but is not a general infinite-family argument. Some high-degree polynomial coefficients are consequences of general zero-forcing-polynomial results; the novel content asserted here is the complete Petersen enumeration, especially the lower coefficients and the all-minimum-set structural classification. Literature search cannot logically prove global novelty, so an unindexed prior computation remains a residual originality risk.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” Linear Algebra and its Applications 428 (2008), 1628–1648, DOI 10.1016/j.laa.2007.10.009. Article header: available online 2007-11-26; AMS 05C50, 15A18, 15A03.
2. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, M. Young, “Propagation time for zero forcing on a graph,” arXiv:1410.4191 (2014), especially Example 3.14.
3. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910 (2018); Discrete Applied Mathematics 258 (2019), 35–48.
4. S. Rashidi, N. Shajareh Poursalavati, M. Tavakkoli, “Computing the zero forcing number for generalized Petersen graphs,” Journal of Algebra Combinatorics Discrete Structures and Applications 7 (2020), 183–193, DOI 10.13069/jacodesmath.729465.
