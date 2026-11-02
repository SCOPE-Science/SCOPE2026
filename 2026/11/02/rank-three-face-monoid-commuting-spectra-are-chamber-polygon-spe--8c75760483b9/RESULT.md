# Rank-three face-monoid commuting spectra are chamber-polygon spectra

## Finding
Let \(\mathcal A\) be any finite essential central arrangement of distinct real hyperplanes in dimension three. Write \(F(\mathcal A)\) for its Tits face monoid, \(f_i\) for its number of \(i\)-dimensional relatively open faces (\(f_0=1\)), and \(n_m\) for the number of chambers with exactly \(m\) two-dimensional facets (\(m\ge3\)). Let \(C_k\) be the number of ordered \(k\)-tuples of faces whose entries commute pairwise, permitting repetitions and including \(C_0=1\). Then, for every integer \(k\ge0\),
\[
C_k=1+f_1(2^k-1)+f_2(1-4^k)-f_3+\sum_{m\ge3}n_m(2m+2)^k.
\]
Consequently, the entire commuting-tuple sequence \((C_k)_{k\ge0}\) uniquely determines, and is uniquely determined by, \(f_1\), \(f_2\), and the complete chamber facet-number spectrum \((n_m)_{m\ge3}\); it therefore determines \(f_3=\sum_m n_m\) as well. In particular,
\[
C_2=1+3f_1+f_2+3f_3+4\sum_{m\ge3}m^2n_m.
\]
The face vector alone does **not** determine commuting probability or any full tuple-count profile: two explicit generic six-hyperplane arrangements both have \((f_0,f_1,f_2,f_3)=(1,30,60,32)\) but have \(C_2=2103\) and \(C_2=2119\), respectively.

## Assumptions and scope
An arrangement is essential when the intersection of all hyperplanes is \(\{0\}\), so its full-dimensional cones are pointed. Every face is represented by its sign vector relative to oriented defining normal forms, with coordinates in \(\{-1,0,+1\}\); sign choices do not affect commutation. The Tits product \(FG\) takes the sign of \(F\) at every nonzero coordinate of \(F\), and otherwise the sign of \(G\). Thus commuting means no coordinate has opposite nonzero signs. The face-poset order \(F\le G\) means \(\overline F\subseteq\overline G\). A chamber with \(m\) facets has a transverse polygonal section with exactly \(m\) edges and \(m\) vertices. Accordingly its closed cone has precisely \(2m+2\) faces: the origin, \(m\) rays, \(m\) facets, and the chamber itself. The theorem applies also to nongeneric arrangements, allowing multiple hyperplanes through a ray. It concerns actual ordered tuples, not conjugacy classes or tuples of distinct elements.

## Proof
**Common upper face.** Two sign covectors commute if and only if they have no opposite nonzero coordinate, by direct comparison of the Tits products. For a finite pairwise-compatible family, its iterated product has the union of the nonzero signs and is again a realizable face covector. This product is the smallest face containing every entry in its closure. Conversely, two subfaces of one closed cone cannot have opposing signs. Hence every commuting tuple has a unique join \(J\) in the face poset, and counting all tuples can be partitioned according to \(J\). This elementary criterion is established in prior work (Petersen, Proposition 5.3); novelty is not claimed for the criterion.

**Local counts.** For each face \(J\) let \(a_k(J)\) count ordered commuting \(k\)-tuples whose join is exactly \(J\), with the empty tuple having join the origin. If \(b(J)\) is the number of subfaces of \(J\), then all \(b(J)^k\) ordered tuples lying below \(J\) commute and have a unique join below it. Thus \(b(J)^k=\sum_{G\le J}a_k(G)\), so finite-poset Möbius inversion applies. The face interval below the origin has one element; below each ray it is the two-element chain; below each two-dimensional face it is a four-element Boolean lattice. Therefore the local counts are, respectively,
\[
1,\qquad 2^k-1,\qquad 4^k-2\cdot2^k+1.
\]
For a chamber \(J\) with \(m\) polygon sides, its interval contains one origin, \(m\) rays, \(m\) polygon facets, and \(J\). Its interval Möbius values toward \(J\) are \(-1\) on the origin, \(+1\) on each ray, \(-1\) on each facet, and \(+1\) on \(J\). Therefore
\[
a_k(J)=(2m+2)^k-m4^k+m2^k-1.\]
Summing these contributions over all faces, and using the incidence identity \(\sum_m mn_m=2f_2\) because every two-face borders exactly two chambers, proves the displayed formula. Substitution at \(k=2\) yields the chamber-square-moment expression.

**Inversion of the spectrum.** Rewrite the identity as a finite linear combination of exponential sequences:
\[
C_k=(1-f_1+f_2-f_3)\,1^k+f_1\,2^k-f_2\,4^k+\sum_{m\ge3}n_m(2m+2)^k.
\]
All displayed bases \(1,2,4,8,10,12,\ldots\) are distinct. The sequences of powers of distinct positive integers are linearly independent over \(\mathbb Q\), by a Vandermonde determinant applied to the first sufficiently many values of \(k\). Therefore \((C_k)_{k\ge0}\) determines every coefficient, including \(f_1\), \(f_2\), and each \(n_m\). The reverse implication is the proved counting formula, completing the equivalence.

