# A two-slack reconfiguration transition in powers of cycles

## Finding
Let \(r\geq 2\), \(m\geq 2\), \(s\in\{0,1,2\}\), and put \(L=(r+1)m+s\). Write \(G=C_L^r\) for the graph with vertex set \(\mathbb Z/L\mathbb Z\) in which two distinct vertices are adjacent when their cyclic distance is at most \(r\). Define \(\mathcal R(G)\) to have as vertices **all maximum-cardinality independent vertex sets** of \(G\), with two sets adjacent when one selected vertex can be exchanged for one unselected vertex while remaining independent. Then \(\alpha(G)=m\) and:

1. If \(s=0\), \(\mathcal R(G)\cong (r+1)K_1\): precisely \(r+1\) isolated maximum sets.
2. If \(s=1\), \(\mathcal R(G)\cong C_L\): precisely \(L\) configurations, arranged in one cycle.
3. If \(s=2\), \(\mathcal R(G)\) is a **connected, four-regular** graph with precisely \(L(m+1)/2\) configurations, \(L(m+1)\) exchange edges, and **exactly \(L\) triangles**.

In all three cases every admissible single-vertex exchange moves its vertex along an edge of \(G\). Thus the token-jumping and token-sliding reconfiguration graphs coincide; equivalence for maximum independent sets is known much more generally and is not itself asserted as new.

In particular, an \(n\)-antiprism graph is \(A_n\cong C_{2n}^2\). For \(n\geq3\), the three residues \(n\bmod3\) give, respectively, \(3K_1\) (remainder zero), a connected four-regular graph with \(n(2n+1)/3\) vertices and exactly \(2n\) triangles (remainder one), or \(C_{2n}\) (remainder two).

## Assumptions and scope
All graphs are finite, simple and undirected. The condition \(m\geq2\) excludes single-token degeneracies, and \(r\geq2\) ensures that a jump across two consecutive cycle edges is a legal token slide. The formula holds for all parameter pairs in the specified ranges, not merely the computationally checked examples. The circumference \(L\) is at least \(2r+2\), so the two clockwise arcs between consecutive selected vertices have their usual unambiguous cyclic-gap meaning.

An independent set \(S\) of cardinality \(m\) is written in cyclic order \(x_1,\ldots,x_m\). Its clockwise gaps are \(d_i=x_{i+1}-x_i\pmod L\), with \(x_{m+1}=x_1\). Independent sets are exactly those with \(d_i\ge r+1\) for all \(i\). Define nonnegative slack values \(g_i=d_i-(r+1)\); they sum to \(s\).

## Proof
**Maximum size and counting.** Each selected vertex requires a clockwise gap of at least \(r+1\), so \(|S|\le\lfloor L/(r+1)\rfloor=m\). Distributing the \(s\) surplus positions over \(m\) gaps constructs an independent set of cardinality \(m\), proving equality. Counting pairs of a maximum set and a distinguished selected vertex gives
\[
 m\,|V(\mathcal R)|=L\binom{m+s-1}{s}.
\]
For \(s=0,1,2\), this gives, respectively, \(r+1\), \(L\), and \(L(m+1)/2\) configurations.

**All exchanges are local.** Let \(S,T\) be maximum sets with \(|S\cap T|=m-1\), and fix their common selected subset \(U\). The gaps between consecutive vertices of \(U\) each have length at least \(r+1\), and their sum is \(L=(r+1)m+s\). At most one such gap can have length at least \(2(r+1)\), since two such gaps would force total length at least \((m+1)(r+1)>L\). Inserting the one missing vertex must occur in that unique long gap. Its feasible insertion positions form a consecutive interval of length at most \(s+1\le3\). Therefore the removed and inserted vertices have cyclic distance at most two and are adjacent in \(C_L^r\). Conversely, any movement described below that leaves all gaps at least \(r+1\) is a valid exchange.

**Degree and edges.** Moving a selected vertex one step clockwise transfers one unit of slack from its following gap to its preceding gap; moving it counterclockwise does the opposite. A gap with \(g_i=1\) supplies one legal unit slide at either end (two moves); a gap with \(g_i=2\) supplies moves of length one and two at either end (four moves). These candidate moves give distinct neighboring configurations because \(m\ge2\) and the minimum circumference is six (at least eight when \(s=2\)). When \(s=0\), all degrees are zero. When \(s=1\), every degree is two. When \(s=2\), either one gap contains two slack units or two gaps each contain one, and every degree is four. Thus the \(s=2\) graph has \(L(m+1)\) edges.

