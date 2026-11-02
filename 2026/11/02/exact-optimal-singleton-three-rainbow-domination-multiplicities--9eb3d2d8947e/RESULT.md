# Exact optimal singleton three-rainbow domination multiplicities of Möbius ladders

## Finding
Let \(M_n\) be the Möbius ladder with \(n\ge6\) even, obtained from the rim cycle \(C_n\) by adding the opposite chords \(v_iv_{i+n/2}\). A singleton three-rainbow dominating function is a map \(f:V(M_n)\to\{0,1,2,3\}\) for which every vertex assigned \(0\) has neighbours assigned all three distinct positive labels. Its weight is the number of nonzero labels. Write \(a_n\) for the number of minimum-weight functions with three **named** positive labels and labelled rim vertices. Then
\[
a_n=\begin{cases}
12,&n\equiv6\pmod{12},\\
6n,&n\equiv0,4,8\pmod{12},\\
\frac{9n(3n-2)}2,&n\equiv2\pmod{12},\\
\frac{9n(3n-10)}2,&n\equiv10\pmod{12}.
\end{cases}\]
The previously established minimum weights are, respectively, \(n/2\), \(n/2+1\), and \(n/2+2\). The new statement gives every corresponding optimal-function multiplicity. In particular the solution-space size changes between constant, linear, and quadratic growth as the length varies modulo twelve.

## Assumptions and scope
All graphs are finite, undirected, simple, and vertex-labelled. The order \(n\) is even and at least \(6\); \(m=n/2\). The three positive labels are distinguished, and zero means uncoloured. Only singleton rainbow domination is used: one vertex cannot carry two positive colours. The claimed multiplicity is of assignments, not of symmetry classes, and is not the classical set-valued three-rainbow domination count.

## Proof
The minimum **weight** values are established for this singleton model by Lange [1, Theorem 13] (with the corresponding set-valued precursors of Kuzman [2]); we prove the asserted exact multiplicities. We also recall the universal elementary bound: in a cubic graph every zero has three distinct nonzero neighbours, so if there are \(u\) zeros and \(c\) coloured vertices, \(3u\le3c\); hence \(c\ge n/2\). Furthermore the zero set is independent.

View \(M_{2m}\) as a two-row strip with columns \(0,1,\ldots,m-1\), each containing a rung \(u_iv_i\). Consecutive columns are connected in corresponding rows; the wrap edges are twisted, \(u_{m-1}v_0\) and \(v_{m-1}u_0\). If a zero support \(U\) is independent, each column contains at most one zero. In a consecutive run of nonempty columns its chosen rows must alternate. At the twisted wrap, two consecutive nonempty columns have the opposite relation. For any fixed support, form the *constraint graph* \(H(U)\) on coloured vertices by joining every pair of neighbours of each zero. Valid assignments of the three positive colours are exactly proper three-colourings of \(H(U)\).

**Triangle-chain lemma.** A run of \(r\ge1\) consecutive alternating zero columns induces a chain of \(r\) triangles in \(H(U)\), each new triangle sharing an edge with its predecessor and adding one vertex. Its \(r+2\) involved coloured vertices admit exactly \(3!=6\) proper three-colourings. In each one, the colours of the consecutively exposed vertices repeat with period three: the colour on a newly introduced vertex equals the colour of the vertex dropped when the triangle window advances. This follows inductively because every triangle must use all three colours.

First assume \(m\equiv3\pmod6\). Equality weight \(m\) forces \(m\) zeros, one in each column, and equality in the cubic incidence bound forces all edges to cross the zero/coloured cut. Connectedness gives exactly the two bipartition supports (the two rim parities). Fix the even zeros. Write the colours of the odd vertices as \(c_a=f(v_{2a+1})\) for \(a\in\mathbb Z/m\mathbb Z\) and set \(s=(m-1)/2\). The domination condition is that \((c_{a-1},c_a,c_{a+s})\) are all distinct for every \(a\). Since \(2s+1=m\), the conditions indexed by \(a\) and \(a+s+1\) yield \(c_{a+s+1}=c_{a-1}\). Using the condition indexed by \(a+1\) now makes \((c_{a-1},c_a,c_{a+1})\) all distinct. Consecutive triples therefore enforce \(c_{a+3}=c_a\). Conversely every period-three permutation of the labels works because \(s\equiv1\pmod3\). There are six choices for each of two supports, giving \(12\).

Next assume \(m\) even. The known optimum is \(m+1\), so each optimal zero support has \(m-1\) vertices, exactly one empty column. Its other \(m-1\) columns form one alternating run; for any position of the empty column there are two row choices, hence \(2m=n\) zero supports. The triangle-chain lemma covers all \(m+1\) coloured vertices, giving exactly six assignments per support and \(a_{2m}=12m=6n\). This includes each even \(m\ge4\), independently of its residue modulo six.

