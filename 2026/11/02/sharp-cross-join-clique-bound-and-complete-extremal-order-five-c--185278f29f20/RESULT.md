# Sharp cross-join clique bound and complete extremal order-five classification

## Finding

Let \(\mathcal C_n\) be the simple graph whose vertices are binary de Bruijn cycles of order \(n\), considered up to cyclic rotation, and where an edge joins two cycles when one cross-join operation transforms one into the other. For every integer \(n\ge4\),
\[
\omega(\mathcal C_n)\le 2^{n-1}-2.
\]
The bound is sharp at orders four and five. In particular,
\[
\boxed{\omega(\mathcal C_5)=14,\qquad \#\{K_{14}\text{ subgraphs of }\mathcal C_5\}=16.}
\]
At order four, there are exactly four maximum cliques of size six. Moreover, every clique of size at least five has a star-shaped description in feedback-table coordinates (proved below). The order-five classification covers all \(2048\) cycles, not only a selected family. The phrase “exactly sixteen” counts distinct fourteen-vertex subsets; cliques are not counted modulo reversal, complement, or any other additional symmetry.

## Assumptions and scope

A binary order-\(n\) de Bruijn cycle is a binary cyclic word of length \(2^n\) containing each binary length-\(n\) word exactly once as a cyclic factor. A cross-join exchanges the successors of two different conjugate-state pairs and yields another full de Bruijn cycle. Each vertex is a cycle modulo rotation, with the bit labels fixed.

Set \(V=2^{n-1}\). The feedback rule for a cycle is the unique bit table \(m=(m_u)_{0\le u<V}\) for which the successor of the \(n\)-bit state \(xu\), with \(x\in\{0,1\}\) and \(u\) a fixed-width \((n-1)\)-bit suffix, is \(u(x\oplus m_u)\). The table is represented as the integer \(\sum_{u=0}^{V-1}m_u2^u\). It is a valid table precisely when this successor permutation has a single orbit of length \(2^n\). For every valid table \(m_0=m_{V-1}=1\), so only the \(q=V-2\) interior entries are variable.

## Proof

**First, the universal upper bound.** Let \(K\) be a clique and fix one table \(m\in K\). For each other table \(m'\in K\), a single cross-join means that the symmetric difference of the two tables consists of a two-element subset \(S_{m'}\) of the \(q\) interior indices. Indeed, a successor interchange at one conjugate-state pair toggles exactly one feedback bit; two such interchanges are precisely a cross-join when the result remains one full cycle. Conversely, two valid full-cycle tables differing at two such entries are related by a cross-join.

If \(m'\) and \(m''\) are two different neighbors in \(K\), their symmetric difference must likewise contain exactly two entries. Thus \(|S_{m'}\cap S_{m''}|=1\). An intersecting family of two-element subsets of a \(q\)-set either is a star (every set contains a single fixed index) or consists of at most the three edges of a triangle. To see this, choose \(\{a,b\}\) and \(\{a,c\}\); any set omitting \(a\) must be \(\{b,c\}\), which forbids any further distinct set compatible with all three. Therefore \(|K|-1\le\max(q-1,3)\), giving \(|K|\le q\) when \(n\ge4\), since then \(q\ge6\). The same argument proves that any clique of size at least five is described, relative to each vertex, by pairwise changes sharing one fixed coordinate.

**Second, the finite extremal count.** For order five, \(V=16\) and \(q=14\). A clique attains size fourteen if and only if there exist a valid table \(m\) and an interior index \(i\in\{1,\ldots,14\}\) for which all thirteen tables
\[
 m\oplus 2^i\oplus 2^j\quad (j\in\{1,\ldots,14\}\setminus\{i\})
\]
are valid. Each such choice produces the clique consisting of the original table and those thirteen toggled tables. The exhaustive procedure in `verify_cliques.py` checks the full set of \(2^{16}\) Boolean tables using the one-orbit criterion. Exactly \(2048\) are valid, and there are exactly \(224\) valid ordered choices \((m,i)\) of this form. A fourteen-clique has fourteen vertices; relative to each vertex its thirteen distinct two-bit changes have a unique common index (thirteen is greater than three), so each fourteen-clique contributes exactly fourteen choices \((m,i)\). Consequently there are exactly \(224/14=16\) different fourteen-cliques.

