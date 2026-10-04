# Review

## Correctness
PASS. The proof uses the discrete support-transfer lemma to reduce any solution to a polytope with exactly the prescribed \(2n\) normals. Linear independence turns that polytope into an affine image of a box. The facet \((n-1)\)-Jacobian is computed explicitly, the \(L_p\) mass equations reduce to a common scalar, and the exponent \(n-p\) is positive, giving one and only one scale. Direct substitution verifies existence. The packaged numerical script checks two nonorthogonal instances but is not used as an infinite proof.

## Originality
PASS. The closest recent source establishes existence for spanning antipodal supports and supplies the support-transfer lemma, but its theorem and proof do not give the closed-form inverse or the uniqueness statement for the minimal \(n\)-pair case. The older negative-\(p\) discrete existence theorem excludes antipodal supports through its essential-subspace hypothesis, while the classical polytope theorem for \(p>1\) lies in a disjoint exponent range. Semantic database searches for the explicit parallelotope inverse, minimal antipodal supports, and uniqueness found no statement implying this result. The residual risk is that the elementary special case may have appeared under different terminology outside the inspected literature.

## Value
PASS. Exactly \(n\) antipodal normal pairs are the smallest antipodal support that can span \(\mathbb R^n\), so this is a natural boundary case of the newly solved negative-\(p\) problem rather than an arbitrary parameter slice. The formula supplies a complete inverse, a uniqueness island in a regime where uniqueness is generally delicate, and a concrete benchmark for theory and computation. Unequal opposite masses are informative because they recover the translation, not merely the side lengths of a centered box.

## Closest literature and limitations
The result uses Shan's 2026 existence theorem and support lemma as its nearest input. It does not extend uniqueness beyond the minimal spanning antipodal support, and it assumes unit normals. The accompanying computation only checks sample instances.

Same-model review: passed. Independent audit: not yet performed.
