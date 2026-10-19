# Scientific review: spherical-edge thermal leakage

## Correctness — PASS

For every integer \(d\ge2\), \(\alpha>0\), and fixed thermal threshold shift \(u\in\mathbb R\), the derivation normalizes the turning radius and thermal variance explicitly. The generalized-Stieltjes transform of the spherical Dirichlet mean is a cited known premise. Its positive coefficients decay as \(n^{-1-(d-1)/2}\); an end-block convolution argument, factorial dominated convergence and rotational moment factoring give \(\mathbb ER^s\sim C_{d,\alpha}\Gamma(\alpha+1)s^{-\alpha}\). A monotone Laplace Tauberian theorem gives the athermal shell probability. Regularly varying radial-deficit measures and a Gaussian tail domination give the full thermal crossover, including the crossing constant. The exact two-dimensional beta radial law and numerical moment calculations independently check coefficient normalization. Numerical data are not used to assert an infinite limit.

## Originality — PASS, subject to residual literature risk

Guéneau–Majumdar–Schehr (arXiv:2602.08436, full article read) gives the stationary transform in all dimensions, closed radial examples through three dimensions, and a Gaussian-convolution identity. It does **not explicitly state** the sharp all-dimensional shell coefficient or the shifted thermal leakage profile. Those are mathematically implicit in its exact transform, and obtaining them requires the nontrivial coefficient asymptotic, Tauberian inversion and Gaussian edge matching proved here; the already-known transform and general thermal convolution are excluded from the novelty claim. Frydel (arXiv:2309.12537, full text inspected) works with stationary moment equations and low-dimensional laws, not this thermal edge profile. Claim-specific mathematical-literature and research-record searches did not identify equivalent or stronger explicit asymptotics. General Dirichlet-mean endpoint theory may nevertheless cover them implicitly; this is a live originality risk, not an assertion of exhaustive search.

## Value — PASS

Probability outside the active turning sphere under arbitrarily weak thermal noise is a directly measurable physical observable. The result determines its exact \(D^{\alpha/2}\) decay exponent, previously unstated dimension-dependent amplitude, and the full spatial \(O(\sqrt D)\) threshold crossover in every integer dimension at least two. The formula quantifies how weak Gaussian forcing rounds an athermal turning surface, and provides a sharp benchmark for numerical or experimental finite-noise fits. The constant's strict ordering by dimension distinguishes otherwise qualitatively similar boundary accumulation regimes.

## Source comparisons and limitations

The core source's exact moment transform is a genuine broad antecedent, not dismissed as unrelated. Its all-dimensional exact representation determines any stationary observable in principle but does not state the present closed leading asymptotics. The source's two- and three-dimensional radial conclusions are acknowledged and used as checks, not claimed as discoveries. The theorem does not give finite-noise formulas, scaling with diverging threshold shifts, or uniform-in-dimension bounds. A relevant general Dirichlet-process asymptotic theorem might entail the coefficient without this proof. Independent review could alter the originality assessment.

Self-review: passed. Independent audit: not yet performed.
