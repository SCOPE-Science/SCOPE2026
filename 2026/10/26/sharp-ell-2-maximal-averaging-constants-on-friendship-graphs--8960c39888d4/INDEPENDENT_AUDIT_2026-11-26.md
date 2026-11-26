# Independent mathematical audit

## correctness

PASS

For nonnegative inputs the maximal map is represented by independent row choices; its norm is the largest selector norm because every selector is dominated coordinatewise on nonnegative inputs, and its top singular input may be chosen nonnegative. The hub-singleton/all-triangle selector has the two-dimensional constant-outer block given in the source, with Gram trace (2m+13)/9 and determinant 4/9. Its other singular sectors have squared norms at most 4/9. The positive row-Gram eigenvector (r,1,…,1) satisfies 1<r<3 and λr=r+2m/3. For m≥5, comparison to this vector works row by row: triangle rows have same-pair overlaps at most 1/3 and other-triangle overlaps at most 1/9; global rows have weighted sum (r+2m)/(2m+1); leaf singleton rows are bounded by 4/3+(2m−2+r)/(2m+1)<7/3<λ₅; the hub singleton is bounded by λr. For m=4 and a singleton hub the leaf singleton bound drops to 2. With a global hub the all-ones row comparison gives at most 19/9<λ₄, with the triangle and global rows bounded by 13/9 and one. The m=1,2,3 threshold tests were reproduced independently for all 18, 162 and 1,458 labeled selectors, using the symmetric shifted Gram characteristic coefficients in the exact quadratic field. Nonnegative coefficients of the monic det(xI+λI−AAᵀ) preclude a positive root, exactly the required bound, since eigenvalues are real. The original checker uses the same exact test with a scaling and removes only permutations of whole pairs, retaining both orders within a pair. The right singular input h/a=(9λ−4)/2 activates the stated selector; expanding the radical gives the stated asymptotic.

## originality

PASS

The accepted claim is the exact centered ℓ² constant and displayed extremizer for m≥2 on the hub joined to disjoint pairs. The m=1 complete-graph benchmark and general existence of centered finite graph maximal inequalities are credited to prior work. The closest different graph/operator claims and exact star result do not determine these norms. The search establishes a bounded statement-level distinction, not priority over all possible windmill or cone formulations.

## value

PASS

Friendship graphs are a natural companion to stars and wheels in which a common hub combines with nontrivial local averaging inside each pair. An all-size sharp Hilbert norm, a matching input and its exact asymptotic clarify the effect of the local triangles; the value is not just a new small example or numerical spectral guess.

The dated certificate retains the supplied scientific assessment, sources and limitations.