**Explicit equal-face-vector separation.** Let \(\mathcal A\) and \(\mathcal B\) be the arrangements with six defining hyperplane normals given by the rows, respectively, of
\[
N_{\mathcal A}=\begin{pmatrix}
1&2&1\\2&-3&1\\3&1&1\\-3&-3&1\\-1&0&1\\-1&2&1
\end{pmatrix},\qquad
N_{\mathcal B}=\begin{pmatrix}
2&0&1\\1&-3&1\\-2&-2&1\\-3&-2&1\\1&-1&1\\2&-3&1
\end{pmatrix}.
\]
All twenty determinants formed from three distinct rows are nonzero in either matrix, so the rank-three arrangements are generic. Their common face vector, obtained from planar sections or the certified enumeration described next, is \((1,30,60,32)\). Their chamber-facet multisets are
\[
\mathcal A:\quad 3^{[12]},4^{[16]},5^{[4]};\qquad
\mathcal B:\quad3^{[12]},4^{[18]},6^{[2]},
\]
where \(m^{[a]}\) means exactly \(a\) chambers with \(m\) facets. These finite census statements are certified using the exhaustive, integer-arithmetic face-enumeration algorithm supplied in `verify.py`. They imply \(\sum m^2n_m=464\) and \(468\), hence \(C_2=2103\) and \(2119\), respectively, while each arrangement has 123 faces. Their normalized commuting probabilities are therefore \(2103/15129\) and \(2119/15129\), strictly different. The chamber multisets additionally show their maximal commuting cliques have sizes \(8,10,12\) versus \(8,10,14\), so even their commuting graphs differ.

## Verification
The standalone `verify.py` uses only Python's standard library. For each displayed matrix it tests all twenty triple determinants, generates every ray as one of the two orientations of each row-pair cross product, generates every planar face as a sign vector of an interior sum of its two extreme rays, and generates both adjacent chambers by replacing the sole zero coordinate of every planar-face sign vector. Every ray of a generic central three-arrangement occurs in this list; every two-face is a wedge with two boundary rays; every chamber borders a two-face. Hence this is an exhaustive face enumeration, not a finite-radius sample. It finds exactly 123 faces with layer sizes \(1,30,60,32\), and independently checks the 123-by-123 sign-compatibility relation. The direct ordered commuting-pair and commuting-triple counts are \((2103,25455)\) for \(\mathcal A\) and \((2119,26031)\) for \(\mathcal B\). Independent maximal-clique enumeration agrees with the chamber-face sets. Its assertions additionally verify the first five formula values for both arrangements, while the preceding mathematical argument establishes every \(k\).

## Relationship to prior work
The sign-vector/Tits product and pairwise-commuting/common-upper-face characterization are established in the literature (notably Petersen, *Eulerian Numbers*, Proposition 5.3; Margolis–Saliola–Steinberg, arXiv:1212.6683). Bastidas–Brauner–Saliola (arXiv:2306.14985) and Commins (arXiv:2404.00536) develop the semigroup and braid-arrangement algebraic context. An existing type-A face-monoid computation gives a centralizer parametrization and commuting-pair total; it is not claimed as new here. The present claim is instead the rank-three all-arity chamber-facet-spectrum identity, its converse, and the explicit pair of generic six-plane arrangements with identical face numbers and unequal commuting-pair totals. The accessible portions of cited foundational literature establish structural ingredients but do not state this combined enumerative theorem. Possible broader unlocated oriented-matroid counting results remain an originality risk.

## Limitations
The closed chamber-spectrum formula relies on three-dimensional pointed cones having polygonal face intervals; it is not asserted in higher rank or for nonessential arrangements without quotienting their common intersection. The finite verifier certifies the two concrete examples, not the general infinite family independently. The foundation literature already contains the underlying commutativity criterion. The originality comparison is evidence-based and not an independent priority certification; independent mathematical audit has not been performed.

## References
- J. Bastidas, S. Brauner, F. Saliola, *Left regular bands of groups and the Mantaci–Reutenauer algebra*, first public arXiv submission 2023-06-26, https://arxiv.org/abs/2306.14985.
- P. Commins, *Invariant theory for the face algebra of the braid arrangement*, first public arXiv submission 2024-03-31, https://arxiv.org/abs/2404.00536.
- T. K. Petersen, *Eulerian Numbers*, Springer, 2015, Proposition 5.3 and Section 8, https://doi.org/10.1007/978-1-4939-3091-3.
- S. W. Margolis, F. V. Saliola, B. Steinberg, *Semigroups embeddable in hyperplane face monoids*, https://arxiv.org/abs/1212.6683.
