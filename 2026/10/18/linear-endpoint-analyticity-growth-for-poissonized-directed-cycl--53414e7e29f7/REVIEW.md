# Self-review

## Correctness — PASS

For each integer \(n\ge2\), the norm of the derivative of the rate-one oriented-cycle semigroup is exactly the total variation of the cyclic difference of a wrapped Poisson law. Convolution and endpoint row/column sums justify equality, including real and complex spaces. The small-time bound follows from unimodality of the unwrapped Poisson law; the large-time bound follows from the discrete Fourier spectral gap. On compact diffusive windows \(t=sn^2\), a Fourier expansion with Gaussian domination and uniform shifted Riemann sums yields the circular Gaussian total-variation functional. Jacobi's product makes the Gaussian strictly unimodal on each half-circle. An explicit inequality excludes \(u\le3/5\), and the negative derivative excludes \(u\ge1\). Strict concavity of the odd-theta-series objective on \([3/5,1]\), with checked exponential-tail bounds, proves a unique critical maximum and thereby convergence of every maximizing time. Fourier multiplier optimization gives the exact \(\ell^2\) comparator. The standalone checker passed 879 finite consistency assertions; these are not used as proofs of asymptotic uniqueness.

## Originality — PASS with residual priority risk

Closest primary literature: Saloff-Coste, *Random Walks on Finite Groups*, §2.2, formulates Poissonization of group convolution and not a sharp endpoint derivative norm; Gerencsér, arXiv:1401.1692 (originally posted 2014-01-08), establishes mixing-time statements on cyclic walks with extra edges, not the derivative-norm asymptotic; Xu, arXiv:1402.2344 (originally posted 2014-02-11), develops analytic semigroups on interior \(L_p\) scales and functional calculus, not the proposed endpoint asymptotic. Existing published mathematical-record results on Boolean-cube heat derivatives, cyclic \(\ell^4\) convolution, and finite spectral maximal regularity have different generators or quantities and do not logically imply this theorem. Queries for oriented cycles, Poisson semigroups, wrapped-Poisson variation and theta optimization did not identify a covering result; negative search results are not historical-priority certification. An equivalent derivation under total-variation-speed or circular Gaussian smoothing terminology remains possible.

## Value — PASS

The quantity \(\sup_{t>0}t\|Le^{-tL}\|\) is the endpoint analyticity norm for a natural family of nonreversible positive semigroups. The result proves a sharp linear dimensional divergence, identifies its theta-function coefficient, and forces all extremizing times to the same diffusive scale despite microscopic drift. It contrasts with the exact Hilbert-space constant, whose limiting coefficient is strictly smaller. These facts are mathematically distinct from routine Poissonization and from ordinary mixing-time estimates.

## Scope and limitations

The proof is for directed cycles with unit jump rate and for the two endpoint norms; no claim is made about arbitrary directed graphs or a finite-size convergence rate. No independent mathematical or bibliographic audit has been performed.

Self-review: passed. Independent audit: not yet performed.
