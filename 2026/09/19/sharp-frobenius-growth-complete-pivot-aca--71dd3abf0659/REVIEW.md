# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** After permutation and scaling, a complete pivot reduces the problem to a block matrix with pivot one and every entry bounded by one. The rank-one update leaves only the Schur block \(X-rc^T\). The proof bounds this by \(\|X\|_F+\|r\|_2\|c\|_2\), optimizes the resulting scalar rational function exactly, and then uses only the complete-pivot constraints \(\|r\|_2^2\le n-1\) and \(\|c\|_2^2\le m-1\). The sharpness family makes the two inequalities equalities asymptotically while maintaining a unique largest entry for every finite \(\alpha<1\).

The exact change identity was rederived independently by direct Frobenius expansion. The positive-semidefinite contrast follows from the Schur-complement property and \(0\preceq E\preceq A\), which implies \(\operatorname{tr}(E^2)\le\operatorname{tr}(A^2)\). The later-step corollary is applied only to the active residual block, whose previously selected rows and columns are exactly zero in exact arithmetic.

The standalone verification reproduces the sharp-family ratios for \(N=4,5,10,100\), checks the exact change identity numerically, tests the universal bound on several rectangular dimensions, and checks positive-semidefinite residuals. These computations support but do not replace the algebraic proof.

## Originality

**PASS, to the best of our knowledge.** The motivating preprint arXiv:2609.17947 was inspected for its ACA definition, related-work discussion, complete-pivot interpretation, stated rank-one contribution, and discussion of poor greedy behavior. It develops an exterior-algebraic, singular-vector-dependent description and an angle-based rank-one bound; the checked material does not state the dimension-only sharp Frobenius amplification factor proved here.

The complete-pivot cross-approximation analysis of Cortinovis, Kressner, and Massei (arXiv:1902.02283; LAA 2020) was checked in its complete-pivot algorithm and error-analysis sections. It explicitly tracks the classical max-entry growth factor and global approximation error, not the sharp ratio between consecutive Frobenius residual norms. Wilkinson's 1961 work and recent expositions of complete-pivoting growth were checked for the standard entry-growth framing. Additional searches combined “Frobenius norm”, “Schur complement”, “complete pivoting”, “largest entry”, “cross approximation”, and the candidate constants \(nm/(n+m-1)\) and \(N^2/(2N-1)\); no equivalent theorem was located.

The originality claim is deliberately narrow. Complete-pivot ACA, Schur complements, Gaussian-elimination growth, maximum-volume theory, and the possibility of poor greedy ACA behavior are established prior art. The exact norm expansion used as a monotonicity certificate is elementary and is not presented as an independent broad discovery.

The main residual risk is older numerical-linear-algebra literature on norm growth under Gaussian elimination. That literature is extensive, and not every historical source was inspected line by line. A result stated as a Schur-complement norm inequality rather than an ACA theorem could potentially overlap. The recent motivating preprint is also new enough that contemporaneous follow-up work may not yet be indexed.

## Value

**PASS.** The result turns a qualitative concern about greedy largest-entry ACA into a sharp local obstruction. In an \(N\times N\) active residual, one greedy step can amplify the Frobenius error by nearly \(\sqrt{N/2}\), despite choosing the unique largest entry. This directly explains why a pivot rule optimized for a single entry need not be aligned with residual-mass reduction, and it identifies the largest possible one-step damage using only dimensions. The PSD contrast also cleanly separates the general/asymmetric obstruction from the monotone Schur behavior underlying pivoted Cholesky.

## Limitations

The theorem is local and exact-arithmetic. It does not characterize the maximum product of such factors over a full complete-pivot elimination, nor does it imply typical growth on matrices from applications. It does not address floating-point backward stability, partial-pivot ACA, randomized pivoting, or the long-run behavior of weighted-mass and geometry-aware alternatives. The sharp construction is adversarial and structured.
