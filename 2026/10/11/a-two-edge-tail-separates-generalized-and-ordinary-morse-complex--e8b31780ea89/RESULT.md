# A two-edge tail separates generalized and ordinary Morse complexes of \(C_4\)
## Finding
Let \(G\) be the graph with vertex set \(\{0,1,2,3,4,5\}\) and edge set \(\{01,12,23,30,04,45\}\), i.e. a four-cycle with a path of length two attached at vertex \(0\). Then the generalized Morse complex satisfies \(\mathcal{GM}(G)\simeq\bigvee^{2}S^{3}\), while the ordinary Morse complex satisfies \(\mathcal M(G)\simeq\bigvee^{4}S^{3}\). In particular, extending the single pendant edge by one further edge destroys the homotopy-type agreement between generalized and ordinary Morse complexes that holds for a cycle with a single leaf.

## Assumptions and scope
The graph is finite and simple. Its vertices are \(0,1,2,3,4,5\) and its edges are \(01,12,23,30,04,45\). A primitive vector-field pair is an incidence \((v,e)\) with \(v\in e\). A simplex of \(\mathcal{GM}(G)\) is a collection of such incidences in which no graph vertex and no graph edge occurs twice. A simplex of \(\mathcal M(G)\) is such a collection whose induced arrows \(v\to w\), for \(e=vw\), contain no directed cycle.

The claim concerns this single labeled graph; relabeling gives the same complexes. It does not assert a formula for longer cycles or longer tails.

## Proof
There are twelve primitive incidences. Exhaustive enumeration gives the nonempty face vector
\[
(12,53,106,94,30,2)
\]
for \(\mathcal{GM}(G)\), and
\[
(12,53,106,92,24)
\]
for \(\mathcal M(G)\).

Order the primitive incidences as
\[
(0,01),(1,01),(1,12),(2,12),(2,23),(3,23),(0,03),(3,03),(0,04),(4,04),(4,45),(5,45).
\]
Perform the standard staged toggle matching: at each incidence in this order, pair every still-unmatched face not containing that incidence with the face obtained by adjoining it whenever the latter face belongs to the complex. The verifier constructs every Hasse cover and orients matched covers upward and all other covers downward.

For \(\mathcal{GM}(G)\), this produces 147 matched pairs among 297 nonempty faces and leaves one critical \(0\)-simplex and two critical \(3\)-simplices. The directed Hasse graph has all 962 covers and is acyclic. Forman's theorem therefore gives
\[
\mathcal{GM}(G)\simeq\bigvee^2S^3.
\]

For \(\mathcal M(G)\), the same staged procedure produces 141 matched pairs among 287 nonempty faces and leaves one critical \(0\)-simplex and four critical \(3\)-simplices. The directed Hasse graph has all 912 covers and is acyclic. Hence
\[
\mathcal M(G)\simeq\bigvee^4S^3.
\]
The different third Betti numbers imply that the two complexes are not homotopy equivalent.

## Verification
The standalone program `verify.py` enumerates all \(2^12-1\) nonempty subsets of primitive incidences, checks the defining constraints directly, constructs the two complete face posets, performs the stated toggle matchings, and verifies acyclicity by topological sorting of the fully oriented Hasse diagrams. It independently constructs signed simplicial boundary matrices and row-reduces them over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_5\). The resulting Betti vectors are \((1,0,0,2,0,0)\) for \(\mathcal{GM}(G)\) and \((1,0,0,4,0)\) for \(\mathcal M(G)\) over each of the three fields. The captured output is in `verification_output.txt`.

## Relationship to prior work
Donovan and Scoville define the generalized Morse complex as the flag complex of discrete vector fields and record \(\mathcal{GM}(G)\cong M(\operatorname{sd}G)\). They compute generalized Morse complexes of cycles and prove that for a cycle with one attached leaf, \(\mathcal{GM}(C_t\vee\ell)\simeq\mathcal M(C_t\vee\ell)\). Their first open question explicitly asks how the generalized Morse complex can be used to understand the ordinary Morse complex. The present graph is obtained from their one-leaf test case at the smallest cycle length in their theorem, \(t=4\), by extending that leaf by exactly one edge; the equality already fails.

Donovan, Lin, and Scoville compute the ordinary Morse complex for a cycle with a single leaf and several tree families, but their stated families do not contain this unicyclic length-two-tail graph. A later theorem of Bayer, Jelić Milutinović, and Vega shows only that matching complexes of outerplanar graphs are contractible or wedges of spheres; applied through \(\mathcal{GM}(G)\cong M(\operatorname{sd}G)\), it does not supply the exact two-sphere multiplicity and says nothing about the ordinary Morse complex or the separation proved here.

## Limitations
This is an exact finite result for one natural boundary case. It does not classify all cycles with longer attached paths, and it does not claim that the factor-of-two difference persists. The novelty comparison is limited by ordinary literature-search coverage; no exhaustive theorem-index database can prove absence from all unpublished or unindexed sources.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, first public 2022-07-27; New York J. Math. 29 (2023), 1393–1412. Primary MSC 57Q70.
2. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1, first public 2019-09-25; Canadian Math. Bull. 65 (2022), 617–635.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first public 2024-11-07.
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
