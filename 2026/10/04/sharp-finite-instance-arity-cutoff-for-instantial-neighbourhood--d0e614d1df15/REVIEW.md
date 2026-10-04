# Review

## Correctness

PASS. The source semantics says that \(f_k(B_1,\ldots,B_k;A)\) holds at \(x\) exactly when a neighbourhood \(D\in N(x)\) lies inside \(A\) and meets every instance set. Taking \(A=D\) and the instance sets to be all singletons of \(D\) forces the witness to equal \(D\), giving exact reconstruction with at most \(n\) instances.

For sharpness, the pair \(\mathcal P(X)\setminus\{X\}\) and \(\mathcal P(X)\) agrees below arity \(n\): whenever the full carrier witnesses a lower-arity test, one selected point from each nonempty instance set gives a proper transversal of size at most \(n-1\). At arity \(n\), the \(n\) singleton instance sets force the full carrier uniquely. The checker exhaustively confirms these claims for all local neighbourhood families through four worlds.

## Originality

PASS. The 2026 primary source contains the reconstruction mechanism that yields the upper bound, but it does not state or prove that the finite cutoff \(n\) is least possible. The originality of the accepted claim rests on the matching lower bound and explicit indistinguishable frame pair.

Targeted searches for finite arity, bounded arity, frame reconstruction, BAIO truncation, and INL fragments found no statement of the exact \(n\)-world cutoff. The 2022 fragment paper is highly relevant but its full text was inaccessible; its abstract does not state this finite reconstruction result, so overlap there remains an explicit residual risk.

## Value

PASS. The new duality paper works with an \(\omega\)-indexed BAIO signature and explicitly discusses shrinking the complete-atomic signature. The theorem gives an exact finite answer to the complementary question of how much of the ordinary BAIO signature is required on an \(n\)-point carrier. The bound is both constructive and sharp, so it can be used to truncate finite-frame calculations without losing any neighbourhood information.

## Closest literature and limitations

De Groot (2026) is the direct source for the operator semantics and the upper reconstruction mechanism. Van Benthem–Bezhanishvili–Enqvist–Yu (2017) introduce INL and its expressive fragments. De Groot (2022) studies an arity-indexed family of fragments, while Payette–Brunet (2026) studies full and unary Henkin completeness.

The result does not give optimal cutoffs for restricted frame classes or formula-complexity normal forms.

Same-model review: passed. Independent audit: not yet performed.
