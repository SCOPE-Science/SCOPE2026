# Scientific assessment: sharp drift–isotropy synthesis

## Correctness — PASS

The claim fixes positive propulsion speed, rotational diffusion and Poisson angular-reset rate, permits nonnegative isotropic translational diffusion, and assumes stationary orientation initialization. The angular Markov generator yields the stationary first two Fourier coefficients and one common exponential autocovariance factor. Explicit double-time integration gives the finite-time covariance matrix and its long-time effective diffusivity. The sharp complex moment disk follows from the equality-capable inequality \(|\mathbb E(Z-\mu)^2|\le\mathbb E|Z-\mu|^2\), and two-point chord laws realize its entire boundary; convex mixtures use at most four atoms. The zero-traceless criterion yields the exact drift ceiling; equality forces chord support and uniquely fixes the symmetric, deterministic, or antipodal optimizing laws. A standalone checker passed 8,472 finite diagnostics, including the deterministic-angle formula of Baouche et al., exact reset-law syntheses and stationary harmonic samples. Numerical diagnostics supplement the analytic proof rather than certifying infinite parameter families.

## Originality — PASS, subject to independent priority assessment

The 2020 Kumar–Sadekar–Basu paper analyzes orientational resets to a fixed direction. Baouche–Franosch–Meiners–Kurzthaler (2024), arXiv:2405.06769, formulates a general angle-reset law but explicitly fixes a Dirac-angle law for its moment and displacement calculations: their equations (17)–(20) already imply the deterministic-angle special case of the present covariance. Their concluding text motivates changing the angle distribution. Olsen–Löwen (2024), arXiv:2405.14326, treats independent *relative* turning increments with chirality, not absolute redraws; Ghosh–Mandal (2025), arXiv:2501.05149, treats shape anisotropy with deterministic reset orientation. Neither compared claim covers the full prescribed-drift tensor disk, sharp isotropic-drift envelope for arbitrary reset laws, or the exact unique optimal protocol switch. The first-two-Fourier-moment disk is a known general mathematical technique and is credited as such, not claimed as independently original. A reformulation implicit in broader moment-problem or controlled-orientation literature remains a priority risk.

## Scientific value — PASS

The result answers a design question specific to active transport: how large can a swimmer's directed speed remain when one insists on exactly isotropic *fluctuations*, and which angular reset laws achieve that bound? It supplies an if-and-only-if feasibility criterion for every reset/rotation ratio, explicit synthesizable reset protocols with at most four directions, a sharp one-half structural crossover, and finite-time validity. This is a complete physically motivated classification, not an arbitrary parameter evaluation or a known-table lookup.

## Limits and closest literature

The orientation must be redrawn independently at a Poisson reset, not rotated by a random increment. Position is never reset. The underlying particle is an isotropically translating, nonchiral, noninteracting active Brownian particle; no claim concerns full-law rotational symmetry, nonstationary finite-time initialization, nonlinear feedback, or interactions. See Baouche et al. (2024), arXiv:2405.06769, Sections II–III and Appendix B; Kumar et al. (2020), arXiv:2008.03294, Section V and Appendix F; Olsen and Löwen (2024), arXiv:2405.14326, Sections I–III; and Ghosh and Mandal (2025), arXiv:2501.05149, Sections I–III.

Self-review: passed. Independent audit: not yet performed.
