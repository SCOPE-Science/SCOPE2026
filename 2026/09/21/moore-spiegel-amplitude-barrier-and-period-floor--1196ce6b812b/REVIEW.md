# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The proof reduces to generator identities for compactly supported invariant measures and one explicit polynomial derivative identity. The identities were independently re-expanded symbolically. Equality in the nonnegative defect forces the invariant support into z+Tx=0; differentiating that constraint gives R(1-x^2)y=0, and continuity together with x'=y leaves only the origin. The compact-slab statement uses the explicit W with W'<=0 on |x|<=1; along every complete orbit in a compact invariant set, the alpha- and omega-limit sets lie in the largest invariant zero-dissipation set, which is only the origin, forcing W to be constant and the whole orbit to be the origin. The period floor follows from the exact relation integral(x'^2)=T integral(x^2), zero mean, and Wirtinger's inequality; its equality case is excluded by direct substitution of the only extremizing sinusoid into the Moore-Spiegel equation.

The assumptions R>0 and T>0 are essential to the stated rigidity and period formula. Compact support is stated explicitly where generator averaging is used. The periodic-orbit claim is for a nonconstant orbit and its least period.

## Originality

PASS, to the best of our knowledge. The closest fully inspected primary source is Balmforth--Craster (1997), which gives the exact system, the physical interpretation, extensive bifurcation analysis, and periodic-orbit expansions and tables. Targeted searches of its accessible full text did not locate the defect identity, the unit-amplitude compact-invariant obstruction, or the strict T-only period floor.

The original Moore--Spiegel (1966) article is the most important unresolved historical coverage risk because its theorem-level full text was not inspected. Later nearby sources were checked at the level available here: Letellier--Malasoma (2014) studies topology of generalized nonlinearities; Negou--Kengne--Tchiotsop (2018) studies bifurcation, chaos and coexisting attractors; Azam et al. (2023) studies hidden and multiscroll attractors; Igra (2024) gives rigorous topological reduction and torus-knot conclusions for periodic trajectories. Their accessible statements do not state the present identities or bounds, but their complete texts were not all inspected, so they remain residual priority risks rather than evidence of absence.

## Value

PASS. The threshold |x|=1 is parameter-independent despite the two-parameter Moore-Spiegel dynamics and applies to arbitrary compact invariant statistical states, not only a numerically observed attractor. The polynomial W upgrades the measure statement to a geometric obstruction for every compact invariant set. The period inequality gives a rigorous T-only timescale constraint for all finite-amplitude periodic responses. These are direct analytic constraints on a classic oscillator whose modern literature is dominated by numerical bifurcation and topological descriptions.

## Checked evidence and limitations

The 1997 primary paper was read at the system definition, physical interpretation, preliminary dynamical analysis, and periodic-orbit-expansion sections; its published period tables are consistent with the derived lower bound. Bibliographic and abstract-level checks were made for the 1966, 2014, 2018, 2023 and 2024 sources listed in RESULT.md. The 1966 full text and the complete 2014/2018/2023/2024 texts were not all inspected, leaving genuine residual originality uncertainty.

Scientifically, the theorem gives necessary constraints, not existence, stability, uniqueness, or a complete attractor classification. Compact invariant sets are covered by the slab theorem; arbitrary one-sided bounded trajectories are not claimed to satisfy the same geometric conclusion.