**Connectedness.** Each legal unit slide moves one slack unit between consecutive gap positions. Starting at any configuration with \(s=1\) or \(s=2\), such slides can collect all units into a single gap. A configuration with a unique nonzero gap is a rotation of the canonical configuration whose successive gaps are \(r+1+s,r+1,\ldots,r+1\). There are exactly \(L\) such rotations: the unique enlarged gap rules out a nontrivial rotational stabilizer. Circulating one unit of slack once around all \(m\) gaps, via consecutive legal unit slides, moves each selected vertex one cycle position in the same direction while restoring the gap pattern. Therefore all \(L\) rotated configurations are mutually reachable. Together with collection of slack this proves connectedness for \(s=1,2\). Since the \(s=1\) graph is connected, two-regular and has \(L\ge7\) vertices, it is \(C_L\).

**Triangles.** Suppose \(s=2\). Any three pairwise adjacent \(m\)-subsets must share a common \((m-1)\)-subset: otherwise their union contains \(m+1\) vertices and all of its pairs occur together in one of the three independent sets, contradicting maximality of \(m\). Relative to this common subset, the three replacement positions lie in the unique feasible interval of at most three consecutive cycle positions, as established above. Thus a triangle necessarily consists of the three choices in an interval of exactly three sites and contains precisely one exchange of cyclic displacement two. Conversely, every legal displacement-two exchange has the legal intermediate one-step position and hence completes a unique triangle. Displacement-two exchanges occur exactly when some gap has slack two. There are exactly \(L\) maximum configurations of this kind, by the distinguished-token/gap count (\(m\) choices of enlarged gap for each of \(L\) starting points, divided by \(m\)). Each has two displacement-two neighbors, both again with a single slack-two gap. Hence there are \(L\) such edges, and therefore exactly \(L\) triangles.

## Verification
Two standalone Python 3 standard-library programs accompany this result. `verify_bruteforce.py` constructs independent sets directly from the adjacency relation of each power of a cycle, without using the gap classification. It checks 36 cases \(2\le r\le5\), \(2\le m\le4\), \(0\le s\le2\). `verify_gaps.py` independently generates gap compositions and computes all local exchange neighbors, covering 162 cases \(2\le r\le7\), \(2\le m\le10\), \(0\le s\le2\). Both were executed, and their outputs are embedded in the package. Their finite tests corroborate but do not establish the all-parameter theorem; the preceding proof does.

## Relationship to prior work
The identification of antiprisms with squares of even cycles, their independence polynomials, and their independence numbers are standard; see MathWorld and its earlier references. The general study of token-jumping/token-sliding independent-set reconfiguration was initiated in the literature exemplified by Kamiński, Medvedev and Milanič (2010/2012). Avis and Hoang (2022/2023) study the structure of token-sliding reconfiguration graphs and note the general equivalence of jumps and slides for maximum independent sets. None of the inspected relevant passages gives the three-regime exchange-graph classification or the four-regular and triangle-count conclusions for the two-slack cycle powers. The vertex-count formulas by themselves are consequences of established independence-set enumeration, so they are included for context and **not** claimed as the new contribution.

## Limitations
The result concerns only maximum independent sets of the cycle powers with surplus \(s\le2\), not arbitrary-size independent sets or larger slack, and does not determine the exact diameter of the four-regular exchange graphs. The primary-literature comparison is not exhaustive across inaccessible and unindexed sources, so priority remains provisional. No independent external scientific audit has been performed.

## References
- M. Kamiński, P. Medvedev, M. Milanič, *Shortest paths between shortest paths and independent sets*, arXiv:1008.4563, first publicly submitted 2010-08-26; subsequent journal treatment of independent-set reconfiguration in *Theoretical Computer Science* **439** (2012), 9–15.
- D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (2022; revised 2023), *Graphs and Combinatorics* **39** (2023), article 59.
- E. W. Weisstein, *Antiprism Graph*, MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html (background graph identification and preexisting enumeration data).
