# Review of the exact spectral residue law

## Correctness
**PASS.** The full claim is reconstructed from the two explicit derivative matrices, the permutation induced by the number of right-branch visits, and the signed-cycle characteristic polynomial. The only symbolic-counting premise is the published bijection between non-all-left periodic words and nontrivial fixed points of iterates. The \(\ell=2\) parity case is explicitly treated, so the conclusion does not incorrectly assume that a real polynomial of degree two necessarily has nonreal roots. The roots-of-unity filter proves the counts and convergence. Exact symbolic replay on the specified finite ranges returned `CHECK_OK`, but is not treated as an infinite proof.

## Originality
**PASS with residual priority risk.** The closest comparison is Saiki–Takahasi–Yorke, arXiv:2202.04304, Sections 2.1–2.3 and Proposition 2.7. It supplies the two end-residue sufficient conditions and only lower asymptotic bounds, not the exhaustive criterion for every nonzero residue or the exact real/nonreal partition. For \(M\geq4\), middle residues are necessary to attain the sharp nonreal proportion. The related Takahasi paper arXiv:2409.01261 concerns periodic-point distributions of a different heterochaos baker family. An equivalent general signed-monomial spectral observation may exist outside the inspected literature; no claim of absolute priority is made.

## Value
**PASS.** The origin paper identifies simultaneous abundance and equidistribution of the two spectral types but leaves their relative global frequencies at the level of lower bounds. Determining those frequencies exactly for every dimension is a natural model-specific dynamical invariant: the nonreal class actually occupies asymptotic proportion \((M-1)/M\), as opposed to the earlier lower bound \(2/M\) for large \(M\). The proof reveals why every remaining twist class is nonreal, including a nonobvious negative two-cycle case.

## Scientific limitations
The result excludes the nonisolated fixed face; periodic points mean fixed points of the iterate, not primitive cycles. The full spectral-radius distribution and perturbation stability are not determined. The symbolic correspondence is credited to the primary paper; the finite checker verifies only small dimensions and periods.

Same-model review: passed. Independent audit: not yet performed.
