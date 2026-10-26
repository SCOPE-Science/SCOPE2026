# The connected zero-forcing exchange graph of every sufficiently long circular ladder

## Finding

**Theorem.** Let \(n\ge6\) be an integer, and let \(P_n=C_n\square K_2\) be the labelled circular ladder. A connected zero-forcing set is a vertex subset that induces a connected graph and turns the whole graph blue under the rule that a blue vertex having exactly one white neighbour turns that neighbour blue. Let \(\mathcal Z_c(P_n)\) have one vertex for each *minimum-cardinality* connected zero-forcing set, with two vertices adjacent exactly when their underlying sets differ by deleting one vertex and inserting one vertex.

Then the minimum connected zero-forcing cardinality is \(4\), and its complete set of minimum configurations consists of the induced four-vertex paths and the induced four-cycles of \(P_n\). They form four orbits under cycle rotations, reflection, and layer exchange, of sizes \(2n,4n,n,2n\). In particular,
\[
|V(\mathcal Z_c(P_n))|=9n,\qquad |E(\mathcal Z_c(P_n))|=28n.
\]
The exchange graph is connected; exactly \(n\) of its vertices have degree \(8\), and its other \(8n\) vertices have degree \(6\).

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled. The two rims have vertices \(u_i\) and \(v_i\), with indices taken modulo \(n\). Their edges are \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\). A zero-forcing move is legal only if its blue source has *exactly one* currently white neighbour; the initial blue set must induce a connected subgraph. For reconfiguration, a move replaces exactly one initial blue vertex by another and both endpoint sets must be minimum connected zero-forcing sets. No requirement that the exchanged vertices be adjacent is imposed. The theorem is for all integers \(n\ge6\), without an asserted classification of smaller prisms or of unrestricted zero-forcing sets.

## Proof

**1. Minimum size.** The circular ladder is triangle-free and cubic. Any connected set of three vertices induces a path of length two. Its middle vertex has two blue neighbours and therefore forces its third neighbour. The resulting four blue vertices induce a claw: the original path endpoints and the newly forced vertex are the three neighbours of its central vertex. Now the center has no white neighbour, and every leaf has two white neighbours; no further force is possible. Connected sets of one or two vertices cannot initiate a force. Thus a connected forcing set has at least four vertices. The explicit four-vertex configurations in Step 3 force the graph, so the minimum is four.

**2. Classification of connected four-sets.** In a triangle-free cubic graph, every connected induced four-vertex graph is either a four-vertex path, a four-cycle, or a claw (because its connected edge count is at least three, at most four, and a three-edge tree is a path or claw). A claw is not forcing: its central vertex has no white neighbour and each leaf has two. For \(n\ge6\) the only four-cycles in \(P_n\) are its \(n\) rung squares. Every induced four-vertex path contains zero or one rung; a path with two rungs would have an extra horizontal chord completing a rung square. A path with no rung is four consecutive vertices on one rim, yielding \(2n\) choices. If its one rung is an endpoint edge, one chooses one of two rim layers, one of \(n\) starting positions, and one of two ends of a three-vertex rim path: \(4n\) choices. If its rung is the middle edge, the two horizontal edges must point in opposite cyclic directions, otherwise the four vertices form a square: \(2n\) choices. These cases are disjoint for \(n\ge6\). They give \(8n\) induced four-paths and \(n\) rung squares.

**3. Each path and square forces.** Symmetry reduces to four representatives, where indices are modulo \(n\):
\[
\begin{aligned}
A&=\{u_0,u_1,u_2,u_3\},\\
B&=\{u_0,u_1,u_2,v_0\},\\
C&=\{u_0,u_1,v_0,v_1\},\\
D&=\{u_0,u_1,v_1,v_2\}.
\end{aligned}
\]
For \(A\), the middle two upper vertices first force \(v_1,v_2\); these force \(v_0,v_3\), then both rims extend outward in paired steps. For \(B\), \(u_0\) forces \(u_{-1}\) and \(u_1\) forces \(v_1\); next \(v_0\) forces \(v_{-1}\) and \(v_1\) forces \(v_2\), after which both rims propagate in paired steps. For \(C\), the four vertices force \(u_{-1},u_2,v_{-1},v_2\) and both paired fronts propagate. For \(D\), \(u_1\) forces \(u_2\) and \(v_1\) forces \(v_0\); next \(u_0\) forces \(u_{-1}\) and \(v_2\) forces \(v_3\), followed by propagation along both rims. In each case propagation may stop only when the two expanding fronts meet; at that point every vertex is blue. The initial sets therefore are exactly the \(9n\) four-paths and four-squares classified in Step 2.

**4. Exhaustive local exchange calculation.** Write \(X:a\mapsto b\) when the removed vertex is \(a\), the inserted vertex is \(b\), and the new set belongs to class \(X\). Directly checking which insertion into each of the four possible retained triples produces another induced path or rung square gives this complete table for the four representatives (all subscripts modulo \(n\)):

