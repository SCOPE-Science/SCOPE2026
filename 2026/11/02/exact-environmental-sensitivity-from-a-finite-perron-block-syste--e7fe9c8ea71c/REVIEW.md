# Review of exact environmental sensitivity from a finite Perron block system

## Correctness — PASS

The hypotheses make the normalized random positive-matrix cocycle uniformly contractive on the positive projective simplex. The common-left-Perron relation makes the zeroth-order logarithmic mass depend only on the environmental state; dominated convergence gives the derivative without an unverified response term from the stationary profile. The Markov conditional first moments satisfy an exactly solvable strictly positive finite block eigenvector equation, with correctly normalized environmental masses. Substitution proves the full entry and direction formulas, and strict positivity establishes the iid if-and-only-if boundary. The noncommuting rational example was computed exactly. Standalone exact-rational and numerical checks passed; they support but do not replace the analytic proof. All claims restrict perturbations to a small neighborhood of the original strictly positive family.

## Originality — PASS, subject to named residual priority risks

Giaimo (2023, DOI 10.1111/anzs.12382), whose accessible full article Sections 3–5 were inspected, already disproves the iid proportionality conjecture using a small-demographic-variation argument and simulation; it also proves the total-elasticity frequency identity. Neither is presented as a new theorem here. Caswell (2010, DOI 10.1111/j.1365-2745.2009.01627.x) supplies a more general stochastic response methodology, but its general asymptotic derivatives are not this explicit finite Markov block solution or sharp iid iff characterization. A positive eigenproblem for conditional population compositions is derived rather than assumed. Literature searches and published mathematical claim comparisons returned unrelated stochastic SIRS diffusion, numerical-radius sensitivity and static reproduction-number perturbation results; none entails the demographic Markov closure. Previously published mathematical findings available for comparison were searched for overlapping objects and implications and did not show a dominating result.

**Priority risk:** Caswell (2005, DOI 10.1111/j.1467-842X.2005.00373.x) and Åberg et al. (2009, Ecological Modelling 220, 605–610) were accessible only at abstract/metadata level, not as full papers. An independently published equivalent restricted result may exist. Lack of search results is not evidence of unique priority.

## Mathematical value — PASS

The 2023 motivating article explains why environment-specific demographic growth sensitivities are central to intervention planning and generally require simulation or approximations. For a nontrivial and structurally natural family with common reproductive values, the present theorem yields exact finite-dimensional sensitivities even when environmental matrices do not commute, and precisely determines when iid state frequencies proportionally determine interventions. A transparent rational example proves temporal correlation can change actionable sensitivities without changing the baseline growth exponent. The method supplies substantive computational and conceptual information not contained in the known elasticity sum, while recognizing the restriction to strictly positive fixed-transition common-left families.

## Scope and checks

The `verify.py` script uses exact fractions for matrix computations and reproducible environmental-word checks. It also checks two directional derivatives numerically with 220,000 transitions per direction. No finite calculation is offered as proof of the universal mathematical statement. The risk of inaccessible older special-case literature and exclusion of demographic structural zeros is openly stated in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
