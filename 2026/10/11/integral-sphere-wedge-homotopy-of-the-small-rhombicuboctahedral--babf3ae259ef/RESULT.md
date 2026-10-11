# Integral sphere-wedge homotopy of the small rhombicuboctahedral independence complex

## Finding
Let \(G\) be the edge graph of the convex small rhombicuboctahedron (the cantellated cube). Its ordinary independence complex has the homotopy type
\[
\operatorname{Ind}(G)\simeq S^4\vee\bigvee^{4}S^5.
\]
In particular, its nonzero reduced integral homology groups are \(\widetilde H_4\cong\mathbb Z\) and \(\widetilde H_5\cong\mathbb Z^4\), and the corresponding integral discrete-Morse matching is perfect: one critical vertex, one critical four-cell, and four critical five-cells. The homotopy claim is stronger than the homology statement.

## Assumptions and scope
The object is the **convex small** rhombicuboctahedral graph, with 24 vertices and 48 edges, not the 48-vertex great rhombicuboctahedral graph. Give vertices labels \((a,\varepsilon)\) with \(a\in\{0,1,2\}\) and \(\varepsilon\in\{-1,1\}^3\). Two distinct labels \((a,\varepsilon)\), \((b,\delta)\) are adjacent precisely when either (i) \(a=b\) and the sign vectors differ in exactly one coordinate other than \(a\), or (ii) \(a\ne b\) and \(\varepsilon=\delta\).

This gives the Euclidean edge graph on all coordinate permutations and independent sign choices of \((1,1,1+\sqrt2)\). Indeed, these two cases, and only these, give Euclidean distance two; the graph is four-regular. Its vertices are ordered first by \(a=0,1,2\), then lexicographically by \(\varepsilon\), using \(-1<1\). The independence complex contains exactly the subsets with no graph edge, including the empty simplex for the abstract complex but excluding it from the nonempty face-poset matching.

All statements are about this one finite graph and ordinary nonequivariant integral homotopy. No theorem for other Archimedean solids or all cantellated polytopes is asserted.

## Proof
**Exact face enumeration.** Encode a set of labeled vertices by the nonnegative integer \(m=\sum_{i\in S}2^i\). Starting from the empty mask, process the 24 vertices in increasing label order, adjoining bit \(i\) to a mask only when it contains no neighbor of \(i\). This constructs every independent set uniquely. Excluding the empty set gives 13,874 faces, with numbers of \(d\)-faces for \(0\le d\le7\) equal to
\[
(24,228,1104,2940,4368,3536,1440,234).
\]

**Acyclic matching.** Use the following order of vertex-bit indices:

`23,22,17,4,13,8,2,6,18,20,1,21,19,11,3,10,9,0,15,16,5,7,12,14`.

At each stage, scan unmatched nonempty face masks in increasing numerical order. Whenever an unmatched face \(f\) does not contain the stage's bit \(v\) and the face \(f\cup\{v\}\) is also unmatched, match this lower/upper pair and remove both from subsequent stages. This is a valid simplicial face pairing. Exactly 6,934 pairs are found. To check acyclicity without relying on a heuristic, orient every Hasse incidence from the containing face to its codimension-one face, except that paired incidences are reversed. The resulting digraph has 13,874 vertices and 70,536 directed incidences. A complete topological sorting visits all 13,874 vertices, so the matching is acyclic.

The unmatched masks are exactly: `8388608` (dimension zero), `2163272` (dimension four), and `99426`, `807456`, `2183304`, `3146889` (dimension five). Thus Forman's discrete-Morse theorem gives a CW model with one zero-cell, one four-cell and four five-cells, and no other cells.

