# Scientific review: Phase-resolved excursion laws for a rational-degree grazing map

## Correctness — PASS

The result uses the source's exact rational-degree map, for fixed \(0<\nu<1\), \(a>0\), and rational \(0<\gamma<1\), with a Lebesgue-uniform normalized initial condition on \([\nu,1]\). The first image is bounded below by \(\nu\mu\), and any image above \(\mu\) follows the exact contracting branch until its first return. Therefore the stated ceiling identity for the return time and the exact return location follow without an asymptotic approximation. Under \(\mu_j=(a\nu^{j+\theta})^{1/(1-\gamma)}\), the logarithmic remainder vanishes almost surely away from null lattice boundaries. The uniform-to-exponential change of variables yields the displayed phase tail, geometric deficit and power-law joint density. The implicit-function calculation gives the first finite-parameter correction, and a geometric left-tail bound gives uniform integrability of the centered return time. These steps prove, rather than numerically suggest, the infinite-limit and expectation claims. The script passed exact-rational square-root orbit checks, exact rational moment checks and a floating-point tail-threshold consistency test; these finite tests cannot establish generality.

## Originality — PASS (priority uncertainty remains)

Lima and Perdigão, arXiv:2407.02782v1, equations (4), (8), (9), (11)–(16), Proposition 2 and Lemmas 4–6, already provide the map, first-return section, individual return-length constraints, and induced map. Nothing here claims those ingredients as novel. The full-text sections dealing with return lengths, bifurcation theory and the appendix do not state the phase-resolved **joint** law for Lebesgue-uniform starts, the conditional time/location independence and power-law density, or the first finite-parameter tail correction. The companion arXiv:2407.02434v1 treats order-four impact discontinuity maps, not this first-return distribution. Halse–Homer–di Bernardo period-adding and Haydn–Vaienti invariant-measure return-time laws are related concepts but do not demonstrably imply this exact parameter-dependent first-excursion kernel. Search comparisons against published research records found no directly covering result, but absence of a match is not proof of absolute priority. Generic lattice-overshoot theory may yield an equivalent formulation; this remains a residual risk.

## Value — PASS

The source's shrinking return section is a natural object for its period-adding and bifurcation analysis. Exact pointwise return lengths do not reveal the distributional effect of uniformly chosen initial impact positions. The phase-resolved joint law, an explicit independent geometric duration/power-law reinjection kernel on every complete excursion band, and a first finite-scale correction answer a motivated quantitative problem about how transient orbit lengths and landing positions co-vary near grazing. They can be used as a precise reference for induced-return ensembles, while not claiming a stationary law or a general invariant-measure theorem. This is more than a reparameterization or an isolated numerical cutoff.

## Closest literature and limits

Primary: Lima and Perdigão (2024), arXiv:2407.02782v1, notably equations (4), (8)–(16) and Lemmas 4–6. Companion: Lima and Perdigão (2024), arXiv:2407.02434v1. Background: Halse, Homer and di Bernardo (2003), period-adding; Haydn and Vaienti (2004), return-time limiting laws for other dynamical settings. The complete possible priority landscape of lattice renewal/overshoot results has not been exhausted. All limits require a fixed logarithmic phase, and the sampling ensemble is not invariant.

Self-review: passed. Independent audit: not yet performed.
