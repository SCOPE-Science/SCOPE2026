# Scientific review: entropy-optimal three-state cycle

## Correctness — PASS

The fixed-occupation, fixed-kinetic-prefactor optimization reduces exactly to one scalar current. The derivative is strictly increasing, so existence and uniqueness follow without numerical search. With half-forces \(x_i\), stationarity is \(\sum_i[x_i+\tanh x_i]=0\); the three-term addition identity proves that an optimal conservative solution must have a zero edge current and two opposing forces. This gives all three exceptional straight lines, not merely a near-equilibrium approximation. The analytic implicit expansion then provides the cubic affinity coefficient, while a bracketing argument on the ordered offset currents provides the strong-driving limiting root and affinity. The proof states positive-weight assumptions and excludes tied offsets only where needed. The standalone numerical verifier passed 5,007 deterministic assertions, which supplement but do not replace these analytic arguments.

## Originality — PASS (qualified best-knowledge)

The closest sources are Remlein–Seifert (arxiv:2103.08376), van der Meer–Dechant (arxiv:2602.18321v2), and Dechant–van der Meer (arxiv:2605.00656). They give the same physical rate model, the cycle-current variational condition, nonconservative optimality in general, numerical triangle examples, near-equilibrium cubic *order*, and a universal affinity bound. These known statements are expressly not claimed new. Full scientific texts were inspected and compared to the precise three-line zero-affinity locus, six-sector all-amplitude sign rule, cubic coefficient and generic direction-specific saturation formula. The nearest earlier three-state control example, Muratore-Ginanneschi et al. (arxiv:1203.4062), is a nearest-neighbor chain, not a closed triangular cycle. Targeted searches of published mathematical research summaries did not identify a dominating result. Nonetheless, an implicit general formulation might subsume this theorem, and supplemental prior material was not fully accessible; publication priority is not independently certified.

## Value — PASS

The classification settles a concrete thermodynamic design question on the smallest cycle: the exact conditions under which unrestricted entropy-optimal force control coincides with conservative control. The sign of chirality cannot reverse by changing the speed of a prescribed probability change, and the finite high-drive affinity gives a quantitative prediction within a previously known upper bound. These are motivated structural facts of the whole two-dimensional velocity space, not an arbitrary parameter slice or a routine single numerical substitution.

## Scientific limits

Only instantaneous entropy-production rate minimization is addressed. Strictly positive occupations and symmetric rate prefactors are required. Strong-drive saturation assumes a generic velocity with three nonzero components; boundary cases retain the exact conservative-line and sign conclusions. The argument assumes no external amplitude cap on the driving forces. Neither numerical checks nor this review constitute independent mathematical or priority validation.

Self-review: passed. Independent audit: not yet performed.
