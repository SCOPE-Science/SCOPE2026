# Self-review

## Correctness — PASS

The theorem’s two logarithmic derivatives are exact, and the scaled population states solve a conservative Lotka–Volterra system with a strictly convex coercive first integral. The stationary-incidence ray has a unique constrained energy minimum. Two transverse crossings for energies above that minimum give one incidence peak and trough per scaled period; the separate prevalence threshold follows from a vertical-line minimization. The equality tangencies do not generate extrema. `verify.py` checks the algebra symbolically and supplies a physical numerical example, without treating finite numerics as an infinite proof.

## Originality — PASS, with risks

Rabajante (2026, arXiv:2610.05556v1) already gives the arbitrary-transmission peak criteria, including the incidence logarithmic derivative. Maheshwari et al. (2020/2021, doi:10.1101/2020.11.10.20211995) already derive a Lotka–Volterra system for a different, controlled transmission law. Those equations and classical LV periodicity are not claimed as new. The missing new fact is a global incidence-stationary energy minimum and its strict separation from the prevalence minimum for externally fixed exponential transmission. Prior high-energy prevalence-wave results do not imply incidence-only waves at intermediate energy. An uncatalogued matching specialization remains an originality risk; the control paper's publisher full text was inaccessible, but indexed relevant sections and theorem statements were compared.

## Mathematical value — PASS

The result identifies an exact, nonempty region in which repeated reported new-infection incidence peaks coexist with monotonically declining infectious prevalence. It resolves a natural distinction between epidemic observables that matters when interpreting wave counts, and the boundary is an explicit sharp global invariant rather than a fitted threshold.

## Scope and limitations

The forcing grows without bound, all strict peaks eventually fall below any fixed reporting threshold, and finite epidemic extinction or stochastic effects are not modeled. The claim does not endorse the forcing law as a realistic long-term contact policy or assert that all oscillations would be clinically detectable.

Self-review: passed. Independent audit: not yet performed.
