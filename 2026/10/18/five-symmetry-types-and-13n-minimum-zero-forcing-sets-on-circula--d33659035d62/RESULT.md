# Five symmetry types and \(13n\) minimum zero forcing sets on circular ladders

## Finding
For each integer \(n\ge5\), let \(G_n=C_n\square K_2\) be the labeled circular ladder (prism), and let \(Z(G_n)\) denote the zero forcing number under the standard color-change rule. Then
\[
Z(G_n)=4,\qquad z(G_n;4)=13n.
\]
Here \(z(G_n;4)\) counts distinct four-vertex zero forcing sets, with no quotient by graph symmetry. More precisely, the minimum zero forcing sets form exactly five orbits under the dihedral rotations/reflections of the cycle and simultaneous exchange of the two layers. The orbit sizes, in order below, are \(2n,4n,4n,n,2n\). Thus the first nonzero coefficient of the zero forcing polynomial is \(13n\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Write \(u_i=(i,0)\) and \(v_i=(i,1)\) for \(i\in\mathbb Z/n\mathbb Z\). Edges are \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\), with cycle indices interpreted modulo \(n\). A blue vertex with exactly one white neighbor may make that neighbor blue. A zero forcing set is an initial set of blue vertices from which repeated legal forces color every vertex blue. The statement concerns exactly \(n\ge5\) and minimum sets, not the complete zero forcing polynomial.

Representatives of the five orbits are:
\[
\begin{aligned}
A&=\{u_0,u_1,u_2,u_3\},\\
B&=\{u_0,u_1,u_2,v_0\},\\
C&=\{u_0,u_1,u_3,v_1\},\\
D&=\{u_0,u_1,v_0,v_1\},\\
E&=\{u_0,u_1,v_0,v_{-1}\}.
\end{aligned}
\]
The acting group has order \(4n\). Its stabilizer orders on these representatives are respectively \(2,1,1,4,2\).

## Proof
**Lower bound.** Every vertex has degree three, hence a set of fewer than three blue vertices cannot start forcing. Suppose three blue vertices permit an initial force. Its forcing vertex must have two blue neighbors, so by symmetry the three blue vertices form either a horizontal length-two path \(\{u_0,u_1,u_2\}\), or a rung angle \(\{u_0,u_1,v_0\}\). In the first case the only initial force is \(u_1\to v_1\); in the second it is \(u_0\to u_{-1}\). Directly from the listed adjacency relations, none of the four blue vertices remaining after that first force has exactly one white neighbor, because \(n\ge5\). Thus a three-vertex set cannot force the graph. Consequently \(Z(G_n)\ge4\).

**Necessity for a four-set.** A successful four-set must have some first force. Choose its blue forcing vertex and the two blue neighbors witnessing that force. By an automorphism, these three blue vertices are either \(\{u_0,u_1,u_2\}\) or \(\{u_0,u_1,v_0\}\); call the fourth initial vertex \(d\). The first force and the possibilities allowing at least one subsequent force are exactly:

| Three initial vertices | First force | Necessary possible locations of \(d\) for another force |
| --- | --- | --- |
| \(\{u_0,u_1,u_2\}\) | \(u_1\to v_1\) | \(u_{-1},u_3,v_0,v_2\) |
| \(\{u_0,u_1,v_0\}\) | \(u_0\to u_{-1}\) | \(u_2,u_{-2},v_1,v_{-1}\) |

To verify the table, list the blue vertices immediately following the designated first force and inspect their three neighbors. In the first row these are \(u_0,u_1,u_2,v_1,d\). The only candidates making any vertex have one white neighbor are the four locations shown: they supply a second blue neighbor to \(u_0\), \(u_2\), or \(v_1\). In the second row the blue vertices are \(u_0,u_1,v_0,u_{-1},d\); a subsequent force requires one of the locations shown, supplying the necessary extra blue neighbor to \(u_1\), \(v_0\), or \(u_{-1}\). Any other \(d\) leaves no legal force. These neighborhood checks hold modulo \(n\) for every \(n\ge5\), including the short-cycle wraparound cases. The eight allowed cases reduce under rotations, reflections, and layer exchange to the five representatives \(A,B,C,D,E\).

**Sufficiency.** Each representative forces two adjacent complete rungs:

- From \(A\), use \(u_1\to v_1\) and \(u_2\to v_2\).
- From \(B\), use \(u_0\to u_{-1}\) and \(u_1\to v_1\); rungs zero and one are then complete.
- From \(C\), use \(u_1\to u_2\) and \(u_2\to v_2\).
- For \(D\), rungs zero and one are complete initially.
- From \(E\), use \(v_0\to v_1\), completing rungs zero and one.

Once two adjacent rungs are blue, the endpoints of this two-rung block each have their rung-mate and inward horizontal neighbor blue and can force their respective outward horizontal neighbors. Iterating expands the blue block until both cyclic layers are all blue. Hence every representative, and thus every set in its orbit, is zero forcing. The lower bound gives \(Z(G_n)=4\).

**Counting.** Distinct orbit types have, respectively, four selected vertices in a single layer; three in one layer forming three consecutive vertices; three in one layer with exactly one adjacency; two in each layer occupying the same two rungs; and two in each layer occupying adjacent rung-pairs with one rung in common. These descriptions are mutually exclusive for \(n\ge5\). Counting dihedral and layer-exchange images of the representatives gives stabilizer orders \(2,1,1,4,2\) in the group of order \(4n\). By orbit-stabilizer their sizes sum to \(2n+4n+4n+n+2n=13n\). This exhausts all four-vertex zero forcing sets.

## Verification
The standalone Python 3 program `verify.py` constructs the graph directly from adjacency lists, executes the standard simultaneous-round color-change closure, independently generates all five symmetry orbits, and tests complete equality between the predicted and exhaustive four-set collections for every \(5\le n\le15\). It also exhaustively excludes successful three-vertex sets in those instances, checks orbit sizes and constructive forcing for \(5\le n\le19\), and verifies representatives' complete orbits at \(n\in\{20,30,50,100\}\). `verification_output.txt` gives the observed counts. These finite checks corroborate rather than replace the uniform proof.

## Relationship to prior work
Boyer et al., *The zero forcing polynomial of a graph* (arXiv:1801.08910v1, first public 2018-01-26), introduced the count \(z(G;k)\), derived general coefficients and exact polynomials for paths, cycles, wheels, and threshold graphs, and studied general structural properties. Its accessible full text does not state the five orbit classes or the prism count above. Curtis et al., *Zero Forcing with Random Sets* (arXiv:2208.12899v1, first public 2022-08-27), studied random-set forcing probabilities and general inequalities involving \(z(G;k)\), rather than an exact prism enumeration. Related indexed findings on zero forcing in fans, friendship graphs, and spider trees concern different graph families; indexed studies of circular ladders address other invariants. No implication from these checked sources to the claimed exact count was identified. This search does not prove global novelty.

## Limitations
The result covers standard (not positive-semidefinite, skew, or connected) zero forcing and the first nonzero polynomial coefficient, not all coefficients or propagation-time distributions. It does not classify the four-vertex forcing sets when \(n=3\) or \(n=4\), where special small-cycle effects occur. Equivalent results in literature not indexed or not inspected remain possible. No independent mathematical review has occurred.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018-01-26), https://arxiv.org/html/1801.08910v1.
2. B. Curtis, L. Gan, J. Haddock, R. Lawrence, S. Spiro, *Zero Forcing with Random Sets*, arXiv:2208.12899v1 (2022-08-27), https://arxiv.org/pdf/2208.12899.
