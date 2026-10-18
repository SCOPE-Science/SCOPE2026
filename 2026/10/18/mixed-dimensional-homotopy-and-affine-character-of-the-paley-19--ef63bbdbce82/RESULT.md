# Mixed-dimensional homotopy and affine character of the Paley-19 out-neighborhood complex

## Finding
Let \(P_{19}\) be the quadratic-residue tournament on \(\mathbb F_{19}\), and let \(X=\overrightarrow{\mathcal N}(P_{19})\) be its ordinary **out-neighborhood simplicial complex**. Then there is an integral homotopy equivalence
\[
X\simeq S^2\vee\bigvee^{78}S^3.
\]
For the order-\(171\) affine automorphism group \(G=\mathbb F_{19}\rtimes(\mathbb F_{19}^{\times})^2\), its degree-two rational homology character is trivial. Its degree-three rational homology character is \(78\) at the identity, \(2\) at a nonidentity translation, \(-3\) at each affine element with multiplier of order \(3\), and \(0\) at each element with multiplier of order \(9\). Consequently,
\[
\widetilde H_i(|X|/G;\mathbb Q)\cong
\begin{cases}\mathbb Q&i=2,\\0&i\ne2.\end{cases}
\]
The character is specified on **all** elements of \(G\). No integral homology assertion is made about the orbit space.

## Assumptions and scope
Write \(R=\{1,4,5,6,7,9,11,16,17\}\subset\mathbb F_{19}\) for the nonzero quadratic residues. The arc \(u\to v\) is present exactly when \(v-u\in R\). Since \(-1\notin R\), this defines a tournament. For each \(u\in\mathbb F_{19}\), put \(B_u=u+R\). The finite abstract simplicial complex \(X\) contains the empty face and exactly the nonempty sets \(S\subseteq B_u\) for at least one \(u\). Thus it is not the directed flag complex, not a tournaplex, and not the neighborhood complex of an undirected Paley graph.

The group elements are maps \(g_{a,b}(v)=av+b\), with \(a\in R\), \(b\in\mathbb F_{19}\). It has exactly \(19\cdot9=171\) elements and preserves all \(B_u\). An affine element with \(a\ne1\) has the same order as \(a\); this order is either \(3\) or \(9\).

## Proof
**Exact simplicial reduction.** Enumerating nonempty subsets of the nineteen nine-point blocks \(B_u\), with duplicate subsets removed, gives the face counts by dimension \(0\) through \(8\):
\[
(19,171,969,2223,2394,1596,684,171,19).
\]
The accompanying `certificate.json` specifies \(3508\) ordered pairs \((\sigma,\tau)\) of faces (as vertex bitmasks). The independent `verify_certificate.py` checks, sequentially on the evolving complex, that \(\sigma\) has precisely the sole immediate coface \(\tau\), and that \(\tau\) has no coface at all. Hence each is a valid elementary free-face simplicial collapse. The terminal three-dimensional simplicial complex \(Y\) has face counts
\[
(f_0,f_1,f_2,f_3)=(19,171,558,482).
\]
In particular, \(X\simeq Y\). The initial complex contains all \(\binom{19}{3}=969\) triangles and all \(\binom{19}{2}=171\) edges, so its entire two-skeleton is that of an eighteen-simplex and is simply connected. Consequently \(Y\) is simply connected, and attaching its three-cells cannot affect the fundamental group; thus its two-skeleton \(Y^{(2)}\) is also simply connected.

**Integral chain calculation.** Order the terminal triangles and tetrahedra by increasing bitmask, orient every simplex by increasing vertex label, and let \(\partial_3:\mathbb Z^{482}\to\mathbb Z^{558}\) be the signed simplicial boundary. In this precise basis `certificate.json` records \(404\) unit pivots, each with row, column and sign. `verify_certificate.py` reconstructs \(\partial_3\) from the actual terminal faces and replays each pivot as integral row/column elimination: a pivot \(\varepsilon\in\{\pm1\}\) updates the other entries to \(A_{ij}-A_{i,c}A_{r,j}/\varepsilon\). After \(404\) such unimodular pivots, the remaining \(154\)-by-\(78\) matrix is **zero**. Thus the Smith invariants of \(\partial_3\) consist of \(404\) units and zeros, with no nonunit torsion factors.

Since \(Y\) is connected and simply connected, the image of its \(\partial_2\) is the \(153\)-dimensional cycle lattice of its connected complete one-skeleton, and \(\ker\partial_2\) has rank \(558-153=405\). The image of \(\partial_3\) is a primitive subgroup of \(\mathbb Z^{558}\), hence also of \(\ker\partial_2\). Therefore
\[
\widetilde H_2(Y;\mathbb Z)\cong\mathbb Z^{405-404}=\mathbb Z,
\qquad
\widetilde H_3(Y;\mathbb Z)\cong\mathbb Z^{482-404}=\mathbb Z^{78},
\]
with all other reduced integral homology zero.

