# Two-primary Moore summand in the cap complex of binary projective three-space

## Finding

Let \(V=\mathbb F_2^4\setminus\{0\}\), the fifteen points of \(\operatorname{PG}(3,2)\). Define \(K\) as the abstract simplicial complex of all subsets \(A\subseteq V\) containing no three distinct points on one projective line. Then

\[
K\simeq M(\mathbb Z/2\mathbb Z,3)\vee\bigvee^{77}S^4.
\]

Here \(M(\mathbb Z/2\mathbb Z,3)=S^3\cup_{\deg 2}e^4\). Thus

\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=3,\\
\mathbb Z^{77},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]

The torsion summand is essential: this is not a wedge of spheres.

## Assumptions and scope

Represent each nonzero vector by its integer label \(1,\ldots,15\), using the usual four-bit binary coordinates. A projective line has the form \(\{a,b,a\oplus b\}\), for distinct nonzero labels \(a,b\); \(\oplus\) is bitwise XOR. There are exactly 35 distinct line triples. A nonempty subset is a face precisely when it contains none of these triples. No restriction to linearly independent subsets is imposed: caps can have as many as eight points, so \(K\) is not the independence complex of the projective-geometry matroid.

Every subset is enumerated, not sampled. The complete nonempty face vector, in dimensions zero through seven, is

\[
(15,105,420,945,1008,420,120,15).
\]

The maximal caps consist of 168 five-point caps and 15 eight-point caps. Hence this natural complex is nonpure.

## Proof

Write each subset as a 15-bit mask; its bit at position \(i-1\) represents point \(i\). Starting with all nonempty faces, process the points \(i=1,\ldots,15\) in order. At stage \(i\), pair every still-unmatched face \(F\) omitting \(i\) with \(F\cup\{i\}\) when both are still unmatched. Remove both from consideration. Every stage uses disjoint pairs. The executable certificate constructs all 1,484 pairs directly from this rule.

Orient every incidence between a face and a codimension-one face downward, except matched incidences, which are oriented upward. Direct topological sorting of the entire directed incidence graph (3,048 nodes and 13,770 arcs) reaches every node. Thus the matching is acyclic. The critical cells are exactly one vertex, one three-cell and 78 four-cells; there are no other critical cells. By discrete Morse theory, \(K\) is homotopy equivalent to a CW complex with precisely these cells. Its three-skeleton is \(S^3\).

It remains to compute the integral attaching degrees of the 78 critical four-cells. Give each simplex the orientation of its increasingly ordered vertex labels. For a codimension-one incidence \(F\subset U\), denote the signed incidence by \(\epsilon(F,U)\in\{+1,-1\}\), equal to \((-1)^j\) when the deleted vertex occupies zero-based position \(j\) in \(U\).

The critical three-cell is represented by mask 534. Define the signed gradient-path projection \(P\) on three-faces recursively. It equals 1 on mask 534; it equals 0 when the three-face is the upper partner of a two/three pair; and if the three-face \(F\) is the lower partner of the four-face \(U\), set

\[
P(F)=-\epsilon(F,U)\sum_{G\subset U,\,\lvert G\rvert=4,\,G\ne F}\epsilon(G,U)P(G).
\]

The acyclic directed incidence graph makes this recursion finite. For each critical four-face \(U\), its Morse attaching coefficient is

\[
d(U)=\sum_{F\subset U,\,\lvert F\rvert=4}\epsilon(F,U)P(F).
\]

The exact, fully enumerated coefficient multiset is

\[
\{-2\text{ (15 times)},\ 0\text{ (44 times)},\ 2\text{ (19 times)}\}.
\]

Consequently the unique nontrivial Morse boundary \(\partial_4:\mathbb Z^{78}\longrightarrow\mathbb Z\) has image \(2\mathbb Z\). Elementary integer column operations take its coefficient row to \((2,0,\ldots,0)\). Because every attaching map \(S^3\to S^3\) is classified by its degree, the four-dimensional CW complex has the asserted homotopy type: one degree-two Moore attachment and 77 trivial four-sphere attachments.

## Verification

Run `python3 verify_pg32.py` using Python 3.9 or later; it has no external dependencies. The verifier reconstructs all 35 line triples, all nonempty faces, the 1,484 pairs and their entire directed incidence graph. It recomputes the signed Morse coefficients and greatest common divisor. Separately, it computes ordinary simplicial boundary ranks over \(\mathbb F_2\) in all positive dimensions and over \(\mathbb F_3\) in dimensions three through five. The direct ranks over \(\mathbb F_2\) are \((14,91,329,615,315,105,15)\); the corresponding ranks in dimensions three through five over \(\mathbb F_3\) are \((329,616,315)\). These field computations corroborate, but do not replace, the exact integer attaching-degree calculation.

The file `verification_output.txt` records one complete execution. The signed boundary calculation, not merely the Betti numbers, is the certificate of the Moore-space summand.

## Relationship to prior work

Grynkiewicz and Lev [1] investigate caps, complete caps, and minimal saturating sets in binary projective spaces. Their binary-vector description agrees with the forbidden-triple condition used here, but the reported theorems classify additive/geometric subsets rather than the homotopy type of the entire downward-closed cap complex. Superdock [2] studies topological complexes assembled from projective **planes** and colored configurations; its facet construction differs from the cap complex of three-dimensional binary projective space. Discrete Morse theory [3] supplies the homotopy-preserving reduction used above. No homotopy classification of this exact 15-vertex cap complex was identified in the inspected primary literature; the possibility of an unindexed equivalent computation remains.

## Limitations

This is an exact finite classification for \(\operatorname{PG}(3,2)\) only, not a theorem for all binary projective spaces or arbitrary Steiner triple systems. The proof depends on a complete, deterministic finite certificate whose source is included. A successful program execution is not independent mathematical review. Searches cannot rule out an unindexed equivalent result.

## References

[1] D. J. Grynkiewicz and V. F. Lev, *1-Saturating Sets, Caps and Round Sets in Binary Spaces*, arXiv:0811.1322 (first version 2008-11-09); journal development: *1-Saturating Sets, Caps, and Doubling-Critical Sets in Binary Spaces*, SIAM J. Discrete Math. 24 (2010), 169–190, DOI:10.1137/090747099.

[2] M. Superdock, *Simplicial complexes from finite projective planes and colored configurations*, arXiv:2110.12314 (first version 2021-10-23), *Discrete Mathematics* 346 (2023), 113117.

[3] R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
