# Scientific review

## Correctness — PASS

The nonterminal-time conditional triple probability follows from a one-sided occupancy ODE, an exact central success-time density, and conditional independence of the two half-lines. Integrating \(2e^{-2u}/(1-e^{-2t})\) against \((1-u)e^{u-t}\) and its square gives the two displayed transient joint probabilities. Their covariance is a variance of a strictly monotone function of a nondegenerate time variable and is strictly positive for all \(0<t<1\). A separate symbolic integral check confirmed both identities exactly, while the standalone code tests twenty nonterminal times and the saturation boundary against finite simulations. None of the numerical checks replaces the proof.

## Originality — PASS, with priority risk

The same-process source (Amaral and dos Santos, arXiv:2210.05627) establishes densities and all-distance pair correlations, not the transient three-site Palm joint probabilities conditional on an occupied center. The saturated two-gap matrix is **not** newly claimed: at jamming occupation at two sites four apart forces occupation of the middle site, so the matrix is algebraically determined by previously published separation-two and separation-four pair probabilities. This removes the endpoint law from the original claim. The transient-time dependence is not fixed by those pair statistics because two occupied sites four apart need not have an occupied middle site before saturation. Gerin's Page–Rényi analysis and random-greedy local-limit results do not state the transient conditioned three-site law. General higher-order hierarchy methods, particularly Evans–Burgess–Hoffman (1984), remain a substantive priority risk because that primary full text was not accessible.

## Scientific value — PASS

The first genuinely three-location conditional dynamic correlation in the path adsorption model is a natural test of whether conditioning on a successful particle creates dependence between its two initially separate neighborhoods. The exact law and its strictly positive sign across the **entire open time interval** supply a structural, time-resolved description beyond the standard density and pair functions; the underlying half-line mixture provides a mechanism. The endpoint matrix is explicitly treated only as a previously implied boundary check.

## Boundaries and further verification

The exact transient formula holds on the infinite iid-uniform-priority line, under hard exclusion with one attempt per site. The result does not compute full unrestricted three-point functions, prove other multigap laws, or establish finite-volume error rates. Early correlation-hierarchy results could already contain an equivalent specialization. Independent priority and correctness reviews are outstanding.

Self-review: passed. Independent audit: not yet performed.
