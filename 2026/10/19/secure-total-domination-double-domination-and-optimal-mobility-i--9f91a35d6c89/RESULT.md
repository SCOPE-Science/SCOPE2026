# Secure-total domination, double domination, and optimal mobility in two Paley graphs

## Finding
For the prime-order Paley graphs \(P_{13}\) and \(P_{17}\), **every** vertex subset is secure-total dominating if and only if it is double dominating. Thus the secure-total domination and double-domination generating polynomials agree coefficient by coefficient, not just at their least nonzero term. Their common minimum cardinality is \(5\), but their minimum-configuration reconfiguration graphs have radically different connectivity.

For the order-\(13\) graph the common polynomial is
\[
195z^{5}+1157z^{6}+1625z^{7}+1287z^{8}+715z^{9}+286z^{10}+78z^{11}+13z^{12}+z^{13}.
\]
For the order-\(17\) graph it is
\[
136z^{5}+4420z^{6}+15028z^{7}+23069z^{8}+24157z^{9}+19448z^{10}+12376z^{11}+6188z^{12}+2380z^{13}+680z^{14}+136z^{15}+17z^{16}+z^{17}.
\]
All lower coefficients vanish. In particular, the two graphs have exactly \(195\) and \(136\) minimum secure-total dominating sets, respectively.

Under single-token exchanges among minimum sets, \(P_{13}\) has a connected token-sliding graph with \(195\) vertices, \(663\) edges, radius \(5\), and diameter \(5\); its token-jumping graph has \(936\) edges and likewise radius and diameter \(5\). By contrast, **both** reconfiguration graphs for \(P_{17}\) are disjoint unions of exactly \(68\) copies of \(K_2\). In particular, allowing nonadjacent token jumps adds no mobility for the order-\(17\) graph.

The affine automorphisms \(x\mapsto a+bx\), with \(a\in\mathbb F_p\) and nonzero quadratic-residue \(b\), partition the order-\(13\) minimum sets into three orbits of sizes \(78,78,39\), with vertex-subset representatives \(\{0,1,3,5,7\}\), \(\{0,2,3,5,7\}\), and \(\{0,2,4,6,8\}\). The order-\(17\) minimum sets form one orbit of size \(136\), represented by \(\{0,2,3,5,10\}\). That representative has just one exchange neighbor, \(\{0,2,3,5,12\}\), which is reached by an adjacent slide as well as a jump.

## Assumptions and scope
For \(p\in\{13,17\}\), identify \(V(P_p)\) with \(\mathbb Z/p\mathbb Z\); join distinct \(u,v\) precisely when \(v-u\) is a nonzero quadratic residue modulo \(p\). Let \(N(u)\) be the **open** neighborhood and \(N[u]=N(u)\cup\{u\}\) the closed neighborhood.

A set \(S\) is *total dominating* when \(N(u)\cap S\ne\varnothing\) for every \(u\). It is *secure-total dominating* when, in addition, for every \(u\notin S\) some adjacent \(v\in S\) has \((S\setminus\{v\})\cup\{u\}\) total dominating. The replacement set need not itself be secure-total dominating. A set is *double dominating* when \(|N[u]\cap S|\ge2\) for every \(u\). A *token jump* replaces one selected vertex with any unselected vertex; a *token slide* makes this replacement along an edge. The endpoints of an admissible exchange must both be minimum secure-total dominating sets. All graph distances reported for disconnected graphs are computed within connected components.

## Proof
For every graph, secure-total domination implies closed-neighborhood double domination: a selected vertex must have another selected neighbor by total domination; an unselected vertex must have two selected neighbors, since moving its **only** selected neighbor onto it would leave the moved-in vertex without a selected neighbor. Therefore the reverse implication is the nonautomatic part of the theorem.

Define for each vertex \(u\) its integer open-neighborhood bitmask \(A_u=\sum_{v\in N(u)}2^{v}\), and let the integer \(s\in\{0,\ldots,2^p-1\}\) encode a selected subset. The following exhaustive finite recurrence-free decision rules are exact:

1. Total domination holds exactly when \(s\mathbin{\&}A_u\ne0\) for all vertices \(u\).
2. Double domination holds exactly when \(\operatorname{popcount}(s\mathbin{\&}(A_u\mathbin{|}2^u))\ge2\) for all vertices \(u\).
3. Secure-total domination holds exactly when rule 1 holds and, for each bit \(u\) absent from \(s\), some bit \(v\) in \(s\mathbin{\&}A_u\) makes the mask obtained by clearing \(v\) and setting \(u\) satisfy rule 1.

