# The \(5\)-adic Fano scheme of Clebsch's diagonal cubic

## Finding
Let \(R=\mathbb Z_5\), and let \(\mathscr X\subset\mathbb P^4_R\) be the relative cubic surface
\[
\sum_{i=0}^{4}x_i=\sum_{i=0}^{4}x_i^3=0.
\]
Let \(\mathscr F=\operatorname{Hilb}^{t+1}(\mathscr X/R)\) denote its relative scheme of projective lines. Then \(\mathscr F\) is finite flat of rank \(27\) over \(R\), with an isomorphism of \(R\)-schemes
\[
\boxed{\mathscr F\simeq
\coprod_{15}\operatorname{Spec}R\;\coprod\;
\coprod_{6}\operatorname{Spec}\bigl(R[t]/(t^2+t-1)\bigr).}
\]
The quadratic factor is the ramified quadratic extension of \(R\) of discriminant \(5\). Thus the reduction of \(\mathscr F\) has exactly \(21\) geometric points, all rational over \(\mathbb F_5\): fifteen are reduced, while six have local ring \(\mathbb F_5[\varepsilon]/(\varepsilon^2)\). These six nonreduced points parametrize lines through the unique ordinary double point of the special cubic. The inertia action on the \(27\) geometric generic lines fixes fifteen and exchanges six disjoint pairs.

## Assumptions and scope
The base is the complete unramified discrete valuation ring \(R=\mathbb Z_5\), and the family is the indicated integral diagonal cubic; no alternative characteristic-five model is considered. The relative Fano scheme is the closed subscheme of \(\operatorname{Gr}_R(2,4)\) cut out by the four coefficients of the cubic restricted to the universal line. All decompositions are as \(R\)-schemes, not merely bijections on geometric points.

## Proof
**1. Fibers and the node.** Write \(x_0=-x_1-x_2-x_3-x_4\). In characteristic different from \(2,3\), the four partial derivatives of \(\sum_i x_i^3\) on this hyperplane are \(3(x_j^2-x_0^2)\), \(1\le j\le4\). A singular point has all five coordinates equal up to sign. Over characteristic zero, five signs cannot sum to zero. In characteristic five, their sum vanishes only if all five signs agree. Hence the sole singular point of \(X_5\) is \(v=[1:1:1:1:1]\). In the affine chart \(x_4=1\), putting \(x_j=1+u_j\) for \(1\le j\le3\) and \(S=u_1+u_2+u_3\), the local equation begins with the quadratic form \(3(\sum_j u_j^2+S^2)\). Its symmetric matrix is \(3(I_3+\mathbf 1\mathbf 1^{\mathsf T})\), of nonzero determinant modulo \(5\), so the singularity is an ordinary double point.

**2. Finiteness and flatness.** Lines avoiding \(v\) are contained in the smooth locus of \(X_5\). By adjunction on the smooth cubic surface near any such line \(\ell\), \(\ell^2=-1\); hence its normal bundle is \(\mathcal O_{\mathbb P^1}(-1)\), and its Fano-scheme tangent space vanishes. Lines through \(v\) correspond to common zeros in the projective plane of tangent directions of the quadratic and cubic parts of the node equation. The quadratic is smooth and the cubic does not contain it, since otherwise the cubic surface would factor and have a positive-dimensional singular locus. Bézout therefore gives at most six such directions. Thus the special Fano scheme is finite. The four universal-line cubic coefficients cut it out in the relative four-dimensional smooth Grassmannian. All local ideals have the expected codimension four in the regular total space; the resulting relative local complete intersection is Cohen--Macaulay, finite and flat over the DVR. The generic fiber is the classical smooth Clebsch cubic with \(27\) distinct lines. Hence the relative degree is exactly \(27\).

**3. Explicit generic lines and their fields.** Fifteen lines are spanned by the two difference vectors supported on two disjoint pairs of the five coordinates, with the remaining coordinate zero. Their parameter fields are \(\mathbb Q_5\). Let \(\zeta\) be a primitive fifth root of unity. A further line is spanned by
\[
(1,\zeta,\zeta^2,\zeta^3,\zeta^4),\qquad
(1,\zeta^{-1},\zeta^{-2},\zeta^{-3},\zeta^{-4}).
\]
Its twelve distinct coordinate-permutation translates account for the other twelve lines: the stabilizer in \(S_5\) is the dihedral group of order ten. The automorphism \(\zeta\mapsto\zeta^{-1}\) fixes each line, whereas \(\zeta\mapsto\zeta^2\) pairs the twelve lines into six orbits. Their common field of definition is \(K=\mathbb Q_5(t)\), with \(t=\zeta+\zeta^{-1}\) satisfying \(t^2+t-1=0\). The algebra \(O=R[t]/(t^2+t-1)\) is a ramified quadratic DVR because its discriminant is \(5\).

