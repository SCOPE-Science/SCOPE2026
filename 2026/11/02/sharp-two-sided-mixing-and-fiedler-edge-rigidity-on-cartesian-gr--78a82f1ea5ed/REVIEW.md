# Scientific review

## Correctness (PASS)

The claim is for every finite Cartesian product of connected vertex- and edge-transitive simple regular factors with at least two coordinates. Product diagonalization gives the exact two extremal nonconstant modes. Any orbit-constant feasible edge weights obey simultaneous sharp budget and negative-eigenvalue bounds, and the displayed weights attain the maximum of these lower bounds. The equality cases force all orbit-constant weights, with no overlooked free variables. For unrestricted uniqueness the PSD deficit of every arbitrary optimum, averaged over automorphisms, annihilates all lifted factor Fiedler eigenvectors. The local projected neighbor differences are linearly independent, so each independent edge weight must equal the displayed one. The Peterson adjacency identity gives an exact local Gram matrix \((2/3)I_3\); Fourier sine and cosine modes give an invertible two-neighbor difference system for every cycle. The phase boundary follows from the explicitly evaluated extreme eigenvalues. `verify.py` returned 4,801 assertions; the finite stress tests supplement rather than substitute for the proof.

## Originality (PASS on inspected evidence; remaining risk)

Boyd–Diaconis–Parrilo–Xiao, arXiv:0709.0955 (2007, published 2009), is the closest broad method: its semidefinite program and automorphism symmetrization already establish existence of a symmetric optimal walk, so neither the SDP nor averaging is claimed novel. Its inspected Petersen, Hamming and Cartesian-product calculations do not give the local projected-edge-rank criterion or prove that a non-orbit-constant optimum is impossible on mixed Petersen–cycle products. The 2026 product-eigenvalue analysis maximizes only algebraic connectivity at fixed directional budget, which cannot settle the simultaneous smallest/second-eigenvalue balance or uniqueness among arbitrary stochastic edge weights. Previously established all-clique and all-cycle product formulas are special cases and are deliberately excluded as independent novelty; their statements do not entail the mixed-factor Petersen–cycle holding phase without the new local rigidity argument. The closest articles have been compared at the level of objectives, assumptions, and theorem implications. Residual risk: historical work may contain a generalized uniqueness characterization that subsumes this local condition, or a separate unpublished mixed-product solution. The public bibliographic record of the 2007 technical report is month-only.

## Mathematical value (PASS)

The local independence condition converts a merely symmetrized eigenvalue design into a verifiably unique solution under all stochastic edge choices, which is a substantive structural guarantee for implementation and robustness. The mixed Petersen–cycle products supply an infinite nonhomogeneous family on which the sufficient condition can be proved exactly using a three-dimensional local projection certificate, and give a sharp all-dimension threshold: exactly one Petersen factor forces positive holding, whereas two or more force zero. The phase result cannot be obtained by extending formulas from homogeneous complete or cyclic products by parameter substitution because the Petersen spectral and local eigenspace structure is different.

## Closest sources and limitations

- Boyd–Diaconis–Parrilo–Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, https://arxiv.org/abs/0709.0955, 2007-09-06 (focal day-verified record); DOI:10.1137/070689413.
- Boyd–Diaconis–Xiao, *Fastest Mixing Markov Chain on a Graph*, https://stanford.edu/~boyd/papers/fmmc.html, general SDP foundations.
- *Algebraic Connectivity and Exact Laplacian Spectra of Generalized Graph Products*, DOI:10.29121/ijoest.v10.i4.2026.781, comparison of one-sided objective.

Unrestricted uniqueness requires the displayed local rank property. The analysis does not cover nonsymmetric chains or alternative stationary measures. Historical overlap beyond the inspected material remains possible. No independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