| Source | Destination type and every legal exchange |
|---|---|
| \(A\) | \(A:u_3\mapsto u_{-1},\ A:u_0\mapsto u_4;\ B:u_3\mapsto v_0,v_2;\ B:u_0\mapsto v_1,v_3\) |
| \(B\) | \(A:v_0\mapsto u_{-1},u_3;\ B:v_0\mapsto v_2;\ C:u_2\mapsto v_1;\ D:u_2\mapsto v_{-1};\ D:u_0\mapsto v_1\) |
| \(C\) | \(B:v_1\mapsto u_2;\ B:v_0\mapsto u_{-1};\ B:u_1\mapsto v_2;\ B:u_0\mapsto v_{-1};\ D:v_1\mapsto v_{-1};\ D:v_0\mapsto v_2;\ D:u_1\mapsto u_{-1};\ D:u_0\mapsto u_2\) |
| \(D\) | \(B:v_1\mapsto u_2;\ B:v_2\mapsto u_{-1};\ B:u_1\mapsto v_0;\ B:u_0\mapsto v_3;\ C:v_2\mapsto v_0;\ C:u_0\mapsto u_2\) |

For completeness of each row, deleting one of the four blue vertices leaves a specified triple; an inserted vertex must be adjacent to a vertex of that triple to keep the new set connected. Enumerating the at most nine neighbours of the triple and discarding repeated or retained vertices leaves precisely the listed insertions, after testing whether the new four-set is a path or a rung square. The table is a local modular calculation valid from \(n=6\) onward; no configurations far around the cycle can appear. Hence the degree of a vertex of types \(A,B,D\) is \(6\), while the degree of type \(C\) is \(8\). Since their orbit sizes are \(2n,4n,n,2n\), the handshake lemma gives
\[
|E|=\frac{(2n+4n+2n)6+n8}{2}=28n.
\]

**5. Connectivity.** For each rim, the \(A\)-configurations of four successive vertices are joined to their one-step translates by the \(A\to A\) exchanges in the table; thus each rim gives a cycle of connected \(A\)-configurations. Every \(B\)-configuration is adjacent to an \(A\)-configuration. Every \(C\)-configuration is adjacent to \(B\)-configurations based on both rims, joining those two cycles. Every \(D\)-configuration is adjacent to a \(C\)-configuration. Thus the entire exchange graph is connected.

## Verification

Two separately written, standalone Python programs are included. `bruteforce.py` constructs the graph by explicit neighbourhood sets and exhaustively tests every labelled four-subset for connectedness and closure under all legal color changes, then independently constructs and searches its token-exchange graph. It checks \(6\le n\le15\), including all connected subsets of sizes one through three for \(6\le n\le11\). `structural.py` independently constructs the four symmetry orbits, tests their disjointness, replays forcing from representatives, and computes the complete adjacency-type counts for \(6\le n\le35\). The recorded outputs are `bruteforce.out` and `structural.out`. Run `python3 bruteforce.py 15` and `python3 structural.py 35` from the directory containing these files. The unrestricted theorem is proved symbolically above; checked finite instances are not used as a substitute for its quantifiers.

## Relationship to prior work

The minimum connected zero-forcing number \(4\) for long circular ladders is known: Premodkumar, Dominic and Chacko (2020, Proposition 22) determine the cardinality and exhibit one of the configurations of type \(B\). Brimkov and Davila (2016) introduce connected forcing and study other families. Geneson, Haas and Hogben (2020) study the token-exchange graph of *unrestricted* minimum zero-forcing sets. The present result classifies all *connected* minimum configurations of these prisms and determines their complete exchange graph size, degree distribution and connectivity. It does not assert novelty of the minimum cardinality or of token exchange itself.

## Limitations

Only the connected minimum zero-forcing configuration space is classified. Its token-exchange graph is not claimed to have a determined isomorphism type, diameter, or Hamiltonicity. The method does not classify prisms with \(n=3,4,5\) or nonminimum connected forcing sets. The literature search and comparisons support originality at best knowledge; unindexed equivalent results could exist. There has been no independent external validation.

## References

1. B. Brimkov and R. Davila, *Characterizations of the Connected Forcing Number of a Graph*, arXiv:1604.00740, first posted 2016-04-04. https://arxiv.org/abs/1604.00740
2. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658, first posted 2016-07-03. https://arxiv.org/abs/1607.00658
3. K. P. Premodkumar, Charles Dominic, and Baby Chacko, *Connected k-forcing sets of graphs and splitting graphs*, Journal of Mathematics and Computer Science 10 (2020), 656–680, Proposition 22. https://doi.org/10.28919/jmcs/4446
4. J. Geneson, R. Haas, and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first posted 2020-09-01. https://arxiv.org/abs/2009.00220
