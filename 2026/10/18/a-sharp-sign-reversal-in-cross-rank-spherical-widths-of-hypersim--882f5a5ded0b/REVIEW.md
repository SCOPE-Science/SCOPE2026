# Supported review: rank-indexed hypersimplex spherical widths

## Correctness — PASS
The support-function identity is proved from indicator vertices and Gaussian ranks. The DKW-based empirical-quantile argument bounds the trimmed-sum linearization error by \(o_{L^2}(\sqrt n)\) at every fixed nonzero rank fraction. A joint central limit theorem with the independently distributed Gaussian radius yields the kernel; an exact covariance identity establishes moment convergence. Gaussian-tail integration supplies the closed form, and differentiation establishes the single sign transition. The standalone checker independently repeats 250 finite support computations, six Gaussian integrals, root verification, and fixed-seed covariance checks at opposite sides of the transition. Finite computations are corroboration, not asymptotic proof.

## Originality — PASS, qualified
The eligible geometric source (Pineda-Villavicencio and Schröter, arXiv:2010.10227, public 2020-10-20, 52B11) covers matroid/hypersimplex combinatorial reconstruction rather than angular width. Kabluchko–Litvak–Zaporozhets (arXiv:1511.08479) already establishes regular-polytope Gaussian-width and radial-normalization methods; these methods are not claimed as new. The specific two-rank hypersimplex kernel and the exact uniqueness of its negative-to-positive half-rank covariance threshold were not found in reviewed material or mathematical record searches. Closest records concern matroid-polytope inradii, uniform independence polytope radii and simplex-section face fluctuations, which do not imply the proposed statement. A potentially equivalent generalized jointly self-normalized L-statistic result under another terminology remains a real bibliographic risk; negative search evidence does not certify priority.

## Mathematical value — PASS
The natural fixed-proportion rank parameter compares distinct uniform-matroid hypersimplices under exactly the same random unit vector. Spherical normalization reverses the nonnegative leading raw Gaussian trimmed-sum covariance for a precisely characterized interval; the unique boundary \(\alpha_*=0.207998088885\ldots\) provides a sharp geometric dependency transition. The theorem is infinite-dimensional in scope and describes a full covariance kernel, not an isolated coefficient.

## Scientific limits
The theorem does not cover sublinear ranks, arbitrary affine images, or independent directions. Numerical computations do not imply the asymptotic statements. The novelty assessment is bibliographic and qualified, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
