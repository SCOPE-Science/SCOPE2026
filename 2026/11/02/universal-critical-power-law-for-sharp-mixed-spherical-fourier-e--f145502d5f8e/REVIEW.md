# Self-review

## Correctness — PASS

The domain is each fixed integer \(d\ge3\), real \(q>2d/(d-1)\), with actual sphere surface measure and the unnormalized Fourier transform. The finite-exponent sharpness and mode ordering are established published premises [1, Theorems 1.2--1.3]. The proof explicitly computes the shared critical residue \(A_d\), proves conditional convergence and differentiability in exponent of the adjacent-mode difference \(L_d\) via a zero-mean periodic phase and a uniform integrable Hankel remainder, uses [1, Theorem 3.9] to establish strict positivity at the critical exponent, and derives the fractional law and the sharper relative linear law algebraically. Crucially, positivity does not follow merely from strict positivity at exponents above critical; it follows from positive finite Bessel-zero cells at the endpoint and convergence along those cells. The numerical code passes two-dimension and six-near-endpoint checks but is non-certifying and not the basis for the infinite conclusion.

## Originality — PASS under inspected evidence

Xu [1] proves the exact finite-exponent stability coefficient but neither its critical fractional-power vanishing rate nor the renormalized limiting constant. His circle calculation keeps a common critical moment pole explicit to obtain modal ordering, which is not an asymptotic sharp-global-stability theorem. Carneiro--Oliveira e Silva--Sousa [2] provide the earlier modal reduction, and Ciccone--Sousa [3] treat different modal optimization regimes; no inspected result entails the stated \(1/d\) sharp stability coefficient asymptotics. Previously known large-exponent asymptotics have a different endpoint and do not imply the critical limit. Relevant published research index records about spherical modes, critical Fourier kernel norms, and Bessel Turán inequalities concern different domains or invariants. Similarity searches are negative evidence only, not a proof of novelty. Residual risk: equivalent historical or unpublished endpoint renormalizations.

## Value — PASS

The exact optimal global stability coefficient is the stability modulus of a sharp Fourier extension inequality; its behavior becomes singular at the natural critical integrability threshold. Showing \(\Gamma\asymp(q-q_d)^{1/d}\) for every fixed dimension, identifying a positive finite-part coefficient and proving a different linear *relative* collapse describes the boundary of the full-dimensional sharp result rather than a routine substitution. The dimension-dependent exponent and the coexistence of norm blow-up with absolute stability decay are informative for understanding near-critical inequalities. No claim of a new endpoint inequality is made.

## Limits and closest literature

The theorem uses Xu's exact global finite-exponent spectral identity and Bessel zero-cell positivity. It applies neither to the plain unmixed norm nor to dimension two, where a different highest nonconstant mode may govern the sharp gap. Source [1] contains critical-tail cancellation in the circle but not this coefficient limit. The earlier high-exponent asymptotic works at the opposite exponent endpoint. Literature indexing is incomplete. No independent external mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
