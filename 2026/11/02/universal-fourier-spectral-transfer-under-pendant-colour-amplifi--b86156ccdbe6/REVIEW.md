# Scientific review

## Correctness — PASS

The theorem fixes the uniform-colouring law and the probability normalization. Full permutation symmetry of the palette makes all nonzero character-frequency blocks equal and orthogonal. Each attached leaf has conditional Fourier mean equal to minus \((q-1)^{-1}\) times its parent's character and conditional variance \(1-(q-1)^{-2}\); the leaf residuals are independent given the core. The resulting exact block matrix splits into \(n(s-1)\) contrast eigenspaces and two-by-two blocks over every core eigenvector. The trace, determinant, strict rank-one monotonicity, and the large-\(s\) expansion independently verify the spectral, nullity, sharp-bound, monotonicity, and asymptotic assertions. The standalone finite checker passed 228 assertion groups; none is used as a substitute for an infinite proof. The two-colour and singular-core boundaries are excluded from the affected assertions.

## Originality — PASS under bounded review

The closest inspected primary literature: Engbers–Galvin (arXiv:1101.0840v1) studies hard-constraint colourings on regular tori and spatial correlations, not pendant-correlation Gram spectra; Furmańczyk–Kubale (arXiv:1409.0650v1) studies equitable-colouring complexity on corona graphs, not Fourier sampling; Liu–Zhou (arXiv:1209.5906v1) and Lu–Miao (arXiv:1302.0457v1) study adjacency, Laplacian and signless-Laplacian matrices of other corona operations. These results do not imply the claimed formula without the distinct conditional-colouring analysis and do not state its rank and sharp quadratic-conditioning consequences. Previously recorded graph-colouring Fourier results on fixed graph families do not cover arbitrary cores after leaf attachment. The standard rank-one Schur/orthogonal block technique is explicitly not claimed original. Risk: an unlocated historical Potts covariance/graph sampling paper could give equivalent spectral transfer.

## Mathematical value — PASS

Pendant attachments are a basic graph operation that preserve the uniform core law but add substantial dependent measurements. It is a natural stability question whether those extra Fourier coordinates introduce new relations, improve reconstruction, or damage conditioning. The theorem resolves all three outcomes uniformly for every finite core: exact inherited nullity, strictly worse bounds for each attachment multiplicity, and a sharp quadratic blow-up with a leading coefficient that unexpectedly ignores the core's smallest eigenvalue. The complete-graph specialization gives a clean colour-palette rank threshold across an infinite two-parameter decorated graph family. This is more than restating a generic two-by-two eigenvalue calculation because the universal graph-colouring conditional law, all-frequency decomposition, structural invariants, and sharp asymptotic are required.

## Closest literature and limitations

Source identities and original posting dates appear in RESULT.md. Prior adjacency-corona spectra are close in block-structure technique but refer to different operators. The general statement does not provide an independent classification of the core spectrum and does not address q=2, nonuniform weights, or higher-degree characters. Full historical uniqueness cannot be established by a bounded search. The public mathematical statements are not externally certified.

Self-review: passed. Independent audit: not yet performed.
