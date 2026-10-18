# Review: endpoint-lag correlation transition

## Correctness

**PASS.** The declared stationary Gaussian chain is stable because its drift is a finite lower-triangular matrix with diagonal \(-a\). The covariance recursion, independent-noise Itô isometry, and nilpotent matrix exponential yield the claimed normalized endpoint correlation and variance. Dividing the derivative by its final monomial proves a unique maximizing lag. A uniform geometrically dominated expansion yields the root \(\lambda_m=2m-2+O(m^{-1})\); Stirling and the central-binomial generating function produce all three depth regimes and the critical \(h_m=e^{\theta/m}\) window. Finite Lyapunov and matrix-exponential checks independently reproduce the exact formulas; they are not substituted for the analytical argument.

## Originality

**PASS with residual risk.** In Hennequin–Vogels–Gerstner (2012), the random triangular network and its ensemble-amplification calculation do not determine the lag maximizing the stationary normalized endpoint correlation in a deterministic nearest-neighbor cascade. Browning–Jenner–Baker–Maini (2024) drive downstream compartments from only a single noisy input; their explicit one-noise stationary covariance does not supply the fresh-noise-at-each-site normalization \(S_m(h)\) and its critical coupling window. Pal–Gupta (2026) discuss exceptional-point covariance relaxation, but its accessible abstract does not state the sharp endpoint peak and its three size regimes. Searches for aliases (feedforward OU, nonnormal linear cascade, triangular Gaussian network, Lag/Poisson polynomial, variance amplification) returned no equivalent theorem. General Gaussian semigroup identities themselves are known prerequisites, not claimed discoveries. The full motivating 2026 paper could not be read; implicit coverage or unindexed earlier work remains a risk, as does derivability from known linear-system formulas.

## Value

**PASS.** Directional time-delayed sensing in stable feedforward stochastic chains is a natural counterpart to known nonnormal amplification. The exact location of the correlation peak and its exponentially/algebraically separated detectability regimes give an interpretable sharp design boundary at coupling equal to damping. The transition occurs entirely without an eigenvalue stability change, with a finite-depth critical window that quantifies what a downstream observer can detect. This is more informative than a fixed-size covariance entry or a numerical peak location.

## Closest literature and limitations

Pal and Gupta, arXiv:2609.05391 (2026), motivate the exceptional-point question but their full preprint could not be inspected. Hennequin, Vogels and Gerstner, Phys. Rev. E 86, 011909 (2012), analyze random triangular network amplification; Browning et al., Phys. Rev. E 109, 054405 (2024), analyze one-noise-input multicompartment smoothing. The current claim is limited to the exact open-chain homogeneous independent-noise model defined in the result; no novelty is claimed for general OU covariance calculus. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
