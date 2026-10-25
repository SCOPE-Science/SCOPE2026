# Coordinate-transposition fixed loci of scale-two hypercube Rips complexes

## Finding

Let \(n\ge3\), let \(Q_n=\{0,1\}^n\) with the Hamming metric, and let \(\sigma\) interchange any two coordinates. Write \(m=n-2\), let \(X_n=\operatorname{VR}_{\le2}(Q_n)\), and put \(c_1=c_2=0\) and, for \(m\ge3\),
\[
c_m=\sum_{0\le j<i<m}(j+1)\bigl(2^{m-2}-2^{i-1}\bigr).
\]
Then the geometric fixed-point space has the **integral homotopy type**
\[
\boxed{
|X_n|^{\langle\sigma\rangle}\simeq
\bigvee^{(m-1)2^m+1}S^2\ \vee\ \bigvee^{2c_m}S^3.}
\]
The zero-fold wedge is a point. For \(n=3,4,5,6\), these types are respectively \(S^2\), \(\bigvee^5S^2\), \(\bigvee^{17}S^2\vee\bigvee^2S^3\), and \(\bigvee^{49}S^2\vee\bigvee^{18}S^3\). The claim is about the **geometric fixed locus**, not the quotient of \(|X_n|\) by \(\sigma\) or the invariant part of ambient homology.

## Assumptions and scope

Vertices are binary words; the distance of two words is the number of differing coordinates. A finite subset is a face of \(X_n\) exactly if every pair of its words has distance at most \(2\), including equality. The involution \(\sigma\) acts simplicially by swapping two chosen coordinates. The fixed locus is taken on the geometric realization, so an orbit of two non-fixed vertices may contribute its barycenter. The theorem holds for every integer \(n\ge3\) and every coordinate transposition. Coefficients in the statement are integral; no assertion is made for other scales or arbitrary permutations.

## Proof

**1. A geometric orbit complex.** Order the exchanged coordinates first, writing words as \((a,b,z)\), where \(a,b\in\{0,1\}\) and \(z\in Q_m\). The orbits are \(A_z=\{(0,0,z)\}\), \(B_z=\{(1,1,z)\}\), and \(C_z=\{(0,1,z),(1,0,z)\}\). Each orbit is itself a face of \(X_n\), because the two vertices in \(C_z\) are at distance two. Define a complex \(K_m\) on these \(3\cdot2^m\) orbit symbols by allowing a set of symbols if the union of their orbits is an \(X_n\)-face. Sending each symbol to the uniform barycenter of its orbit extends to a PL homeomorphism \(|K_m|\to|X_n|^{\langle\sigma\rangle}\). Indeed every fixed barycentric point has equal weights on vertices of each orbit; the sum of each orbit's weights supplies a unique inverse coordinate, and its support is an invariant face. Compactness and the finite simplexwise-affine formulas prove the claimed homeomorphism, including face-boundary compatibility.

**2. The exact orbit adjacency rules.** Put \(h=d_H(z,w)\). Two distinct orbit symbols occur in a common face exactly under the following conditions: \(A_z,A_w\) or \(B_z,B_w\) require \(h\le2\); \(A_z,B_w\) require \(h=0\); \(A_z,C_w\) or \(B_z,C_w\) require \(h\le1\); and \(C_z,C_w\) for distinct \(z,w\) never occur, because the maximum distance between their original words is \(h+2>2\). These conditions follow by inspecting the four possible leading-bit pairs. Since the original Rips condition is pairwise and each orbit has internal diameter at most two, \(K_m\) is exactly the flag complex of this adjacency graph.

**3. Two copies and cone links.** Let \(T_m=\operatorname{VR}_{\le2}(Q_m)\). Delete all \(C_z\) symbols from \(K_m\), obtaining \(Y\): two disjoint copies \(T_m^A,T_m^B\), connected by the \(q=2^m\) edges \(e_z=[A_z,B_z]\), and with no mixed-dimensional simplices. For every \(z\), let \(N[z]=\{w\in Q_m:d_H(z,w)\le1\}\), of size \(m+1\). The link \(L_z=\operatorname{lk}_{K_m}(C_z)\) comprises an \(m\)-simplex on \(\{A_w:w\in N[z]\}\), an \(m\)-simplex on \(\{B_w:w\in N[z]\}\), and the \(m+1\) separate joining edges \(e_w\), with no mixed higher faces. Collapsing the two disjoint contractible simplices in this link gives a two-vertex graph with \(m+1\) parallel edges. Hence \(L_z\simeq\bigvee^mS^1\). No face contains two distinct \(C\)-symbols, so
\[
K_m=Y\cup_{\bigsqcup_z L_z}\bigsqcup_z\operatorname{Cone}(L_z)
\]
with the evident separate cone attachments.

