# Three atom-permuting qualitative representation classes for \(\mathfrak E_8^{\{3\}}\)

## Finding
Let \(\mathfrak E_8^{\{3\}}\) be the seven-colour trichromatic chromatic algebra. Classify its qualitative representations up to a bijection of the base together with an arbitrary permutation of the seven diversity atoms. Then there are exactly three classes: two on seven points and one on eight points.

The unique eight-point class is the unique perfect one-factorization of \(K_8\). Its atom-permuting automorphism group has order \(42\) and has two vertex orbits, of sizes \(1\) and \(7\). Since every seven-point representation uniquely extends to an eight-point representation, deleting a vertex from those two orbits gives exactly the two seven-point classes.

Equivalently, among the six nonisomorphic one-factorizations of \(K_8\), exactly one satisfies the qualitative requirement that every three distinct colours occur on a triangle.

## Assumptions and scope
The equivalence relation used here permits simultaneous relabelling of the seven diversity atoms. This is natural for \(\mathfrak E_8^{\{3\}}\), whose multiplication table depends only on whether three diversity colours are distinct, so every permutation of those atoms is an algebra automorphism. The result is therefore coarser than classification of representations in which every atom name is fixed pointwise.

The structural input from Al-Juaid, Jackson, Koussas and Kowalski is that a qualitative representation of \(\mathfrak E_{n+1}^{\{3\}}\) has base size \(n\) or \(n+1\), and every representation on \(n\) points extends uniquely to one on \(n+1\) points. Here \(n=7\). Their paper also gives the exact edge-colouring interpretation: monochromatic and dichromatic triangles are forbidden and every trichromatic colour triple must occur.

## Proof
Consider an eight-point qualitative representation. At each vertex the seven incident edges have pairwise distinct colours, because a repeated colour would create a monochromatic or dichromatic triangle. Hence each of the seven colours is a perfect matching, and the colouring is a one-factorization
\[
\mathcal F=\{F_1,\ldots,F_7\}
\]
of \(K_8\).

We first show that the qualitative condition is equivalent, at order eight, to \(\mathcal F\) being perfect.

Fix two factors \(F_i,F_j\). Their union is a spanning 2-regular graph, hence either an 8-cycle or two 4-cycles. If it is two 4-cycles, then a triangle containing one edge of colour \(i\) and one edge of colour \(j\) closes across a diagonal of one of those 4-cycles. There are only four such diagonals in total. Thus at most four of the five remaining colours can occur with the pair \(\{i,j\}\), so at least one required trichromatic triple is missing. Therefore every qualitative representation has \(F_i\cup F_j\cong C_8\) for all \(i\ne j\): it is a perfect one-factorization.

Conversely, suppose \(\mathcal F\) is perfect and some triple \(\{i,j,k\}\) is missing. Label the Hamiltonian cycle \(F_i\cup F_j\) cyclically as \(0,1,\ldots,7\), with the two factors alternating. An edge of \(F_k\) at cyclic distance two would close an \(i,j,k\)-triangle, so the missing-triple assumption forces \(F_k\) to avoid all cycle edges and all eight distance-two chords. There are exactly seven perfect matchings of \(K_8\) with that avoidance property. A direct finite check of those seven matchings shows that each forms two 4-cycles with at least one of the two alternating factors, contradicting perfectness. Hence every three distinct colours occur, and every perfect one-factorization gives a qualitative representation.

Seah and Stinson record that \(K_8\) has six nonisomorphic one-factorizations and, up to isomorphism, a unique perfect one-factorization. It follows that there is exactly one eight-point representation class under base and atom relabelling.

For the seven-point classes, use the unique-extension theorem of Al-Juaid et al. Any equivalence between two seven-point representations extends uniquely to an atom-permuting automorphism of their common eight-point extension. Consequently two vertex deletions of the unique eight-point class are equivalent exactly when the deleted vertices lie in the same vertex orbit of its atom-permuting automorphism group. Exact enumeration gives automorphism group order \(42\) and vertex-orbit sizes \(1\) and \(7\). Hence there are exactly two seven-point classes, and therefore three classes in total.

## Verification
The bundled `verify.py` gives a complete independent finite replay of the \(K_8\) part. It generates all 105 perfect matchings, then all 416 one-factorizations containing a fixed perfect matching. Canonicalization under vertex relabelling recovers exactly six isomorphism classes.

Across those 416 fixed-factor instances, the numbers of distinct trichromatic colour triples have distribution
\[
7^{\times2},\quad 11^{\times42},\quad 13^{\times28},\quad
17^{\times168},\quad 26^{\times112},\quad 35^{\times64}.
\]
Exactly the 64 instances with all \(\binom73=35\) colour triples are perfect one-factorizations, and they form one isomorphism class. The verifier then exhausts all \(8!\) vertex permutations of one representative, obtaining automorphism-group order \(42\) and vertex-orbit sizes \(1,7\). Finally it directly canonicalizes the eight seven-vertex deletions under \(S_7\), obtaining exactly two classes with multiplicities \(1\) and \(7\).

The current replay ends with `VERIFY_OK 164307 exact assertions`.

## Relationship to prior work
Al-Juaid, Jackson, Koussas and Kowalski classify existence for the family \(\mathfrak E_{n+1}^{\{3\}}\), prove the \(n\)-or-\(n+1\) base-size restriction, and prove unique extension from \(n\) to \(n+1\) points. The inspected article does not identify the eight-point condition with perfect one-factorizations, and searches in the article find no occurrence of “one-factorization” or “perfect one-factorization”.

The enumeration of one-factorizations is classical prior work: Seah and Stinson state that \(K_8\) has six nonisomorphic one-factorizations and a unique perfect one-factorization. Those facts are treated as prior. The retained contribution is the bridge between the qualitative trichromatic condition and perfectness at \(K_8\), together with the resulting three-class representation census and its two-orbit deletion refinement.

Targeted semantic and web searches for combinations of “chromatic algebra”, “qualitative representation”, “perfect one-factorization”, \(K_8\), and \(\mathfrak E_8^{\{3\}}\) found the two ingredient literatures but no source stating this bridge or the three-class census.

## Limitations
The equivalence “qualitative iff perfect one-factorization” is proved here only for \(K_8\). It should not be extrapolated to larger complete graphs without further work. The classification also allows permutation of diversity atoms; fixing all atom names pointwise gives a finer enumeration not claimed here.

The originality risk is mainly uncatalogued folklore: once the 2023 qualitative-representation theorem and the classical \(K_8\) one-factorization census are placed side by side, the deduction is short. The computational verifier certifies all finite \(K_8\) claims but does not re-prove the published general unique-extension theorem.

## References
1. B. Al-Juaid, M. Jackson, J. Koussas, T. Kowalski, “Edge colourings and qualitative representations of chromatic algebras”, *Journal of Algebraic Combinatorics* 58 (2023), 157–182. DOI: 10.1007/s10801-023-01251-5. First public preprint: arXiv:2201.03098, 2022-01-09.
2. E. Seah, D. R. Stinson, “On the Enumeration of One-Factorizations of Complete Graphs Containing Prescribed Automorphism Groups”, *Mathematics of Computation* 50 (1988), 607–618. DOI: 10.1090/S0025-5718-1988-0929557-1.
