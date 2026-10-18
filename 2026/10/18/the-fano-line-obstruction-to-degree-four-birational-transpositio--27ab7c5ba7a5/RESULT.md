# The Fano-line obstruction to degree-four birational transpositions over \(\mathbf F_2\)

## Finding
Let \(f:\mathbf P^2_{\mathbf F_2}\dashrightarrow\mathbf P^2_{\mathbf F_2}\) be birational, with both \(f\) and \(f^{-1}\) defined at all seven rational points. Define its degree to be the common degree of a reduced homogeneous triple defining it. **If this degree is at most four, the permutation induced by \(f\) is never a single transposition.** More precisely: degree-one maps preserve all seven rational lines; degree-two maps send none of the seven rational lines to a rational line and induce exactly \(1344\) distinct permutations, all odd; there are no degree-three birational permutations; and all degree-four birational permutations are even. Therefore the least degree of a birational permutation inducing a transposition, if attained, is at least five.

## Assumptions and scope
The ground field is exactly \(\mathbf F_2\). A rational line is a three-point subset of the Fano plane \(\mathbf P^2(\mathbf F_2)\). A permutation sends a rational line to a rational line when the image of its three rational points is collinear. This incidence statistic is invariant under projective-coordinate changes on the source and target. All birational maps are separable field isomorphisms; infinitely near base points are allowed when counting homaloidal multiplicities. The result does **not** assert the existence of a transposition in degree five.

## Proof
Write \(G=\operatorname{PGL}_3(\mathbf F_2)\), of order \(168\). This simple group acts by even permutations on the seven rational points and preserves the seven Fano lines. A degree-one map belongs to \(G\), hence cannot be a transposition.

For a quadratic birational permutation, its three noncollinear geometric base points have no rational member and therefore form a single degree-three Frobenius orbit. Over \(\mathbf F_8=\mathbf F_2[\alpha]/(\alpha^3+\alpha+1)\), put
\[
 H=\begin{pmatrix}1&1&1\\\alpha&\alpha^2&\alpha^4\\\alpha^2&\alpha^4&\alpha\end{pmatrix},\qquad
 \tau([X:Y:Z])=[YZ:XZ:XY].
\]
The conjugate \(u=H\tau H^{-1}\) descends to \(\mathbf F_2\) and is given by
\[
 u([X:Y:Z])=[X^2+Y^2+YZ+Z^2:\ XY+Y^2+Z^2:\ XZ+Y^2].
\]
It is a birational involution and is defined at every rational point, as is its inverse. Number the nonzero binary coordinate triples by their binary numbers \(1,\ldots,7\). Then its rational-point permutation, expressed in zero-based indexing in the verifier, is \((0,6,3,2,5,4,1)\), equivalently \((1,7,4,3,6,5,2)\) in one-based image notation. The seven rational lines are
\[
 246,\ 145,\ 347,\ 123,\ 257,\ 167,\ 356,
\]
and their images under \(u\) are respectively
\[
 357,\ 136,\ 234,\ 147,\ 267,\ 125,\ 456.
\]
None of the seven image triples is collinear. The corresponding finite test is also performed by `verify_quadratic.py`.

There are \(73\) projective points over \(\mathbf F_8\), of which \(7\) are rational, hence \(22\) Frobenius orbits of degree three. Exactly \(14\) such orbits are collinear, because every one of the seven rational lines contains six nonrational degree-three points, and a nonrational point belongs to at most one rational line. Thus there are exactly \(8\) noncollinear degree-three base orbits. The \(168\) binary projective transformations act transitively on these eight orbits, as verified directly by matrix enumeration; each base-orbit stabilizer has order \(21\). Any quadratic birational permutation is \(guh\) for \(g,h\in G\), because the conics through its base orbit give a three-dimensional vector space and an arbitrary choice of coordinates on the image differs by a projective transformation. Consequently every quadratic birational permutation sends zero rational lines to lines. By comparison, a transposition of two distinct points preserves precisely three of the seven lines: the unique line through the swapped points and the two lines avoiding both. Hence it cannot come from a quadratic map.