**Upgrade to homotopy.** The simply connected, finite, two-dimensional CW complex \(Y^{(2)}\) has free \(H_2\) of rank \(405\); by Hurewicz and Whitehead it is homotopy equivalent to \(\bigvee^{405}S^2\). The homotopy classes of the \(482\) three-cell attaching maps are completely determined by their \(\pi_2\cong H_2\) degree vectors. Their degree matrix has Smith form with \(404\) entries \(1\), one remaining zero row and \(78\) zero columns: the full integer image is primitive as shown above. Unimodular basis changes of the two-sphere wedge and of the attaching spheres induce homotopy-equivalent cofibres. Thus \(404\) degree-one two/three-cell pairs are contractible, leaving one \(S^2\) and \(78\) copies of \(S^3\), as asserted. This argument uses both the explicit free collapses and the *integral* unit-pivot certificate; ranks over a field would not alone justify the homotopy conclusion.

**Affine character.** Because \(G\) has odd order and \(\widetilde H_2(X;\mathbb Q)\) is one-dimensional, its rational character is identically \(1\). For \(g\in G\), let
\[
L(g)=\sum_{\substack{\varnothing\ne S\in X\\gS=S}}(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
The simplicial Lefschetz identity gives \(L(g)=1+\operatorname{tr}(g|\widetilde H_2)-\operatorname{tr}(g|\widetilde H_3)=2-\operatorname{tr}(g|\widetilde H_3)\). The independent checker enumerates invariant faces and their orientation signs for every one of the \(171\) affine elements. In the order identity, nonidentity translation, multiplier order \(3\), multiplier order \(9\), the ordinary Lefschetz values are \((-76,0,5,2)\), the degree-three traces are \((78,2,-3,0)\), and the element counts are \((1,18,38,114)\). For order \(3\), the fixed faces have cardinalities \(1,3,6,9\) with counts \(1,6,3,1\); for order \(9\), the fixed faces have cardinalities \(1,9\) with counts \(1,1\). These are independent checks of the signed formulas.

The dimension of \(\widetilde H_3(X;\mathbb Q)^G\) is the character average \((78+18\cdot2-38\cdot3)/171=0\), whereas \(\dim\widetilde H_2(X;\mathbb Q)^G=1\). Over characteristic zero, the rational homology of a finite simplicial quotient is the group-invariant part of rational homology (apply barycentric subdivision and averaging). This proves the quotient statement.

## Verification
From the same directory, run `python3 make_certificate.py`, `python3 verify_certificate.py`, and `python3 independent_mod2.py`. The first regenerates `certificate.json` using exact integer operations; the second independently reconstructs all faces by combinations and checks every elementary collapse, integral pivot and affine trace. The third independently computes the full, unreduced simplicial boundary ranks over \(\mathbb F_2\), obtaining reduced Betti ranks \((0,0,1,78,0,0,0,0,0)\). Expected standard output is recorded in `CHECKS.txt`. Python \(3.10\) or later is sufficient; no third-party packages or network connection are used. The integral argument relies on the integer replay, not on the finite-field experiment.

## Relationship to prior work
Dochtermann and Singh introduced directed out-neighborhood complexes, related them to directed Hom complexes and studied restrictions on their homology; their tournament discussion gives small cases and poses broader homotopy questions [1, Definition 4.1, Sections 5 and 7]. Their results do not give the homotopy type or affine character of this named \(19\)-vertex example. Govc investigated *directed flag complexes* of tournaments [2]; that complex depends on transitive directed cliques, whereas the present complex is a union of nine-vertex out-neighborhood simplices. Existing calculations for the Paley-19 directed flag complex do not imply the displayed neighborhood-complex decomposition. The previously recorded Paley-11 out-neighborhood example is a different graph order and does not subsume this calculation.

## Limitations
This is a complete result for the single specified order-\(19\) tournament and its specified affine subgroup, not a uniform formula for all Paley tournaments, not a classification of every tournament, and not a computation of integral homology for the orbit quotient. The checker exhausts a finite, explicitly defined simplicial complex; no infinite computation or formal proof assistant is claimed. An independently performed mathematical audit has not been carried out.

## References
[1] A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first public version 2021-08-24; European Journal of Combinatorics 110 (2023), article 103704. https://arxiv.org/abs/2108.10948

[2] D. Govc, *Computing homotopy types of directed flag complexes*, arXiv:2006.05333, first public version 2020-06-09. https://arxiv.org/abs/2006.05333
