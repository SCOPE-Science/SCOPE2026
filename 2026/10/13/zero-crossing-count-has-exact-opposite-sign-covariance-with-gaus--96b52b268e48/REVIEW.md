# Self-review

## Correctness
PASS. The bivariate calculation gives \(\operatorname{Cov}(I_i,X_i^2)=-\sigma^2\rho\sqrt{1-\rho^2}/\pi\). Gaussian AR(1) conditional second moments propagate this local covariance by \((\rho^2)^d\) to every other site, and finite summation yields the displayed total covariance. The sign follows because every \(1-\rho^{2r}\) is positive for \(|\rho|<1\). The standalone checker reproduces the local integral and the two algebraically equivalent finite covariance evaluations.

## Originality
PASS. The closest inspected primary source, Sinn–Keller, studies zero-crossing probabilities, crossing-crossing covariances, and the variance of empirical crossing rates, including the same AR(1) model. Its full text was inspected around the definitions, theorem map, and AR(1) application, together with targeted searches for energy, square, amplitude, and quadratic terminology; the present mixed crossing/energy covariance was not found. Finch's full arXiv text defines the same finite sign-change count and explicitly focuses on its variance and higher count moments, not on amplitude energy. Semantic database searches using zero crossing, sign change, AR(1), squared amplitude, energy, and covariance aliases returned no equivalent statement. The closest prior local result concerns sign-blind runs versus centered sample variance for iid symmetric observations; there the uncentered magnitude energy is independent of the sign statistic, so it does not imply the dependent AR(1) theorem here.

## Value
PASS. Zero-crossing counts and quadratic energy are canonical time-domain summaries used respectively for oscillation/sign activity and amplitude scale. The result gives an exact finite dependence law, not only an asymptotic approximation: serial persistence makes crossings occur preferentially at low-energy configurations, while negative serial correlation reverses the effect. The edge-to-site kernel identifies the mechanism and shows how dependence activates a coupling that disappears at \(\rho=0\).

## Closest literature and limitations
Sinn–Keller is the closest exact Gaussian zero-crossing source and explicitly treats AR(1); Finch is the closest finite-segment sign-change source. Neither inspected text states the mixed quadratic-energy covariance. A residual risk remains that older Gaussian nonlinear-functional or signal-processing literature contains the same local sign/square identity or the summed AR(1) formula under different notation. The theorem is limited to zero threshold, Gaussian AR(1), and uncentered energy.

Self-review: passed. Independent audit: not yet performed.
