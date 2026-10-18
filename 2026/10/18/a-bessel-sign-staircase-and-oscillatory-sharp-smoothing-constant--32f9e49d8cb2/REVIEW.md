# Mathematical review: sharp lattice temporal smoothing

## Correctness — PASS

The proof constructs the integer-lattice heat kernel, identifies the exact \(\ell^1\) and \(\ell^\infty\) convolution norm, and establishes the single sign crossing of each Bessel derivative by a Riccati argument. A discrete telescope proves sharpness and characterizes the signed extremizing inputs. Uniform Fourier kernel expansions control both the threshold locations and the oscillatory second-order error. The included code passed 134 finite numerical assertions, which are supporting checks and not substitutes for the analytic proof.

## Originality — PASS within examined sources

Abadias et al. (2021) provide the closest direct comparison: they bound the exact same discrete-Laplacian heat-kernel \(\ell^1\) norm by a non-sharp constant times inverse time. Abadias and de León-Contreras (2022) independently give related spatial-difference and time-derivative estimates. Ciaurri et al. (2014) and Grünbaum–Iliev (2002) supply the classical Bessel heat kernel, and Ignat (2006) provides qualitative heat-kernel estimates. These premises do not imply the exact all-time norm, phase-switching law, or oscillatory correction without additional analysis. Abadias et al. (2021), Theorem 4.3(iii), directly prove the relevant non-sharp \(\ell^1\) Laplacian-kernel decay estimate \(\|\Delta G_t\|_1\lesssim t^{-1}\), so this is the closest stronger-coverage comparison. Their inspected full manuscript gives neither the exact constant nor the switching times or the second-order correction. Global historical priority remains uncertain.

## Mathematical value — PASS

The norm concerns sharp deterministic amplification of the time derivative of a canonical Markov semigroup. Its spatial sign staircase identifies the exact worst input at every time. Its large-time correction has an entire accumulation interval rather than a numerical constant, a lattice phenomenon hidden by qualitative diffusion bounds. Together these give a precise benchmark for discrete smoothing and quantify the limitation of continuum approximations.

## Scientific limitations

The model is the homogeneous one-dimensional integer lattice with the specified unnormalized generator. No higher-dimensional or arbitrary-graph result is claimed. Independent mathematical and bibliographic audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
