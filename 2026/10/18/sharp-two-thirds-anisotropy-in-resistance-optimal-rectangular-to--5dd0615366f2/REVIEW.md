# Review of sharp two-thirds anisotropy in resistance-optimal rectangular tori

## Correctness

**PASS.** The proof treats every independently chosen conductance, not merely a symmetric ansatz. Strict positive curvature of the trace-inverse objective and edgewise identifiability establish unrestricted uniqueness, hence symmetry under graph automorphisms. The Fourier-mode stationary equation has a unique positive solution, and the exact periodic resolvent identity gives the fixed-width limit. Matching first and second terms is justified by explicit dominant orders. The included standalone `verify.py` independently checks full weighted Laplacian spectra, trace pseudoinverses, Green identities, and representatives of the asymptotic balance; it passed 1,296 assertions. Numerical evidence is not used as an infinite proof.

## Originality

**PASS, subject to residual literature risk.** Ghosh–Boyd–Saberi (2006, 2008) develop general resistance-optimal conductance allocation and graph symmetry. Bamieh–Jovanović–Mitra–Patterson (2011) develop Fourier-mode coherence scaling for periodic local-feedback networks. Tovar et al (2026) develop general network architecture under conductance cost models. The primary papers and their relevant sections were inspected; none yields the fixed-width optimal anisotropy exponent and its explicit coefficient as a stated result. Searches of the published-results index and literature using Kirchhoff index, coherence, torus, anisotropy, and equivalent budget terminology found no equivalent specialization. General convexity and Fourier diagonalization are prior knowledge, not claimed as new. Unindexed specialist literature could still contain an equivalent result.

## Value

**PASS.** Unlike generic graph optimization, the result gives the full allocation rule for the infinite rectangular-torus family and identifies the exact singular limiting law, with a quantitative factor-two improvement over uniform spending. The geometric fixed cross section and large longitudinal circumference motivate this narrow regime. The explicit two-thirds scaling and leading correction supply concrete mathematical information for choosing anisotropic resource ratios rather than routine normalization.

## Limits

All graph edges have identical linear conductance price. Both graph factors are cycles of length at least three. The limit keeps the second circumference fixed. The finite ratio is defined implicitly by a unique scalar root. No proof for arbitrary inhomogeneous edge prices, open boundaries or simultaneous two-parameter growth is claimed. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