**4. Exact special-fiber lengths.** The fifteen pairing lines reduce to fifteen distinct lines avoiding \(v\), and each has Fano tangent dimension zero. For the cyclotomic line the Plücker ratios relative to the nonzero chart coordinate \(p_{01}\) satisfy
\[
\frac{p_{0j}}{p_{01}}=\frac{\zeta^j-\zeta^{-j}}{\zeta-\zeta^{-1}},
\qquad\frac{p_{02}}{p_{01}}=t.
\]
These ratios lie in \(O\), and modulo its maximal ideal they equal \(j\in\mathbb F_5\). Thus its closure reduces to the line spanned by \(v=(1,1,1,1,1)\) and \((0,1,2,3,4)\). Coordinate permutations give exactly six such lines: distinct permutations yield the same two-dimensional subspace precisely under an affine transformation of the five residues, so the stabilizer has order \(5\cdot4=20\). The six lines are all through the node. At any line through a singular point the linearization of the \(s^3\) coefficient of the line-restriction cubic is zero, so its Fano tangent dimension is at least one and its local length at least two. The fifteen other exhibited lines have local length one. Since \(\mathscr F_5\) has total length \(27\), the already exhibited lines contribute at least \(15+6\cdot2=27\), forcing completeness and exact lengths \(1\) and \(2\). Each length-two local ring with one-dimensional tangent space and residue field \(\mathbb F_5\) is \(\mathbb F_5[\varepsilon]/(\varepsilon^2)\).

**5. Isomorphism over \(R\).** Properness of the Grassmannian extends the fifteen rational generic lines uniquely to \(R\)-sections and each of the six \(K\)-lines uniquely to an \(O\)-point. Their disjoint union induces a finite morphism
\[
\coprod_{15}\operatorname{Spec}R\;\coprod\;
\coprod_{6}\operatorname{Spec}O\longrightarrow\mathscr F
\]
which is an isomorphism on geometric generic fibers and bijective on geometric special supports. On the fifteen reduced special points its coordinate-ring homomorphism is automatically an isomorphism. At a doubled point, \(O/5O=\mathbb F_5[t]/((t-2)^2)\), and the local Plücker coordinate \(p_{02}/p_{01}=t\) shows that the homomorphism from the Fano local ring onto \(O/5O\) hits its nonzero nilpotent generator \(t-2\). This map is therefore an isomorphism of the two length-two local algebras; permutation symmetry handles all six. Because both source and target are finite free \(R\)-modules of rank \(27\), a map inducing an isomorphism modulo \(5\) is an isomorphism over \(R\) by Nakayama's lemma. This proves the stated decomposition.

## Verification
The accompanying standalone `CHECK.py` performs exact arithmetic over \(\mathbb F_5\). It enumerates all \(806\) two-dimensional subspaces of \(\mathbb F_5^4\), verifies exactly \(21\) satisfy the four line-on-cubic coefficient equations, identifies the fifteen pairing and six node lines, and computes tangent dimensions zero and one respectively. It also checks the quadratic relation defining the ramified factor. These computations corroborate the geometric proof; enumerating rational lines alone would not establish completeness over an algebraic closure, which is instead obtained from finiteness, flatness, and the rank-\(27\) length argument above.

## Relationship to prior work
The explicit decomposition of the \(27\) geometric Clebsch lines into fifteen pairing lines and twelve cyclotomic lines is classical and is presented in the cited 2016 account. Cynk--van Straten use the reduction of the diagonal cubic modulo \(5\) and identify its new node. Casalaina-Martin--Grushevsky--Hulek describe the general one-node complex cubic's \(21\) lines and the multiplicity-two contribution of six node lines. These sources establish the underlying geometric pieces, but their inspected relevant treatments do not give the complete integral \(5\)-adic coordinate algebra or its explicit six quadratic ramified components. The result here is the relative scheme-theoretic, arithmetic synthesis, not the preexisting nodal line count or the classical list of lines.

## Limitations
The result concerns the specified diagonal integral cubic over \(\mathbb Z_5\), not every deformation of a nodal cubic. The quadratic decomposition is a local arithmetic statement at the prime \(5\); it makes no assertion about primes \(2\) or \(3\). Independently written treatments under another arithmetic or moduli-theoretic description may contain an equivalent identification; no assertion of exhaustive historical uniqueness is made.

## References
1. S. Cynk and D. van Straten, *Small resolutions and non-liftable Calabi--Yau threefolds*, Manuscripta Math. 130 (2009), 233--249, https://doi.org/10.1007/s00229-009-0293-0; full text: https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/42.Small%20Resolutions%20and%20Non-Liftable%20Calabi-Yau%20threefolds%20-%202009.pdf, Section 6.1.
2. J. Baez, *27 Lines on a Cubic Surface*, Visual Insight, 2016-02-15, https://blogs.ams.org/visualinsight/2016/02/15/27-lines-on-a-cubic-surface/.
3. S. Casalaina-Martin, S. Grushevsky and K. Hulek, *The birational geometry of moduli of cubic surfaces and cubic surfaces with a line*, Moduli 2 (2025), e1, https://doi.org/10.1112/mod.2024.12, Lemma 3.4.
4. F. Hirzebruch, *Die Hilbertsche Modulgruppe für \(\mathbb Q(\sqrt5)\) und die kubische Diagonalfläche von Clebsch und Klein*, working paper (May 1976), https://hirzebruch.mpim-bonn.mpg.de/id/eprint/203/; examined as historical modular context.
