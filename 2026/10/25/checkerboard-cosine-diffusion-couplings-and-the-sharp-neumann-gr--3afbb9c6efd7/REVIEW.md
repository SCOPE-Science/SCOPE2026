# Scientific assessment

## Correctness — PASS

The operator is the original orthonormal DCT-II Neumann modal heat step. The second derivative of a closed Dirichlet-kernel identity yields every cosine second moment exactly. Because the difference and sum of two nodal indices have opposite parity, the constant terms cancel; a sine-product identity proves the remaining cotangent-square difference strictly positive for every off-diagonal index pair. Counting same-parity pairs gives the exact number of negative generator entries. The one-to-two-node positivity and three-or-more-node nonpositivity follow from direct diagonalization and the derivative of the matrix exponential at zero. A zero-mode projector and Cauchy–Schwarz prove the stated sufficient eventual-positivity time. The exact three-node spectral projectors and a strictly monotone cubic complete the sharp smallest-grid recovery result. The standalone checker passed 19,645 deterministic checks; it is supplementary, not an infinite proof.

## Originality — PASS, subject to priority uncertainty

The original 2023 Neumann DCT diffusion study provides the method and observed maximum-principle violations but no complete exact signed off-diagonal generator classification or dimension threshold in its inspected ten-page paper. The 2021 effective maximum-principle analysis treats periodic rather than the exact unfiltered half-cell Neumann DCT heat step. Classical cosine-transform and difference-matrix literature provides related algebra but uses different discretized generators. A published general result on positivity times for self-adjoint semigroups with three spectral levels covers the qualitative eventual-positivity structure of the three-node example; the distinctive claim is the **all-grid alternating generator sign law and exact census**, not novelty of eventual positivity itself. A prior explicit cosine differentiation formula might imply the parity theorem through reflection and elementary trigonometry; that remains a material priority risk. No corresponding statement was located in the inspected source texts or targeted mathematical-record searches.

## Value — PASS

This is a complete, naturally motivated structural classification of the precise operator used in a published spectral maximum-principle investigation, rather than an arbitrary finite example. It identifies the first grid size at which nodal positivity must fail, which pairs are responsible in every dimension, exactly how many harmful couplings occur, and when all-time failure gives way to eventual strict positivity. These distinctions matter when assessing whether the exact spatial heat substep may be used as a positivity-preserving building block. The three-node recovery formula supplies a small exact reproducibility benchmark. The result does not assert a practical superiority theorem or general-grid sharp recovery time.

## Literature and limits

Primary source: Kim et al., Electronic Research Archive (2023), DOI 10.3934/era.2023273; full definitions and experiments were inspected. Relevant broader literature: Dong Li (2021), arXiv:2107.09438, inspected introductory and main-theorem portions; Strang (1999), DOI 10.1137/S0036144598336745; Strang and MacNamara (2014), DOI 10.1137/120897572. Some classical spectral differentiation literature and general self-adjoint-semigroup positivity results may contain equivalent or dominating component statements. The operator assumptions are unfiltered cosine modes, fixed one-dimensional Neumann boundary conditions, and exact exponential time evolution; neither nonlinear stability nor finite-step explicit time discretization is covered.

Self-review: passed. Independent audit: not yet performed.
