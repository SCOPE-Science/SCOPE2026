# Scientific review: pulse-time invariance in shared-crowding competition

## Correctness — PASS

The common-crowding flow admits the exact fractional representation obtained by differentiating its positive denominator. Ordered composition of diagonal fractional maps closes algebraically; the explicit \(k\)-iterate follows by induction. Elementary asymptotics of the resulting geometric sums prove all three sharp threshold cases, including ties and the \(1/k\) law. Equal multiplier ratios and the strictly increasing scalar Beverton–Holt restriction exclude nonfixed periodic points. Direct differentiation gives the full spectrum on the winning simplex, with the neutral tangent modes kept distinct from exponentially attracting normal modes. The self-contained `verify.py` program passed exact rational composition, iterates, two pulse-timing witnesses, and the neutral-simplex matrix checks. The computations are consistency checks, not a substitute for the general proof.

## Originality — PASS, subject to historical-priority uncertainty

The one-step map is a special case of the known multispecies Leslie–Gower recurrence; the existence of such maps is explicitly **not** claimed as new. A recent motivating preprint, arXiv:2609.09343, addresses permanence under periodic pulses, but only its metadata and a secondary scientific account were available. Schreiber (2025) gives broad flow–kick invasion and permanence theory; Hosack, El-Hachem, and Beeton (2025) give local stability results for generic multispecies Leslie–Gower maps; Sacker (2011) establishes periodic coexistence when coupling is sufficiently small. Inamine and collaborators (2022) analyze disturbance regimes in two-species competition, and Xiao and collaborators (2026) give comparison and Lyapunov criteria in an additional-pollutant model. Their inspected statements do not directly imply the complete, exact shared-crowding classification with asynchronous species-specific pulse timing, critical extinction rates, and neutral simplex. Searches of published mathematical finding summaries under projective, impulse, rank-one, common-denominator, Leslie–Gower, and competitive-exclusion formulations found no direct match.

A significant residual risk is that uninspected text in the motivating preprint or older periodic Leslie–Gower literature could contain an equivalent special case. The claim of originality is limited to the available comparisons, not a guarantee of global priority.

## Mathematical value — PASS

A recurring ecological question is whether changing *when* interventions occur, while keeping the same total doses, changes which species persist. The theorem identifies an exact structural boundary: pulse timing alters effective competition loads and survivor abundance but cannot alter the winning species if all receivers experience the same competition pressure. This is stronger than mere numerical illustration and includes all species counts, seasonal forcing, staggered pulses, critical extinction, neutral multistability, and an exclusion of subharmonic cycles. The neutral tied-winner simplex is an important nonhyperbolic boundary that cannot be inferred from generic asymptotic-stability criteria. These results furnish a complete benchmark against which more general competition or state-dependent pulse models can be compared.

## Closest literature and scientific limits

The general multispecies Leslie–Gower map and flow–kick invasion framework are existing mathematics. The result is specific to equal-row, shared-crowding interactions and predetermined repeated positive multiplicative pulses; it does not hold by assertion for general competition matrices, state-dependent pulse times, stochastic dynamics, or nonlinear pulse responses. The motivating preprint's full text was not accessible, so a later independent historical-priority inspection is appropriate.

Self-review: passed. Independent audit: not yet performed.
