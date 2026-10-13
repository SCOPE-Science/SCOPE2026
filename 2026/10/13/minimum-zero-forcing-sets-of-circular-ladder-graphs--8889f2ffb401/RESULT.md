# Minimum zero forcing sets of circular ladder graphs
## Finding
For every integer \(n\ge5\), let the circular ladder (prism) graph
\[
Y_n=C_n\mathbin{\square}K_2
\]
have rails \(U=\{u_i:i\in\mathbb Z/n\mathbb Z\}\) and \(V=\{v_i:i\in\mathbb Z/n\mathbb Z\}\), with edges \(u_i u_{i+1}\), \(v_i v_{i+1}\), and \(u_i v_i\). A blue vertex with exactly one white neighbor forces that neighbor blue.

Then \(Z(Y_n)=4\), and the minimum zero forcing sets are exactly the following four families, with all indices read modulo \(n\):

1. Two adjacent complete rungs:
\[
\{u_i,v_i,u_{i+1},v_{i+1}\}.
\]
2. One complete rung at \(i\), together with two vertices on the same rail whose offsets from \(i\) are one of
\[
\{1,2\},\qquad \{-2,-1\},\qquad \{-1,2\},\qquad \{1,-2\}.
\]
Thus, for example, \(\{u_i,v_i,u_{i+a},u_{i+b}\}\) is allowed precisely for one of those four offset pairs; the analogous set on the \(v\)-rail is also allowed.
3. One complete rung at \(i\), together with opposite-rail vertices in the two neighboring columns:
\[
\{u_i,v_i,u_{i-1},v_{i+1}\}\quad\text{or}\quad
\{u_i,v_i,v_{i-1},u_{i+1}\}.
\]
4. Four consecutive vertices on one rail:
\[
\{u_i,u_{i+1},u_{i+2},u_{i+3}\}
\]
or the corresponding four vertices on the \(v\)-rail.

