# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The statement reduces to three exact checks plus one standard discretization.

First, Lewko's finite Fourier block has a fixed positive-measure bad set for a real unit coefficient vector, and his combinatorial lemma forces the corresponding permutation pattern into at least one of two frequency orderings for every permutation of the selected columns.

Second, an open bad set on \(\mathbb T\) can be sampled with a positive proportion of points of the uniform \(M\)-grid for every sufficiently large \(M\). This follows by inserting a continuous cutoff supported in the bad set and using convergence of uniform Riemann sums. Choosing \(M\) prime and larger than the original frequency range ensures that every nonzero progression step is invertible modulo \(M\). Translation contributes only a unimodular factor, while multiplication by the step permutes the grid exactly.

Third, the functions
\[
u_n(r,0)=e(nr/M),\qquad
u_n(r,1)=e(\widetilde\sigma(n)r/M),
\qquad
v_n(r,\varepsilon)=(-1)^\varepsilon u_n(r,\varepsilon)
\]
have exact inner products
\[
\langle u_n,u_m\rangle=\langle v_n,v_m\rangle=\delta_{nm},
\qquad
\langle u_n,v_m\rangle=0.
\]
There are \(2M\) such vectors on \(2M\) atoms, so they form a complete orthonormal basis. Their evaluation matrix is square, unimodular, and has orthogonal columns, hence is complex Hadamard; for odd \(M\), all entries are \(2M\)-th roots of unity.

Finally, for an arbitrary permutation of all \(2M\) basis vectors, restricting to the distinguished \(u_1,\dots,u_N\) columns produces a permutation to which Lewko's combinatorial lemma applies. All unused columns receive coefficient zero. Interspersed zero-coefficient columns cannot reduce the maximal partial sum, so the finite Fourier obstruction survives in the full complete basis. The bad proportion loses only the factor \(1/2\) from choosing one of the two layers.

No limiting argument is used after \(M\) is fixed.

## Originality

**PASS, to the best of our knowledge.**

Lewko's arXiv:2609.18491v1 was inspected at Theorem 1, the explicit two-copy finite construction, Lemma 2, Lemma 4, the proof of the finite theorem, and Remark 5 on completeness. The finite theorem gives a finite unimodular ONS on \(\mathbb T\times\{0,1\}\). Remark 5 completes the infinite construction by adjoining complementary functions, but the paper does not state a finite atomic complete-basis or complex-Hadamard strengthening.

Searches were made for combinations of Garsia's conjecture, Kolmogorov rearrangement, finite groups, finite probability spaces, finite atomic orthonormal bases, complex Hadamard matrices, Butson matrices, Fourier matrices, and maximal partial sums. No source stating the theorem above was located.

Dutkay--Han--Sun, arXiv:1103.4380 / Trans. AMS 366 (2014), is a relevant neighboring source because it studies scrambled Fourier series and Hadamard-related spectral structures. Its stated divergence result concerns particular structured rearrangements and Dirichlet-kernel growth, not the universal-over-column-permutations Garsia property established here.

Bourgain's 1989 paper was checked as the main classical source around Garsia's conjecture. The accessible bibliographic and preview material confirms the subject and earlier maximal-inequality framework but does not provide evidence for this finite Butson-Hadamard restriction.

No specifically identified inaccessible source was found whose title or available statement gives concrete evidence of prior coverage. The main residual risk is that this strengthening is a short finite-cyclic completion of a very recent preprint, so a contemporaneous or folklore observation may not yet be indexed.

## Value

**PASS.**

The result removes two structural freedoms from the known finite counterexample at once. The system is not merely finite but lives on a finite atomic space and is a complete basis of that space. Equivalently, the counterexample can be encoded by a square Butson-Hadamard matrix.

This is stronger than enlarging an incomplete ONS by unused functions on the same nonatomic space: arbitrary completion could destroy unimodularity or introduce a basis not controlled by a rigid finite matrix class. Here completeness, finite atomicity, and exact unimodularity are built into the construction and the every-permutation obstruction survives.

The result also gives infinitely many matrix orders for each threshold \(H\), because every sufficiently large prime modulus works after the continuous bad set has been discretized.

The result does not provide useful dimension-versus-threshold bounds and does not address real Hadamard matrices.

## Literature checked

- M. Lewko, arXiv:2609.18491v1, especially Theorem 1, equations (1.2) and (3.2), Lemmas 2 and 4, the finite proof, and Remark 5.
- J. Bourgain, DOI 10.1007/BFb0090057, the classical Garsia/Kolmogorov rearrangement source and its accessible bibliographic material.
- D. E. Dutkay, D. Han, Q. Sun, arXiv:1103.4380, for adjacent Hadamard/scrambled-Fourier divergence phenomena.
- Search results for finite-group, finite-atomic, complex-Hadamard, Butson-Hadamard, and Fourier-matrix formulations of Garsia's conjecture.

## Scope of the claim

The novelty claim is limited to the finite atomic complete-basis strengthening, its Butson-Hadamard matrix formulation, and the observation that every sufficiently large prime modulus can realize the construction after discretization.

No novelty is claimed for Lewko's negative solution of Garsia's conjecture, his two-copy permutation mechanism, the classical divergent rearranged Fourier block, Bourgain's estimates, or standard facts about Fourier and complex Hadamard matrices.