For a concrete certificate take \(m=\mathtt{0x82c7}\) and \(i=11\). The fourteen decimal-unambiguous hexadecimal masks of its clique are

`0x82c7, 0x88c7, 0x8a47, 0x8a87, 0x8ac3, 0x8ac5, 0x8acf, 0x8ad7, 0x8ae7, 0x8bc7, 0x8ec7, 0x9ac7, 0xaac7, 0xcac7`.

Every listed mask generates one full 32-state orbit; every two masks in the list differ at exactly two feedback entries. The first mask generates the cyclic word `00000110101100010100111110111001`, starting at the all-zero state. Repeating the same computation at order four gives \(16\) valid tables, \(24\) rooted maximum-clique certificates, and \(24/6=4\) distinct six-cliques.

## Verification

Run `python3 verify_cliques.py` with Python 3; no external packages or input data are required. The program enumerates all Boolean feedback tables through order five, and independently enumerates all outgoing-edge priority choices for Euler tours of the order-\((n-1)\) binary de Bruijn digraph. Both methods yield identical cycle sets: two, sixteen, and 2048 cycles at orders three, four, and five. For any suffix \(u\), the two possible initial bits yield two length-\((n+1)\) factors determined by the feedback-table entry \(m_u\). Flipping this bit replaces exactly those two factors by the disjoint alternative pair. Hence two masks whose Hamming distance is \(h\) have exactly \(2^n-2h\) common cyclic length-\((n+1)\) factors; in particular exactly \(2^n-4\) such factors is equivalent, for two distinct full-cycle masks, to one cross-join. A separate graph construction infers adjacency from direct intersections of cyclic \((n+1)\)-factor sets (exactly \(2^n-4\) common factors for adjacent cycles). A generic Bron–Kerbosch maximal-clique enumeration on this independently constructed graph returns sixteen fourteen-cliques, exactly the same sixteen vertex sets as the feedback-coordinate construction. It also independently returns four six-cliques at order four and verifies the displayed witness edge by edge. These are finite exhaustive checks, rather than evidence for an unproved all-order equality.

## Relationship to prior work

Cross-join transformations and the connectivity of binary de Bruijn cycles are established by Mykkeltveit and Szmidt [1,2]. Alhakim [3] establishes Hamiltonian paths in the cross-join graph and explicitly tabulates the degree frequencies of its 2048 order-five vertices. Ezerman, Fahreza, and Szmidt [4] give feedback-table perturbation distributions and a diagram for the smaller order-four cross-join graph. These results are the starting point, not claims of novelty here. The present classification concerns a different invariant: simultaneous pairwise adjacency of large collections of cycles, especially maximum complete subgraphs. Neither the published degree frequencies nor the single-reference distance polynomial alone determines these mutual-adjacency patterns. The all-order upper bound and exact order-five maximum-clique count are not stated in the inspected relevant sections of those sources.

## Limitations

The upper bound and star characterization apply to all binary orders at least four. Sharpness is established only for orders four and five; the exact clique number for order six and above is not determined. The exact count sixteen is specific to order five. The code gives an exhaustive finite certificate only, and no independent mathematical audit or conclusive historical-priority certification is asserted. Other unindexed work on interlacement and cross-join clique structure could contain related conclusions.

## References

1. J. Mykkeltveit and J. Szmidt, *Nonlinear Feedback Shift Registers and Joining of Cross-Pairs States*, Studia Bezpieczeństwa Narodowego 6(2), published December 5, 2014, https://doi.org/10.37055/sbn/135237 .
2. J. Mykkeltveit and J. Szmidt, *On cross joining de Bruijn sequences*, Cryptology ePrint Archive 2013/760, https://eprint.iacr.org/2013/760 . The archive records a 2013 receipt date; the exact initial public-posting day was not independently established.
3. A. Alhakim, *Hamiltonicity of the Cross-Join Graph of de Bruijn Sequences*, arXiv:1805.12059 (May 30, 2018), https://arxiv.org/abs/1805.12059 .
4. M. F. Ezerman, A. A. Fahreza, and J. Szmidt, *Perturbations of Binary de Bruijn Sequences*, BFA 2018, June 20, 2018, https://www.researchgate.net/publication/326436065_Perturbations_of_Binary_de_Bruijn_Sequences .
