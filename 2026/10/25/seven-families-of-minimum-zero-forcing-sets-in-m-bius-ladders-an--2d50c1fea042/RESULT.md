# Seven families of minimum zero-forcing sets in Möbius ladders and their connected exchange graphs

## Finding

For every integer \(n\ge 6\), let \(M_{2n}\) be the Möbius ladder on \(\mathbb Z/(2n)\mathbb Z\), with adjacency \(i\sim i-1,i+1,i+n\). It has zero-forcing number \(Z(M_{2n})=4\). Its complete family of minimum ordinary zero-forcing sets consists of exactly seven rotation classes with the representatives in Table 1. There are precisely \(13n\) distinct minimum sets.

Let \(\mathcal R(M_{2n})\) join two minimum sets when they have exactly three vertices in common (unrestricted single-vertex token jumping). This graph is connected, has \(13n\) vertices and \(48n\) edges, and has degree enumerator
\[
4n t^5+8n t^8+n t^{12}.
\]
There is a sharp finite topological distinction despite the same first-order statistics: at \(n=6\), the exchange graph of \(M_{12}\) is not isomorphic to that of the circular ladder \(C_6\square K_2\). The two graphs both have \(78\) vertices and \(288\) edges but their sixth adjacency traces are, respectively, \(464832\) and \(464856\).

**Table 1. All representatives**, with indices read modulo \(2n\). Each type is rotated by all \(2n\) shifts, with duplicate sets counted only once.

| Type | Representative | Orbit size | Exchange degree |
|---|---|---:|---:|
| A | \(\{0,1,2,3\}\) | \(2n\) | 8 |
| B | \(\{0,1,2,n\}\) | \(2n\) | 8 |
| C | \(\{0,1,2,n+2\}\) | \(2n\) | 8 |
| D | \(\{0,1,3,n+1\}\) | \(2n\) | 5 |
| E | \(\{0,1,n-1,n\}\) | \(2n\) | 8 |
| F | \(\{0,1,n,2n-2\}\) | \(2n\) | 5 |
| G | \(\{0,1,n,n+1\}\) | \(n\) | 12 |

## Assumptions and scope

All graphs are finite, undirected, and simple. Ordinary zero forcing starts with a chosen blue vertex set. A blue vertex with precisely one white neighbor can make that neighbor blue. A set is zero forcing if a finite sequence of legal forces makes every vertex blue. Minimum means smallest possible cardinality, not inclusion-minimal. The exchange rule permits swapping any one chosen vertex with any one unchosen vertex, whether or not they are adjacent in the original graph. Every statement about the infinite family assumes integer \(n\ge6\); the nonisomorphism comparison concerns only the explicit case \(n=6\).

## Proof

**1. Minimum size and the first-force obstruction.** The graph is triangle-free and cubic. A three-vertex zero-forcing set would have to make a first force. A vertex making that first force has exactly two blue neighbors; by rotation and reflection its three selected vertices are either \(\{-1,0,1\}\) or \(\{0,1,n\}\), with a blue center \(0\). The force completes \(\{-1,0,1,n\}\). In that four-element set the center has no white neighbors, and each other blue vertex has two white neighbors. Thus no three-vertex set can force. The same argument excludes smaller zero-forcing sets. The four-vertex seeds displayed below do force, proving \(Z(M_{2n})=4\).

**2. The complete first-force classification.** Let \(S\) be any forcing four-set. At its first legal force, rotate and possibly reflect the graph to place the forcing vertex at \(0\) and its two initially blue neighbors in one of the two triples above. Write \(t\) for the remaining selected vertex. After the first force, the blue set contains
\[
B_t=\{-1,0,1,n,t\}.
\]
If \(t\notin\{2,-2,n-1,n+1\}\), the four core vertices have no forceable boundary vertex: adding \(t\) has not supplied a second blue neighbor to any of \(-1,1,n\), whose other neighbors lie precisely in that four-element candidate set. Also \(t\) cannot itself have two blue neighbors, since those would include one of \(-1,1,n\). If \(t\) is the unused third neighbor of the forcing center, that center could not have made a first force to begin with. Therefore the displayed four candidates are necessary.

They are sufficient. Reflection \(i\mapsto-i\) interchanges \(2\) with \(-2\) and \(n+1\) with \(n-1\). For \(t=2\), the blue vertex \(1\) forces \(n+1\), so it suffices to show that \(B_{n+1}\) forces the whole graph. In \(B_{n+1}=\{-1,0,1,n,n+1\}\), the first available forces include \(1\to2\), \(n\to n-1\), and \(n+1\to n+2\). Next the four boundary fronts advance via \(j\to j+1\), \(n-j+1\to n-j\), \(n+j\to n+j+1\), and \(2n-j+1\to2n-j\), beginning at \(j=2\) whenever target vertices are still white. The two fronts on each strand meet, so every vertex is eventually blue. The nondiagonal boundary indices are valid for every \(n\ge6\); when fronts meet, redundant forces are simply omitted.

The eight possible normalized straight/bent seeds and their reflections, together with rotations, yield exactly the seven classes A–G of Table 1. Reflection fixes the rotation classes A, E, G and interchanges B with C and D with F. All seven representatives are therefore forcing sets and no additional ones exist. Their rotation orbits are disjoint for \(n\ge6\); only G has a nontrivial rotational stabilizer, namely the half-turn by \(n\). Hence the count is \(6(2n)+n=13n\).

