# Scientific review: sharp DGDA finite-horizon transient

## Correctness — PASS

For \(A^{\mathsf T}A=a^2I\) and \(\rho=1/2,\eta=1/a\), the update reduces by the skew-complex-structure eigenbasis to \(B=\left(\begin{smallmatrix}1/2-i&1/2\\1/2&1/2\end{smallmatrix}\right)\). Subtracting its eigenvalue \(\lambda=(1-i)/2\) leaves a rank-one nilpotent of norm one. The exact singular value of its binomial power yields the operator-gain formula and quadratic prefactor. The discrete upper bound for all \(k\ge4\), with explicit comparisons at \(k=0,1,2,3\), proves the unique global maximum. Direct evaluation on synchronized states yields the original-variable amplification. The embedded standard-library verifier passed 209 direct and algebraic checks; it does not substitute for the all-horizon proof.

## Originality — PASS, with limitations

Zheng, Loizou, You and Mallada, *Dissipative Gradient Descent Ascent Method* (arXiv:2403.09090v1, 2024), Secs. III–IV and Appendix B, introduce the same iteration and its geometric convergence rates. Their inspected analysis does not furnish the exact induced power norm, sharp all-time integer peak, synchronized-state amplification or critical Jordan polynomial prefactor. De Montbrun and Renault (arXiv:2208.03085, 2022) analyze a distinct optimistic two-step method. The published published-finding corpus Jordan affine-norm result (2026/10/11, id 00a25760cd57) optimizes an affine nilpotent pencil and spectral-set constant, not DGDA powers; the published PDHG results (2026/10/4, ids f8268fe426bc and 788191221208) concern different primal-dual update operators and asymptotic ratios. The algebraic Jordan-power identity itself is standard and is **not** claimed as new. Search absence alone does not prove novelty; an equivalent DGDA analysis in another source remains possible.

## Value — PASS

The sharp squared finite-time amplification \((10+3\sqrt{11})/8\) occurs for an algorithmically recommended tuning even in a perfectly conditioned bilinear game. Natural synchronized initialization yields an actual-variable error spike \(9/4\). The resulting \(k^2 2^{-k}\) norm behavior differentiates spectral-radius convergence from uniform finite-horizon performance and provides exact stress benchmarks for damping and finite-iteration assessments. This is a complete structural boundary, not a claim that DGDA diverges.

## Scope and residual risks

The finding covers only equal-singular-value square bilinear games and the stated fixed steps. Published methods with equivalent state-space similarity, alternative norms, or finite-step transient estimates may overlap even where keyword searches do not. Independent external originality assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
