# Scientific review: spectral correction to a spherical hard-edge coefficient

## Correctness — PASS

The statement covers every real positive semidefinite trace-one matrix in dimension at least two; it does not presume inverse-profile invertibility. Gaussian polar independence gives the second, third and fourth central moments of \(X=nU^{\mathsf T}HU\) exactly. The scalar polynomial identity in the proof holds for **all** \(X\ge0\), and its fourth-order remainder kernel is positive and bounded by \(5/16\), including at the potentially singular endpoint \(X=0\). Thus expectation immediately proves the global signed bound. The fourth-moment estimate and Cauchy–Schwarz give the relative diffuse limit without assuming a bounded condition number. A positive-definite, equal-purity/opposite-cubic pair checks the sign and confirms the cubic dependence.

The included independent rational Dirichlet computation checked the Gaussian moment coefficients and boundary profiles. Periodic circle quadrature checked the complete inequality numerically in dimension two, with finite integration error explicitly allowed. 1,478 assertions passed. Finite computations support the exact algebra, not the infinite-dimensional result; no external proof certification has occurred.

## Originality — PASS, with historical-priority qualifications

Häggblom's arXiv:2610.31143v1 Proposition 7.1 identifies the exact variance and gives only \(1-\vartheta_n(H)\le v/2\), while Corollary 1.3 records the qualitative diffuse limit. That source supplies neither the sharp ratio \(1-\vartheta_n(H)\sim v/8\), the signed cubic correction involving \(\operatorname{tr}(H-I_n/n)^3\), nor the globally positive fourth-order remainder. Its coefficient's universality and the basic variance identity are not claimed here. The primary article was read in its introduction, Proposition 7.1, surrounding proof, and applications.

Gusakova–Spodarev–Zaporozhets (arXiv:2206.14002v2) provides a broader exact integral representation of ellipsoid mean width, which includes the spherical square-root mean after normalization. It does not state the moment enclosure assessed here; the underlying mean-width equivalence is acknowledged. Häggblom's earlier phase-retrieval preprint (arXiv:2609.28198v1), especially Section 9, develops another inverse-tail spherical-norm coefficient and trace concentration, not an all-profile centered-spectrum cubic inequality. Hillier (2001) treats densities of spherical quadratic forms; the abstract was read but its full text was not available during the search. Mathematical-record queries for spectral cubic correction, Haar quadratic-form square-root expansion and hard-edge anisotropy did not uncover an equivalent complete statement. Absence of a matching search result is not uniqueness certification. A comprehensive historic mean-width perturbation treatment could already imply the cubic formula, and independent historical-priority checking remains necessary.

## Mathematical value — PASS

The new probability-theory application has a deterministic leading coefficient controlling extremely rare singularity events; existing results identify the coefficient by a spherical integral and give only a coarse variance-scale bound. The exact leading constant, together with a uniform explicit signed third-spectral-moment refinement and positive fourth-order error enclosure, improves quantitative calibration of that coefficient on arbitrary diffuse inverse profiles and supplies an algebraic replacement for high-dimensional spherical integration. Two profiles can have the same effective spectral purity but different coefficients already at cubic order. These distinguishable natural inverse profiles are not arbitrary numerical slices. The bound is a coefficient-level improvement, not a new universality error rate, and the quartic envelope is not asserted optimal.

## Known limitations

The result is a deterministic spectral correction and does not improve the independently existing random-matrix probability error term, which can dominate the bias correction. For non-diffuse sequences the global inequality remains valid but its polynomial may not be a close approximation. The result relies on Haar directions and positive semidefinite forms; it does not treat singular-value distributions beyond the first hard-edge coefficient. General ellipsoid mean-width expansions remain a historical priority risk. No independent verification is claimed.

Self-review: passed. Independent audit: not yet performed.