The supplied Python and independently structured C++17 enumerators evaluate rules 1–3 for every one of the \(2^{13}=8192\) and \(2^{17}=131072\) masks. Both report **zero disagreements** between rules 2 and 3. Their nonzero cardinality histograms are the coefficients above. The least positive cardinality is therefore exactly five and **all** minimum subsets are found; these are finite exhaustive computations, not extrapolations.

For each five-element subset, enumerate ordered choices of removed selected vertex and inserted unselected vertex. Retain an undirected edge precisely when the resulting subset is in the certified minimum list, and for token sliding additionally require the removed and inserted vertices to be adjacent. The exact resulting edge lists, connected components and all-source shortest-path computations are stored in the finite certificate. Two independent implementations reconstruct the same counts, component profiles, and eccentricities. The order-\(17\) five-element sets form a single orbit under the verified affine graph automorphisms: the orbit of \(\{0,2,3,5,10\}\) has \(136\) distinct members and equals the complete enumerated optimum list. Directly checking all five possible removals and twelve possible insertions for this representative leaves exactly the one neighbor \(\{0,2,3,5,12\}\), with \(10\) adjacent to \(12\). By symmetry every optimum has exactly one such neighbor, proving that both exchange graphs consist of \(68\) disjoint edges. For order \(13\), complete breadth-first search from every one of the \(195\) vertices proves the asserted connectivity, radius and diameter.

For the affine orbit claims, multiply each representative by every nonzero quadratic residue and independently translate by every field element, and compare the resulting union with the complete minimum-subset lists. The three sizes at order \(13\) are \(78,78,39\); the single order-\(17\) size is \(136\). The transformations preserve quadratic-residue differences, so they are valid graph automorphisms.

## Verification
The included `check_python.py` prints the canonical `certificate.json` by exhaustive examination, while `check_cpp.cpp` independently derives the cardinality histograms, configuration graphs, connected-component counts, and eccentricity histograms. The certificate includes all minimum subsets as integer masks, every admissible exchange edge, orbit membership, and all-source distance histograms. The two programs use only standard Python 3 and C++17 respectively. Reproduce with `python3 check_python.py > regenerated.json` and compare `regenerated.json` byte-for-byte with `certificate.json`; compile `check_cpp.cpp` using a C++17 compiler and compare its standard output with `checked_cpp.txt`. All integers are exact.

The universal equivalence claim depends on exhaustive tests for **all** subsets; the statements about exchanges depend only on the complete minimum lists. The order-\(17\) disjoint-edge conclusion also follows from the certified affine orbit and one-representative neighbor examination.

## Relationship to prior work
Secure-total domination was introduced by Benecke, Cockayne and Mynhardt (2007), and developed further in the cited foundational literature; the general relation from secure-total to double domination follows directly from their definitions. Cabrera Martínez, Montejano and Rodríguez-Velázquez (2019) study secure-total domination bounds and connections with classical graph parameters. These results do not yield the asserted coefficientwise equality and contrasting reconfiguration graphs for the two Paley graphs. Prior reports on complete multipartite graphs have a different graph class and cannot be specialized to these noncomplete Paley graphs.

## Limitations
The equivalence, coefficients, orbits and reconfiguration conclusions concern **only** the two specified graphs. They do not establish the reverse double-to-secure-total implication for arbitrary graphs or for other Paley orders. For example, the cycle \(C_6\) has a double-dominating set \(\{0,1,3,4\}\) that is not secure-total dominating. Exact finite verification does not by itself establish publication priority, and potentially relevant inaccessible or unindexed sources remain a residual literature risk. An independent external audit has not been performed.

## References
1. S. Benecke, E. J. Cockayne, and C. M. Mynhardt, *Secure total domination in graphs*, Utilitas Mathematica **74** (2007), 247–259. An available bibliographic record indicates November 2007 but not a verified exact day.
2. W. F. Klostermeyer and C. M. Mynhardt, *Secure domination and secure total domination in graphs*, Discussiones Mathematicae Graph Theory **28** (2008), 267–284, DOI `10.7151/dmgt.1405`. The dated bibliographic portal gives 2009-02-26; the journal volume bears the year 2008.
3. A. Cabrera Martínez, L. Montejano, and J. A. Rodríguez-Velázquez, *On the Secure Total Domination Number of Graphs*, Symmetry **11** (2019), 1165, DOI `10.3390/sym11091165`.
4. A. Cabrera Martínez, A. Estrada-Moreno, and J. A. Rodríguez-Velázquez, *Secure Total Domination in Rooted Product Graphs*, Mathematics **8** (2020), 600, DOI `10.3390/math8040600`. It explicitly records that secure-total domination implies double domination.
