# Scientific review

## Correctness — PASS

For all \(0<\lambda\leq1\), \(\delta,h>0\), normalization by \(\sqrt S\) reduces the Itô Euler chain to two variance coordinates and one cross-moment coordinate. The forced nonnegative symmetric variance matrix has the exact eigenvalue criterion \(\rho(T)<1\), and its Perron eigenvalue bounds the modulus of the cross-moment multiplier. The \(2\times2\) principal minors prove an if-and-only-if step interval; the unique root is the stated exact formula. A positive Perron eigenvector proves linear divergence exactly at the threshold and exponential divergence above it from zero initial conditions, excluding finite-second-moment invariant laws. Inside the interval, mean-square contraction gives the unique quadratic-Wasserstein invariant law; inversion yields its two stationary variances. Strict inflation follows from a positive residual and positive inverse. The three power-law scaling limits and the noncommuting vanishing-step covariance limit follow from exact formulae. The verifier independently constructs the entire three-dimensional moment operator, checks exact symbolic identities, 1,500 numerical parameter cases and four rational examples.

## Originality — PASS, with priority risk

The 2019 Stratonovich sampler literature established the reversible perturbation and gave Euler experiments; it did not state the present sampler-specific covariance and exact timestep characterization in the inspected complete text. The October 2, 2026 Louis–Pavliotis–Vilmart paper proves continuous-time covariance decay and its critical perturbation scaling, and implements Euler–Maruyama with a fixed small timestep (Sections 3.1, 4.2, 6.1). The complete relevant sections and appendix were checked for a discrete counterpart. The present sharp discrete second-moment interval, stationary covariance formula and joint \(h\to0\) nonuniform bias limit were not located. The 2009 Buckwar–Sickenberger analysis uses a scalar linear test system (possibly representable as a planar isotropic complex equation), not this anisotropic two-coordinate Gaussian sampler. Search comparisons also considered general numerical-stability results and existing related numerical findings, which do not imply the exact present claim. Generic mean-square spectral-radius and Lyapunov facts are acknowledged as prior tools, not presented as discoveries. A specialized older two-dimensional formulation may still be equivalent.

## Mathematical value — PASS

The source's continuous-time prescription \(\delta=\lambda^{-1/2}\) is intended to overcome ill-conditioning; actual Euler discretization introduces a competing sharp stability constraint. The identity \(h_*=g/[(1+c)(\lambda+c)]\) connects the *continuous covariance decay gap* directly to the *maximum admissible discrete timestep*. The complete scaling trichotomy shows that stronger perturbations can yield no asymptotic continuous-rate advantage while collapsing the stable numerical step like \(\lambda^{4\alpha-2}\). The exact nonuniform variance limit \((1-t)^{-1}\) shows how even a vanishing step at the natural stability scale can retain macroscopic sampling bias. These answer a natural algorithm-design question not answered merely by proving generic small-step convergence.

## Literature and limits

- Louis, Pavliotis, Vilmart (2026), arXiv:2610.03191v1, Sections 3.1, 4.2, 6.1 and appendix: https://arxiv.org/html/2610.03191v1
- Abdulle, Pavliotis, Vilmart (2019), arXiv:1903.03024, complete HTML text including numerical discretization: https://arxiv.org/abs/1903.03024
- Buckwar, Sickenberger (2009), arXiv:0912.1968, scalar stochastic mean-square test equations: https://arxiv.org/abs/0912.1968
- The scope excludes nonlinear samplers, alternative integrators, stationary nonquadratic observables, and certified global absence of older equivalent special cases.

Self-review: passed. Independent audit: not yet performed.
