# Six rank-four theories of finite Paley graphs, with a sharp 29-vertex bound

## Finding
Let \(q\) range over prime powers congruent to \(1\) modulo \(4\), with \(q\ge5\). Write \(P(q)\) for the Paley graph on \(\mathbb F_q\): distinct vertices \(a,b\) are adjacent when \(a-b\) is a nonzero square. In the first-order signature consisting only of equality and undirected adjacency, agreement on all sentences of quantifier rank at most four is characterized exactly by
\[
P(q)\equiv_4P(q')\quad\Longleftrightarrow\quad
\min(q,29)=\min(q',29).
\]
Thus the family has six rank-four theories, represented by the orders \(5,9,13,17,25,29\). The largest minimum representative has 29 vertices, and this bound is sharp *within the family of Paley graphs*.

A notable feature is that \(P(13)\) and \(P(17)\) realize the same isomorphism types of induced four-vertex graphs but are not rank-four equivalent; the same phenomenon holds for \(P(25)\) and \(P(29)\). Quantifier alternation, rather than mere existence of four-vertex induced subgraphs, makes the distinction.

## Assumptions and scope
The finite fields are of odd order \(q\equiv1\pmod4\); neither parameters nor field operations are named in the graph language. Define the three-extension property \(\mathrm{EC}_3\): for every triple of distinct vertices and every assignment of adjacent or nonadjacent to its three members, some fourth distinct vertex realizes that assignment. Define the following rank-at-most-four graph sentences: \(T\) asserts the existence of a triangle; \(D\) asserts the existence of an induced diamond (the four-vertex graph with five edges); \(K\) asserts the existence of a four-clique; \(U\) asserts that there are distinct vertices \(a,b,c\) with exactly the edge \(ab\) among them, such that every other vertex is adjacent to at least one of \(a,b,c\); and \(E\) asserts \(\mathrm{EC}_3\). In particular \(U\) has prefix \(\exists a\exists b\exists c\forall w\), and \(E\) has maximal quantifier nesting \(\forall a\forall b\forall c\exists w\). All five sentences have quantifier rank at most four.

The truth vectors of \((T,D,U,K,E)\) for orders \(5,9,13,17,25,29\), respectively, are \((0,0,1,0,0)\), \((1,0,1,0,0)\), \((1,1,1,0,0)\), \((1,1,0,0,0)\), \((1,1,0,1,0)\), and \((1,1,0,1,1)\). Here the entries are Boolean truth values, not counts.

## Proof
**The infinite range.** Write \(\chi\) for the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Given distinct \(a_1,a_2,a_3\) and signs \(\varepsilon_i\in\{-1,1\}\), let \(N\) count vertices \(x\) outside the triple for which \(\chi(x-a_i)=\varepsilon_i\) for each \(i\). Expanding the product of the three indicator factors gives
\[
8N=\sum_{x\notin\{a_1,a_2,a_3\}}\prod_{i=1}^3(1+\varepsilon_i\chi(x-a_i)).
\]
The constant part is \(q-3\). Each of the three single-character sums has absolute value at most two because its full-field sum is zero and two excluded values are each \(\pm1\). Each of the three two-character sums has absolute value at most two: its full-field sum is \(-1\) and the remaining excluded root contributes \(\pm1\). The three-character sum has absolute value at most \(2\sqrt q\) by the classical Weil bound for a nonsquare square-free cubic polynomial (equivalently the Hasse bound for its associated elliptic curve). Consequently
\[
8N\ge q-15-2\sqrt q>0\qquad(q>25).
\]
Every allowable prime-power order \(q\ge29\) therefore has \(\mathrm{EC}_3\). In a four-round Ehrenfeucht--Fraïssé game between any two such graphs, after at most three distinct vertices have been chosen, the duplicator realizes the same adjacency pattern at the next move using \(\mathrm{EC}_3\). Repeated vertices are matched to their already corresponding partners. For fewer than three chosen vertices, extend the specified pattern arbitrarily to three distinct vertices first. Thus all \(P(q)\) with \(q\ge29\) are rank-four equivalent.

**The five smaller orders.** The Paley parameters are \((q,(q-1)/2,(q-5)/4,(q-1)/4)\). The graph \(P(5)\) is triangle-free, while \(P(9)\) contains a triangle: the subfield \(\mathbb F_3\subset\mathbb F_9\) supplies one. At order nine each edge has only one common neighbor, so \(D\) is false, whereas the four residues \(0,1,4,10\) in \(\mathbb F_{13}\) induce a diamond, with \(0,1\) its degree-three vertices.

To separate orders 13 and 17, normalize any adjacent ordered pair to \((0,1)\) by a square-affine automorphism of the prime-field Paley graph. A third vertex forming exactly this one edge has \(\chi(c)=\chi(c-1)=-1\). At order 13 the possible values are \(c\in\{6,7,8\}\), with respectively \(1,0,1\) vertices nonadjacent to all of \(0,1,c\); thus \(U\) is true with \(c=7\). At order 17 the possible values are \(c\in\{6,7,11,12\}\), with respectively \(2,1,1,2\) common nonneighbors; thus \(U\) is false. This argument covers every one-edge triple, not merely a selected triple.

At order 17 there is no four-clique: after normalizing any adjacent pair to \((0,1)\), its common neighbors are \(c\in\{2,9,16\}\), and no such \(c\) has a further common neighbor of \(0,1,c\). At order 25 there is a five-clique given by the embedded subfield \(\mathbb F_5\): every nonzero element of \(\mathbb F_5\) is a square in \(\mathbb F_{25}\). Thus \(K\) separates 17 and 25.

Finally represent \(\mathbb F_{25}\) as \(\mathbb F_5[u]/(u^2-2)\). The vertices \(0,1,3+2u\) form a triangle having no fourth vertex adjacent to all three, as follows by enumerating the twelve nonzero squares \(\{1,1+u,1+4u,2,2+2u,2+3u,3,3+2u,3+3u,4,4+u,4+4u\}\). So \(P(25)\) is not \(\mathrm{EC}_3\), while \(P(29)\) is. The distinguishing truth vectors listed above are pairwise different; combined with the infinite-range argument, this proves all six classes and the sharp bound.

## Verification
Run `python3 verify.py` from a directory containing that file; it requires only Python's standard library. The program constructs \(P(5),P(9),P(13),P(17),P(25),P(29)\) by exact finite-field arithmetic, checks the five sentences directly, confirms the normalized one-edge-triple tables and the explicit witnesses, and independently calculates the complete rank-four logical type of each finite representative using atomic diagrams and sets of one-point extension types. It reports six pairwise different types and terminates with `VERIFY_OK`. The exact generated output is provided in `verification_output.txt`. Computation checks the finite boundary cases; it does not replace the Weil-bound proof for all higher orders.

## Relationship to prior work
Blass, Exoo, and Harary (1981) established eventual first-order adjacency extension properties of Paley graphs. Ananchuen and Caccetta (1993) established, in particular, that every Paley graph of order at least 29 has \(\mathrm{EC}_3\), as explicitly recorded in Forbes, Grannell, and Griggs (2005). The existence of this 29-threshold is therefore *not* asserted to be new. The finding here is an exact classification of all rank-four theories **including smaller orders**, with explicit alternating-quantifier separators at orders 13 versus 17 and 25 versus 29, and an optimal Paley-family representative bound. Gordinowicz and Prałat (2010) investigate the smallest general \(\mathrm{EC}_3\) graphs, not this complete logical classification.

## Limitations
No claim is made concerning richer field signatures, ranks other than four, non-Paley conference graphs, or minimum model order among arbitrary graphs. The full text of the directly relevant 1993 Networks article was not accessible during this comparison; overlap with a small-order classification there or in unindexed literature remains possible. The 29-threshold for three-existential closure is already published. The rank-four classification has not undergone independent external validation.

## References
1. A. Blass, G. Exoo, F. Harary, *Paley graphs satisfy all first-order adjacency axioms*, Journal of Graph Theory 5 (1981), 435–439, doi:10.1002/jgt.3190050414.
2. W. Ananchuen, L. Caccetta, *On the adjacency properties of Paley graphs*, Networks 23 (1993), 227–236, doi:10.1002/net.3230230404.
3. A. D. Forbes, M. J. Grannell, T. S. Griggs, *Steiner triple systems and existentially closed graphs*, Electronic Journal of Combinatorics 12 (2005), R42, published 2005-08-30, doi:10.37236/1939.
4. P. Gordinowicz, P. Prałat, *The search for the smallest 3-e.c. graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 74 (2010), 129–142.