**Integral attaching degrees.** The only possibly nonzero cellular boundary in this CW model is a \(1\times4\) integer matrix \(\partial_5^M\). Its entries are computed with the exact oriented Morse boundary formula. For a face \(f\) matched upward to \(g\), let \([g:f]\in\{-1,+1\}\) be the signed simplicial incidence, and recursively project its chain class using
\[
P(f)=-[g:f]^{-1}\sum_{\substack{h\prec g\\h\ne f}}[g:h]P(h).
\]
For a critical face \(c\), set \(P(c)=c\); for a face matched downward, set \(P(c)=0\). Recursion terminates by the verified acyclicity. For each critical five-face \(c\), evaluate \(\sum_{f\prec c}[c:f]P(f)\) in the critical four-face basis. The four integer coefficients are exactly \((0,0,0,0)\). The program `verify_morse.py` supplies the complete reproducible computation and checks the acyclicity and all four coefficients from the encoded graph.

The CW four-skeleton is \(S^4\). Each five-cell is attached by a map \(S^4\to S^4\) whose degree is the corresponding entry of \(\partial_5^M\). Since degree classifies \(\pi_4(S^4)\cong\mathbb Z\), each attaching map is null-homotopic. Hence the CW model, and therefore \(\operatorname{Ind}(G)\), is homotopy equivalent to \(S^4\vee\bigvee^4 S^5\). This is an integral homotopy argument; no inference from finite-field homology alone is used.

## Verification
Run `python3 verify_morse.py` and `python3 verify_chains.py` with Python 3.10 or later; neither needs a third-party package. The first checks the 24-vertex/48-edge graph, every independent face, all 6,934 matching pairs, the complete directed-incidence acyclicity certificate and each signed integral Morse boundary coefficient. The second constructs the graph independently from Euclidean coordinates and performs a complete mod-two simplicial chain computation. It obtains boundary ranks \((23,205,899,2041,2326,1206,234)\) and reduced mod-two Betti numbers \((0,0,0,0,1,4,0,0)\). These are separate checks on different constructions; the mod-two computation alone would not establish the integral attaching degrees. The face Euler characteristic is \(-2\), agreeing with the wedge's reduced Euler characteristic \(-3\).

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418, first posted July 2, 2010) develops general tools for independence complexes, but does not calculate this small rhombicuboctahedral graph. In particular, its triangle-free-vertex suspension criterion is not directly applicable because every vertex here lies in a triangle. Goyal, Shukla and Singh's *Homotopy Type of Independence Complexes of Certain Families of Graphs* (arXiv:1905.06926, 2019) gives a general acyclic matching construction and exact results for categorical products and generalized Mycielskian graphs; the present graph, with 24 vertices and degree four, is not a member of those explicit families. Its edge-replacement formulas also do not determine the stated four- and five-dimensional multiplicities. The matching construction used here is consistent with the standard element-toggling Morse method; its exact critical set and boundary coefficients are the graph-specific contribution.

The small rhombicuboctahedral graph's elementary parameters and synonyms appear in MathWorld and in OEIS A159055 (a chromatic-polynomial sequence originating April 3, 2009). Those sources do not tabulate or imply its independence-complex homotopy type. Literature searches under the small rhombicuboctahedral, cantellated cube, cube vertex–face incidence, and complementary clique-complex formulations did not identify a more general theorem that computes this exact type. Nonretrieval does not prove global novelty.

## Limitations
The proof is a finite, exhaustive, reproducible calculation for one naturally specified graph. It does not classify other Archimedean graphs or supply a parameter-family theorem. It uses the standard discrete-Morse homotopy equivalence and the degree classification of self-maps of \(S^4\). A separate independent mathematical audit has not been performed; equivalent unindexed work may exist. The alternate chain check is over \(\mathbb F_2\), whereas the integral conclusion depends on the signed Morse certificate.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (first version July 2, 2010), https://arxiv.org/abs/1007.0418.
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first version May 16, 2019), https://arxiv.org/abs/1905.06926; journal version in *Contributions to Discrete Mathematics* 16 (2021), 74–92.
3. E. W. Weisstein, *Small Rhombicuboctahedral Graph*, MathWorld, https://mathworld.wolfram.com/SmallRhombicuboctahedralGraph.html.
4. OEIS A159055, *Number of n-colorings of the Small Rhombicuboctahedral Graph*, originating April 3, 2009, https://oeis.org/A159055.
