# Independent mathematical audit — 2026-10-01

## Final claim assessed

Ikeda critical delay stability and sharp relaxation law

## Correctness — PASS

PASS. For \(0<\mu<1\), the scalar inequality \(|\sin u|\le|u|\) yields a Halanay estimate and global exponential decay. At \(\mu=1\), direct differentiation of the stated Lyapunov–Krasovskii functional gives exactly \(-\tfrac12(x-\sin y)^2-\tfrac12(y^2-\sin^2y)\), so the largest invariant zero-dissipation set is the zero solution and global attraction follows. For \(\mu>1\), the real characteristic equation has a positive root. At criticality the characteristic root \(0\) is simple, with center coordinate \(u=Q/(1+h)\) and \(Q'=\sin x(t-h)-x(t-h)\); the odd center-manifold expansion therefore gives \(u'=-u^3/(6(1+h))+O(u^5)\), hence generic \(\sqrt t\,x(t)\to\pm\sqrt{3(1+h)}\). The statement correctly separates the strong-stable exceptional set.

## Originality — PASS

PASS to the best of current knowledge. Published-record searches found no earlier result combining the exact delay-independent threshold, a global proof at the nonhyperbolic endpoint, and the sharp critical coefficient. Kubyshkin–Moriakova's 2020 Ikeda paper is the closest source located: its full public abstract describes local normal-form bifurcation analysis of special Ikeda cases and resonant characteristic roots, not a global critical-stability theorem. The public PDF link timed out, and a lawful institutional retrieval found no verified PDF, so the unread full text remains a material originality risk rather than evidence of noncoverage.

### equivalent_formulations

Searches: Resultary: Ikeda critical delay mu=1 global asymptotic stability sharp algebraic relaxation; "x'(t) = -x(t) + sin(x(t-h))" global asymptotic stability; "Ikeda equation" "mu=1" stability zero equilibrium delay

Evidence: No earlier exact published record with the threshold plus critical relaxation coefficient was found.

Reasoning: The Lyapunov identity and the center-manifold coefficient are equivalent formulations of the critical boundary behavior, and no inspected source states both.

### broader_coverage

Searches: DOI 10.20537/nd200303; DOI 10.20537/nd180302; DOI 10.1103/PhysRevA.33.2465

Evidence: The 2020 source's public abstract studies bifurcations and normal forms near special equilibria; accessible earlier Ikeda literature concerns local stability and periodic/chaotic bifurcations.

Reasoning: No inspected theorem mechanically implies the global endpoint attraction and the stated asymptotic amplitude.

### exact_database_or_table

Searches: Published-record semantic search for zero-phase Ikeda critical decay \(\sqrt{3(1+h)}\)

Evidence: No exact earlier record or data table was located.

Reasoning: The claim is a dynamical asymptotic theorem rather than a tabulated quantity.

### claim_vs_prior_implication

Searches: Kubyshkin–Moriakova 2020 article page and abstract; targeted search for scalar delay \(x'=-x+\sin x_h\) global stability

Evidence: Accessible prior material does not state the exact global threshold or the generic \(t^{-1/2}\) coefficient.

Reasoning: The audited Lyapunov–Krasovskii identity supplies the global endpoint step, and the normalized center coordinate supplies the quantitative relaxation law.

## Scientific value — PASS

PASS. Closing the stability boundary at the nonhyperbolic endpoint and identifying the exact \(t^{-1/2}\) relaxation amplitude are natural dynamical questions for a standard delay equation. The result distinguishes global attraction from exponential stability and supplies a quantitative critical-slowing law useful for numerical and bifurcation interpretation.

## Source inspections

- **Analysis of Special Cases in the Study of Bifurcations of Periodic Solutions of the Ikeda Equation** — https://doi.org/10.20537/nd200303. Material read: Complete public article page and abstract; the public full-text link timed out and no verified PDF was obtained through lawful institutional access. Assessment: INACCESSIBLE_PLAUSIBLE_PRIOR_SOURCE. Evidence: The abstract describes local bifurcation normal forms, resonant characteristic roots, and multistability, but does not expose the audited global endpoint theorem or critical amplitude.
- **Features of Bifurcations of Periodic Solutions of the Ikeda Equation** — https://doi.org/10.20537/nd180302. Material read: Bibliographic and indexed abstract material. Assessment: BACKGROUND_LOCAL_BIFURCATION_SOURCE. Evidence: It concerns periodic-solution bifurcations and chaotic multistability rather than a global zero-equilibrium threshold theorem.

## Limitations and residual risks

The theorem is restricted to the zero-phase scalar Ikeda equation. The sharp algebraic law describes generic critical trajectories; for positive delay the strong-stable set is exceptional and decays faster. No classification of the supercritical recurrent dynamics is claimed.

- The complete 2020 Kubyshkin–Moriakova article could not be read in verified full text and is the principal originality risk.
- General scalar-delay stability theory is broad, so an equivalent endpoint theorem under abstract feedback hypotheses may exist under different terminology.

## Disposition

**passed**