The four families are disjoint for \(n\ge5\). Their cardinalities are respectively \(n\), \(8n\), \(2n\), and \(2n\). Hence the exact number of minimum zero forcing sets is
\[
13n.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is stated only for \(n\ge5\). This is the stable circular-ladder range and avoids the exceptional small prisms: direct computation gives different minimum-set profiles for \(n=3\) and \(n=4\).

The scalar zero forcing number of prism graphs has been studied previously. The contribution here is the exact classification and enumeration of all minimum zero forcing sets in the stable family, not novelty of the scalar value alone.

## Proof
First, \(Y_n\) is cubic and triangle-free for \(n\ge5\). Suppose three blue vertices formed a zero forcing set. A first force can occur only at a blue vertex \(x\) having exactly two blue neighbors. Since there are only three blue vertices and no triangle, those three vertices form a three-vertex path with center \(x\). Up to rotation, reflection, and interchange of the rails, there are two possibilities.

If the two blue neighbors of \(x=u_0\) are the rail neighbors \(u_{-1}\) and \(u_1\), then \(u_0\) forces \(v_0\). With only these four vertices blue, every blue vertex has either zero or at least two white neighbors, so no second force exists. If instead the two blue neighbors of \(u_0\) are \(u_1\) and \(v_0\), then \(u_0\) forces \(u_{-1}\), after which the same stall occurs. Thus no three-vertex set is zero forcing. Sets of size at most two cannot even have a first force in a cubic graph. Therefore \(Z(Y_n)\ge4\).

A type-A set is zero forcing: from two adjacent complete rungs, the two rails force outward in both directions until every vertex is blue. Hence \(Z(Y_n)=4\).

The other three listed types reduce to type A. For type D, the two interior vertices of four consecutive blue rail vertices force their rung mates, creating two adjacent complete rungs. For type B with offsets \(\{1,2\}\) or \(\{-2,-1\}\), the rail vertex between the full rung and the farther singleton forces its rung mate, again creating adjacent complete rungs. For offsets \(\{-1,2\}\) or \(\{1,-2\}\), a vertex of the complete rung first fills the missing rail position, producing four consecutive blue vertices on one rail, hence type D. For type C, the two vertices of the complete rung force into the two neighboring columns on opposite rails; this creates an adjacent complete rung and again reduces to type A. Thus every listed set is zero forcing.

It remains to prove necessity. Let \(S\) be any four-vertex zero forcing set, and choose an actual first force \(x\to y\). Since \(x\) has degree three, exactly two neighbors of \(x\) lie in \(S\). Up to the graph symmetries there are again two cases.

In the rail-rail case take \(x=u_0\) with \(u_{-1},u_1\in S\), so \(y=v_0\). Write \(q\) for the fourth initially blue vertex. Immediately after the first force, a second force is possible only if
\[
q\in\{u_{-2},u_2,v_{-1},v_1\}.
\]
Indeed, outside those four positions, each of \(u_{-1}\), \(u_1\), and \(v_0\) still has two white neighbors, while \(q\) has at most one blue neighbor. The choices \(u_{-2}\) and \(u_2\) give type D, while \(v_{-1}\) and \(v_1\) give type B.

In the rail-rung case take \(x=u_0\) with \(u_1,v_0\in S\), so \(y=u_{-1}\). Again write \(q\) for the fourth initially blue vertex. A second force is possible only if
\[
q\in\{u_{-2},u_2,v_{-1},v_1\}.
\]
These four choices yield, respectively, type B, type B, type C, and type A (up to reflection). Hence every four-vertex zero forcing set belongs to exactly one of A--D.

Finally, count. Type A has \(n\) choices. Type B has \(n\) choices for the complete rung, four offset pairs, and two choices of rail, giving \(8n\). Type C gives \(2n\), and type D gives \(2n\). For \(n\ge5\), the relevant offsets are distinct modulo \(n\), so no identifications occur. The total is \(13n\).

## Verification
The standalone checker `verify.py` constructs \(Y_n\) directly from its two cycles and rungs, implements the zero forcing rule without using the theorem's classification, and exhaustively tests all subsets of size at most four for \(5\le n\le11\). It verifies that no set of size at most three forces, that a four-set forces if and only if it is in one of the four stated families, and that there are exactly \(13n\) such sets for every checked \(n\).

Replay with:

`python3 verify.py`

Expected output:

`VERIFY_OK n_range=5..11 subset_checks=24521 basis_count_formula=13n max_order=22`

This finite computation is a stress test, not the proof for arbitrary \(n\); the infinite-family claim rests on the local first-force argument above.

## Relationship to prior work
The foundational paper of the AIM Minimum Rank -- Special Graphs Work Group introduced the standard zero forcing parameter; its public version was available online on 26 November 2007 and lists 05C50 first in its AMS classification.

Petruk's paper is directly about zero forcing numbers and processes for gear and prism graphs, so the scalar prism minimum is treated as prior context rather than the claimed contribution. Rashidi, Shajareh Poursalavati, and Tavakkoli study the broader generalized Petersen family \(P(n,k)\). Their inspected full text defines that family for \(n\ge5\), but the stated exact results concern \(k=2\), \(k=3\), and \(P(2k+1,k)\); it does not state a count or classification of the minimum sets of the \(k=1\) circular ladders.

Boyer et al. introduce the zero forcing polynomial, which makes counting zero forcing sets a natural enumerative problem. Their inspected full text contains no occurrence of “prism” or “circular ladder.” Geneson, Haas, and Hogben define the zero forcing reconfiguration graph whose vertices are precisely the minimum zero forcing sets, directly motivating exact basis classification; their inspected full text likewise contains no occurrence of “prism” or “circular ladder.” A further full-text article on minimum zero forcing sets from 2022 was inspected and treats paths, wheels, ladders, trees, and complete (bi)partite graphs, but not prism or circular-ladder graphs.

Thus the located literature covers the scalar invariant, the generalized-Petersen setting, and the general counting/reconfiguration frameworks, while no inspected source supplies the four-family classification or the \(13n\) minimum-set count.

## Limitations
The theorem does not classify nonminimum zero forcing sets or the adjacency structure of the resulting zero forcing reconfiguration graph. The brute-force checker stops at \(n=11\); it is not used as an infinite proof. Bibliographic searches cannot exclude an unindexed treatment under alternate prism notation, so a residual literature risk remains.

## References
1. AIM Minimum Rank -- Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628--1648. DOI: 10.1016/j.laa.2007.10.009.
2. V. Petruk, “Zero Forcing Number of Some Families of Graphs,” *Mohyla Mathematical Journal* (2021), 48--52. DOI: 10.18523/2617-70803202048-52cs.
3. S. Rashidi, N. Shajareh Poursalavati, and M. Tavakkoli, “Computing the zero forcing number for generalized Petersen graphs,” *Journal of Algebra Combinatorics Discrete Structures and Applications* 7 (2020), 183--193. DOI: 10.13069/jacodesmath.729465.
4. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910.
5. J. Geneson, R. Haas, and L. Hogben, “Reconfiguration graphs of zero forcing sets,” arXiv:2009.00220.
6. S. P. Susanth and P. Sunitha, “Minimum Zero-Forcing Sets of Various Graphs: Insights and Real-World Applications,” *ShodhKosh* 3 (2022), 965--969. DOI: 10.29121/shodhkosh.v3.i2.2022.3593.
