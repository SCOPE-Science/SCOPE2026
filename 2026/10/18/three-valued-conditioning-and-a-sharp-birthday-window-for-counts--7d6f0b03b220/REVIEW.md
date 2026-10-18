# Scientific review: three-valued CountSketch QR conditioning

## Correctness

**PASS.** The proof separates every possible bucket occupancy pattern. On the sole nonsingular collision pattern, an explicit orthogonal decomposition of the mean-zero hyperplane yields the compressed Gram spectrum \(\{2,1^{[m-3]},2/m\}\), giving exact preconditioned condition number \(\sqrt m\). Counting independent hashes and signs gives the three rational probabilities, and a falling-factorial expansion gives the critical-window limits. The included checker exhaustively verifies 48,160 bucket/sign assignments across four small cases, including the spectral classification, and checks actual QR right preconditioning on selected higher-dimensional samples. These tests supplement but do not replace the analytic proof.

## Originality

**PASS, with residual bibliographic uncertainty.** CountSketch itself, classical birthday collisions, quadratic sketch-size lower bounds for one-sparse oblivious embeddings, and the 2024 QR preconditioning algorithm are prior work. A known three-row tight-frame rank-loss calculation also covers the corresponding two-dimensional special configuration; the claim is expressly restricted to dimensions \(m\ge4\) and uses a different all-dimensional spectral and critical-window statement. Targeted searches did not identify a previously stated complete three-valued right-QR-condition distribution or the nonzero-collision penalty \(\sqrt m\) for all these mean-zero subspaces. These negative searches are not a uniqueness guarantee. A fully general earlier sparse-embedding analysis may implicitly imply parts of the law; priority has not been independently established.

## Value

**PASS.** The full condition distribution reveals more than whether a signed collision creates a singular sketch: an *opposite*-sign collision keeps QR operational yet creates a condition number growing as \(\sqrt m\) even though the original matrix is an isometry. The finite-\(m\) probabilities and sharp quadratic-scale limits quantify separate chances of exact preservation, degraded but invertible preconditioning, and complete QR failure. The mean-zero subspace is naturally the column space of any connected tree incidence matrix, so the obstruction is a motivated linear-algebraic benchmark, not an arbitrary coordinate slice.

## Boundaries and related literature

The guarantee in Chen–Tan's 2024 work is conditional on embedding; known one-sparse oblivious embedding lower bounds already cover the quadratic **order** of sketch dimension. This finding does not assert a new general lower bound, and a sketching algorithm may preprocess zero rows or adopt a stronger sketch. Relevant primary references and residual priority concerns appear in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
