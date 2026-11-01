# Scientific review: circular Fock interpolation asymptotics

## Correctness — PASS

The claim is precisely about the squared spectral condition number of the normalized kernel Gram matrix at \(N\) roots of unity scaled to squared radius \(\rho N\), for each fixed \(\rho>0\). The Fourier–Poisson residue identity is exact; it is not asserted as new. Uniform Poisson-mode estimates prove the largest-eigenvalue normalization. The subcritical proof compares the first \(N\) Poisson masses using unimodality and the exact ratio at \(N-1\), and correctly retains the critical value \(\rho=e^{-1}\). The supercritical proof establishes a unique rate-balancing point, an all-residue localization estimate, uniformly controlled two-term Stirling asymptotics, and the finite shifted-integer minimum. It treats both potential discrete minimizers without claiming uniqueness. Bounds on the positive phase factor justify division and the relative error estimate. The standalone finite checker passed 85 assertions, but universal claims depend on the proof, not those tests.

## Originality — PASS with stated access risks

The closest **stronger-looking** baseline is Horoshko–De Bièvre–Kolobov–Patera, arXiv:1602.07852, Eq. (9), which already states the exact Poisson residue spectrum. The new claim does not repackage that identity as a discovery. Its work is the sharp, joint large-\(N\) optimization of all residues in the regime where the squared radius is proportional to \(N\). Neither the complete 2016 article nor the full 2026 Fock representer-theorem article identifies the \(e^{-1}\) worst-residue phase boundary, critical mode or phase-modulated prefactor. The 2024 study *Optimal circular states* addresses photon-number optimization; its accessible preview does not permit a conclusive full-text comparison. The 1993 circular-state paper was accessible as an abstract only. These last two are residual originality risks, not asserted noncoverage proofs. Exact spectra imply all derived asymptotics **in principle**, but the new statements require a nontrivial rate-envelope optimization and a two-saddle discrete local calculation absent from the inspected primary text.

## Value — PASS

Optimal kernel interpolation stability is a natural quantitative invariant in complex reproducing-kernel approximation. The scaling \(|z_j|^2=\rho N\) compares the number of sampling sites with photon number/intensity; this is not an arbitrary finite slice. A sharp transition from a one-tail Poisson obstruction to a balanced two-alias obstruction, together with its oscillating exact prefactor, distinguishes stability mechanisms that the already known exact spectrum alone does not articulate. It gives an explicit exponential cost for worst-case interpolation and a precise input for the conditioning of numerical kernel solvers. No generalization to arbitrary sampling patterns is claimed.

## Closest sources, limits and verification status

Relevant full primary text: N. Alpay, A. De Martino, K. Diki, arXiv:2604.22165v1, specifically Section 4; D. B. Horoshko, S. De Bièvre, M. I. Kolobov, G. Patera, arXiv:1602.07852v1, especially equations (5)–(9), (22)–(25), Sections IV–V. Partial related literature: S. Luo, S. Tang, Y. Zhang, DOI:10.1088/1751-8121/ad8792, publisher preview only; J. Janszky, P. Domokos, P. Adam, DOI:10.1103/PhysRevA.48.2213, abstract only. Results are fixed-\(\rho\), not uniform at the transition; no claim about perturbed polygons or a finite-index supercritical optimizer. There is no external independent validation.

Self-review: passed. Independent audit: not yet performed.
