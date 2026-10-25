# A 96-three-sphere stage in the mixed ternary–quaternary Hamming box

## Finding

On the vertex set \(X=[3]\times[3]\times[4]\), where \([m]=\{0,\ldots,m-1\}\), use the coordinate Hamming metric \(d(p,q)=\#\{i:p_i\ne q_i\}\). For every real \(r\ge0\), let \(R_r\) be the inclusive Vietoris–Rips complex with faces precisely the finite subsets of diameter at most \(r\). Then the **complete filtration of homotopy types** is

\[
R_r\simeq
\begin{cases}
\bigsqcup^{36}\{\mathrm{pt}\},&0\le r<1,\\
\bigvee^{40}S^1,&1\le r<2,\\
\bigvee^{96}S^3,&2\le r<3,\\
\{\mathrm{pt}\},&r\ge3.
\end{cases}
\]

Consequently, reduced integral persistence has \(35\) intervals \([0,1)\) in degree zero, \(40\) intervals \([1,2)\) in degree one, and \(96\) intervals \([2,3)\) in degree three, with no other intervals and no torsion. Most significantly,

\[
R_2=\operatorname{Ind}(K_3\times K_3\times K_4)\simeq\bigvee^{96}S^3.
\]

The integer \(96\) is the value predicted, but not proved for this case, by the conjectural sphere-count expression in [1]. The new assertion is the integral *homotopy type* of the first unequal, all-nonbinary, three-complete-factor case, not merely the predicted Euler characteristic.

## Assumptions and scope

The categorical graph product \(K_3\times K_3\times K_4\) has the same \(36\) triples as vertices and an edge between two distinct triples **if and only if all three coordinates differ**. The Cartesian graph product \(H=K_3\square K_3\square K_4\) has edges between triples that differ in exactly one coordinate. All complexes are finite abstract simplicial complexes, and homotopy equivalence refers to their geometric realizations. The theorem concerns this exact mixed-alphabet \((3,3,4)\) box, not arbitrary \((m,n,p)\) or an infinite family. The sole non-elementary ingredient is the standard acyclic-discrete-Morse matching theorem, applied to a fully specified, reproducible finite matching.

## Proof

**Zero scale and large scale.** Distinct triples have integer distances \(1,2,3\). Below scale \(1\), the complex is the discrete set of its \(36\) vertices. At and above scale \(3\), all triples span one \(35\)-simplex.

**Scale one.** Every maximal clique in \(H\) lies in a single coordinate fiber (a copy of \(K_3\), \(K_3\), or \(K_4\)): a clique of at least two vertices differs in only one fixed coordinate. There are \(12\) fibers of the first type, \(12\) of the second, and \(9\) of the third, for \(33\) contractible clique simplices. Two distinct fibers intersect at either one vertex or not at all; the natural incidence graph between \(36\) point-vertices and \(33\) fibers is connected and has \(108\) incidences (each of the \(36\) points lies in exactly three fibers). Replacing each contractible fiber simplex by a cone on its vertices realizes a graph homotopy equivalence, so the one-scale complex is homotopy equivalent to a connected graph of cycle rank \(108-(36+33)+1=40\), namely \(\bigvee^{40}S^1\).

**Scale two as an independence complex.** Every pair of distinct triples is at Hamming distance \(1,2\), or \(3\). Therefore a set of triples spans a face of \(R_2\) precisely when it contains no pair at distance \(3\); these forbidden pairs are exactly the edges in the categorical product \(G=K_3\times K_3\times K_4\). Hence \(R_2=\operatorname{Ind}(G)\), as simplicial complexes, not merely up to homotopy.

**Exact acyclic matching.** Index the triples lexicographically \((a,b,c)\), with \(a,b\in\{0,1,2\}\) and \(c\in\{0,1,2,3\}\), by integers \(0,\ldots,35\). List *all* independent vertex subsets, including the empty subset, once each by increasing-index recursion. Write \(U_0\) for that face set. At stage \(i\) in ascending order, simultaneously pair each unpaired face \(F\in U_i\) not containing vertex \(i\) to \(F\cup\{i\}\), provided both belong to \(U_i\), and delete both from the unmatched set to obtain \(U_{i+1}\). No face can enter two pairs. This exact recipe, carried out by the standalone verifier `verify.py`, produces \(30,992\) augmented faces, \(15,448\) matched pairs, and precisely \(96\) unmatched faces, **each of cardinality four**.

The verifier checks **all** \(178,704\) cover incidences of the augmented face poset. It orients unmatched incidences from upper to lower and reverses matched incidences, then topologically sorts the entire directed graph of \(30,992\) vertices. Every vertex is removed, so the directed graph is acyclic; this is an exhaustive finite acyclicity certificate, not a random search or a numerical rank test. The pair \((\varnothing,\{(0,0,0)\})\) occurs among the matches. Omitting the empty face and this single pair yields an acyclic matching on the ordinary nonempty face poset with exactly **one critical vertex and \(96\) critical three-simplices** and no others. Forman's discrete-Morse theorem gives a CW model with precisely one zero-cell and \(96\) three-cells. Their attaching maps are constant because there are no one- or two-cells, hence that CW model is a wedge of \(96\) copies of \(S^3\).

**Barcode.** In each constant-scale interval the homology groups above are torsion-free, and positive-degree homology in adjacent scale intervals occurs in disjoint degrees. Consequently all positive-degree homology maps at thresholds are zero and the interval decompositions have the stated births/deaths. In degree zero the \(36\) isolated components merge into one at scale \(1\), giving \(35\) reduced intervals \([0,1)\).

## Verification

Run `python3 verify.py` using any Python 3.9+ installation. The checker imports only the standard library, enumerates every independent face, verifies the full f-vector by cardinality

`(1, 36, 414, 2028, 4869, 6804, 6816, 5184, 3042, 1324, 396, 72, 6)`,

checks all graph adjacencies and every independent set, constructs the stated deterministic matching, verifies the full directed cover graph is acyclic, and prints `IND_K3_K3_K4_WEDGE_96_S3_VERIFIED`. The f-vector gives reduced Euler characteristic \(-96\) independently of Morse critical-cell counting. The topological theorem uses the *exact complete finite acyclicity check*, not the Euler characteristic alone. The verifiable domain has exactly \(36\) vertices; no extrapolation to untested sizes is made.

## Relationship to prior work

Camarena and Carnero Bravo [1], first public on July 23, 2023, prove a wedge-of-three-spheres homotopy theorem whenever one of the three complete-graph factors is \(K_2\) and formulate their broader all-three-factor conjecture. Their conjectural multiplicity formula already gives \(96\) when the factors are \((3,3,4)\); that predicted number is **not** claimed as a new numerical discovery. Goyal, Shukla, and Singh [2] calculate two-complete-factor products and provide the discrete-Morse framework, neither of which settles the triple with all factor sizes at least three. Adamaszek and Adams [3] study binary Hamming hypercubes, which are distinct from the mixed ternary–quaternary box. A previously indexed calculation of \(K_3\times K_3\times K_3\) [4] establishes the \(27\)-vertex equal-factor case, not the \(36\)-vertex unequal case. The assessed contribution is a complete finite homotopy proof of this next, independently motivated case plus the resulting full Rips barcode.

## Limitations

This is a finite case of the general conjecture, not its proof. The acyclicity certificate is exhaustive *only* for the \((3,3,4)\) parameter. The homotopy type does not determine equivariant group-module structure, and no such description is asserted. Literature and database comparisons are bounded: an unindexed equivalent proof, or an implication from a stronger general theorem not located, remains possible. All scientific verification here is non-independent; no independent audit or priority certification has occurred.

## References

[1] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public July 23, 2023), Section 4, Proposition 25 and Conjecture 26. https://arxiv.org/abs/2307.12401

[2] S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first public May 16, 2019), Sections 2–3. https://arxiv.org/abs/1905.06926

[3] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public March 1, 2021), Theorem 1. https://arxiv.org/abs/2103.01040

[4] *The ternary Hamming Rips filtration and the \(K_3\times K_3\times K_3\) case*, October 11, 2026; indexed public summary identifier `2026/10/11/SCOPE-the-ternary-hamming-rips-filtration-and-the-k-3-times-k-3-times--964b171a73c5`. This prior result addresses only the equal-ternary case.
