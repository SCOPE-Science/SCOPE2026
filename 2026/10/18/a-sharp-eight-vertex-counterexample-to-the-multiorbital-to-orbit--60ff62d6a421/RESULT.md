# A sharp eight-vertex counterexample to the multiorbital-to-orbital converse

## Finding
For faithful actions of the cyclic group \(C_2\) on finite simple graphs, equality of multiorbital bivariate chromatic polynomials does **not** imply equality of orbital bivariate chromatic polynomials. An explicit counterexample exists on eight vertices, and eight is the least possible number of vertices for such a counterexample.

For \(x,y\) as indeterminates, define
\[
T(x,y)=y(x-y)(x^4-4x^3-4x^2y+10x^2+12xy-16x+y^2-12y+12).
\]
Our two eight-vertex examples satisfy \(F_A(x,y)=F_B(x,y)\) but \(O_A(x,y)-O_B(x,y)=2T(x,y)\neq0\).

## Assumptions and scope
Graphs here are undirected, finite, loopless and simple before taking a quotient. Their orbit quotient graphs may have loops, which count as monochromatic edges in the bivariate chromatic polynomial. The group \(C_2=\langle\tau\rangle\) acts faithfully via \(\tau=(0\ 1)\), fixing vertices 2 through 7. Both examples have vertex set \(\{0,1,2,3,4,5,6,7\}\), and the following complete undirected edge sets:

\(E(A)=\{(0,1),(0,2),(0,3),(0,4),(0,6),(0,7),(1,2),(1,3),(1,4),(1,6),(1,7),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(6,7)\}.\)

\(E(B)=\{(0,1),(0,2),(0,4),(1,2),(1,4),(2,3),(2,4),(2,5),(2,6),(2,7),(3,4),(3,5),(3,6),(3,7),(4,5),(4,6),(5,6),(6,7)\}.\)

The bivariate chromatic polynomial \(P_G(x,y)\) counts \(x\)-colour assignments in which a monochromatic edge is allowed only when its colour is among the \(x-y\) unrestricted colours; this applies to quotient loops. Write \(Q_G=P_{G/\tau}\). For \(C_2\) the orbital and multiorbital invariants are \(O_G=(P_G+Q_G)/2\) and \(F_G=(3P_G+Q_G)/2\), respectively. The minimality statement concerns **faithful \(C_2\)-actions**, not all finite groups or arbitrary graph invariants.

## Proof
Both listed edge sets are invariant under the simultaneous swap of vertices 0 and 1, as their incident edges occur in matched pairs and their internal edge \((0,1)\) is fixed. Hence both define faithful \(C_2\)-actions.

For any graph \(G\), including quotient loops, partition its vertices into the nonempty monochromatic colour classes of a colouring. A partition with \(k\) blocks, of which \(t\) contain at least one edge (including a loop), contributes
\[
(x-y)_{\underline t}(x-t)_{\underline{k-t}}
\]
assignments, with falling factorials interpreted as polynomials. Indeed, the \(t\) edge-bearing blocks must use distinct unrestricted colours, and the other \(k-t\) blocks can use distinct colours among those still unused. Summing over all set partitions gives an exact integral-polynomial algorithm for \(P_G(x,y)\). It does not rely on finite evaluation at test colours.

The symbolic evaluation for the two displayed graphs and their seven-vertex orbit quotients gives the **polynomial identities**
\[
P_A-P_B=-2T,\qquad Q_A-Q_B=6T.
\]
Therefore
\[
F_A-F_B=\tfrac12(3(-2T)+6T)=0,\qquad
O_A-O_B=\tfrac12(-2T+6T)=2T.
\]
The second expression is nonzero; for example, at \((x,y)=(3,1)\) its value is 64. This proves failure of the proposed implication with eight vertices.

For minimality, use the complete standard atlas of unlabelled simple graphs on at most seven vertices. For each graph, enumerate every automorphism of order two, form the quotient including possible loops, and calculate exact polynomial coefficient vectors for \(3P+Q\) and \(P+Q\). Identical \(3P+Q\) vectors never give unequal \(P+Q\) vectors. No smaller faithful \(C_2\)-action can be missed: every graph of that order is isomorphic to an atlas member, and every \(C_2\)-action arises from an order-two automorphism. This finite exhaustive check uses exact integer arithmetic rather than samples. The supplied verifier reproduces the search; it considers 2729 distinct per-graph quotient-polynomial cases after removing duplicates. Since an eight-vertex counterexample exists, eight is minimal.

## Verification
The standalone \(verify.py\) executes the quotient and polynomial computations, independently reconstructs the two differences and checks the complete standard graph atlas through seven vertices. The actual recorded output is in \(verification_output.txt\). Its graph-atlas dependency is specified in \(requirements.txt\). The certificate proves only the finite minimality claim and polynomial identities; it makes no assertion about existence, uniqueness or reconstruction for other acting groups.

## Relationship to prior work
Gerling's 2026 paper introduces \(F\), proves that the ordinary orbital polynomial need not determine the multiorbital polynomial, and explicitly leaves open the converse implication treated here. The known three-vertex example gives \(O_A=O_B\) but \(F_A\ne F_B\), the reverse logical direction; it does **not** imply the present result. The current explicit eight-vertex pair witnesses \(F_A=F_B\) with \(O_A\ne O_B\). The minimality bound is additionally obtained by exhaustive exact classification of all smaller faithful involutory graph actions.

## Limitations
The finite minimum eight is for faithful \(C_2\)-actions on simple graphs. Graph quotients retain induced loops. The certificate depends on the completeness of the standard seven-vertex graph atlas and the validity of ordinary exact integer computations. This work does not classify all eight-vertex counterexamples or establish any converse implication for other group actions. Bibliographic priority beyond the primary literature searched remains subject to independent verification.

## References
Melanie Gerling, *The Multiorbital Bivariate Chromatic Polynomial: A Subgroup-Lattice Refinement*, arXiv:2609.01866, first public posting 2026-09-01; version 2 (2026-10-03) explicitly formulates the still-open converse. https://arxiv.org/abs/2609.01866

Dohmen and Lange-Geisler, work on orbital bivariate chromatic polynomials, arXiv:2009.08235 (background definitions). https://arxiv.org/abs/2009.08235

Read and Wilson, *An Atlas of Graphs*, Oxford University Press (1998), standard small-graph classification used for the exhaustive lower-order check.