**4. Compute the attaching words and the two-dimensional remainder.** By Adamaszek--Adams, \(T_m\simeq\bigvee^{c_m}S^3\) for \(m\ge3\). For \(m=1,2\), \(T_m\) is a simplex. Thus every \(T_m\) is connected and simply connected, and each copy can be retained as a wedge summand while the \(q\) bridges contribute \(q-1\) free circle generators. More explicitly, choose base paths inside the two copies and one bridge \(e_0\), and denote by \(x_w\) the loop obtained by traversing \(e_w\) and returning via \(e_0\) and these base paths; set \(x_0=1\). Then \(Y\simeq T_m^A\vee T_m^B\vee\bigvee^{q-1}S^1\).

The \(m\) independent loops of the link \(L_z\) compare each edge \(e_w\), \(d_H(z,w)=1\), against \(e_z\). Under inclusion in \(Y\), their words in the free fundamental group are, up to conjugacy and orientation, \(x_wx_z^{-1}\). Any map from a graph into \(Y\) is, up to homotopy, determined by these fundamental-group words; the simply connected \(T_m\) summands cannot contribute a nontrivial loop. Homotopy invariance of mapping cones therefore splits the two \(T_m\) summands from a two-dimensional CW complex \(Z_m\), with \(q-1\) one-cells \(x_w\) for \(w\ne0\), and \(qm\) two-cells indexed by all oriented nearest-neighbor pairs \((z,w)\) of the \(m\)-cube, attached by the words \(x_wx_z^{-1}\).

Choose a spanning tree of the connected one-skeleton of \(Q_m\), rooted at \(0\). The \(q-1\) relations oriented from parent to child along this tree eliminate, one after another, all \(q-1\) circle generators by elementary cell cancellation (equivalently, a sequence of free-generator Tietze moves preserving the CW homotopy type). Once eliminated, all remaining two-cell attaching words are null and the complex is a wedge of
\[
qm-(q-1)=(m-1)2^m+1
\]
two-spheres. Consequently \(K_m\simeq T_m\vee T_m\vee\bigvee^{(m-1)2^m+1}S^2\), and inserting the integral homotopy classification of \(T_m\) gives the displayed formula. The cancellation argument is integral and produces a homotopy equivalence, not merely a field-homology identity.

## Verification

The standalone `verify.py` constructs the actual orbits in the original binary cube and compares every pairwise union-diameter predicate against the independently coded adjacency rules, for \(m=1,2,3,4\). It enumerates every face of the resulting flag complexes, computes all reduced mod-two Betti numbers via explicit boundary matrices and Gaussian elimination, and compares them against the theorem. Independently, for \(m=1,2,3\), it enumerates all ambient scale-two Rips simplices and checks the signed simplicial Lefschetz number of the coordinate swap against the Euler characteristic of the proposed fixed locus. The recorded output reports 2,468 nonempty orbit-complex faces in all four tests and ends in `VERIFY_OK`. Execute `python3 verify.py` from the directory containing the extracted files. These finite checks are corroboration, not a substitute for the infinite-family integral proof.

## Relationship to prior work

Adamaszek--Adams give the integral nonequivariant equivalence \(T_m\simeq\bigvee^{c_m}S^3\); its sphere counts are used here and are not claimed as new. Feng further studies the larger scale-three hypercube Rips homotopy type. The 2026 work of Bendersky--Elia--Grbić examines connectivity and cohomology classes of ambient hypercube Rips complexes. Galetto--Montaño--Wellner compute rational hyperoctahedral representation characters in ambient homology at small scales, including scale two. An ambient character can determine the fixed-space Euler characteristic by a Lefschetz computation, but it does not determine the geometric fixed-space homotopy type, nor distinguish the separate \(S^2\) and \(S^3\) wedge multiplicities proved here. The fixed locus of a coordinate flip is a different symmetry problem: unlike the present transposition, it has no fixed cube vertices. The new result treats coordinate-transposition fixed *spaces*, using their full orbit simplicial complex and cone-attachment homotopy structure.

## Limitations

The theorem assumes a single coordinate transposition, binary Hamming cubes, the inclusive integer scale two, and \(n\ge3\). It gives no homotopy classification for products of transpositions, other automorphisms, other scales, or orbit quotients. The finite verifier only checks \(n\le6\) (and ambient Lefschetz traces for \(n\le5\)); it does not independently certify the general proof. The priority comparison draws on accessible primary literature and research-index searches and cannot exclude an unindexed equivalent statement. No independent scientific audit has been performed.

## References

1. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040 (first submitted 2021-03-01), Theorem 1 and proof, https://arxiv.org/abs/2103.01040.
2. Z. Feng, *Homotopy types of Vietoris-Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (first submitted 2023-05-11), introduction and its citation of the scale-two formula, https://arxiv.org/abs/2305.07084.
3. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first submitted 2026-05-01), Sections 1 and 5, https://arxiv.org/abs/2605.00705.
4. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first submitted 2026-06-18), Theorem 5.4 and Sections 5.6 and 8, https://arxiv.org/abs/2606.20784.
