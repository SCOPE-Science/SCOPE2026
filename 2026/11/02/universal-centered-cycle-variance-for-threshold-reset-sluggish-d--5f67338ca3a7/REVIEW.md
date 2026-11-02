# Self-review

## Correctness
The diffusion is defined by a natural-scale Brownian clock, avoiding ambiguity at the singular origin. Brownian exit-time domination supplies finite cycle moments. The displayed Green kernel yields the published mean occupation fraction, and the Dirichlet Poisson potential has the required boundary values and continuous derivative. The identity \(u(\rho)=0\) is essential: it turns the centered excursion reward into a stopped martingale and its second moment into the explicit nonnegative energy integral. Direct integration reduces the latter to the stated universal factor \(1-\rho^2\); dividing by mean cycle duration produces the central limit coefficient. Independent rational and numerical checks corroborate the algebra. Risk: the theorem is for the natural-scale continuum limit only, not the finite lattice walk.

## Originality
The closest source is Frimpong–Bresque–Roldán (arXiv:2610.21962v1), whose threshold-reset section provides an exact law of large numbers, Green function, and order of fluctuations but no evaluated Gaussian constant. Its Poisson-reset calculation is not a threshold-reset variance formula. The 2024 Méndez–Flaquer-Galmés–Pal paper's reset section was examined and uses independent Poissonian reset times. Prior mathematical-record and literature searches found no directly equivalent coefficient, universal centered-excursion second-moment identity, or exact Brownian-constancy versus sluggish-strictness classification. Absence of a matching search result cannot prove priority; generic renewal-reward and Green-function theory could enable the calculation without explicitly stating it.

## Mathematical value
The motivating study explicitly quantifies occupation concentration only to order and predicts a Gaussian concentration profile for a different reset protocol. An exact variance provides a model-calibrated fluctuation law and a sharp comparison of Brownian versus sluggish restart-point sensitivity. The \(1-\rho^2\) cycle-moment factor and Brownian invariance are structural, not arbitrary numerical specializations. The result concerns a natural observable and the entire continuum parameter family rather than a selected parameter point. The scope remains one-dimensional and does not deliver a general reset-design theorem.

## Closest literature and limitations
Primary comparison: Frimpong, Bresque, Roldán (2026), arXiv:2610.21962v1 §§6.1.1–6.1.2. Related comparison: Méndez, Flaquer-Galmés, Pal (2024), arXiv:2412.05247v1 §VI. Both works were consulted in primary text. Related first-passage literature with externally timed resetting and general renewal-reward central limit theory are not equivalent statement coverage. A more general additive-functional variance result, if located, might supersede the formula; this remains a priority risk, not a correctness qualification.

Self-review: passed. Independent audit: not yet performed.
