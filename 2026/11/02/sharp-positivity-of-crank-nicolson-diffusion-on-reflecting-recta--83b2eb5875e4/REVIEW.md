# Scientific review: reflecting-grid Crank–Nicolson positivity

## Correctness — PASS

The scope is the graph-reflecting product of two unit path Laplacians, with \(s=\kappa\Delta t/(2\Delta x^2)\). The proof explicitly identifies every possible negative entry through \(C=2(I+sL)^{-1}-I\); proves strict central diagonal minimization using a cycle heat-kernel difference system; derives a unique finite positive crossing from the path cosine spectrum; obtains the universal elliptic integral via image sums; and applies a one-dimensional Laplace method to the massive square-lattice axis Green function. The two parity constants reflect the exact nearest-image offsets \(\pm n\) versus \(n-1\) and \(-(n+1)\). An exponential moment bounds all remaining image terms. The independent finite rational matrix test and high-precision spectral/elliptic tests passed all 2806 checks; the arbitrary-size and asymptotic conclusions rest on the written analytic proof, not on finite tests.

## Originality — PASS on inspected evidence, qualified

The general resolvent diagonal criterion in “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains” is acknowledged in the first proof step. Faragó–Horváth (DOI:10.1137/050627241) were compared in substantial publicly accessible full text, especially Sections 5, 6 and 7: their 2D Crank–Nicolson finite-difference restriction is a sufficient maximum-principle bound, rather than the exact finite reflecting-grid criterion or parity correction. Higueras–Roldán (arXiv:2301.01066) were inspected in the available open PDF, including the hypotheses, main one-dimensional Dirichlet theorem and method. Their matrix boundary conditions and dimension differ. The full texts of Sun (DOI:10.1002/num.20402), Gao–Sun (DOI:10.1002/num.21760), Kraaijevanger (1992), and Beale (DOI:10.1137/080731645) could not all be accessed, so specialist priority remains a genuine limitation rather than a certified absence of prior work. The elliptic lattice Green formula of Morita and standard Laplace asymptotics are not separately claimed as original.

## Value — PASS

The already-motivated discrete maximum-principle problem has a simple but conservative two-dimensional sufficient CFL bound \(\kappa\Delta t/\Delta x^2\le1/2\). This theorem replaces it by the sharp all-rectangle constant approximately \(0.58819728\), gives finite-grid exact roots, identifies the precise sites of first violation, and provides a nontrivial two-parity exponentially small approach to that constant. These are useful reproducible benchmarks for one-step qualitative stability tests with reflecting boundaries, not arbitrary small numerical refinements.

## Scope, sources and residual risk

The exact root and center-minimization statements hold for every pair of integers \(m,n\ge2\). The elliptic limit requires both dimensions to grow, and the parity coefficients are for square grids. No claims are made about different boundary closures, general variable coefficients, multi-step norm stability, or independent publication priority. Relevant earlier works: Faragó–Horváth (2006), Kraaijevanger (1992), Sun (2009), Gao–Sun (2012 first published), Higueras–Roldán (2023), Morita (1971), and the prior resolvent-return note (2026).

Self-review: passed. Independent audit: not yet performed.
