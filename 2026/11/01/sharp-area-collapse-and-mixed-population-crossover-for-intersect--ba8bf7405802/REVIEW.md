# Scientific review of the common Brownian-hull intersection theorem

## Correctness

**PASS (self-review).** The stated domain is two-dimensional standard independent Brownian motions and bridges on a fixed unit interval. The exact geometric identity \(A_{m,n}=2\pi\int_0^\infty rS_K(r)^mS_B(r)^n\,dr\) follows from radial intersection, hull independence, polar area integration, and Tonelli; it requires no directional independence. The two radial mixture laws are established in Kabluchko (2026). Differentiating their mixture integrals gives the explicitly normalized Bessel derivatives, and integrating the \(K_0\) expansions gives both small-radius constants. The proof separately derives the second-order asymptotic integrals for pure motions and bridges, and the mixed extreme-value limit with moment convergence. Truncation bounds control the tails. The submitted standalone code passed 25 independent numerical/algebraic checks. That finite evidence corroborates but does not prove the limiting estimates.

## Originality

**PASS, provisional historical priority.** Kabluchko (2026) obtains the one-hull radial laws and coverage asymptotics; these are explicitly credited, not repackaged. The reported new theorem addresses intersections of independently generated hulls, with two explicit logarithmic correction coefficients and a two-population critical crossover. The closely relevant earlier papers by Randon-Furling, Majumdar, and Comtet (2009) and Šebek (2024) instead study the hull of a union of trajectories. Their formulas cannot be changed from union to intersection by substituting parameters. Search comparisons to published records of other random-set intersections (disks, rotated polygons) also found materially different objects; their displayed summaries do not establish comprehensive noncoverage. Historical equivalence under alternate terminology remains a residual risk.

## Mathematical value

**PASS.** This is an exact asymptotic description of the common territory of independently generated random convex sets. The motion-only and bridge-only intersection areas have distinct orders, and the theorem finds the non-obvious critical population scale \(n\asymp m^2\log m\), a continuous limiting interpolation, and first nontrivial finite-size corrections. The result concerns a natural full-family statistic rather than an arbitrary small finite calculation. The law also separates the geometric effect of path pinning from the one-hull coverage inputs.

## Limitations

Only expectations, standard isotropic planar paths, and finite crossover ratios are proved; neither area fluctuations nor an arbitrary divergent crossover parameter is addressed. The theorem uses the 2026 radial-law theorem as a premise. Independent proof validation and exhaustive historical-priority verification remain open.

Self-review: passed. Independent audit: not yet performed.