**3. Exchange incidence and degrees.** For each of the seven representatives compare it with all translated representatives, counting exactly those sharing three vertices. Rows and columns in the following table are A, B, C, D, E, F, G. The entry counts neighbors in the column class of one vertex in the row class:

\[
\begin{array}{c|rrrrrrr}
 & A&B&C&D&E&F&G\\ \hline
 A&2&2&2&1&0&1&0\\
 B&2&0&1&1&2&1&1\\
 C&2&1&0&1&2&1&1\\
 D&1&1&1&0&1&0&1\\
 E&0&2&2&1&0&1&2\\
 F&1&1&1&0&1&0&1\\
 G&0&2&2&2&4&2&0
\end{array}
\]

This table has a finite, uniform check rather than a graph-size cutoff. The entries of each representative are affine expressions \(a n+b\), with \(a\in\{0,1,2\}\) and \(-2\le b\le3\). A three-element overlap must align at least one pair of vertices, so all candidate relative rotations occur among at most sixteen pairwise differences of the two representatives. Each remaining overlap comparison is an affine congruence \(A n+B\equiv0\pmod{2n}\) with \(|B|\le12\). For \(n\ge13\), this congruence holds exactly when \(A\) is even and \(B=0\). Consequently all overlap decisions are identical for all \(n\ge13\), and checking the finite values \(6\le n\le13\) establishes the neighbor table for every \(n\ge6\). The standalone `template_certificate.py` evaluates precisely these at-most-sixteen candidate rotations for each ordered pair of classes and checks the table, including orbit disjointness and stabilizers, at those eight values; its logic is reproduced in the preceding argument. Row sums give degrees \((8,8,8,5,8,5,12)\). Accounting for the orbit sizes gives \(4n\) vertices of degree five, \(8n\) of degree eight, and \(n\) of degree twelve. By the handshake lemma the edge count is \((4n\cdot5+8n\cdot8+n\cdot12)/2=48n\).

**4. Connectivity.** The translated A-type sets \(A_j=\{j,j+1,j+2,j+3\}\) and \(A_{j+1}\) share three vertices. They form a connected spanning cycle for the A class. The incidence table shows that every B-, C-, D-, and F-type set has an A-type neighbor. Every E- and G-type set has a B-type neighbor, so also reaches the A class within two moves. Therefore the entire exchange graph is connected.

**5. A finite twist witness.** At \(n=6\), separately build the complete exchange graphs of the Möbius ladder and the circular ladder. They both have \(78\) vertices and \(288\) edges. Exact integer closed-walk dynamic programming from each root gives the respective trace vectors at lengths two through six:
\[
(576,1152,12192,60720,464832),\qquad
(576,1152,12192,60720,464856).
\]
Since the trace of the sixth power of an adjacency matrix is preserved under graph isomorphism, these exchange graphs are not isomorphic. This is a finite, exhaustive certificate, not an unproved infinite-family spectral claim.

## Verification

Two complete source programs accompany this result. `exhaustive.py` independently enumerates all four-subsets of \(M_{2n}\) for each \(6\le n\le14\), runs ordinary forcing to termination, compares with the seven orbit templates, constructs all token-jumping edges and checks connectivity and degrees. It also excludes all three-set solutions for \(6\le n\le10\). `template_certificate.py` checks the seven-class neighbor matrix and stabilizers for \(6\le n\le13\), and supplies the bounded-offset congruence reasoning proving stabilization for all larger \(n\). Its independent labeled-state construction for \(n=6\) computes the exact sixth adjacency traces in both ladder models. Outputs from actual executions are `exhaustive_output.txt` and `template_output.txt`. The infinite-family statements rest on the symbolic first-force and congruence arguments, not merely finite enumeration.

## Relationship to prior work

The AIM Minimum Rank–Special Graphs Work Group introduced zero forcing in 2008. Duong, Kroschel, Riddell, Vander Meulen and Van Tuyl explicitly state and prove \(Z(M_{2n})=4\) for \(n\ge3\) (Theorem 5.2 in their 2019 preprint) and treat Möbius ladders as cubic circulants, without classifying the minimum sets or their exchanges. Geneson, Haas and Hogben defined precisely the token-jumping zero-forcing reconfiguration graph and proved general results (2020 preprint), without a Möbius-ladder census. The circular-ladder case has the same total \(13n\), degree enumerator and edge count, but it is a different base graph; the finite sixth-trace witness demonstrates that these numerical coincidences do not identify the exchange graphs. The present theorem is not implied by a cardinality result, generic connectivity of forests, or results about circular ladders.

## Limitations

This theorem is confined to the stated family and to minimum ordinary zero-forcing sets. The one-step rule is token jumping, not token sliding. It does not determine exchange diameters for all \(n\) or establish spectral nonisomorphism for all \(n\); nonisomorphism is proved only for \(n=6\). No claim is made about novelty beyond the inspected and searched literature, which may omit unindexed tables or equivalent generalized theorems. The foundational 2008 publisher text was not retrievable from the accessible lawful routes, although its specific known result is confirmed by the fully inspected 2019 preprint.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
2. L. Duong, B. K. Kroschel, M. Riddell, K. N. Vander Meulen, A. Van Tuyl, *Maximum nullity and zero forcing of circulant graphs*, arXiv:1906.03079v1 (7 June 2019), especially Theorem 5.2.
3. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (1 September 2020), especially Sections 1–2.