Finally suppose \(m\) is odd with \(3\nmid m\); the established minimum is \(m+2\), so an optimal support has exactly \(m-2\) zeros and **two empty columns**. Up to the rotation of column indices, let their cyclic distance be \(d\), with \(1\le d\le h=(m-1)/2\). Since \(m\) is odd, for every \(d\) there are exactly \(m\) unordered pairs of empty columns. If \(d=1\), one alternating run of length \(m-2\) remains, and there are two choices of its row phase. The triangle chain involves \(m\) coloured vertices; the other two coloured vertices are unconstrained. It contributes \(2\cdot6\cdot3^2=108\) functions for each pair of empty columns.

For \(2\le d\le h\), there are two nonempty runs, of lengths \(d-1\) and \(m-d-1\), with four choices of their two row phases. Directly comparing the choices at the endpoints of the two runs gives **two disjoint cases**. For two choices, their triangle-chain vertex sets are disjoint; all \(m+2\) coloured vertices occur in those two chains, and the count is \(6^2=36\) per choice. For the other two phase choices, the chains share exactly two coloured vertices, and two other coloured vertices are unconstrained. In the period-three propagation along the respective chains, the shared vertices occur at index separations \(d\) and \(m-d\). Since they belong to one triangle at a boundary, their labels must be distinct. They can have distinct labels consistently in both chains precisely when \(3\nmid d\) and \(3\nmid(m-d)\). If this holds, the shared ordered pair fixes the two chain colourings, yielding \(3\cdot2\cdot3^2=54\) assignments per phase choice. Otherwise the count is zero. These four cases exhaust the zero supports: the alternation of row choices within each run is forced, and the two possible endpoint matchings are obtained twice each among the four initial choices. This proves the local case table without extending a finite computation to infinitely many \(m\).

Thus, writing \(g=|\{d:2\le d\le h,\ 3\nmid d,\ 3\nmid(m-d)\}|\), the total is
\[
a_{2m}=108m+72m(h-1)+108mg.\]
If \(m=6q+1\ge7\), then \(h=3q\), the permissible distances are \(d\equiv2\pmod3\), and \(g=q\). Hence \(a_{2m}=36m(9q+1)=18m(3m-1)=9n(3n-2)/2\). If \(m=6q+5\ge5\), then \(h=3q+2\), permissible distances are \(d\equiv1\pmod3\), and \(g=q\). Hence \(a_{2m}=36m(9q+5)=18m(3m-5)=9n(3n-10)/2\). These cover the last two congruence classes and finish the proof.

## Verification
The accompanying standalone `verify.py` enumerates independent zero supports on each Möbius ladder, independently constructs the pairwise inequality graph on coloured vertices, and counts its proper three-colourings by exact recursive search. It matches the stated count for every even order from \(6\) through \(42\). Independent direct enumeration of all four-label assignments confirms the cases \(n=6,8,10\). Running `python3 verify.py` reports `VERIFY_OK`. These finite tests are corroboration only: the infinite proof is the preceding support classification and triangle-chain argument, combined with the published exact minimum weights.

## Relationship to prior work
Lange [1, Theorem 13] determines the exact singleton three-rainbow domination **number** of each Möbius ladder and provides witnesses. Kuzman [2, Theorem 4.5] determines related numbers in the classical **set-valued** rainbow domination model. Neither inspected theorem provides this family-wide enumeration of all named optimal singleton functions; the set-valued model is not interchangeable. Earlier related work on cylindrical graphs [3] concerns numerical bounds and constructions. The present result determines the new multiplicity invariant, with a constant/linear/quadratic residue-class structure and a complete structural count of feasible zero supports and colourings.

## Limitations
The result concerns only the minimum-weight coefficient, not the full weight polynomial; it does not cover non-singleton set-valued assignments, graph modifications, or functions modulo automorphisms. Literature search cannot prove absolute historical uniqueness, and an unlocated general theorem about equitable/perfect graph colourings or three-colour triangle chains might imply the count. There is no claim of independent audit or external certification.

## References
[1] P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906v1 (first publicly available 2026-10-01), Theorems 7 and 13, and Appendix A. https://arxiv.org/html/2610.06906v1

[2] B. Kuzman, *On k-rainbow domination in regular graphs*, arXiv:1907.08430v1 (2019-07-19), Theorems 3.1 and 4.5. https://arxiv.org/html/1907.08430v1

[3] J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics 14(16), 2917 (2026). https://www.mdpi.com/2227-7390/14/16/2917
