# Independent mathematical audit

## correctness

PASS

Reassessed the corrected RESULT.md and SLOGAN.txt under repairs/3. Each ordinary Ritz eigenvector gives the quotient u*TAu/(u*Tu), where T=S*S and u is the normalized trial vector determined by the eigenvector. The denominator is positive by the joint-space embedding, with no diagonalizability needed. In the orthonormal basis formed by u and the nonzero normalized residual of Au, the first column of the Hermitian compression of T−I gives h²+|z|²≤ε². The quotient is a+bz/(1+h), where a=u*Au>0 and b is the residual norm. Completing the square gives |z|/(1+h)≤ε/√(1−ε²), and taking h=−ε² with the traceless Hermitian completion realizes the entire allowed disk with a Gram square root. Tangency gives the maximal argument for a disk to the right of zero. The spectral polynomial of A bounds b/a by (L−μ)/(2√(μL)); the displayed endpoint-weighted vector realizes that bound. Complex conjugate tangent points are both attainable and the third-coordinate extension remains an embedding on the same two-dimensional trial/image plane. The degenerate cases ε=0 and κ=1 give positive real eigenvalues. Direct evaluation of the explicit κ=9 witness gives denominator 24/25, numerator 8/5+8√2 i/25 and angle arctan(√2/5). The earlier harmonic frontier and equality failures are correctly derived by inversion as prior coverage. Inspected the frozen RESULT.md, VERIFICATION.md and verify.py; the expected output and finite tests were not rerun and are not the universal proof.

## originality

PASS

For the repaired angular claim only. The original package cannot pass with the strict positivity frontier and its failure cases treated as a distinct new contribution: the earlier published harmonic result implies those statements exactly by operator inversion and exchanging the trial/image bases. This is positive evidence of coverage, not an access-related objection. The replacement removes that novelty assertion and credits the implication explicitly. The supported distinction is the sharp distortion-to-argument law below the known frontier, with attainable complex and dimension-reducing equality. The inspected prior results do not supply that refinement; the classical turning-angle ingredients are credited.

## value

PASS

The repaired claim turns the known qualitative sign assurance into a precise optimal worst-case angular tolerance for a standard non-Hermitian projected eigenproblem with Hermitian input. The exact sector is uniform over every trial dimension and improves the sign-only information at each strictly subcritical nontrivial distortion; one-vector sketches with genuine dimension reduction establish that no smaller sector can hold under the same assumptions. Neither the known positivity frontier nor the numerical example alone is being counted as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
