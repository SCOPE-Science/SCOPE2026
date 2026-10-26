# Scientific review

## Correctness — PASS

The exact six-character mixed-moment identity is derived from branching for the natural permutation representation, the dimensions and eigenvalues are reconstructed using hook lengths and Frobenius's transposition-ratio formula, and the covariance is obtained by subtracting first moments. For \(n\ge7\), a strict Jensen inequality using the *exact* convex-combination identity proves negativity at every unbounded integer step \(t\ge2\). For \(n=6\), the one negative eigenvalue is handled separately by parity; the \(n=5,t=3\) positive boundary is an exact finite count. An independently implemented exact-arithmetic state-enumeration checker confirms all stated tested finite cases. No finite experiment is used as a substitute for the general proof.

## Originality — PASS (best-knowledge, with residual historical-priority risk)

The accessible literature supplies exact one-cycle-count expectation formulas and general character tools, but the inspected theorems and sections do not cover the complete signed *mixed* covariance in the non-lazy discrete walk. Alon and Kozma (2010) provide a decomposition for **one** cycle-length count, Berestycki and Kozma (2012) derive single-length expectations for continuous time, and Diaconis and Shahshahani (1981) give group-Fourier machinery and mixing for a lazy walk. Bernstein (2016) treats a different involution kernel. The mixed-character identity and strict-convexity sign classification are additional nontrivial steps. Search failure is not a proof of priority; earlier equivalent computations may exist.

## Mathematical value — PASS

A persistent sign law for two classical, correlated-at-finite-time cycle statistics is relevant to the transient structure of permutation shuffles. The result contrasts with their zero covariance at the uniform stationary distribution and identifies the exact finite-size threshold \(n=6\), with an explicit \(n=5\) counterexample. It is an all-time structural classification rather than an arbitrary numerical slice or simply a marginal expectation restatement.

## Closest sources and limits

The prior-work comparison includes full accessible primary manuscripts by Alon–Kozma (2010), Berestycki–Kozma (2012), Diaconis–Shahshahani (1981), and Bernstein (2016). The distinction between non-lazy discrete and lazy/continuous-time kernels is essential. The four published works' general spectral methods can in principle derive mixed moments, but none of their inspected asserted conclusions fixes the mixed covariance sign at every step. Older historical equivalences remain possible.

Self-review: passed. Independent audit: not yet performed.