The set \(GuG\) consists of exactly \(168^2/21=1344\) permutations. Indeed \(G\cap uGu^{-1}\) is the stabilizer of the quadratic base orbit: preserving the orbit permits conjugation by \(u\) to remain projective, whereas moving that orbit forces positive degree in the conjugate. Each quadratic involution has exactly one rational fixed point and three two-cycles; it is odd. Every element of \(G\) is even, so all \(1344\) quadratic permutations are odd. The verifier independently enumerates the complete double coset and its incidence signature.

For degrees three and four, use the standard Noether homaloidal multiplicity equations \(\sum m_i=3d-3\) and \(\sum m_i^2=d^2-1\), valid also for infinitely near points after resolving the map. In degree three the only type is \((2,1,1,1,1)\). Its unique multiplicity-two base point is Frobenius fixed; its proper support is rational, contradicting rational-point definedness. Hence no degree-three birational permutation exists.

In degree four the possible types are \((3,1,1,1,1,1,1)\) and \((2,2,2,1,1,1)\). The first is excluded by its unique rational multiplicity-three base point. In the second, the three multiplicity-two base points must form a noncollinear degree-three Frobenius orbit of proper points: otherwise the full Frobenius orbit at their positive infinitely-near depth would require an additional orbit of multiplicity at least two at an earlier depth; collinearity would force a common line component by Bézout. Compose the quartic map with the quadratic involution based at this orbit. The plane Cremona degree formula yields
\[
 d'=2\cdot4-(2+2+2)=2.
\]
Both factors are birational permutations, since compositions and inverses remain defined at all rational points. They are each odd, so their product is even. A single transposition is odd, completing the degree-four obstruction and the theorem.

## Verification
Three finite-field Python programs included here run with the standard library only, from the directory containing the files. Execute `python verify_quadratic.py`, then `python verify_quartic_proper.py`, and `python verify_quartic_infinitesimal.py`. The first enumerates the \(168\) invertible projective matrices, the rational Fano lines, and the \(1344\)-element quadratic double coset and verifies its zero-line-preservation property and absence of transpositions. The remaining two programs provide an auxiliary exhaustive cross-check of the quartic parity conclusion: they enumerate \(168\) proper-orbit and \(72\) infinitely-near candidate base configurations, with a three-dimensional quartic linear system for each; among their chosen bases, exactly \(112\) and \(16\), respectively, induce a bijection of the seven rational points, all even. These finite enumerations are overcounts of potentially birational quartic systems, so they provide an obstruction without presuming that every system is birational. Exact original program outputs are included and regenerated during verification.

## Relationship to prior work
Asgarli, Lai, Nakahara and Zimmermann, *Bijective Cremona transformations of the plane*, arXiv:1910.05302, establish that the full birational-permutation group over \(\mathbf F_2\) induces the full symmetric group on the seven points and prove the parity of quadratic birational permutations (Lemmas 5.6–5.7). Thus the existence of transpositions at some degree and the quadratic parity statement are prior work, not claimed as new. Schneider, *Generators of the plane Cremona group over the field with two elements*, arXiv:2008.07991, supplies further classification of Galois base orbits and generators. The present statement refines these results **by homogeneous degree** using a Fano-line incidence obstruction and the low-degree homaloidal filtration. The double-coset count is an explicit finite refinement, not an assertion about the size of the full birational-permutation group.

## Limitations
No transposition of degree five is constructed; the bound five is only necessary. Published generator descriptions and classical homaloidal formulas already give substantial ingredients, so the novelty lies in their degree-filtered combination and incidence signature. Another source may contain an equivalent unindexed low-degree calculation. The finite programs verify finite permutation and jet data, but they are not a replacement for the resolution-of-base-points proof. Independent mathematical audit has not been performed.

## References
1. S. Asgarli, K.-W. Lai, M. Nakahara, S. Zimmermann, *Bijective Cremona transformations of the plane*, arXiv:1910.05302, first public 2019-10-11, relevant sections 1, 2.3 and 5.2.
2. J. Schneider, *Generators of the plane Cremona group over the field with two elements*, arXiv:2008.07991, first public 2020-08-18, relevant sections 1, 2.2 and 2.3.
3. Classical Noether homaloidal equations and the standard quadratic transformation, also reviewed in the cited Cremona literature.
