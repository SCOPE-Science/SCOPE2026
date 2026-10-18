# Self-review

## Correctness — PASS

The exact Gram-matrix eigenprojector gives the squared principal-angle observable, with independent beta-prime radial and beta angular laws for the two Gaussian columns. At three rows, the Wishart eigenvalue Jacobian produces an exactly integrable angular density and gives \(R_3(\varepsilon)=\varepsilon^2/(1+\varepsilon^2)\) for every \(0<\varepsilon<1\). At two rows, the large-ratio angular kernel is \(1/(2x)+O(x^{-2})\), yielding \(R_2(\varepsilon)=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2)\). For every fixed \(s>2\), a negligible low-ratio region and an integrable \(t^2/r\) dominator yield \(R_s(\varepsilon)/\varepsilon^2\to1/(s-2)\). These are analytic proofs. The package verifier independently checks 1,500 Gaussian Gram eigenvector identities, 18 exact three-row integral identities, and 10 moment-integral asymptotic sanity tests; its finite calculations do not prove the continuous formulas.

## Originality — PASS, with limitations

Nakatsukasa and Park, arXiv:2206.00975 (2022), analyze exactly the left-sketch trailing-singular-vector problem but give perturbation and probability bounds, not the present exact mean squared angle or critical two-row log law. Gilbert–Park–Wakin, arXiv:1211.0361, likewise give recovery guarantees. Most closely, Takemura–Sheena, METR02-13 (2002), give weak Wishart eigenvector limits, but the nonintegrable limiting squared ratio for \(s=2\) cannot settle its finite-small-eigenvalue mean; that paper does not give the three-row nonasymptotic risk formula. Dong–Martinsson–Nakatsukasa, arXiv:2211.04676, address another leading-subspace randomized scheme. Relevant published published-finding corpus searches reveal no evaluated matching mean-angle law. Residual risk: a specialized classical Wishart eigenprojector identity may reproduce some or all of the claim under another formulation. No independent priority certification is claimed.

## Value — PASS

The expected squared trailing-vector angle is a motivated diagnostic for approximate null-space extraction. The sharp transition between the minimal two-row Gaussian sketch and three rows isolates an oversampling phenomenon that high-probability singular-vector bounds need not quantify. The exact three-row risk gives a nonasymptotic algorithmic benchmark, and the general fixed-s leading constant makes the row dependence transparent. The claim is confined to a two-singular-mode model with exact arithmetic and standard real Gaussian left sketches; it does not generalize to arbitrary spectra, non-Gaussian embeddings, or high-probability tails.

Self-review: passed. Independent audit: not yet performed.
