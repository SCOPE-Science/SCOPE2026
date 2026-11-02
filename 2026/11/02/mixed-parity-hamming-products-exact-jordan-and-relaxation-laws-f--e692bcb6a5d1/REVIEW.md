# Review of mixed-parity Hamming-product parity dynamics

## Correctness

PASS. On each odd-sized clique factor, the all-ones matrix is a rank-one idempotent; on each even-sized factor it is a rank-one square-zero map. Their tensor-sum decomposition gives the exact two-eigenvalue Jordan form. A chain-contraction argument on every selected two-dimensional even factor proves the exact rank, including factors of size two. The periodic and transient counts follow by the generalized zero/one eigenspace split and counting nested kernels. Explicit finite-state and matrix-rank checks reproduced all claimed consequences in tested cases (see `VERIFICATION.md` and the standalone files).

## Originality

PASS for the mixed-parity statement, with residual risk. The closest published ancestor is Peeters (2002), Section 3, treating Hamming graphs with a common alphabet size, including a characteristic-two rank formula when the common alphabet is even. Tadaki (1993) treats rule-90/150 dynamics on one-dimensional paths, not products of clique factors. The 2023 generalized-Hamming paper computes ordinary spectra of graph powers, not finite-characteristic Jordan chains. Actual semantic research searches did not identify a published result stating the mixed-odd/even coexistence or its all-field orbit and relaxation counts. The elementary nature of the tensor algebra creates an incremental-novelty risk; unindexed treatments remain possible.

## Mathematical value

PASS. Coordinate heterogeneity changes the qualitative behavior: the same neighbor parity rule necessarily has both nonzero primitive oscillations and sharp two-update transient layers on every mixed-parity product. Exact Jordan-block counts and time-to-recurrence distributions provide an invariant for a natural, unbounded family of product networks, rather than an arbitrary finite slice. The coexistence is absent from the uniform-parity limiting cases discussed by Peeters and is not encoded in ordinary real eigenvalue spectra.

## Literature and scope limits

The main claimed domain requires at least one odd and one even graph coordinate size. Uniform-product calculations are used as known or elementary components, not claimed as new. The proof does not cover other characteristics, self-inclusive parity, or changing update orders. The closest competing source (Peeters) was materially inspected through its full available text; the 2023 comparison used its stated scope and exposed spectral theorems, with full-text accessibility limited. Historical equivalence and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
