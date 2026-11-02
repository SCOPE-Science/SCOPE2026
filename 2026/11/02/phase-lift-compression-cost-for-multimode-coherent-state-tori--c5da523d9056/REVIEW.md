# Review: Phase-lift compression cost for multimode coherent-state tori

## Correctness — PASS

For a normalized oscillator vector, the Fourier coefficient vectors of the phase orbit are orthogonal; for the rank-one Hilbert--Schmidt orbit, matrix diagonals with distinct difference indices are orthogonal. Their squared norms are respectively the number-distribution weights and the difference-convolution weights. Averaging any complex rank-\(N\) projection gives the Ky Fan lower bound, attained uniformly by keeping the top Fourier coefficients. Convolution majorization gives the width inequality, strict for full-support product Poisson laws. Stirling and Fourier inversion yield the product Gaussian local limit; tightness, radial level-set separation and lattice counting give the two exact dimension limits and ratio \(2^{d/2}\). The companion script passed 724 finite checks, but infinite claims depend on proof. The statement does not concern physical encoding or positive reconstruction.

## Originality — PASS (best-knowledge; priority risk remains)

The general isometric orbit-width spectral method is closely related to Arbes--Greif--Urban, *The Kolmogorov N-width for linear transport: exact representation and the influence of the data* (2025), whose primary proof and eigenspace characterization were examined. This method and elementary Poisson/Skellam identities are acknowledged as prior ingredients. The specific infinite-dimensional coherent phase torus, the convolution comparison of pure vectors with their rank-one Hilbert--Schmidt lift, and the anisotropic fixed-error ratio \(2^{d/2}\) were not located in checked primary literature or published-finding corpus mathematical records. Drummond--Reid describes projected phase states but not widths; Mamon studies orbit dimension, not approximation cost. The Mensah 2026 motivating work's primary text was inaccessible, and a broader result might implicitly subsume the sharp quantitative comparison. No absence-of-search-result is asserted to prove uniqueness.

## Mathematical value — PASS

The exact budget for optimally approximating a full multimode phase orbit is a natural operator approximation invariant. Rank-one lifting is an essential representation change from state vectors to Hilbert--Schmidt observables. The constant \(2^{d/2}\), independent of anisotropy and fixed positive tolerance, quantifies a nontrivial dimension-driven overhead; its covariance-convolution mechanism also explains the exact finite-intensity ordering. This offers a sharp reusable benchmark for linear reduced-order models, without claiming physical admissibility.

## Literature limits

Main closest general method: Arbes--Greif--Urban, DOI 10.1007/s10444-025-10224-0. Other inspected full texts: Drummond--Reid, arXiv:1610.01261; Mamon, arXiv:2506.07995. Mensah, arXiv:2608.29976, was available as an abstract and third-party report only; primary full text was inaccessible. The remaining risk is implicit coverage by more general prior shift-group width theory or a separately published coherent-state approximation result.

Self-review: passed. Independent audit: not yet performed.
