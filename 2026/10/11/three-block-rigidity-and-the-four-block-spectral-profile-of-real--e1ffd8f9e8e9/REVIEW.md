# Scientific review: three-block rigidity and four-block Paley profile

## Correctness — PASS

The block normalization is reconstructed from [1] Theorem 4.2 and its displayed signature formula; at \(q=13\), \(12(G_A-I)\) has off-diagonal blocks \(\bigl(\begin{smallmatrix}1&\sqrt{11}\chi(a-b)\\\sqrt{11}\chi(a-b)&-1\end{smallmatrix}\bigr)\). The determinant-negative-one reflection holonomy forces the universal three-block eigenvalues. For quartets, the real-antilinear reduction to \(H=(C+i\sqrt{11}S)(C-i\sqrt{11}S)\) yields the four exact integer polynomials. The supplied program completes all \(715\) quartets and independently tests the triple formula at two field orders; a direct symbolic eight-by-eight determinant also confirms the exceptional factorization. The root maxima are \(100\), \(60+8\sqrt3\), \(56\), and \(108\), so only the 52 exceptional sets attain \(\delta_4=\sqrt3/2\). Residual risk: the finite proof depends on the transparent exact-arithmetic certificate, and no independent audit has been conducted.

## Originality — PASS (bounded claim)

The construction, character normalization, and conference-matrix realization are prior results of [1] and [2]. Neither the inspected construction theorem and proof nor its conference-matrix reformulation gives the quartet characteristic-polynomial distribution or the 52 maximizing four-subsets. The discussion of block restricted isometry in [3] motivates this question but addresses highly symmetric, different ensembles and does not imply this arithmetic distribution. General subframe-erasure theory [4] provides no numerical classification of these particular quartets. The contribution is **not** the existence of the frame or a routine restatement of the signature blocks; it is the exact restricted Gram spectral profile, its sharp extremizers, and the reflection-holonomy mechanism. Residual risk: an older classification of principal submatrices of Paley conference matrices could express this same data in different terminology.

## Value — PASS

The restricted isometry constant controls four-block stability of a natural 13-plane harmonic frame. Pairwise equi-isoclinism alone does not determine higher-order spectra; the triple rigidity and the transition to exactly four quartet profiles give a structural answer at the next block size. The full optimizer classification is a natural invariant, not an arbitrary parameter slice. There is no claimed downstream theorem beyond the stated sharp spectral characterization.

## Closest literature and limits

[1] Fickus–Iverson–Jasper–Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267, Theorem 4.2 and equation (44); [2] the same authors, *Equi-isoclinic subspaces, covers of the complete graph, and complex conference matrices*, arXiv:2212.12617, Proposition 8; [3] the same authors, *Totally symmetric Grassmannian codes*, arXiv:2406.19542, block restricted isometry discussion; [4] Cheng–Lv–Sun, *Frames of uniform subframe bounds with applications to erasures* (2018), abstract and accessible article information. Four-plane results are confined to \(q=13\); the polynomial census requires exact enumeration. Related conference-matrix tables remain a bibliographic risk.

Same-model review: passed. Independent audit: not yet performed.
